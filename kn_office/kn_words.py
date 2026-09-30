"""Kannada clip check + word timings.
  python3 kn_office/kn_words.py <scenes.json> <clip.mp4> [...]
For each clip: whisper (kn) transcript with word times -> consonant-skeleton recall vs the script (whisper spells Kannada
phonetically, or answers in Latin / Devanagari), per-third recall (every part of the line must be heard), speech bounds from
silence detection, then script words aligned to whisper words -> <clip>.words.json (script spelling + times)."""
import sys, os, re, json, subprocess, tempfile, unicodedata
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts"))
from envkeys import OPENAI_API_KEY
KN = dict(zip("ಕಖಗಘಙಚಛಜಝಞಟಠಡಢಣತಥದಧನಪಫಬಭಮಯರಲವಶಷಸಹಳ", "kkggnccjjnttddnttddnppbbmyrlvssshl")); KN["ಂ"] = "n"
DV = dict(zip("कखगघङचछजझञटठडढणतथदधनपफबभमयरलळवशषसह", "kkggnccjjnttddnttddnppbbmyrllvsssh")); DV["ं"] = "n"
NUM_STEMS = ["ಒಂದು", "ಎರಡು", "ಹತ್ತ", "ಹದಿನೈದ", "ಹನ್ನೆರಡು", "ಸಾವಿರ", "ಐನೂರು", "ನೂರು"]
def roman(t):
    t = re.sub(r"[^a-z]", "", t.lower())
    for a, b in ((r"(k|g|c|j|t|d|p|b)h", r"\1"), ("sh", "s"), ("ch", "c"), ("w", "v"), ("f", "p"), ("q", "k"), ("z", "j"), ("x", "ks")): t = re.sub(a, b, t)
    return re.sub(r"[aeiou]", "", t)
# Indic scripts share one layout (ISCII): a consonant sits at the same offset in every 0x80-wide block, so one table
# (built from Kannada) reads Devanagari, Tamil, Telugu, Malayalam... whisper answers Kannada audio in any of them.
OFF = {ord(k) - 0x0C80: v for k, v in KN.items()}; OFF.update({0x29: "n", 0x31: "r", 0x34: "l"})
def skel(word):
    """Latin consonant skeleton of one token in Latin or any Indic script."""
    w = unicodedata.normalize("NFC", word); out = []; lat = ""
    for ch in w:
        cp = ord(ch)
        if 0x0900 <= cp <= 0x0D7F:
            out.append(roman(lat)); lat = ""; out.append(OFF.get(cp % 0x80, ""))
        elif ch.isascii() and ch.isalpha(): lat += ch
    out.append(roman(lat)); return "".join(out)
def pairs(s):
    m = {}
    for i in range(len(s) - 1): m[s[i:i+2]] = m.get(s[i:i+2], 0) + 1
    return m
def recall(want, heard):
    a, b = pairs(want), pairs(heard); n = sum(a.values())
    return (sum(min(c, b.get(k, 0)) for k, c in a.items()) / n) if n else 1.0
def want_tokens(text, heard_has_digits):
    toks = [t for t in text.split() if re.search(r"\w", t)]
    if heard_has_digits: toks = [t for t in toks if not any(t.startswith(s) for s in NUM_STEMS)]
    return toks
def transcribe(clip):
    tmp = tempfile.mkdtemp(); mp3 = os.path.join(tmp, "a.mp3")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", clip, "-vn", "-ac", "1", "-ar", "16000", "-b:a", "64k", mp3], check=True)
    r = subprocess.run(["curl", "-s", "-m", "180", "https://api.openai.com/v1/audio/transcriptions", "-H", f"Authorization: Bearer {OPENAI_API_KEY}",
                        "-F", f"file=@{mp3}", "-F", "model=whisper-1", "-F", "response_format=verbose_json", "-F", "timestamp_granularities[]=word", "-F", "language=kn",
                        "-F", "prompt=ಇದು ಕನ್ನಡ ಭಾಷೆಯ ವಿಡಿಯೋ. ಲಾ ವರ್ಲ್ಡ್."],   # keeps whisper in Kannada script (it drifted to Tamil and truncated)
                       capture_output=True, text=True, check=True)
    d = json.loads(r.stdout)
    if "words" not in d: raise SystemExit(f"[kn] bad whisper response: {r.stdout[:300]}")
    return d
