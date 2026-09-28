"""Full explainer: clips + word timings -> timeline.json (overlay cues) + plan.json (compose).
Usage: python3 build_full_plan.py --clips downloads/full --broll downloads/full/broll_3d --music audio/bed_full_170s.mp3 --out out/full"""
import sys, os, json, re, argparse, subprocess
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

ap = argparse.ArgumentParser()
ap.add_argument("--clips", required=True); ap.add_argument("--broll", required=True); ap.add_argument("--music", required=True); ap.add_argument("--out", required=True)
ap.add_argument("--stand_in", default=None, help="dry run: use this clip + synthetic word times for missing clips"); ap.add_argument("--sting_end", type=float, default=2.4); ap.add_argument("--overlap", type=float, default=0.35); ap.add_argument("--end_hold", type=float, default=3.6)
a = ap.parse_args(); os.makedirs(a.out, exist_ok=True)
SKIP = set()   # (2026-09-28: owner first asked to drop Argument Presenter c12, then corrected: Deep Research is the one not launched yet)
IDS = [f"c{i:02d}" for i in range(1, 21) if f"c{i:02d}" not in SKIP]
presenter_start = a.sting_end - a.overlap
clips = []; base = presenter_start; all_words = []
for i, cid in enumerate(IDS):
    c = os.path.join(a.clips, cid + ".mp4"); wj = os.path.join(a.clips, cid + ".words.json")
    if not (os.path.exists(c) and os.path.exists(wj)):
        if not a.stand_in: raise SystemExit(f"[plan] missing {cid} clip or words")
        sc = next(x for x in json.load(open(os.path.join(os.path.dirname(a.clips), "..", "storyboards", "full_all_scenes.json")))["scenes"] if x["sceneId"] == cid)
        t0 = 0.3; words = []
        for wd in sc["dialogue"].split():
            dd = max(0.16, len(wd) / 16.0); words.append({"word": wd, "start": round(t0, 2), "end": round(t0 + dd, 2)}); t0 += dd + 0.05
        c = a.stand_in; w = {"words": words, "speech_start": 0.3, "speech_end": words[-1]["end"]}; print(f"[plan] stand-in for {cid} ({len(words)} words, {w['speech_end']:.1f}s)")
    else:
        w = json.load(open(wj))
    d = dur(c); words = w["words"]; s0, s1 = w["speech_start"], w["speech_end"]
    tin = max(0.0, s0 - 0.45) if (s0 is not None and s0 > 0.9 and i > 0) else 0.0
    tout = min(d, s1 + 0.42) if (s1 is not None and d - s1 > 0.55) else d
    CUT = {"c18": ("end_before", ["pro"], 0.37), "c19": ("start_at", ["so"], 0.24), "c04": ("end_before", ["deep"], 0.32)}   # c04: Deep Research not launched yet   # drop "Pro includes five users ... Pick whichever fits you best."
    if cid in CUT:
        mode, alts, pad = CUT[cid]; r = None
        for alt in alts:
            r = find(words, alt); 
            if r: break
        if r and mode == "end_before": tout = round(r[0] - pad, 3)
        elif r and mode == "start_at": tin = round(max(0.0, r[0] - pad), 3)
        else: print(f"[plan] WARNING {cid}: cut anchor {alts} not found; clip left whole")
    clips.append({"id": cid, "clip": c, "in": round(tin, 3), "out": round(tout, 3), "base": base, "words": words, "dur": d})
    for x in words:
        if x["end"] <= tin or x["start"] >= tout: continue
        all_words.append({"word": x["word"], "start": round(base + x["start"] - tin, 3), "end": round(base + x["end"] - tin, 3)})
    base += tout - tin
