"""16:9 split-screen explainer (Cause of Action, first minute): presenter clips c01..c09 on the left, animated panel
(overlays/split_panel.html) on the right. Default = v2 layout (16:9 walnut-studio clips in downloads/split, presenter 55 % / panel
45 %, out/split). --wide = v3 "one screen" layout (owner 15-10-2026: avatar 33 %, explanation 66 %, avatar background = panel
background): 9:16 ivory-backdrop clips in downloads/split9, composed from downloads/split9/flat (backdrop flattened to the panel
cream by split/flatten_bg.py), presenter box 640 px, no eq grade (it would lift the flattened backdrop off the cream), out/split9. Builds land on the spoken words: script tokens are aligned to whisper word
times (same alignment as office/build_office_plan.py), clip head/tail pauses are trimmed, clips are laid end to end after
the opening sting. Any anchor word that cannot be found is FATAL (a silently mistimed build is worse than a stop).
Writes out/split/timeline.json, out/split/plan.json, out/split/anchors.txt and out/split/captions.srt."""
import os, sys, json, subprocess, difflib, importlib.util
spec = importlib.util.spec_from_file_location("words", "scripts/words.py"); W = importlib.util.module_from_spec(spec); spec.loader.exec_module(W); norm = W.norm
def dur(f): return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f],capture_output=True,text=True).stdout.strip())

WIDE = "--wide" in sys.argv
D = "downloads/split9" if WIDE else "downloads/split"; OUT = "out/split9" if WIDE else "out/split"; os.makedirs(OUT, exist_ok=True)
CLIPS = f"{D}/flat" if WIDE else D                                   # what compose2 reads (words/timing always come from D)
SCENES = "split/split9_all_scenes.json" if WIDE else "split/split_all_scenes.json"
BOX_W = 640 if WIDE else 1056
ALL = json.load(open(SCENES))["scenes"]
SCRIPT = {s["sceneId"]: s["spoken"] for s in ALL}                 # what the avatar was asked to say (alignment)
SHOWN = {                                                            # how the words are written on screen / in captions
    "c05": "The classic statement comes from an English case, Read v. Brown, decided in 1888.",
    "c07": "Our Supreme Court adopted this in A.B.C. Laminart v. A.P. Agencies,",
    "c08": "and put it simply: a bundle of facts which, with the law that applies to them, gives the plaintiff a right to relief against the defendant.",
}
IDS = [s["sceneId"] for s in ALL]
missing = [c for c in IDS if not (os.path.exists(f"{D}/{c}.mp4") and os.path.exists(f"{CLIPS}/{c}.mp4"))]
if missing and "--allow-missing" not in sys.argv: sys.exit(f"[plan] missing clips: {missing}")
# a retake replaces downloads/split9/cNN.mp4 but not its flattened copy: composing the old take with the new take's word times
# would mistime every build, so a flat clip older than its source is FATAL (re-run split/flatten_bg.py on it)
stale = [c for c in IDS if c not in missing and CLIPS != D and os.path.getmtime(f"{CLIPS}/{c}.mp4") < os.path.getmtime(f"{D}/{c}.mp4")]
if stale: sys.exit(f"[plan] FATAL flattened clips older than their source (retake?): {stale} -> python3 split/flatten_bg.py " + " ".join(f"{D}/{c}.mp4" for c in stale))
IDS = [c for c in IDS if c not in missing]
FX = json.load(open(f"{OUT}/face_x.json")) if os.path.exists(f"{OUT}/face_x.json") else {}
ZOOM = {c: (1.0 if i % 2 == 0 else 1.06) for i, c in enumerate(IDS)}   # alternate punch-in hides the cut between clips
HOOK = 1.6; END = 3.2

