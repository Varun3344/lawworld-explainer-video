"""Creator-style fast edit: jump cuts at pauses, punch-in zooms, kinetic captions, emoji pops, stat cards, flash inserts, SFX.
Inputs: downloads/creator/h01..h05 (+ .words.json), existing 3D scenes in downloads/full/broll_3d. Output: out/creator/{timeline,plan}.json"""
import sys, os, json, subprocess, difflib, importlib.util
spec = importlib.util.spec_from_file_location("words", "scripts/words.py"); W = importlib.util.module_from_spec(spec); spec.loader.exec_module(W); norm = W.norm
def dur(f): return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f],capture_output=True,text=True).stdout.strip())
D = os.environ.get("CREATOR_DIR", "downloads/creator"); B = "downloads/full/broll_3d"; OUT = os.environ.get("CREATOR_OUT", "out/creator"); os.makedirs(OUT, exist_ok=True)
SCRIPT = {s["sceneId"]: s["dialogue"] for s in json.load(open("creator/creator_all_scenes.json"))["scenes"]}
IDS = [c for c in ["h01", "h02", "h03", "h04", "h05"] if os.path.exists(f"{D}/{c}.mp4")]
HOOK_END = 1.5; END_HOLD = 3.2
GAP_CUT, GAP_KEEP, PAD_IN, PAD_OUT = 0.42, 0.10, 0.10, 0.12   # cut any pause >= 0.42 s down to 0.10 s
ZOOMS = [1.0, 1.14, 1.06, 1.22, 1.0, 1.12]
# ---- 1. segments (jump cuts) with absolute timeline positions ----
segs = []; t = HOOK_END; zi = 0; all_words = []
for cid in IDS:
    clip = f"{D}/{cid}.mp4"; d = dur(clip); words = json.load(open(f"{D}/{cid}.words.json"))["words"]
    if not words: continue
    # script-spelled words aligned to whisper words (same as the explainer)
    toks = [x for x in SCRIPT[cid].split() if x.strip("—–-")]
    sm = difflib.SequenceMatcher(a=[norm(x) or "x" for x in toks], b=[norm(w["word"]) or "x" for w in words], autojunk=False); times = [None] * len(toks)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1): times[i1 + k] = (words[j1 + k]["start"], words[j1 + k]["end"])
        elif tag == "replace" and j2 > j1:
            t0, t1 = words[j1]["start"], words[j2 - 1]["end"]; n = i2 - i1
            for k in range(n): times[i1 + k] = (t0 + (t1 - t0) * k / n, t0 + (t1 - t0) * (k + 1) / n)
    for i in range(len(toks)):
        if times[i] is None:
            prev = next((times[k][1] for k in range(i - 1, -1, -1) if times[k]), 0.0); nxt = next((times[k][0] for k in range(i + 1, len(toks)) if times[k]), d)
            times[i] = (prev, min(nxt, prev + 0.3))
    sw = [{"word": toks[i], "s": times[i][0], "e": times[i][1]} for i in range(len(toks))]
    # split into speech runs at long pauses
    runs = []; cur = [sw[0]]
    for a, b in zip(sw, sw[1:]):
        run_len = a["e"] - cur[0]["s"]
        if b["s"] - a["e"] >= GAP_CUT or (a["word"].rstrip('"').endswith((".", "!", "?")) and run_len >= 1.2): runs.append(cur); cur = [b]
        else: cur.append(b)
    runs.append(cur)
    for r in runs:
        tin = max(0.0, r[0]["s"] - PAD_IN); tout = min(d, r[-1]["e"] + PAD_OUT)
        if tout - tin < 0.3: continue
        seg = {"clip": clip, "in": round(tin, 3), "out": round(tout, 3), "zoom": ZOOMS[zi % len(ZOOMS)], "base": round(t, 3), "cid": cid}; zi += 1
        for w in r: all_words.append({"word": w["word"], "start": round(t + w["s"] - tin, 3), "end": round(t + w["e"] - tin, 3), "cid": cid})
        segs.append(seg); t += tout - tin