presenter_end = base
total = presenter_end + a.end_hold
# captions in the script's own spelling, timed by aligning script tokens to whisper words
import difflib
ORIG = {"c17": "The Pro plan costs just ₹1,500 per month, or ₹12,000 for the whole year, plus GST.",
        "c04": "Everything you need is ready in one place.",
        "c18": "It covers most of your needs, and you pay extra only for add-ons and AI usage.",
        "c19": "So what are you waiting for? Explore LawWorld today.",
        "c20": "New users get ₹200 in free AI credits — click the link below and start using it right now."}
SC = {x["sceneId"]: x for x in json.load(open(os.path.join(os.path.dirname(os.path.abspath(a.clips)), "storyboards", "full_all_scenes.json")))["scenes"]} if False else None
def script_words(c):
    sc_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(a.clips))), "storyboards", "full_all_scenes.json") if False else "storyboards/full_all_scenes.json"
    scenes = {x["sceneId"]: x for x in json.load(open(sc_path))["scenes"]}
    text = ORIG.get(c["id"], scenes[c["id"]]["dialogue"]); toks = [t for t in text.split() if t.strip("—–-")]
    ws = [w for w in c["words"] if w["end"] > c["in"] and w["start"] < c["out"]]
    a_n = [norm(t) or "x" for t in toks]; b_n = [norm(w["word"]) or "x" for w in ws]
    NUMW = {"fifteen": "15", "twelve": "12", "ten": "10", "five": "5", "two": "2"}
    a_n = [NUMW.get(t, t) for t in a_n]; b_n = [NUMW.get(t, t) for t in b_n]
    sm = difflib.SequenceMatcher(a=a_n, b=b_n, autojunk=False); times = [None] * len(toks)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1): times[i1 + k] = (ws[j1 + k]["start"], ws[j1 + k]["end"])
        elif tag == "replace" and j2 > j1:
            t0, t1 = ws[j1]["start"], ws[j2 - 1]["end"]; n = i2 - i1
            for k in range(n): times[i1 + k] = (t0 + (t1 - t0) * k / n, t0 + (t1 - t0) * (k + 1) / n)
    # fill gaps by interpolation between neighbours
    for i in range(len(toks)):
        if times[i] is None:
            prev = next((times[k][1] for k in range(i - 1, -1, -1) if times[k]), c["in"]); nxt = next((times[k][0] for k in range(i + 1, len(toks)) if times[k]), c["out"])
            gap = [k for k in range(i, len(toks)) if times[k] is None and (k == i or times[k - 1] is None)]
            n = 1; k = i
            while k + 1 < len(toks) and times[k + 1] is None: n += 1; k += 1
            for m in range(n): times[i + m] = (prev + (nxt - prev) * m / n, prev + (nxt - prev) * (m + 1) / n)
    return [{"word": toks[i], "start": round(c["base"] + max(c["in"], times[i][0]) - c["in"], 3), "end": round(c["base"] + min(c["out"], times[i][1]) - c["in"], 3)} for i in range(len(toks))]
all_words = [w for c in clips for w in script_words(c)]
C = {c["id"]: c for c in clips}
def T(cid, target, nth=1, edge="start", after=0.0, fallback=None):
    c = C[cid]; r = None
    for alt in (target if isinstance(target, (list, tuple)) else [target]):
        r = find(c["words"], alt, nth, after)
        if r: break
    if not r:
        fb = fallback if fallback is not None else 0.0
        print(f"[plan] WARNING {cid}: '{target}' not found; fallback +{fb}s from clip start"); return round(c["base"] + fb, 3)
    v = r[0] if edge == "start" else r[1]
    return round(c["base"] + v - c["in"], 3)
def S(cid): return round(C[cid]["base"], 3)            # clip start on the timeline
def E(cid): return round(C[cid]["base"] + C[cid]["out"] - C[cid]["in"], 3)  # clip end
B = lambda name: os.path.join(a.broll, name + "_broll.mp4")
cues = []; cuts = []
def cut(name, t0, t1, offset=0.0):
    p = B(name)
    if not os.path.exists(p): print(f"[plan] WARNING no B-roll {name}; presenter stays on screen"); return False
    if t1 - t0 > 9.9: print(f"[plan] WARNING cut {name} {t1-t0:.1f}s > clip; clamped"); t1 = round(t0 + 9.9, 3)
    cuts.append({"clip": p, "start": round(t0, 3), "end": round(t1, 3), "offset": offset, "fade": 0.2}); return True

