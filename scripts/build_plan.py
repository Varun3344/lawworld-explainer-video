"""Turn the sample's clips + word timings into (a) timeline.json for the overlay renderer and (b) plan.json for compose.py.
Usage: python3 build_plan.py --sb storyboards/sample_presenter.json --clips a.ravi.mp4 b.ravi.mp4 c.ravi.mp4 \
         --b01 downloads/sample/broll_3d/b01_features_broll.mp4 --b02 .../b02_caseprep_broll.mp4 --music audio/bed.mp3 --out out/sample"""
import sys, os, json, re, argparse, subprocess
def norm(w): return re.sub(r"[^a-z0-9']+", "", w.lower().replace("’", "'"))
def dur(f): return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f],capture_output=True,text=True).stdout.strip())

def find(words, target, nth=1, after=0.0):
    """Start/end (source seconds) of the nth occurrence of `target` (normalised, may span 1-3 whisper tokens)."""
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
ap.add_argument("--sb", required=True); ap.add_argument("--clips", nargs="+", required=True)
ap.add_argument("--b01"); ap.add_argument("--b02"); ap.add_argument("--music", required=True); ap.add_argument("--out", required=True)
ap.add_argument("--sting_end", type=float, default=2.3); ap.add_argument("--overlap", type=float, default=0.35)
ap.add_argument("--endcard_dur", type=float, default=3.4); ap.add_argument("--xfade", type=float, default=0.4)
a = ap.parse_args()
os.makedirs(a.out, exist_ok=True)

presenter_start = a.sting_end - a.overlap
clips = []; base = presenter_start; all_words = []
for i, c in enumerate(a.clips):
    wj = json.load(open(c[:-4] + ".words.json"))
    d = dur(c); words = wj["words"]
    s0, s1 = wj["speech_start"], wj["speech_end"]
    tin = max(0.0, s0 - 0.5) if (s0 is not None and s0 > 0.9) else 0.0
    tout = min(d, s1 + 0.45) if (s1 is not None and d - s1 > 0.6) else d
    if i == 0: tin = 0.0  # keep the natural lead-in on the opening clip
    clips.append({"clip": c, "in": round(tin, 3), "out": round(tout, 3), "base": base, "words": words, "dur": d})
    for w in words:
        if w["end"] <= tin or w["start"] >= tout: continue
        all_words.append({"word": w["word"], "start": round(base + w["start"] - tin, 3), "end": round(base + w["end"] - tin, 3)})
    base += tout - tin
presenter_end = base
total = presenter_end + a.endcard_dur - a.xfade

def A(ci, target, nth=1, edge="start", after=0.0):
    c = clips[ci]; r = None
    for alt in (target if isinstance(target, (list, tuple)) else [target]):
        r = find(c["words"], alt, nth, after)
        if r: break
    if not r: return None
    s, e = r; v = s if edge == "start" else e
    return round(c["base"] + v - c["in"], 3)

def need(v, what, fallback):
    if v is None: print(f"[plan] WARNING: could not find {what}; using fallback {fallback}"); return fallback
    return v

cues = [{"type": "sting", "t0": 0, "t1": a.sting_end, "fade_out": a.overlap, "tag": "AI platform for advocates"}]
# clip 1: lower third on the name
t_name = need(A(0, "Ravishankar"), "'Ravishankar' in clip 1", clips[0]["base"] + 3.0)
cues.append({"type": "lower_third", "t0": round(t_name - 0.1, 3), "t1": round(t_name + 4.8, 3), "name": "Ravishankar", "role": "Founder, LawWorld"})
# clip 2: pills -> lockup -> 3D cut-away with 15+
t_better = need(A(1, "better"), "'better'", clips[1]["base"] + 2.0)
t_faster = need(A(1, "faster"), "'faster'", t_better + 0.5)
t_cheaper = need(A(1, "cheaper"), "'cheaper'", t_faster + 0.6)
t_let = need(A(1, "let"), "'let me introduce'", t_cheaper + 1.2)
t_lw_intro = need(A(1, "lawworld", 1, after=0.0), "'LawWorld' (introduce)", t_let + 0.9)
t_lw_has = A(1, "lawworld", 2)
t_fifteen = need(A(1, ["fifteen", "15"]), "'fifteen'", clips[1]["base"] + 8.6)
cut_start = round((t_lw_has if t_lw_has else t_fifteen - 1.3) - 0.12, 3)
t_for = need(A(2, "for"), "'For case preparation'", clips[2]["base"] + 5.0)
cut_end = round(t_for - 0.08, 3)
if cut_end - cut_start > 9.9: print("[plan] WARNING: cut-away longer than the B-roll clip; clamping"); cut_end = round(cut_start + 9.9, 3)
cues.append({"type": "pills", "t0": round(t_better - 0.05, 3), "t1": round(t_let - 0.1, 3), "items": [
    {"text": "Better", "at": round(t_better - 0.05, 3)}, {"text": "Faster", "at": round(t_faster - 0.05, 3)}, {"text": "Cheaper", "at": round(t_cheaper - 0.05, 3)}]})