t = HOOK; segs = []; words = []
for cid in IDS:
    c = f"{D}/{cid}.mp4"; d = dur(c); ws = json.load(open(f"{D}/{cid}.words.json"))["words"]
    toks = [x for x in SCRIPT[cid].split() if x.strip("—–-")]
    sm = difflib.SequenceMatcher(a=[norm(x) or "x" for x in toks], b=[norm(w["word"]) or "x" for w in ws], autojunk=False); tm = [None] * len(toks)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1): tm[i1 + k] = (ws[j1 + k]["start"], ws[j1 + k]["end"])
        elif tag == "replace" and j2 > j1:
            a, b = ws[j1]["start"], ws[j2 - 1]["end"]; n = i2 - i1
            for k in range(n): tm[i1 + k] = (a + (b - a) * k / n, a + (b - a) * (k + 1) / n)
    for i in range(len(toks)):
        if tm[i] is None:
            p = next((tm[k][1] for k in range(i - 1, -1, -1) if tm[k]), 0.0); q = next((tm[k][0] for k in range(i + 1, len(toks)) if tm[k]), d); tm[i] = (p, min(q, p + 0.3))
    s0 = tm[0][0]; s1 = tm[-1][1]
    tin = max(0.0, s0 - 0.12); tout = d if cid == IDS[-1] else min(d, s1 + 0.28)   # the last clip runs to its end: room for the payoff before the end card
    segs.append({"clip": f"{CLIPS}/{cid}.mp4", "in": round(tin, 3), "out": round(tout, 3), "zoom": ZOOM[cid], "base": round(t, 3), "cid": cid, "fx": FX.get(cid)})
    for i, x in enumerate(toks): words.append({"word": x, "start": round(t + tm[i][0] - tin, 3), "end": round(t + tm[i][1] - tin, 3), "cid": cid})
    t += tout - tin
pend = round(t, 3); total = round(pend + END, 3)

ANCH = []
def at(cid, target, nth=1):
    tg = [norm(x) for x in (target if isinstance(target, list) else [target])]; h = 0
    for w in words:
        if w["cid"] != cid: continue
        n = norm(w["word"])
        if any(n == g or (len(g) >= 4 and n.startswith(g)) for g in tg):
            h += 1
            if h == nth: ANCH.append(f"{cid:4} {str(target):28} -> {w['start']:7.3f}  ({w['word']})"); return w["start"]
    sys.exit(f"[plan] FATAL {cid}: anchor {target!r} (#{nth}) not found in {[w['word'] for w in words if w['cid'] == cid]}")
S = lambda cid: next(s["base"] for s in segs if s["cid"] == cid)
E = lambda cid: next(round(s["base"] + s["out"] - s["in"], 3) for s in segs if s["cid"] == cid)
r3 = lambda x: round(x, 3)
cues = []; sfx = []
def fx(n, tt, g=-16): sfx.append({"file": f"audio/sfx/{n}.mp3", "at": r3(max(0, tt)), "gain_db": g})
def cue(**k): cues.append({kk: (r3(v) if isinstance(v, float) else v) for kk, v in k.items()})

# ── opening sting (frame 0 = finished card = thumbnail) and the persistent panel ─────────────────────────────────────────
cue(type="sting", t0=0.0, t1=HOOK + 0.35, kicker="CIVIL PROCEDURE · EXPLAINED", title="Cause of Action", sub="The starting point of every civil suit")
fx("slam", 0.02, -8); fx("riser", HOOK - 0.9, -18)
cue(type="panel", t0=HOOK - 0.3, t1=pend + 0.25, scenes=[{"at": r3(HOOK), "label": "1 · THE HOOK"}, {"at": r3(S("c04") - 0.1), "label": "2 · WHAT IT IS"}])
cue(type="lower_third", t0=S("c01") + 0.5, t1=S("c01") + 5.2, name="Ravishankar", role="LawWorld")

# ── Scene 1: hook ──────────────────────────────────────────────────────────────────────────────────────────────────────
q_at = at("c02", "do") - 0.1
cue(type="title", t0=HOOK, t1=q_at - 0.05, title="CAUSE OF ACTION", title_at=S("c01") + 0.1, sub="The starting point of every civil suit", sub_at=at("c01", "begins"))
fx("pop", S("c01") + 0.1, -18); fx("pop", at("c01", "begins"), -20)
st_at = at("c02", "thrown") - 0.12
cue(type="question", t0=q_at - 0.05, t1=E("c02") + 0.05, at=q_at, text="Do you have a cause of action?", hl="cause of action")
cue(type="stamp", t0=st_at - 0.05, t1=E("c02") + 0.05, at=st_at, line1="NO CAUSE OF ACTION", line2="= PLAINT REJECTED")
fx("whoosh", q_at - 0.12, -18); fx("slam", st_at + 0.06, -9)
items = [{"n": 1, "text": "What it is", "at": r3(at("c03", "what") - 0.08)},
         {"n": 2, "text": "How to spot it", "at": r3(at("c03", "how") - 0.08)},
         {"n": 3, "text": "Why it matters", "at": r3(at("c03", "why") - 0.08)}]
