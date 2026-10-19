"""Word-level timestamps for a clip via OpenAI whisper-1, plus a verbatim check against the storyboard dialogue.
Usage: python3 words.py <storyboard.json> <clip.mp4> [...]  -> writes <clip>.words.json and prints the QA verdict."""
import sys, os, json, re, subprocess, tempfile, difflib
sys.path.insert(0, os.path.dirname(__file__))
from envkeys import OPENAI_API_KEY

import unicodedata
def norm(w):
    """Latin: lowercase alphanumerics only. Other scripts (Kannada...): NFC, drop punctuation/space/zero-width joiners, keep everything else."""
    w = unicodedata.normalize("NFC", w).lower().replace("’", "'")
    if re.search(r"[^\x00-\x7f]", w):
        return re.sub(r"[\s\u200b-\u200d\ufeff.,;:!?\"'()\[\]{}\-–—…/]+", "", w)
    return re.sub(r"[^a-z0-9']+", "", w)

LANG = "en"; PROMPT = "LawWorld, Ravishankar, advocate, AI chatbot, e-courts, DPDP Act, Pay-as-you-go, GST."
def transcribe(clip):
    tmp = tempfile.mkdtemp(); wav = os.path.join(tmp, "a.mp3")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", clip, "-vn", "-ac", "1", "-ar", "16000", "-b:a", "64k", wav], check=True)
    r = subprocess.run(["curl", "-s", "-m", "180", "https://api.openai.com/v1/audio/transcriptions",
                        "-H", f"Authorization: Bearer {OPENAI_API_KEY}", "-F", f"file=@{wav}", "-F", "model=whisper-1",
                        "-F", "response_format=verbose_json", "-F", "timestamp_granularities[]=word",
                        "-F", f"language={LANG}", "-F", f"prompt={PROMPT}"],
                       capture_output=True, text=True, check=True)
    d = json.loads(r.stdout)
    if "words" not in d: raise SystemExit(f"[words] unexpected response: {r.stdout[:300]}")
    return d

UNITS = {w: i for i, w in enumerate("zero one two three four five six seven eight nine".split())}
TEENS = {w: i + 10 for i, w in enumerate("ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split())}
TENS = {w: (i + 2) * 10 for i, w in enumerate("twenty thirty forty fifty sixty seventy eighty ninety".split())}
SCALES = {"thousand": 1000, "lakh": 100000, "lakhs": 100000, "crore": 10000000, "crores": 10000000}
def numify(tokens):
    """number words -> digit tokens on both sides of the check, so 'fifteen hundred rupees' == '1,500 rupees' == '₹1,500' and the
    Indian way of reading section numbers matches whisper's digits: 'one seventy three' -> '1' '73' (joined '173' in the
    character check) == '173', 'three hundred three' -> '303', 'twenty five thousand' -> '25000'. Ordinals stay words."""
    out = []; total = cur = 0; last = None
    def flush():
        nonlocal total, cur, last
        if last is not None: out.append(str(total + cur))
        total = cur = 0; last = None
    for t in tokens:
        t = t.replace(",", "").replace("₹", "")
        if t in ("", "rs", "rupees", "rupee"): continue          # currency word/symbol carries no meaning for the check
        if t in UNITS or t in TEENS:
            v = UNITS.get(t, TEENS.get(t))
            if last in ("unit", "teen") or (last == "tens" and t in TEENS): flush()
            cur += v; last = "unit" if t in UNITS else "teen"
        elif t in TENS:
            if last in ("unit", "teen", "tens"): flush()
            cur += TENS[t]; last = "tens"
        elif t == "hundred":
            cur = (cur or 1) * 100; last = "hundred"
        elif t in SCALES and last is not None:
            total += (cur or 1) * SCALES[t]; cur = 0; last = "scale"
        else:
            flush(); out.append(t)
    flush()
    return out
def check(dialogue, words):
    exp = numify([norm(w) for w in dialogue.replace("-", " ").split() if norm(w)])
    got = numify([norm(x) for w in words for x in w["word"].replace("-", " ").split() if norm(x)])
    sm = difflib.SequenceMatcher(a=exp, b=got, autojunk=False)
    missing, extra = [], []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag in ("delete", "replace"): missing += exp[i1:i2]
        if tag in ("insert", "replace"): extra += got[j1:j2]
    # verdict on characters, so 'case-ready' vs 'case ready' or 'e-courts' vs 'e courts' never count as a miss
    cr = difflib.SequenceMatcher(a="".join(exp), b="".join(got), autojunk=False).ratio()
    return cr, missing, extra

if __name__ == "__main__":
    args = sys.argv[1:]
    if "--lang" in args: i = args.index("--lang"); LANG = args[i + 1]; del args[i:i + 2]
    if "--prompt" in args: i = args.index("--prompt"); PROMPT = args[i + 1]; del args[i:i + 2]
    sys.argv = [sys.argv[0]] + args
    sb = json.load(open(sys.argv[1]))
    by_id = {s["sceneId"]: s for s in sb["scenes"]}
    for clip in sys.argv[2:]:
        sid = os.path.basename(clip).split(".")[0]
        scene = by_id.get(sid)
        d = transcribe(clip)
        words = d["words"]
        dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", clip], capture_output=True, text=True).stdout.strip())
        first, last = (words[0]["start"], words[-1]["end"]) if words else (None, None)
        out = {"clip": clip, "sceneId": sid, "duration": dur, "text": d.get("text", ""), "words": words,
               "speech_start": first, "speech_end": last}
        if scene:
            ratio, missing, extra = check(scene["dialogue"], words)
            out.update({"match_ratio": ratio, "missing": missing, "extra": extra})
            verdict = "OK" if ratio >= (0.90 if LANG != "en" else 0.97) else "CHECK"   # non-Latin whisper spelling varies more
            print(f"[words] {sid}: {verdict} match={ratio:.2f} speech {first:.2f}-{last:.2f}s of {dur:.2f}s tail={dur-last:.2f}s missing={missing} extra={extra}")
        else:
            print(f"[words] {sid}: (no scene) {first}-{last}s of {dur:.2f}s: {d.get('text','')[:120]}")
        json.dump(out, open(clip[:-4] + ".words.json", "w"), indent=1)
