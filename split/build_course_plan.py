"""Course videos (owner 19-10-2026: the BNSS / CPC storyboard series): the Cause of Action format (presenter on the RIGHT third,
animated panel on the LEFT two thirds, one cream screen) for any set. Same timing engine as split/build_coa_plan.py: script tokens
aligned to whisper word times, head/tail pauses trimmed, clips laid end to end after the opening sting, no zoom / push, per-clip
place from out/<set>/place.json. Everything set-specific lives in two files:
  split/<set>_all_scenes.json   clips: sceneId, seconds, dialogue (spoken form), shown (caption form), chip (chapter label);
                                top level: title, sting {kicker, title, sub}, endcard {title, line, sub}
  split/cues/<set>.py           the panel cues, run with the helpers below in scope:
                                at(cid, word, nth=1) start of a spoken word (FATAL if missing), S(cid) / E(cid) clip start / end on
                                the timeline, cue(**fields), fx(name, t, gain_db), have(*cids), r3(x), PEND (presenter end)
Usage: python3 split/build_course_plan.py --set <set> [--allow-missing]
Writes out/<set>/timeline.json, plan.json, anchors.txt, captions.srt."""
import os, sys, json, math, subprocess, difflib, importlib.util
spec = importlib.util.spec_from_file_location("words", "scripts/words.py"); W = importlib.util.module_from_spec(spec); spec.loader.exec_module(W); norm = W.norm
def dur(f): return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f], capture_output=True, text=True).stdout.strip())

SET = sys.argv[sys.argv.index("--set") + 1]
D = f"downloads/{SET}"; CLIPS = f"{D}/flat"; OUT = f"out/{SET}"; os.makedirs(OUT, exist_ok=True)
SCENES = f"split/{SET}_all_scenes.json"; META = json.load(open(SCENES)); ALL = META["scenes"]
SCRIPT = {s["sceneId"]: s.get("spoken", s["dialogue"]) for s in ALL}          # what the avatar was asked to say (alignment)
SHOWN = {s["sceneId"]: s["shown"] for s in ALL if s.get("shown")}            # how the words are written in the captions
IDS = [s["sceneId"] for s in ALL]
MOCK = "--mock" in sys.argv          # test the cues before the clips exist: missing clips get evenly spaced script words
if MOCK: OUT = f"out/{SET}_mock"; os.makedirs(OUT, exist_ok=True)
missing = [c for c in IDS if not (os.path.exists(f"{D}/{c}.mp4") and os.path.exists(f"{D}/{c}.words.json") and os.path.exists(f"{CLIPS}/{c}.mp4"))]
if missing and not MOCK and "--allow-missing" not in sys.argv: sys.exit(f"[plan] missing clips (source, words or flat): {missing}")
SECS = {s["sceneId"]: s["seconds"] for s in ALL}
def mock_words(cid):
    toks = [x for x in SCRIPT[cid].split() if x.strip("—–-")]; d = SECS[cid] - 0.8; step = d / max(1, len(toks))
    return [{"word": x, "start": round(0.1 + k * step, 3), "end": round(0.1 + (k + 0.8) * step, 3)} for k, x in enumerate(toks)]
if MOCK: missing = []
stale = [] if MOCK else [c for c in IDS if c not in missing and os.path.getmtime(f"{CLIPS}/{c}.mp4") < os.path.getmtime(f"{D}/{c}.mp4")]
if stale: sys.exit(f"[plan] FATAL flattened clips older than their source (retake?): {stale} -> python3 split/flatten_bg.py --seam left " + " ".join(f"{D}/{c}.mp4" for c in stale))
IDS = [c for c in IDS if c not in missing]
PLACE = json.load(open(f"{OUT}/place.json")) if os.path.exists(f"{OUT}/place.json") else {}
HOOK = 39 / 24; END = 4.2          # the opening lead is a whole number of frames (1.6 s = 38.4 frames put the picture 1 frame behind the voice)

