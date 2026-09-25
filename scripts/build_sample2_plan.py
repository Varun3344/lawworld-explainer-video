"""30 s brand sample from the full-run clips c01-c03 (Flow voice) + warm b01. Writes out/sample2/{timeline,plan}.json"""
import sys, os, json, re, subprocess
sys.path.insert(0, os.path.dirname(__file__))
def norm(w): return re.sub(r"[^a-z0-9']+", "", w.lower().replace("’", "'"))
def dur(f): return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f],capture_output=True,text=True).stdout.strip())
def find(words, target, nth=1, after=0.0):
    tgt = norm(target); hits = 0
    toks = [(norm(w["word"]), w["start"], w["end"]) for w in words if norm(w["word"])]
    for i in range(len(toks)):
        if toks[i][1] < after: continue
        for span in (1, 2, 3):
            if i + span > len(toks): break
            joined = "".join(t[0] for t in toks[i:i+span])
            if joined == tgt:
                hits += 1
                if hits == nth: return toks[i][1], toks[i+span-1][2]
                break
            if len(joined) >= len(tgt): break
    return None
D = "downloads/full"; OUT = "out/sample2"; os.makedirs(OUT, exist_ok=True)
sting_end, overlap, end_hold = 2.4, 0.35, 3.2
ps = sting_end - overlap; base = ps; clips = []; all_words = []
for i, cid in enumerate(["c01", "c02", "c03"]):
    c = f"{D}/{cid}.mp4"; w = json.load(open(f"{D}/{cid}.words.json")); d = dur(c); words = w["words"]; s0, s1 = w["speech_start"], w["speech_end"]
    tin = max(0.0, s0 - 0.45) if (s0 is not None and s0 > 0.9 and i > 0) else 0.0
    tout = min(d, s1 + 0.42) if (s1 is not None and d - s1 > 0.55) else d
    clips.append({"id": cid, "clip": c, "in": round(tin, 3), "out": round(tout, 3), "base": base, "words": words, "dur": d})
    for x in words:
        if x["end"] <= tin or x["start"] >= tout: continue
        all_words.append({"word": x["word"], "start": round(base + x["start"] - tin, 3), "end": round(base + x["end"] - tin, 3)})
    base += tout - tin
pend = base; total = pend + end_hold
C = {c["id"]: c for c in clips}
def T(cid, target, nth=1, after=0.0, fallback=0.0):
    c = C[cid]; r = None
    for alt in (target if isinstance(target, (list, tuple)) else [target]):
        r = find(c["words"], alt, nth, after)
        if r: break
    if not r: print(f"[plan] WARNING {cid}: {target} not found"); return round(c["base"] + fallback, 3)
    return round(c["base"] + r[0] - c["in"], 3)
E = lambda cid: round(C[cid]["base"] + C[cid]["out"] - C[cid]["in"], 3)
cues = [{"type": "sting", "t0": 0, "t1": sting_end, "fade_out": overlap}]
t = T("c01", "Ravishankar", fallback=3.0); cues.append({"type": "lower_third", "t0": t - 0.1, "t1": t + 4.8, "name": "Ravishankar", "role": "Founder, LawWorld"})
tb, tf, tc = T("c02", "better", fallback=1.5), T("c02", "faster", fallback=2.0), T("c02", "cheaper", fallback=2.6)
tlet = T("c02", "let", fallback=3.6); tlw1 = T("c02", "lawworld", 1, fallback=4.6); r2 = find(C["c02"]["words"], "lawworld", 2)
t15 = T("c02", ["fifteen", "15"], fallback=8.6)
cut0 = round((C["c02"]["base"] + r2[0] - C["c02"]["in"]) if r2 else t15 - 1.3, 3) - 0.12
tfor = T("c03", "for", fallback=5.0); cut1 = tfor - 0.08
cues.append({"type": "pills", "t0": tb - 0.05, "t1": tlet - 0.1, "items": [{"text": "Better", "at": tb - 0.05}, {"text": "Faster", "at": tf - 0.05}, {"text": "Cheaper", "at": tc - 0.05}]})
cues.append({"type": "lockup", "t0": tlw1 - 0.1, "t1": cut0, "fade_out": 0.25})
cuts = []
b01 = f"{D}/broll_3d/b01_features_broll.mp4"
if os.path.exists(b01):
    cuts.append({"clip": b01, "start": cut0, "end": cut1, "offset": 0.0, "fade": 0.2})
    cues.append({"type": "bignum", "t0": t15 - 0.1, "t1": cut1, "num": "15+", "label": "features", "fade_out": 0.3})
else: print("[plan] WARNING: b01 missing, no cut-away")
cues.append({"type": "chapter", "t0": tfor, "t1": E("c03") - 0.1, "text": "Case preparation", "fade_out": 0.3})
tchat = T("c03", "chatbot", fallback=6.5)
cues.append({"type": "chips", "t0": tchat - 0.15, "t1": E("c03") - 0.1, "side": "right", "fade_out": 0.3, "items": [
  {"text": "AI Chatbot", "icon": "message-square", "at": tchat - 0.15}, {"text": "Drafting", "icon": "file-pen", "at": T("c03", "drafting", fallback=7.3) - 0.1},
  {"text": "Legal Research", "icon": "search", "at": T("c03", "research", fallback=8.3) - 0.1}, {"text": "Translation", "icon": "languages", "at": T("c03", "translation", fallback=9.1) - 0.1}]})
cues.append({"type": "captions", "t0": ps, "t1": pend + 0.4, "words": all_words, "max_words": 4, "max_dur": 1.7})
cues.append({"type": "cta", "t0": pend - 0.3, "t1": total, "fade_out": 0.01, "credit_at": total + 10, "link_at": total + 10, "logo_at": pend - 0.1, "url": "lawworld.ai"})
json.dump({"duration": round(total, 3), "scrim_from": ps, "cues": cues}, open(f"{OUT}/timeline.json", "w"), indent=1)
plan = {"fps": 24, "out": f"{OUT}/sample2.mp4", "presenter_start": ps, "presenter": [{"clip": c["clip"], "in": c["in"], "out": c["out"]} for c in clips],
        "cutaways": cuts, "endcard": None, "music": {"file": "audio/bed_full_170s.mp3", "target_lufs": -29, "fade_in": 1.2, "fade_out": 2.6, "duck": True},
        "voice_lufs": -16, "overlays": {"dir": f"{OUT}/frames", "fps": 24}, "delogo": None, "total": round(total, 3), "tail_black": end_hold}
json.dump(plan, open(f"{OUT}/plan.json", "w"), indent=1)
print(f"[plan] presenter {ps:.2f}-{pend:.2f}s, cut {cut0}-{cut1}, total {total:.2f}s")
for k in cues:
    if k["type"] != "captions": print(f"[plan]  {k['type']:<12} {k['t0']:>7} -> {k['t1']}")