pend = round(t, 3); total = round(pend + END_HOLD, 3)
def at(cid, target, nth=1, fallback=None):
    tg = norm(target); hits = 0
    for w in all_words:
        if w["cid"] != cid: continue
        n = norm(w["word"])
        if n == tg or (len(tg) >= 4 and n.startswith(tg)):
            hits += 1
            if hits == nth: return w["start"]
    print(f"[plan] WARNING {cid}: '{target}' not found"); return fallback if fallback is not None else next(w["start"] for w in all_words if w["cid"] == cid)
def cend(cid): return max(w["end"] for w in all_words if w["cid"] == cid)
def cstart(cid): return min(w["start"] for w in all_words if w["cid"] == cid)
cues = []; cuts = []; sfx = []
S = lambda name, t, g=-8: sfx.append({"file": f"audio/sfx/{name}.mp3", "at": round(max(0, t), 3), "gain_db": g})
def flash(t, d=0.12): cues.append({"type": "flash", "t0": round(t, 3), "t1": round(t + d, 3), "fade_out": 0.01})
def insert(scene, t0, L, offset=0.0):
    p = f"{B}/{scene}_broll.mp4"
    if not os.path.exists(p): print(f"[plan] WARNING no scene {scene}"); return
    cuts.append({"clip": p, "start": round(t0, 3), "end": round(t0 + L, 3), "offset": offset, "fade": 0.06}); S("whoosh", t0 - 0.12, -10); flash(t0, 0.1)
# ---- 2. hook ----
cues.append({"type": "hook", "t0": 0, "t1": HOOK_END + 0.15, "fade_out": 0.15, "l1": "YOU'RE LOSING", "l2": "HOURS", "l3": "every week — not in court"}); S("slam", 0.02, -6); S("riser", HOOK_END - 0.9, -14); flash(HOOK_END, 0.14)
cues.append({"type": "grain", "t0": 0, "t1": total, "fade_out": 0.01})
if "h01" in IDS:
    cues.append({"type": "emoji", "t0": at("h01", "court") - 0.05, "t1": at("h01", "court") + 1.6, "items": [{"emoji": "⚖️", "x": 760, "y": 330, "at": at("h01", "court") - 0.05, "dur": 1.6}]}); S("pop", at("h01", "court"), -10)
    cues.append({"type": "emoji", "t0": at("h01", "paperwork") - 0.05, "t1": at("h01", "paperwork") + 1.6, "items": [{"emoji": "📄", "x": 120, "y": 330, "at": at("h01", "paperwork") - 0.05, "dur": 1.6, "rot": 8}]}); S("pop", at("h01", "paperwork"), -10)
    t3 = at("h01", "three"); cues.append({"type": "stat", "t0": t3 - 0.05, "t1": t3 + 1.7, "num": "3", "label": "AI habits", "sub": "that give you the hours back", "fade_out": 0.2}); S("slam", t3 - 0.05, -8)
if "h02" in IDS:
    t = at("h02", "forty-page", fallback=at("h02", "forty")); insert("b04_database", t - 0.05, 1.5, 2.0)
    t = at("h02", "LawChat"); cues.append({"type": "chips", "t0": t - 0.05, "t1": cend("h02") + 0.1, "side": "lowrow", "fade_out": 0.2, "items": [{"text": "LawChat", "icon": "message-square", "at": t - 0.05}, {"text": "Cited to source", "icon": "badge-check", "at": at("h02", "citation") - 0.05}]}); S("pop", t, -10)
    t = at("h02", "seconds"); cues.append({"type": "emoji", "t0": t - 0.05, "t1": t + 1.4, "items": [{"emoji": "⚡", "x": 780, "y": 320, "at": t - 0.05, "dur": 1.4}]}); S("ding", t, -10)
if "h03" in IDS:
    t = at("h03", "blank"); insert("b02_caseprep", t - 0.05, 1.4, 1.0)
    t = at("h03", "four"); cues.append({"type": "stat", "t0": t - 0.05, "t1": t + 2.2, "num": "4,700+", "label": "document templates", "sub": "petitions · pleadings · notices", "count": True, "fade_out": 0.2}); S("slam", t - 0.05, -8)
    t = at("h03", "Done"); cues.append({"type": "emoji", "t0": t - 0.05, "t1": t + 1.2, "items": [{"emoji": "✅", "x": 760, "y": 330, "at": t - 0.05, "dur": 1.2}]}); S("ding", t, -10)