t = HOOK; segs = []; words = []
for cid in IDS:
    c = f"{D}/{cid}.mp4"
    if os.path.exists(c) and os.path.exists(f"{D}/{cid}.words.json"): d = dur(c); ws = json.load(open(f"{D}/{cid}.words.json"))["words"]
    else: d = float(SECS[cid]); ws = mock_words(cid)
    toks = [x for x in SCRIPT[cid].split() if x.strip("—–-")]
    # whisper writes spoken numbers as digits: compare number-normalised forms (one seventy three == 173) token by token
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
    tin = max(0.0, s0 - 0.12); tout = d if cid == IDS[-1] else min(d, s1 + 0.28)   # the last clip runs to its end: room for the payoff
    # LIP SYNC (owner 19-10-2026): cut on frame boundaries. ffmpeg's trim keeps every frame whose time is < out, so an unaligned cut
    # gives the picture up to one frame more than the sound, clip after clip (Cause of Action: the lips ended 0.64 s behind the voice).
    # in / out sit 0.1 ms before a frame time: the video keeps exactly k_out - k_in frames and the audio the same length.
    k_in, k_out = int(round(tin * 24)), int(min(round(tout * 24), math.floor(d * 24 + 1e-6)))
    tin = max(0.0, k_in / 24 - 1e-4); tout = k_out / 24 - 1e-4
    segs.append({"clip": f"{CLIPS}/{cid}.mp4", "in": round(tin, 6), "out": round(tout, 6), "base": round(t, 6), "cid": cid, "place": PLACE.get(cid)})
    for i, x in enumerate(toks): words.append({"word": x, "start": round(t + tm[i][0] - tin, 3), "end": round(t + tm[i][1] - tin, 3), "cid": cid})
    t += tout - tin
PEND = pend = round(t, 3); total = round(pend + END, 3)

ANCH = []
def at(cid, target, nth=1):
    tg = [norm(x) for x in (target if isinstance(target, list) else [target])]; h = 0
    for w in words:
        if w["cid"] != cid: continue
        n = norm(w["word"])
        if any(n == g or (len(g) >= 4 and n.startswith(g)) for g in tg):
            h += 1
            if h == nth: ANCH.append(f"{cid:4} {str(target):28} #{nth} -> {w['start']:7.3f}  ({w['word']})"); return w["start"]
    sys.exit(f"[plan] FATAL {cid}: anchor {target!r} (#{nth}) not found in {[w['word'] for w in words if w['cid'] == cid]}")
have = lambda *cs: all(c in IDS for c in cs)
S = lambda cid: next(s["base"] for s in segs if s["cid"] == cid)
E = lambda cid: next(round(s["base"] + s["out"] - s["in"], 3) for s in segs if s["cid"] == cid)
# picture and sound of every presenter segment must be the same length to the frame (see LIP SYNC above)
for s_ in segs:
    nf = math.ceil(s_["out"] * 24 - 1e-9) - math.ceil(s_["in"] * 24 - 1e-9)
    if abs(nf / 24 - (s_["out"] - s_["in"])) > 0.0012: sys.exit(f"[plan] FATAL {s_['cid']}: picture {nf} frames vs sound {s_['out'] - s_['in']:.4f} s")
r3 = lambda x: round(x, 3)
cues = []; sfx = []
def fx(n, tt, g=-16): sfx.append({"file": f"audio/sfx/{n}.mp3", "at": r3(max(0, tt)), "gain_db": g})
def cue(**k): cues.append({kk: (r3(v) if isinstance(v, float) else v) for kk, v in k.items()})

# ── the set's own cues (they may also set STING = {kicker, title, sub} and ENDCARD = {title, line, sub}) ──────────────────────────
CUEF = f"split/cues/{SET}.py"; NS = {"at": at, "S": S, "E": E, "cue": cue, "fx": fx, "have": have, "r3": r3, "PEND": pend, "IDS": IDS, "HOOK": HOOK}
exec(compile(open(CUEF).read(), CUEF, "exec"), NS)

# ── opening sting (frame 0 = finished logo card = thumbnail), persistent panel with chapter chips, presenter name ──────────────────
st = NS.get("STING") or META.get("sting", {})
cue(type="sting", t0=0.0, t1=HOOK + 0.35, kicker=st.get("kicker", "LAWWORLD · EXPLAINED"), title=st.get("title", META["title"]), sub=st.get("sub", ""))
fx("slam", 0.02, -8); fx("riser", HOOK - 0.9, -18)
chips = [{"at": r3(HOOK if s["sceneId"] == IDS[0] else S(s["sceneId"]) - 0.1), "label": s["chip"]} for s in ALL if s.get("chip") and s["sceneId"] in IDS]
cue(type="panel", t0=HOOK - 0.3, t1=pend + 0.25, scenes=chips)
cue(type="lower_third", t0=S(IDS[0]) + 0.5, t1=S(IDS[0]) + 5.2, name="Ravishankar", role="LawWorld")