def speech_bounds(clip):
    d = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", clip], capture_output=True, text=True).stdout.strip())
    o = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", clip, "-af", "silencedetect=noise=-36dB:d=0.25", "-f", "null", "-"], capture_output=True, text=True).stderr
    st = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", o)]; en = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", o)]
    sil = list(zip(st, en + [d] * (len(st) - len(en))))
    s0 = next((e for s, e in sil if s <= 0.05), 0.0); s1 = next((s for s, e in reversed(sil) if e >= d - 0.05), d)
    gaps = [(s, e) for s, e in sil if s > s0 + 0.05 and e < s1 - 0.05]
    return d, round(s0, 3), round(s1, 3), gaps
def align(toks, ws, s0, s1):
    """DP alignment of script tokens to whisper words by skeleton similarity; unmatched tokens are interpolated."""
    import difflib
    A = [skel(t) for t in toks]; B = [skel(w["word"]) for w in ws]; n, m = len(A), len(B)
    sim = lambda a, b: (1.0 if a == b else difflib.SequenceMatcher(a=a, b=b).ratio()) if (a or b) else 0.6
    NEG = -1e9; S = [[0.0] * (m + 1) for _ in range(n + 1)]; bt = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1): S[i][0] = -0.45 * i; bt[i][0] = 1
    for j in range(1, m + 1): S[0][j] = -0.45 * j; bt[0][j] = 2
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            c = [S[i-1][j-1] + (sim(A[i-1], B[j-1]) - 0.45), S[i-1][j] - 0.45, S[i][j-1] - 0.45]; k = max(range(3), key=lambda x: c[x]); S[i][j] = c[k]; bt[i][j] = k
    tm = [None] * n; i, j = n, m
    while i > 0 or j > 0:
        k = bt[i][j]
        if k == 0:
            if sim(A[i-1], B[j-1]) >= 0.45: tm[i-1] = (ws[j-1]["start"], ws[j-1]["end"])
            i -= 1; j -= 1
        elif k == 1: i -= 1
        else: j -= 1
    # clamp into the speech window, enforce order, interpolate gaps by token length
    last = s0
    for k in range(n):
        if tm[k]:
            a, b = max(s0, tm[k][0]), min(s1, tm[k][1])
            if a < last - 0.05 or b <= a: tm[k] = None
            else: tm[k] = (a, b); last = b
    k = 0
    while k < n:
        if tm[k] is None:
            e = k
            while e < n and tm[e] is None: e += 1
            p = tm[k-1][1] if k > 0 else s0; q = tm[e][0] if e < n else s1
            L = [max(1, len(toks[x])) for x in range(k, e)]; tot = sum(L); acc = 0
            for x in range(k, e):
                tm[x] = (p + (q - p) * acc / tot, p + (q - p) * (acc + L[x-k]) / tot); acc += L[x-k]
            k = e
        else: k += 1
    matched = sum(1 for a, b in zip(A, B) if a) and sum(1 for t in tm if t)
    return tm
if __name__ == "__main__":
    scenes = {s["sceneId"]: s for s in json.load(open(sys.argv[1]))["scenes"]}
    for clip in sys.argv[2:]:
        sid = os.path.basename(clip).split(".")[0]; text = scenes[sid]["dialogue"]
        d = transcribe(clip); heard = d.get("text", ""); ws = d["words"]
        dur, s0, s1, gaps = speech_bounds(clip)
        toks = want_tokens(text, bool(re.search(r"\d", heard)))
        W = "".join(skel(t) for t in toks); H = "".join(skel(x) for x in heard.split())
        r = recall(W, H)
        third = max(1, len(toks) // 3); parts = [toks[:third], toks[third:2*third], toks[2*third:]]
        rp = [recall("".join(skel(t) for t in p), H) for p in parts]
        big_gap = max([e - s for s, e in gaps], default=0.0)
        ok = r >= 0.58 and min(rp) >= 0.42 and (s1 - s0) >= 0.62 * dur and big_gap < 1.6
        all_toks = [t for t in text.split() if re.search(r"\w", t)]
        tm = align(all_toks, ws, s0, s1)
        out = {"clip": clip, "sceneId": sid, "duration": dur, "text": heard, "speech_start": s0, "speech_end": s1, "recall": round(r, 3), "thirds": [round(x, 2) for x in rp],
               "words": [{"word": all_toks[i], "start": round(tm[i][0], 3), "end": round(tm[i][1], 3)} for i in range(len(all_toks))]}
        json.dump(out, open(clip[:-4] + ".words.json", "w"), ensure_ascii=False, indent=1)
        print(f"[kn] {sid}: {'OK' if ok else 'CHECK'} recall={r:.2f} thirds={[round(x,2) for x in rp]} speech {s0:.2f}-{s1:.2f}s of {dur:.2f}s gap={big_gap:.2f} | {heard[:90]}")
