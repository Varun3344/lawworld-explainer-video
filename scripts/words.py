"""Word-level timestamps for a clip via OpenAI whisper-1, plus a verbatim check against the storyboard dialogue.
Usage: python3 words.py <storyboard.json> <clip.mp4> [...]  -> writes <clip>.words.json and prints the QA verdict."""
import sys, os, json, re, subprocess, tempfile, difflib
sys.path.insert(0, os.path.dirname(__file__))
from envkeys import OPENAI_API_KEY

def norm(w):
    w = w.lower().replace("’", "'")
    w = re.sub(r"[^a-z0-9']+", "", w)
    return w

def transcribe(clip):
    tmp = tempfile.mkdtemp(); wav = os.path.join(tmp, "a.mp3")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", clip, "-vn", "-ac", "1", "-ar", "16000", "-b:a", "64k", wav], check=True)
    r = subprocess.run(["curl", "-s", "-m", "180", "https://api.openai.com/v1/audio/transcriptions",
                        "-H", f"Authorization: Bearer {OPENAI_API_KEY}", "-F", f"file=@{wav}", "-F", "model=whisper-1",
                        "-F", "response_format=verbose_json", "-F", "timestamp_granularities[]=word",
                        "-F", "language=en", "-F", "prompt=LawWorld, Ravishankar, advocate, AI chatbot, e-courts, DPDP Act, Pay-as-you-go, GST."],
                       capture_output=True, text=True, check=True)
    d = json.loads(r.stdout)
    if "words" not in d: raise SystemExit(f"[words] unexpected response: {r.stdout[:300]}")
    return d

NUM = [("fifteen hundred","1500"),("twelve thousand","12000"),("two hundred","200"),("fifteen","15"),("twelve","12"),("ten","10"),("five","5"),("two","2"),("rupees","rs"),("rs","rs")]
def numify(tokens):
    """number words -> digits so 'fifteen hundred rupees' == '1,500 rupees' == '₹1,500'"""
    text = " " + " ".join(tokens) + " "
    for a, b in NUM: text = text.replace(" " + a + " ", " " + b + " ")
    out = []
    for t in text.split():
        if t in ("rs",): continue          # currency word/symbol carries no meaning for the check
        out.append(t)
    return out
def check(dialogue, words):
    exp = numify([norm(w) for w in dialogue.split() if norm(w)])
    got = numify([norm(w["word"]) for w in words if norm(w["word"])])
    sm = difflib.SequenceMatcher(a=exp, b=got, autojunk=False)
    missing, extra = [], []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag in ("delete", "replace"): missing += exp[i1:i2]
        if tag in ("insert", "replace"): extra += got[j1:j2]
    # verdict on characters, so 'case-ready' vs 'case ready' or 'e-courts' vs 'e courts' never count as a miss
    cr = difflib.SequenceMatcher(a="".join(exp), b="".join(got), autojunk=False).ratio()
    return cr, missing, extra

if __name__ == "__main__":
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
            verdict = "OK" if ratio >= 0.97 else "CHECK"
            print(f"[words] {sid}: {verdict} match={ratio:.2f} speech {first:.2f}-{last:.2f}s of {dur:.2f}s tail={dur-last:.2f}s missing={missing} extra={extra}")
        else:
            print(f"[words] {sid}: (no scene) {first}-{last}s of {dur:.2f}s: {d.get('text','')[:120]}")
        json.dump(out, open(clip[:-4] + ".words.json", "w"), indent=1)