if "h04" in IDS:
    t = at("h04", "websites"); cues.append({"type": "emoji", "t0": t - 0.05, "t1": t + 1.4, "items": [{"emoji": "😩", "x": 120, "y": 320, "at": t - 0.05, "dur": 1.4, "rot": -10}]}); S("pop", t, -10)
    t = at("h04", "e-Courts", fallback=at("h04", "syncs")); insert("b10_yourcases", t - 0.05, 1.6, 2.5)
    t = at("h04", "one", nth=1, fallback=cend("h04") - 1.0); cues.append({"type": "chips", "t0": t - 0.05, "t1": cend("h04") + 0.1, "side": "lowrow", "fade_out": 0.2, "items": [{"text": "Your Cases", "icon": "copy", "at": t - 0.05}, {"text": "e-Courts synced", "icon": "calendar", "at": t + 0.25}]}); S("pop", t, -10)
if "h05" in IDS:
    t = at("h05", "Fifteen", fallback=at("h05", "15")); insert("b01_features", t - 0.05, 1.5, 3.0)
    cues.append({"type": "stat", "t0": t - 0.02, "t1": t + 1.5, "num": "15", "label": "tools · one login", "fade_out": 0.2}); S("slam", t - 0.05, -8)
    t2 = at("h05", "two", fallback=at("h05", "200")); cues.append({"type": "endc", "t0": t2 - 0.05, "t1": total, "fade_out": 0.01, "amt": "₹200", "what": "free AI credits", "who": "for every new user", "link": "Link below 👇", "link_at": at("h05", "Link", fallback=t2 + 2.0) - 0.05, "logo_at": at("h05", "Go", fallback=cend("h05") - 0.3), "url": "LAWWORLD.AI"}); S("slam", t2 - 0.05, -6); S("ding", at("h05", "Link", fallback=t2 + 2.0), -10)
# flashes + whoosh on every jump cut between segments (skip the first)
for a, b in zip(segs, segs[1:]):
    if b["cid"] != a["cid"] or b["zoom"] != a["zoom"]: flash(b["base"], 0.08); S("whoosh", b["base"] - 0.1, -16)
cues.append({"type": "kcap", "t0": HOOK_END, "t1": pend + 0.3, "words": [{"word": w["word"], "start": w["start"], "end": w["end"]} for w in all_words], "max_words": 3, "max_dur": 1.3})
json.dump({"duration": total, "scrim_from": 9999, "cues": cues}, open(f"{OUT}/timeline.json", "w"), indent=1, ensure_ascii=False)
plan = {"fps": 24, "out": f"{OUT}/creator.mp4", "presenter_start": HOOK_END, "presenter": [{"clip": s["clip"], "in": s["in"], "out": s["out"], "zoom": s["zoom"]} for s in segs], "cutaways": cuts,
        "endcard": {"clip": "brand/cream_tail.mp4", "dur": round(END_HOLD + 0.3, 3), "offset": 0.0, "xfade": 0.3},
        "music": {"file": "audio/bed_creator_60s.mp3", "target_lufs": -24, "fade_in": 0.3, "fade_out": 2.0, "duck": True}, "voice_lufs": -15, "sfx": sfx,
        "grade_presenter": "eq=contrast=1.09:saturation=1.05:brightness=-0.01,unsharp=5:5:0.45:5:5:0",
        "overlays": {"dir": f"{OUT}/frames", "fps": 24}, "delogo": None, "total": total, "tail_black": 0}
json.dump(plan, open(f"{OUT}/plan.json", "w"), indent=1)
print(f"[plan] {len(segs)} segments from {len(IDS)} clips, {len(cuts)} inserts, {len(sfx)} sfx, speech {HOOK_END}-{pend}s, total {total}s")
for s_ in segs: print(f"[plan]  {s_['cid']} {s_['in']:5.2f}-{s_['out']:5.2f} zoom {s_['zoom']} @ {s_['base']}")