cues.append({"type": "sting", "t0": 0, "t1": a.sting_end, "fade_out": a.overlap, "tag": "The all-in-one AI platform for advocates"})
# c01
t = T("c01", "Ravishankar", fallback=3.0); cues.append({"type": "lower_third", "t0": t - 0.1, "t1": t + 4.8, "name": "Ravishankar", "role": "Founder, LawWorld"})
# c02 pills -> lockup -> 15+ over b01
tb, tf, tc = T("c02", "better", fallback=1.5), T("c02", "faster", fallback=2.0), T("c02", "cheaper", fallback=2.6)
tlet = T("c02", "let", fallback=3.6); tlw1 = T("c02", "lawworld", 1, fallback=4.6); tlw2 = find(C["c02"]["words"], "lawworld", 2)
t15 = T("c02", ["fifteen", "15"], fallback=8.6)
cut1_0 = round((C["c02"]["base"] + tlw2[0] - C["c02"]["in"]) if tlw2 else t15 - 1.3, 3) - 0.12
tfor = T("c03", ["for"], fallback=5.0); cut1_1 = tfor - 0.08
cues.append({"type": "pills", "t0": tb - 0.05, "t1": tlet - 0.1, "items": [{"text": "Better", "at": tb - 0.05}, {"text": "Faster", "at": tf - 0.05}, {"text": "Cheaper", "at": tc - 0.05}]})
cues.append({"type": "lockup", "t0": tlw1 - 0.1, "t1": cut1_0, "fade_out": 0.25})
if cut("b01_features", cut1_0, cut1_1): cues.append({"type": "bignum", "t0": t15 - 0.1, "t1": cut1_1, "num": "15+", "label": "features", "fade_out": 0.3})
# c03 second sentence + c04 first sentence: presenter + case-prep chips; then Deep Research over b03
DEEP_REMOVED = "c04" in CUT
tdeep = E("c04") if DEEP_REMOVED else T("c04", "deep", fallback=3.0)
cues.append({"type": "chapter", "t0": tfor, "t1": tdeep - 0.1, "text": "Case preparation", "fade_out": 0.3})
cues.append({"type": "chips", "t0": T("c03", "chatbot", fallback=6.5) - 0.15, "t1": tdeep - 0.1, "side": "lowrow", "fade_out": 0.3, "items": [
  {"text": "AI Chatbot", "icon": "message-square", "at": T("c03", "chatbot", fallback=6.5) - 0.15}, {"text": "Drafting", "icon": "file-pen", "at": T("c03", "drafting", fallback=7.3) - 0.1},
  {"text": "Legal Research", "icon": "search", "at": T("c03", "research", fallback=8.3) - 0.1}, {"text": "Translation", "icon": "languages", "at": T("c03", "translation", fallback=9.1) - 0.1}]})
if (not DEEP_REMOVED) and cut("b03_deepresearch", tdeep - 0.1, E("c04")):
    cues.append({"type": "title", "t0": tdeep, "t1": E("c04"), "title": "Deep Research", "sub": "Hand over your documents", "sub_at": T("c04", "documents", fallback=5.5), "fade_out": 0.3})
    cues.append({"type": "chips", "t0": T("c04", "reads", fallback=6.5) - 0.1, "t1": E("c04"), "side": "row", "fade_out": 0.3, "items": [
      {"text": "Reads", "icon": "book-open", "at": T("c04", "reads", fallback=6.5) - 0.1}, {"text": "Reasons", "icon": "brain", "at": T("c04", "reasons", fallback=7.2) - 0.1}, {"text": "Case-ready citations", "icon": "sparkles", "at": T("c04", ["case-ready", "caseready", "case"], 1, after=6.0, fallback=8.2) - 0.1}]})