cues.append({"type": "lockup", "t0": round(t_lw_intro - 0.1, 3), "t1": cut_start, "fade_out": 0.25})
cues.append({"type": "bignum", "t0": round(t_fifteen - 0.1, 3), "t1": cut_end, "num": "15+", "label": "features", "fade_out": 0.3})
# clip 3: chapter + chips over the presenter
t_chat = need(A(2, "chatbot"), "'chatbot'", t_for + 2.0)
t_draft = need(A(2, "drafting"), "'drafting'", t_chat + 0.8)
t_res = need(A(2, "research"), "'research'", t_draft + 1.0)
t_tr = need(A(2, "translation"), "'translation'", t_res + 0.9)
cues.append({"type": "chapter", "t0": round(cut_end + 0.05, 3), "t1": round(presenter_end - 0.1, 3), "text": "01 · Case preparation", "fade_out": 0.3})
cues.append({"type": "chips", "t0": round(t_chat - 0.1, 3), "t1": round(presenter_end - 0.1, 3), "top": 400, "fade_out": 0.3, "items": [
    {"text": "AI Chatbot", "icon": "chat", "at": round(t_chat - 0.1, 3)}, {"text": "Drafting", "icon": "draft", "at": round(t_draft - 0.1, 3)},
    {"text": "Legal Research", "icon": "research", "at": round(t_res - 0.1, 3)}, {"text": "Translation", "icon": "translate", "at": round(t_tr - 0.1, 3)}]})
cues.append({"type": "captions", "t0": presenter_start, "t1": presenter_end, "words": all_words, "max_words": 4, "max_dur": 1.7})
cues.append({"type": "endcard", "t0": round(presenter_end - a.xfade, 3), "t1": round(total, 3), "url": "lawworld.ai", "fade_out": 0.01})
timeline = {"duration": round(total, 3), "scrim_from": presenter_start, "cues": cues}
json.dump(timeline, open(os.path.join(a.out, "timeline.json"), "w"), indent=1)

plan = {"fps": 24, "out": os.path.join(a.out, "sample.mp4"), "presenter_start": presenter_start,
        "presenter": [{"clip": c["clip"], "in": c["in"], "out": c["out"]} for c in clips],
        "cutaways": ([{"clip": a.b01, "start": cut_start, "end": cut_end, "offset": 0.0, "fade": 0.2}] if a.b01 else []),
        "endcard": ({"clip": a.b02, "dur": a.endcard_dur, "offset": 0.0, "xfade": a.xfade} if a.b02 else None),
        "music": {"file": a.music, "target_lufs": -33, "fade_in": 1.2, "fade_out": 2.5, "duck": True},
        "voice_lufs": -16, "overlays": {"dir": os.path.join(a.out, "frames"), "fps": 24},
        "delogo": None, "total": round(total, 3)}  # delogo None: no corner mark on the main (ULTRA) account's clips today
json.dump(plan, open(os.path.join(a.out, "plan.json"), "w"), indent=1)
print(f"[plan] presenter {presenter_start:.2f}-{presenter_end:.2f}s, cut-away {cut_start}-{cut_end}s, total {total:.2f}s")
for c in clips: print(f"[plan]  {os.path.basename(c['clip'])}: in {c['in']} out {c['out']} of {c['dur']:.2f}")
for k in cues:
    if k["type"] != "captions": print(f"[plan]  cue {k['type']:<12} {k['t0']:>6} -> {k['t1']}")