cue(type="list", t0=S("c03"), t1=E("c03") + 0.05, head="In the next 5 minutes", head_at=at("c03", "next") - 0.1, items=items)
fx("pop", at("c03", "next") - 0.1, -18)
for it in items: fx("pop", it["at"], -16)

# ── Scene 2: what it is ────────────────────────────────────────────────────────────────────────────────────────────────
fx("whoosh", S("c04") - 0.15, -16)
cpc = at("c04", "code") - 0.1
cue(type="strike", t0=S("c04"), t1=E("c04") + 0.05, text="CPC, 1908: no definition", at=cpc, strike_at=at("c04", "never"), icon="book-open")
courts = at("c04", "comes") - 0.05
cue(type="point", t0=courts - 0.05, t1=E("c04") + 0.05, text="Defined by the courts", at=courts, icon="landmark", accent=True)
fx("pop", cpc, -16); fx("whoosh", at("c04", "never") + 0.1, -20); fx("ding", courts, -18)
cue(type="kicker", t0=S("c05"), t1=E("c06") + 0.05, at=at("c05", "classic") - 0.1, text="THE CLASSIC DEFINITION")
rb = at("c05", ["read", "reid", "reed"]) - 0.1
cue(type="cite", t0=rb - 0.05, t1=E("c06") + 0.02, at=rb, text="Read v. Brown (1888) 22 QBD 128", tag="ENGLISH COURT OF APPEAL")
fx("pop", rb, -16)
qa = at("c05", "statement") - 0.05   # the classic statement appears as he names it, and keeps revealing through his paraphrase
cue(type="quote", t0=qa - 0.05, t1=E("c06") + 0.02, at=qa, reveal=r3(min(6.0, max(3.5, S("c06") + 1.0 - qa))),
    text="Every fact which it would be necessary for the plaintiff to prove, if traversed, in order to support his right to the judgment of the Court.",
    hl=["every fact", "to prove", "if traversed"], note={"text": "traversed = denied", "at": r3(at("c06", "denied") - 0.05)})
fx("whoosh", qa - 0.1, -20); fx("pop", at("c06", "denied") - 0.05, -18)
sc = at("c07", "supreme") - 0.1
cue(type="point", t0=sc - 0.05, t1=E("c07") + 0.05, text="Adopted by the Supreme Court of India", at=sc, icon="landmark", accent=False)
lam = at("c07", ["laminart", "laminar", "lamina"]) - 0.25
cue(type="cite", t0=lam - 0.05, t1=E("c08") + 0.05, at=lam, text="A.B.C. Laminart Pvt. Ltd. v. A.P. Agencies, Salem (1989) 2 SCC 163", tag="SUPREME COURT OF INDIA")
fx("pop", sc, -18); fx("pop", lam, -16)
b1 = at("c08", "bundle") - 0.1; b2 = at("c08", "law") - 0.1; b3 = at("c08", "right") - 0.1
cue(type="equation", t0=S("c08"), t1=E("c08") + 0.05,
    terms=[{"text": "BUNDLE OF FACTS", "at": r3(b1)}, {"op": "+", "text": "APPLICABLE LAW", "at": r3(b2)}, {"op": "=", "text": "RIGHT TO RELIEF", "at": r3(b3), "result": True}])
fx("pop", b1, -16); fx("pop", b2, -16); fx("ding", b3, -14)
one = at("c09", "one") - 0.05; many = at("c09", "every") - 0.25; gather = at("c09", "every") + 0.45   # tied by "...you need", label holds before the end card
cue(type="bundle", t0=S("c09"), t1=pend + 0.25, one_at=one, many_at=many, gather_at=gather, label="Bundle of facts",
    icons=["file-text", "calendar", "indian-rupee", "handshake", "pen-line", "receipt", "file-signature"])
fx("pop", one, -16); fx("whoosh", many, -20); fx("whoosh", gather, -18); fx("ding", gather + 0.55, -16)

# ── close ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="endcard", t0=pend + 0.2, t1=total, title="Cause of Action", sub="Up next: Right + breach", url="lawworld.ai")
fx("whoosh", pend + 0.1, -16)