# ── sound: a soft pop on every build, a whoosh as a big card arrives, a ding on a result, a slam on a stamp (the set's cue file may
#    add its own with fx(); two sounds never sit closer than 0.22 s) ──────────────────────────────────────────────────────────────
if not NS.get("NO_AUTO_SFX"):
    BIG = {"section", "compare", "flow", "counters", "timeline", "equation", "verdicts", "checklist", "splitcard", "notequal", "list", "question"}
    want = []
    for c in cues:
        t = c["type"]
        if t in ("panel", "sting", "endcard", "lower_third", "kicker"): continue
        if t == "stamp": want.append((c.get("at", c["t0"]) + 0.16, "slam", -10)); continue
        if t == "cite": want.append((c.get("at", c["t0"]), "pop", -20)); continue
        if t in BIG: want.append((c["t0"] - 0.08, "whoosh", -20))
        if c.get("at") is not None: want.append((c["at"], "pop", -17))
        for key in ("items", "rows", "steps", "points", "nodes", "cols"):
            for it in c.get(key) or []:
                for tt in ([it.get("at")] + list(it.get("cells_at") or [])):
                    if tt is not None: want.append((tt, "ding" if it.get("ok") or it.get("tone") == "ok" else "pop", -18))
        for it in c.get("terms") or []:
            want.append((it["at"], "ding" if it.get("result") else "pop", -15 if it.get("result") else -18))
        for key in ("left", "right", "verdict", "note"):
            v = c.get(key)
            if isinstance(v, dict) and v.get("at") is not None: want.append((v["at"], "pop", -18))
    taken = sorted(x["at"] for x in sfx)
    for tt, name, g in sorted(want):
        if tt < HOOK or tt > pend: continue
        if any(abs(tt - u) < 0.22 for u in taken): continue
        fx(name, tt, g); taken.append(tt)

# ── close ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
ec = NS.get("ENDCARD") or META.get("endcard", {})
cue(type="endcard", t0=pend + 0.2, t1=total, title=ec.get("title", META["title"]), line=ec.get("line", ""), sub=ec.get("sub", "LawWorld: legal research for advocates"), url="lawworld.ai")
fx("whoosh", pend + 0.1, -16)

# every cue must stay inside the presenter span (or the sting / endcard) and every build must land after its cue starts
for c in cues:
    if c["type"] in ("sting", "endcard", "panel", "lower_third"): continue
    if not (HOOK - 0.5 <= c["t0"] < c["t1"] <= pend + 0.4): sys.exit(f"[plan] FATAL cue outside the presenter span: {c}")
# an empty panel while he talks reads as a mistake (Cause of Action review: "near-empty panels"): report every gap > 1.2 s
def first_seen(c):                                   # the first moment something of the cue is on screen (its first build)
    ts = [c.get("at"), c.get("head_at"), c.get("title_at"), c.get("open_at"), c.get("land_at")]
    for key in ("items", "rows", "steps", "points", "nodes", "terms", "cols"):
        for it in c.get(key) or []: ts.append(it.get("at")); ts += list(it.get("cells_at") or [])
    for key in ("left", "right", "verdict", "note"):
        v = c.get(key)
        if isinstance(v, dict): ts.append(v.get("at"))
    ts = [x for x in ts if isinstance(x, (int, float))]
    return max(c["t0"], min(ts)) if ts else c["t0"]
cover = sorted((first_seen(c), c["t1"]) for c in cues if c["type"] not in ("panel", "sting", "endcard", "lower_third", "kicker", "cite"))
gaps, tcur = [], HOOK + 0.4
for a0, a1 in cover:
    if a0 - tcur > 1.2: gaps.append((round(tcur, 2), round(a0, 2)))
    tcur = max(tcur, a1)
if pend - tcur > 1.2: gaps.append((round(tcur, 2), round(pend, 2)))
# fill every gap: a chapter that opens on an empty panel gets its title card; elsewhere the previous card holds until the next
# card's first build (no blank panel while he talks)
ACR = {"BNSS", "BNS", "FIR", "CPC", "SP", "SC", "HC", "VII", "XLIII"}
def chapter_title(label):
    txt = label.split("·", 1)[-1].strip() if "·" in label else label
    ws = txt.split()
    return " ".join(w if w.strip(":?,.").upper() in ACR or any(ch.isdigit() for ch in w) else (w.capitalize() if i == 0 else w.lower()) for i, w in enumerate(ws))
chip_of = {s_["sceneId"]: s_["chip"] for s_ in ALL if s_.get("chip")}
for g0, g1 in gaps:
    cid = next((s_["cid"] for s_ in segs if s_["base"] - 0.05 <= g0 < s_["base"] + s_["out"] - s_["in"]), None)
    if cid in chip_of and g0 <= S(cid) + 1.6:
        cue(type="title", t0=r3(g0), t1=r3(g1 + 0.25), title=chapter_title(chip_of[cid]), title_at=r3(g0 + 0.05), fade_out=0.3)
        print(f"[plan] gap {g0:7.2f}-{g1:7.2f}s ({g1 - g0:.1f} s, {cid}): chapter title \"{chapter_title(chip_of[cid])}\"")
        continue
    prev = [c for c in cues if c["type"] not in ("panel", "sting", "endcard", "lower_third", "kicker", "cite") and c["t1"] <= g0 + 0.02]
    if prev:
        pc = max(prev, key=lambda c: c["t1"]); old = pc["t1"]; pc["t1"] = r3(g1 + 0.2)
        print(f"[plan] gap {g0:7.2f}-{g1:7.2f}s ({g1 - g0:.1f} s, {cid}): {pc['type']} held from {old:.2f} to {pc['t1']:.2f}")
    else:
        print(f"[plan] EMPTY PANEL {g0:7.2f}-{g1:7.2f}s ({g1 - g0:.1f} s, from {cid}): nothing to hold")
