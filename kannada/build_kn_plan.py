"""Kannada law-explainer sample: clips k01..k04 (+bk01) -> out/kn/{timeline,plan}.json"""
import sys, os, json, subprocess, difflib, importlib.util
spec = importlib.util.spec_from_file_location("words", "scripts/words.py"); W = importlib.util.module_from_spec(spec); spec.loader.exec_module(W); norm = W.norm
def dur(f): return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f],capture_output=True,text=True).stdout.strip())
def find(words, target, nth=1, after=0.0):
    tgt = norm(target); hits = 0; toks = [(norm(w["word"]), w["start"], w["end"]) for w in words if norm(w["word"])]
    for i in range(len(toks)):
        if toks[i][1] < after: continue
        for span in (1, 2, 3):
            if i + span > len(toks): break
            joined = "".join(t[0] for t in toks[i:i+span])
            if joined == tgt or (len(tgt) >= 4 and joined.startswith(tgt)):
                hits += 1
                if hits == nth: return toks[i][1], toks[i+span-1][2]
                break
            if len(joined) >= len(tgt): break
    return None
D = "downloads/kn"; OUT = "out/kn"; os.makedirs(OUT, exist_ok=True)
alts = json.load(open("kannada/alts.json"))
def spoken_text(cid):
    v = open(f"{D}/{cid}.variant").read().strip() if os.path.exists(f"{D}/{cid}.variant") else "0"
    base = {s["sceneId"]: s["dialogue"] for s in json.load(open("kannada/kn_all_scenes.json"))["scenes"]}
    return alts.get(cid, [base[cid]])[int(v)] if cid in alts else base[cid]
IDS = [c for c in ["k01", "k02", "k03", "k04"] if os.path.exists(f"{D}/{c}.mp4")]
sting_end, overlap, end_hold = 2.4, 0.35, 3.0
ps = sting_end - overlap; base = ps; clips = []
for i, cid in enumerate(IDS):
    c = f"{D}/{cid}.mp4"; w = json.load(open(f"{D}/{cid}.words.json")); d = dur(c); words = w["words"]; s0, s1 = w["speech_start"], w["speech_end"]
    tin = max(0.0, s0 - 0.45) if (s0 is not None and s0 > 0.9 and i > 0) else 0.0
    tout = min(d, s1 + 0.45) if (s1 is not None and d - s1 > 0.55) else d
    clips.append({"id": cid, "clip": c, "in": round(tin, 3), "out": round(tout, 3), "base": base, "words": words, "dur": d}); base += tout - tin
pend = base; total = pend + end_hold; C = {c["id"]: c for c in clips}
def T(cid, target, nth=1, after=0.0, fallback=0.0):
    if cid not in C: return None
    c = C[cid]; r = None
    for alt in (target if isinstance(target, (list, tuple)) else [target]):
        r = find(c["words"], alt, nth, after)
        if r: break
    if not r: print(f"[plan] WARNING {cid}: {target} not found; fallback +{fallback}s"); return round(c["base"] + fallback, 3)
    return round(c["base"] + r[0] - c["in"], 3)
S = lambda cid: round(C[cid]["base"], 3); E = lambda cid: round(C[cid]["base"] + C[cid]["out"] - C[cid]["in"], 3)
# captions: script spelling aligned to whisper tokens
all_words = []
for c in clips:
    toks = [t for t in spoken_text(c["id"]).split() if t.strip("—–-")]
    ws = [w for w in c["words"] if w["end"] > c["in"] and w["start"] < c["out"]]
    sm = difflib.SequenceMatcher(a=[norm(t) or "x" for t in toks], b=[norm(w["word"]) or "x" for w in ws], autojunk=False); times = [None] * len(toks)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1): times[i1 + k] = (ws[j1 + k]["start"], ws[j1 + k]["end"])
        elif tag == "replace" and j2 > j1:
            t0, t1 = ws[j1]["start"], ws[j2 - 1]["end"]; n = i2 - i1
            for k in range(n): times[i1 + k] = (t0 + (t1 - t0) * k / n, t0 + (t1 - t0) * (k + 1) / n)
    for i in range(len(toks)):
        if times[i] is None:
            prev = next((times[k][1] for k in range(i - 1, -1, -1) if times[k]), c["in"]); nxt = next((times[k][0] for k in range(i + 1, len(toks)) if times[k]), c["out"])
            n = 1; k = i
            while k + 1 < len(toks) and times[k + 1] is None: n += 1; k += 1
            for m in range(n): times[i + m] = (prev + (nxt - prev) * m / n, prev + (nxt - prev) * (m + 1) / n)
    for i in range(len(toks)): all_words.append({"word": toks[i], "start": round(c["base"] + max(c["in"], times[i][0]) - c["in"], 3), "end": round(c["base"] + min(c["out"], times[i][1]) - c["in"], 3)})