# c05 database over b04
if cut("b04_database", S("c05"), E("c05")):
    cues.append({"type": "title", "t0": S("c05") + 0.1, "t1": E("c05"), "title": "Legal database", "sub": "All your legal data, on one platform", "sub_at": T("c05", "together", fallback=5.5), "fade_out": 0.3})
    cues.append({"type": "chips", "t0": T("c05", "judgments", fallback=2.0) - 0.1, "t1": E("c05"), "side": "row", "fade_out": 0.3, "items": [
      {"text": "Judgments", "icon": "landmark", "at": T("c05", "judgments", fallback=2.0) - 0.1}, {"text": "Acts", "icon": "file-text", "at": T("c05", "acts", fallback=2.6) - 0.1},
      {"text": "Rules", "icon": "book", "at": T("c05", "rules", fallback=3.0) - 0.1}, {"text": "Regulations", "icon": "layers", "at": T("c05", "regulations", fallback=3.5) - 0.1}]})
# c06 library: presenter + chips
cues.append({"type": "chapter", "t0": S("c06") + 0.1, "t1": E("c06") - 0.1, "text": "Library", "fade_out": 0.3})
cues.append({"type": "chips", "t0": T("c06", ["e-books", "ebooks"], fallback=1.6) - 0.1, "t1": E("c06") - 0.1, "side": "lowrow", "fade_out": 0.3, "items": [
  {"text": "E-books", "icon": "book-open", "at": T("c06", ["e-books", "ebooks"], fallback=1.6) - 0.1}, {"text": "Videos", "icon": "monitor-play", "at": T("c06", "videos", fallback=2.3) - 0.1},
  {"text": "Grow every day", "icon": "graduation-cap", "at": T("c06", "grow", fallback=5.0) - 0.1}]})
# c07 slides over b06
if cut("b06_slides", S("c07"), E("c07")):
    cues.append({"type": "title", "t0": S("c07") + 0.1, "t1": E("c07"), "title": "Slides", "sub": "Ready-made presentations on law", "sub_at": T("c07", "presentations", fallback=1.8), "fade_out": 0.3})
    cues.append({"type": "chips", "t0": T("c07", "teach", fallback=4.5) - 0.1, "t1": E("c07"), "side": "row", "fade_out": 0.3, "items": [
      {"text": "Teach", "icon": "presentation", "at": T("c07", "teach", fallback=4.5) - 0.1}, {"text": "Train juniors", "icon": "users", "at": T("c07", "juniors", fallback=5.8) - 0.1}, {"text": "Explain with clarity", "icon": "sparkles", "at": T("c07", "clarity", fallback=8.6) - 0.1}]})
# c08 law stories over b07
if cut("b07_lawstories", S("c08"), E("c08")):
    cues.append({"type": "title", "t0": S("c08") + 0.1, "t1": E("c08"), "title": "Law Stories", "sub": "Audio discussions on legal topics", "sub_at": T("c08", "audio", fallback=2.4), "fade_out": 0.3})
    cues.append({"type": "chips", "t0": T("c08", "move", fallback=5.4) - 0.1, "t1": E("c08"), "side": "row", "fade_out": 0.3, "items": [
      {"text": "Listen on the move", "icon": "headphones", "at": T("c08", "move", fallback=5.4) - 0.1}, {"text": "While travelling", "icon": "map-pin", "at": T("c08", ["travelling", "traveling"], fallback=6.2) - 0.1}]})
# c09 languages over b08
if cut("b08_languages", S("c09"), E("c09")):
    cues.append({"type": "bignum", "t0": T("c09", ["ten", "10"], fallback=4.0) - 0.1, "t1": E("c09"), "num": "10+", "label": "Indian languages", "fade_out": 0.3})