cues.sort(key=lambda c: (0 if c["type"] in ("panel",) else 1, c["t0"]))
json.dump({"duration": total, "width": 1920, "height": 1080, "layout": {"px": 640, "presenter": "right"}, "cues": cues},
          open(f"{OUT}/timeline.json", "w"), indent=1, ensure_ascii=False)
def seg(s):
    d = {"clip": s["clip"], "in": s["in"], "out": s["out"]}
    if s["place"]: d["place"] = s["place"]
    return d
plan = {"fps": 24, "out": f"{OUT}/{SET}_full.mp4", "size": [1920, 1080],
        "presenter_box": {"x": 1280, "y": 0, "w": 640, "h": 1080, "fx": 0.5, "fy": 0.78, "pad": "0xf5f0e8"},   # fy 0.78: the cove line at y~36 stays hidden
        "presenter_start": HOOK, "presenter": [seg(s) for s in segs],
        "match_bg": False, "cutaways": [], "endcard": {"clip": "brand/cream_tail.mp4", "dur": END + 0.3, "offset": 0, "xfade": 0.3},
        "music": {"file": "audio/bed_course_600s.mp3", "target_lufs": -26, "fade_in": 0.2, "fade_out": 2.5, "duck": True},
        "voice_lufs": -14, "level_voice": True, "limit": 0.85, "sfx": sfx,
        "grade_presenter": "unsharp=5:5:0.5:5:5:0", "scenes": SCENES,
        "overlays": {"dir": f"{OUT}/frames", "fps": 24}, "delogo": None, "total": total, "tail_black": 0}
json.dump(plan, open(f"{OUT}/plan.json", "w"), indent=1)
open(f"{OUT}/anchors.txt", "w").write("\n".join(ANCH) + "\n")

# captions (.srt) in the caption spelling, timed on the aligned words
def ts(x): h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60; return f"{h:02d}:{m:02d}:{int(s):02d},{int(round((s - int(s)) * 1000)):03d}"
srt_cues = []
def endch(w): return w.rstrip("'\"”’)")[-1:]
for cid in IDS:
    toks = [x for x in SCRIPT[cid].split() if x.strip("—–-")]; shown = SHOWN.get(cid, SCRIPT[cid]).split()
    cw = [w for w in words if w["cid"] == cid]
    # the caption form has fewer words ("Section 173(1)" for "Section One Seventy Three, sub section One"): time each sentence of it
    # on the matching spoken sentence instead of word by word
    if len(shown) != len(toks):
        def sents(ws):
            out, cur = [], []
            for w in ws:
                cur.append(w)
                if endch(w) in ".?!": out.append(cur); cur = []
            if cur: out.append(cur)
            return out
        sp, sh = sents(toks), sents(shown)
        if len(sp) == len(sh):
            k = 0
            for a_, b_ in zip(sp, sh):
                srt_cues.append([cw[k]["start"], cw[k + len(a_) - 1]["end"], b_]); k += len(a_)
        else: srt_cues.append([cw[0]["start"], cw[-1]["end"], shown])
        continue
    chunks, cur = [], []
    for i, w in enumerate(shown):
        cur.append(i)
        if endch(w) in ".?!:;": chunks.append(cur); cur = []
    if cur: chunks.append(cur)
    out = []
    for ch in chunks:
        while len(ch) > 10:
            commas = [k for k in range(2, len(ch) - 2) if endch(shown[ch[k]]) == ","]
            cut = min(commas, key=lambda k: abs(k - len(ch) / 2)) + 1 if commas else len(ch) // 2
            out.append(ch[:cut]); ch = ch[cut:]
        out.append(ch)
    merged = []
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
json.dump(words, open(f"{OUT}/words.json", "w"), indent=0)
print(f"[plan] {SET}: clips {len(IDS)}/{len(ALL)}  presenter {HOOK}-{pend}s  total {total}s  cues {len(cues)}  sfx {len(sfx)}  anchors {len(ANCH)}" + (f"  MISSING {missing}" if missing else ""))