cues = [{"type": "sting", "t0": 0, "t1": sting_end, "fade_out": overlap, "tag": "ಕಾನೂನು ಸುದ್ದಿ · LawWorld"}]; cuts = []
if "k01" in C:
    cues.append({"type": "lower_third", "t0": S("k01") + 0.3, "t1": S("k01") + 5.3, "name": "ರವಿಶಂಕರ್", "role": "LawWorld"})
    th = T("k01", ["ಐತಿಹಾಸಿಕ"], fallback=4.0); cues.append({"type": "chapter", "t0": th - 0.1, "t1": E("k01") - 0.1, "text": "ಐತಿಹಾಸಿಕ ಬದಲಾವಣೆ", "fade_out": 0.3})
if "k02" in C:
    tj = T("k02", ["ಜುಲೈ", "ಈಗ"], fallback=0.3); tm = T("k02", ["ಮೂರು"], 2, fallback=6.0) or T("k02", ["ಮೂರು"], 1, fallback=6.0)
    tb = T("k02", ["ಬ್ರಿಟಿಷ್", "ಹಳೆಯ", "ಇವು"], fallback=4.0)
    cues.append({"type": "title", "t0": tj - 0.05, "t1": tb - 0.1, "title": "1 ಜುಲೈ 2024", "sub": "ಮೂರು ಹೊಸ ಕಾನೂನುಗಳು ಜಾರಿಗೆ", "sub_at": tj + 0.8, "fade_out": 0.3})
    b = f"{D}/broll_3d/bk01_lawbooks_broll.mp4"
    if os.path.exists(b):
        cuts.append({"clip": b, "start": round(tb - 0.1, 3), "end": E("k02"), "offset": 0.0, "fade": 0.2})
        cues.append({"type": "bignum", "t0": tm - 0.1, "t1": E("k02"), "num": "3", "label": "ಹೊಸ ಕಾನೂನುಗಳು", "fade_out": 0.3})
if "k03" in C:
    t_end = E("k04") if "k04" in C else E("k03")
    rows = [{"old": "IPC 1860", "new": "ಭಾರತೀಯ ನ್ಯಾಯ ಸಂಹಿತೆ", "tag": "BNS", "at": T("k03", ["ದಂಡ"], fallback=0.6) - 0.1},
            {"old": "CrPC 1973", "new": "ಭಾರತೀಯ ನಾಗರಿಕ ಸುರಕ್ಷಾ ಸಂಹಿತೆ", "tag": "BNSS", "at": T("k03", ["ಅಪರಾಧ", "ಪ್ರಕ್ರಿಯಾ"], fallback=4.0) - 0.1}]
    if "k04" in C: rows.append({"old": "Evidence Act 1872", "new": "ಭಾರತೀಯ ಸಾಕ್ಷ್ಯ ಅಧಿನಿಯಮ 2023", "tag": "BSA", "at": T("k04", ["ಸಾಕ್ಷ್ಯ"], fallback=1.0) - 0.1})
    cues.append({"type": "chapter", "t0": S("k03") + 0.1, "t1": t_end - 0.1, "text": "ಮೂರು ಹೊಸ ಕಾನೂನುಗಳು", "fade_out": 0.3})
    cues.append({"type": "swaprows", "t0": rows[0]["at"], "t1": t_end - 0.1, "rows": rows, "fade_out": 0.3})
cues.append({"type": "captions", "t0": ps, "t1": pend + 0.4, "words": all_words, "max_words": 3, "max_dur": 1.8})
cues.append({"type": "cta", "t0": pend - 0.3, "t1": total, "fade_out": 0.01, "credit_at": total + 10, "link_at": total + 10, "logo_at": pend - 0.1, "url": "ಲಾವರ್ಲ್ಡ್ ಫಾಲೋ ಮಾಡಿ · lawworld.ai"})
json.dump({"duration": round(total, 3), "scrim_from": ps, "lang": "kn", "cues": cues}, open(f"{OUT}/timeline.json", "w"), indent=1, ensure_ascii=False)
plan = {"fps": 24, "out": f"{OUT}/kn_sample.mp4", "presenter_start": ps, "presenter": [{"clip": c["clip"], "in": c["in"], "out": c["out"]} for c in clips], "cutaways": cuts,
        "endcard": {"clip": "brand/cream_tail.mp4", "dur": round(end_hold + 0.3, 3), "offset": 0.0, "xfade": 0.3},
        "music": {"file": "audio/bed_full_170s.mp3", "target_lufs": -29, "fade_in": 1.2, "fade_out": 2.6, "duck": True}, "voice_lufs": -16,
        "overlays": {"dir": f"{OUT}/frames", "fps": 24}, "delogo": None, "total": round(total, 3), "tail_black": 0}
json.dump(plan, open(f"{OUT}/plan.json", "w"), indent=1)
print(f"[plan] clips {IDS} presenter {ps:.2f}-{pend:.2f}s total {total:.2f}s cuts {len(cuts)}")
for k in cues:
    if k["type"] != "captions": print(f"[plan]  {k['type']:<12} {k['t0']:>7} -> {k['t1']}")