# c10 client management: presenter + chips
cues.append({"type": "chapter", "t0": S("c10") + 0.1, "t1": E("c10") - 0.1, "text": "Client management", "fade_out": 0.3})
cues.append({"type": "chips", "t0": T("c10", "chat", fallback=2.4) - 0.1, "t1": E("c10") - 0.1, "side": "lowrow", "fade_out": 0.3, "items": [
  {"text": "Team Chat", "icon": "users", "at": T("c10", "chat", fallback=2.4) - 0.1}, {"text": "Billing", "icon": "receipt-indian-rupee", "at": T("c10", "billing", fallback=3.2) - 0.1},
  {"text": "Client Portal", "icon": "shield-check", "at": T("c10", "portal", fallback=4.2) - 0.1}]})
# c11 your cases over b10
if cut("b10_yourcases", S("c11"), E("c11")):
    cues.append({"type": "title", "t0": S("c11") + 0.1, "t1": E("c11"), "title": "Your Cases", "sub": "Connected to e-Courts", "sub_at": T("c11", ["e-courts", "ecourts", "courts"], fallback=2.2), "fade_out": 0.3})
    cues.append({"type": "chips", "t0": T("c11", "case", 1, after=2.5, fallback=4.2) - 0.1, "t1": E("c11"), "side": "row", "fade_out": 0.3, "items": [
      {"text": "Every case", "icon": "copy", "at": T("c11", "case", 1, after=2.5, fallback=4.2) - 0.1}, {"text": "Hearings", "icon": "calendar", "at": T("c11", "hearing", fallback=4.8) - 0.1}, {"text": "Orders", "icon": "gavel", "at": T("c11", "order", fallback=5.3) - 0.1}]})
# c12 argument presenter over b11
if "c12" in C and cut("b11_argument", S("c12"), E("c12")):
    cues.append({"type": "title", "t0": S("c12") + 0.1, "t1": E("c12"), "title": "Argument Presenter", "sub": "No heavy files to carry", "sub_at": T("c12", "files", fallback=6.0), "fade_out": 0.3})
# c13 security: presenter + shield chips
cues.append({"type": "chapter", "t0": S("c13") + 0.1, "t1": E("c13") - 0.1, "text": "Security", "fade_out": 0.3})
cues.append({"type": "chips", "t0": T("c13", ["dpdp"], fallback=3.2) - 0.1, "t1": E("c13") - 0.1, "side": "lowrow", "fade_out": 0.3, "items": [
  {"text": "DPDP Act compliant", "icon": "shield-check", "at": T("c13", ["dpdp"], fallback=3.2) - 0.1}, {"text": "Private", "icon": "lock", "at": T("c13", "private", fallback=5.6) - 0.1},
  {"text": "In your control", "icon": "check", "at": T("c13", "control", fallback=7.0) - 0.1}]})
# c14 devices over b13
if cut("b13_devices", S("c14"), E("c14")):
    cues.append({"type": "chips", "t0": T("c14", "web", fallback=2.0) - 0.1, "t1": E("c14"), "side": "row", "fade_out": 0.3, "items": [
      {"text": "Web", "icon": "monitor", "at": T("c14", "web", fallback=2.0) - 0.1}, {"text": "Android", "icon": "smartphone", "at": T("c14", "android", fallback=2.7) - 0.1}, {"text": "iOS", "icon": "tablet", "at": T("c14", "ios", fallback=3.4) - 0.1}]})
    cues.append({"type": "title", "t0": T("c14", "office", fallback=5.5) - 0.1, "t1": E("c14"), "title": "Work anywhere", "sub": "From your office or on the move", "sub_at": T("c14", "move", fallback=7.5), "fade_out": 0.3})
# c15 training: presenter first sentence, then b14
ttrain = T("c15", "training", fallback=2.8)
cues.append({"type": "chips", "t0": T("c15", "new", fallback=1.4) - 0.1, "t1": ttrain - 0.1, "side": "lowrow", "fade_out": 0.25, "items": [{"text": "New to AI? No problem", "icon": "sparkles", "at": T("c15", "new", fallback=1.4) - 0.1}]})
if cut("b14_training", ttrain - 0.1, E("c15")):
    cues.append({"type": "title", "t0": ttrain, "t1": E("c15"), "title": "Training videos", "sub": "Basic computer skills are enough", "sub_at": T("c15", "basic", fallback=6.5), "fade_out": 0.3})