json.dump({"duration": total, "width": 1920, "height": 1080, **({"layout": {"px": BOX_W}} if WIDE else {}), "cues": cues}, open(f"{OUT}/timeline.json", "w"), indent=1, ensure_ascii=False)
plan = {"fps": 24, "out": f"{OUT}/split_sample.mp4", "size": [1920, 1080],
        # wide: fy 0.78 crops the top ~50 source px, where the 9:16 ivory clips carry a dark cove line at y≈36 that would end at the seam
        "presenter_box": {"x": 0, "y": 0, "w": BOX_W, "h": 1080, "fx": 0.5, "fy": 0.78 if WIDE else 0.35, "pad": "0xf5f0e8"},
        "presenter_start": HOOK,
        "presenter": [{k: v for k, v in {"clip": s["clip"], "in": s["in"], "out": s["out"], "zoom": s["zoom"], "push": 0.03, "fx": s["fx"]}.items() if v is not None} for s in segs],
        "match_bg": False, "cutaways": [], "endcard": {"clip": "brand/cream_tail.mp4", "dur": END + 0.3, "offset": 0, "xfade": 0.3},
        "music": {"file": "audio/bed_split_90s.mp3", "target_lufs": -26, "fade_in": 0.2, "fade_out": 2.5, "duck": True},
        "voice_lufs": -14, "level_voice": True, "limit": 0.85, "sfx": sfx,
        "grade_presenter": "unsharp=5:5:0.5:5:5:0" if WIDE else "eq=contrast=1.05:saturation=1.05,unsharp=5:5:0.5:5:5:0",
        "scenes": SCENES,
        "overlays": {"dir": f"{OUT}/frames", "fps": 24}, "delogo": None, "total": total, "tail_black": 0}
json.dump(plan, open(f"{OUT}/plan.json", "w"), indent=1)
open(f"{OUT}/anchors.txt", "w").write("\n".join(ANCH) + "\n")

# captions (.srt) in the script's own spelling, 2 short lines max, timed on the aligned words
def ts(x): h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60; return f"{h:02d}:{m:02d}:{int(s):02d},{int(round((s - int(s)) * 1000)):03d}"
srt_cues = []
def endch(w): return w.rstrip("'\"”’)")[-1:]
for cid in IDS:
    toks = [x for x in SCRIPT[cid].split() if x.strip("—–-")]; shown = SHOWN.get(cid, SCRIPT[cid]).split()
    cw = [w for w in words if w["cid"] == cid]
    if len(shown) != len(toks):   # different token count (e.g. 'eighteen eighty-eight' -> '1888'): one cue for the line
        srt_cues.append([cw[0]["start"], cw[-1]["end"], shown]); continue
    chunks, cur = [], []
    for i, w in enumerate(shown):             # 1) sentence / clause ends
        cur.append(i)
        if endch(w) in ".?!:;": chunks.append(cur); cur = []
    if cur: chunks.append(cur)
    out = []
    for ch in chunks:                          # 2) long lines split at the comma nearest the middle, else the middle
        while len(ch) > 10:
            commas = [k for k in range(2, len(ch) - 2) if endch(shown[ch[k]]) == ","]
            cut = min(commas, key=lambda k: abs(k - len(ch) / 2)) + 1 if commas else len(ch) // 2
            out.append(ch[:cut]); ch = ch[cut:]
        out.append(ch)
    merged = []                                # 3) no 1-2 word fragments
    for ch in out:
        if merged and (len(ch) < 3 or len(merged[-1]) < 3) and len(merged[-1]) + len(ch) <= 12: merged[-1] = merged[-1] + ch
        else: merged.append(ch)
    for ch in merged: srt_cues.append([cw[ch[0]]["start"], cw[ch[-1]]["end"], [shown[k] for k in ch]])
srt = []
for i, (a, b, ws) in enumerate(srt_cues):
    nxt = srt_cues[i + 1][0] if i + 1 < len(srt_cues) else total
    b = min(max(b + 0.2, a + 0.8), nxt - 0.04)
    srt.append(f"{i + 1}\n{ts(a)} --> {ts(b)}\n{' '.join(ws)}\n")
open(f"{OUT}/captions.srt", "w").write("\n".join(srt))
print(f"[plan] clips {len(IDS)}  presenter {HOOK}-{pend}s  total {total}s  cues {len(cues)}  sfx {len(sfx)}  anchors {len(ANCH)}")