# c16-c18 pricing canvas
tp0 = T("c16", "two", fallback=0.8) - 0.1; tp1 = S("c19") + 0.35
cues.append({"type": "pricing", "t0": tp0, "t1": tp1, "fade_out": 0.35, "heading_at": tp0 + 0.1,
  "payg_at": T("c16", ["pay-as-you-go", "payasyougo", "pay"], 1, after=1.5, fallback=3.2) - 0.1, "payg_lines": [
      {"text": "No monthly fee", "at": T("c16", "monthly", fallback=5.0) - 0.1}, {"text": "Pay only for what you use", "at": T("c16", "only", fallback=6.6) - 0.1}],
  "pro_at": T("c17", "pro", fallback=0.6) - 0.1, "pro_lines": [
      {"text": "₹1,500 / month", "at": T("c17", ["fifteen", "1500", "1,500"], fallback=2.2) - 0.1}, {"text": "₹12,000 / year", "at": T("c17", ["twelve", "12000", "12,000"], fallback=4.2) - 0.1},
      {"text": "+ GST", "at": T("c17", "gst", fallback=6.2) - 0.1}, {"text": "Covers most of your needs", "at": T("c18", "covers", fallback=0.4) - 0.1},
      {"text": "Add-ons & AI usage extra", "at": T("c18", ["add-ons", "addons", "add"], fallback=3.5) - 0.1}]})
# c18 tail + c19: presenter, lockup on "Explore LawWorld"
texp = T("c19", "explore", fallback=3.8); cues.append({"type": "lockup", "t0": texp - 0.1, "t1": E("c19"), "fade_out": 0.25})
# c20 CTA canvas to the end
cues.append({"type": "cta", "t0": S("c20"), "t1": total, "fade_out": 0.01, "credit_at": T("c20", ["two", "200", "₹200"], fallback=1.2) - 0.1, "link_at": T("c20", "click", fallback=5.2) - 0.1, "logo_at": T("c20", "start", fallback=7.5) - 0.1, "url": "lawworld.ai"})
cues.append({"type": "captions", "t0": presenter_start, "t1": presenter_end + 0.5, "words": all_words, "max_words": 4, "max_dur": 1.7})
json.dump({"duration": round(total, 3), "scrim_from": presenter_start, "cues": cues}, open(os.path.join(a.out, "timeline.json"), "w"), indent=1)
plan = {"fps": 24, "out": os.path.join(a.out, "full.mp4"), "presenter_start": presenter_start,
        "presenter": [{"clip": c["clip"], "in": c["in"], "out": c["out"]} for c in clips], "cutaways": cuts,
        "endcard": {"clip": "brand/cream_tail.mp4", "dur": round(a.end_hold + 0.3, 3), "offset": 0.0, "xfade": 0.3},
        "music": {"file": a.music, "target_lufs": -29, "fade_in": 1.2, "fade_out": 3.0, "duck": True}, "voice_lufs": -16,
        "overlays": {"dir": os.path.join(a.out, "frames"), "fps": 24}, "delogo": None, "total": round(total, 3), "tail_black": 0}
json.dump(plan, open(os.path.join(a.out, "plan.json"), "w"), indent=1)
print(f"[plan] presenter {presenter_start:.2f}-{presenter_end:.2f}s, {len(cuts)} cut-aways, total {total:.2f}s")
for c in clips: print(f"[plan]  {c['id']}: {c['base']:6.2f}s  in {c['in']} out {c['out']} of {c['dur']:.2f}")
for k in cues:
    if k["type"] != "captions": print(f"[plan]  cue {k['type']:<12} {k['t0']:>7} -> {k['t1']}")
