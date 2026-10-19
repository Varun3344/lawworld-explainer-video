"""9:16 version of a course video (owner 19-10-2026: "one video, 2 outputs": 16:9 + the same content in 9:16), built only from what
the 16:9 video rendered (no Flow credits): the flattened presenter clips with the same per-clip size match, the 16:9 panel overlay
frames and the 16:9 final mix's audio. Same layout and looks as the Cause of Action 9:16 (split/build_vertical.py, owner-approved
17-10-2026), generalised to any set and with the edit chosen automatically from the timeline:
  A = presenter full screen (chapter openers, questions to the viewer, the close, stretches with nothing building)
  G = the animation full screen (a section card / comparison / flow / counter / timeline / equation / verdicts builds)
  S = split, panel on top and presenter below (he talks through what is on screen)
cut only in a pause before a sentence (or between phrases), every shot >= 2 s.

    python3 split/build_vertical_course.py <set> captions | ptrack [split|full] | edit | final [--t0 S --t1 S] [--out PATH]
"""
import json, math, os, re, subprocess, sys
from difflib import SequenceMatcher

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
SET = sys.argv[1]
OUT = f"out/{SET}9x16"
PLAN = f"out/{SET}/plan.json"
FULL = f"out/{SET}/{SET}_full.mp4"
FRAMES = f"out/{SET}/frames/f%05d.png"
TIMELINE = f"out/{SET}/timeline.json"
WORDS = f"out/{SET}/words.json"
CLIPDIR = f"downloads/{SET}/flat"
VOICE = f"out/{SET}/work/voice.wav"
W, H, FPS = 1080, 1920, 24
PANEL_H = 912
K = 1.6875
BOX_W, BOX_H = 640, 1080
REG_H = H - PANEL_H
HEAD_TOP_BOX = 177
HEAD_MARGIN = 60
Y0 = int(round(HEAD_TOP_BOX * K - HEAD_MARGIN)) & ~1
CREAM, FILL = "0xf5f0e8", "0xf7f2e8"
CAP_Y = 1470
os.makedirs(OUT, exist_ok=True)


def plan(): return json.load(open(PLAN))
def timeline(): return json.load(open(TIMELINE))
def sting_end(): return next(c["t1"] for c in timeline()["cues"] if c["type"] == "sting") - 0.25          # 1.70 for HOOK 1.6
def card_start(): return next(c["t0"] for c in timeline()["cues"] if c["type"] == "endcard")


def base_chains():
    """Per-clip (trim, scale, crop, pad) of compose2's base pass, from its --print-cmds output."""
    n = len(plan()["presenter"])
    out = subprocess.run([sys.executable, "scripts/compose2.py", PLAN, "--print-cmds"], capture_output=True, text=True).stdout
    line = next(l for l in out.splitlines() if l.startswith("ffmpeg") and "base.mp4" in l and f"concat=n={n}:" in l)
    chains = []
    for m in re.finditer(r"\[(\d+):v\]trim=([\d.]+):([\d.]+),setpts=PTS-STARTPTS,scale=(\d+):(\d+):flags=lanczos,crop=(\d+):(\d+):(\d+):(\d+),(pad=640:1080:(\d+):(\d+):color=0x[0-9a-f]+,)?", line):
        i = int(m.group(1))
        if i >= n: continue
        a, b = float(m.group(2)), float(m.group(3))
        SW, SH, cw, ch, cx, cy = (int(m.group(k)) for k in range(4, 10))
        px, py = (int(m.group(11)), int(m.group(12))) if m.group(10) else (0, 0)
        chains.append(dict(i=i, a=a, b=b, SW=SW, SH=SH, cw=cw, ch=ch, cx=cx, cy=cy, px=px, py=py))
    if len(chains) != n: raise SystemExit(f"parsed {len(chains)} clip chains, expected {n}")
    return sorted(chains, key=lambda c: c["i"])


TRACKS = {"split": (K, REG_H, Y0), "full": (H / BOX_H, H, 0)}


def ptrack(name="split"):
    p = plan(); chains = base_chains(); total = p["total"]
    k, rh, ytop = TRACKS[name]
    inputs, f = [], []
    for c in chains:
        clip = os.path.join(CLIPDIR, os.path.basename(p["presenter"][c["i"]]["clip"]))
        inputs += ["-i", clip]
        SWk, SHk = int(round(c["SW"] * k / 2)) * 2, int(round(c["SH"] * k / 2)) * 2
        bwk = BOX_W * k
        X = (c["cx"] - c["px"]) * k + (bwk - W) / 2; Yv = (c["cy"] - c["py"]) * k + ytop
        x0, y0 = int(round(X)), int(round(Yv))
        cx, cy = max(0, x0), max(0, y0)
        cw, ch = min(SWk, x0 + W) - cx, min(SHk, y0 + rh) - cy
        pad = f",pad={W}:{rh}:{cx - x0}:{cy - y0}:color={FILL}" if (cw, ch) != (W, rh) else ""
        f.append(f"[{c['i']}:v]trim={c['a']}:{c['b']},setpts=PTS-STARTPTS,scale={SWk}:{SHk}:flags=lanczos,"
                 f"crop={cw}:{ch}:{cx}:{cy}{pad},fps={FPS},format=yuv420p,setsar=1,unsharp=5:5:0.5:5:5:0[p{c['i']}]")
    lead = p["presenter_start"]
    used = lead + sum(c["b"] - c["a"] for c in chains)
    f.append(f"color=c={CREAM}:s={W}x{rh}:r={FPS}:d={lead:.3f},format=yuv420p,setsar=1[lead]")
    f.append(f"color=c={CREAM}:s={W}x{rh}:r={FPS}:d={max(0.1, total - used + 0.5):.3f},format=yuv420p,setsar=1[tail]")
    f.append("[lead]" + "".join(f"[p{c['i']}]" for c in chains) + "[tail]" + f"concat=n={len(chains) + 2}:v=1:a=0,settb=1/{FPS},setpts=N/{FPS}/TB[v]")
    out = f"{OUT}/ptrack.mp4" if name == "split" else f"{OUT}/ptrack_{name}.mp4"
    cmd = ["ffmpeg", "-hide_banner", "-y", *inputs, "-filter_complex", ";".join(f), "-map", "[v]", "-an",
           "-c:v", "libx264", "-preset", "veryfast", "-crf", "14", "-pix_fmt", "yuv420p", "-r", str(FPS), "-t", f"{total:.3f}",
           out, "-stats_period", "10"]
    print(f"[vertical] ptrack {name}: K {k:.4f}, {W}x{rh}, box rows from {ytop / k:.0f}, {len(chains)} clips, {total:.2f} s -> {out}")
    subprocess.run(cmd, check=True)


# ---------------------------------------------------------------- captions (caption form = the scene's "shown" text)
NUMW = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8",
        "nine": "9", "ten": "10", "eleven": "11", "twelve": "12", "twenty": "20"}


def canon(tok):
    t = tok.lower().replace("’", "'").replace("₹", "")
    t = re.sub(r"[^a-z0-9']", "", t)
    return NUMW.get(t, t)


def align(display, words):
    """[(display token, start, end)]: each caption token gets the time of the whisper words it lines up with; a legal reference
    '173(1)(g)' is matched as '173' '1' 'g' (whisper hears the parts)."""
    dt = display.split()
    wt = [w for w in words if w["word"].strip()]
    a, own = [], []
    for i, t in enumerate(dt):
        parts = re.findall(r"\d[\d,]*|[A-Za-z]+(?:'[a-z]+)?", t) if re.search(r"\d", t) else [t]
        for c in [canon(x) for x in parts] or [canon(t)]: a.append(c); own.append(i)
    b = [canon(w["word"]) for w in wt]
    sub = [None] * len(a)
    sm = SequenceMatcher(None, a, b, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1): sub[i1 + k] = (wt[j1 + k]["start"], wt[j1 + k]["end"])
        elif tag == "replace" and j2 > j1:
            s, e = wt[j1]["start"], wt[j2 - 1]["end"]; n = i2 - i1
            for k in range(n): sub[i1 + k] = (s + (e - s) * k / n, s + (e - s) * (k + 1) / n)
    times = [None] * len(dt)
    for k, i in enumerate(own):
        if sub[k]: times[i] = sub[k] if times[i] is None else (times[i][0], sub[k][1])
    for i, t in enumerate(times):
        if t: continue
        prev = next((times[j][1] for j in range(i - 1, -1, -1) if times[j]), wt[0]["start"] if wt else 0.0)
        nxt = next((times[j][0] for j in range(i + 1, len(times)) if times[j]), wt[-1]["end"] if wt else prev + 0.3)
        times[i] = (prev, max(prev + 0.05, nxt))
    return [(tok, s, e) for tok, (s, e) in zip(dt, times)]


UNITS = [r"(?:BNSS|BNS|CPC|Section|Sections|Article|Articles|Rule|Order [IVXL]+ Rule) \d+(?:\(\d+\))?(?:\([a-z]\))?[,.:;]?",
         r"Order [IVXL]+ Rule", r"Order [IVXL]+", r"(?:Article|Section)s? \d+ and \d+[,.]?", r"₹[\d,]+[.,]?",
         r"\d+(?:-day|-month|-year)", r"\d+ (?:days|months|years|hours|lakh)[.,]?",
         r"Supreme Court", r"High Court", r"Sessions Court", r"Sessions Judge", r"First Schedule[.,]?", r"Zero FIR[.,]?",
         r"Limitation Act[.,]?", r"Public Prosecutor", r"Bharatiya Nagarik Suraksha Sanhita,?", r"Bharatiya Nyaya Sanhita,?",
         r"plea bargaining[.,]?", r"non-cognizable[.,]?", r"non-bailable[.,]?", r"Magistrate's order[.,]?",
         r"Superintendent of Police[.,]?", r"v\. \w+"]
MAX_CHARS, MAX_UNITS = 17, 5
WEAK_END = {"the", "a", "an", "to", "of", "in", "for", "he", "she", "it", "that", "and", "or", "with", "by", "at", "on",
            "your", "his", "her", "every", "any", "can", "is", "was", "not", "no", "as", "if", "we", "how", "under", "from", "this"}


def merge_units(tokens):
    out, i = [], 0
    while i < len(tokens):
        hit = None
        for pat in UNITS:
            for n in range(5, 1, -1):
                if i + n <= len(tokens) and re.fullmatch(pat, " ".join(t[0] for t in tokens[i:i + n])):
                    hit = n; break
            if hit: break
        if hit:
            grp = tokens[i:i + hit]
            out.append((" ".join(t[0] for t in grp), grp[0][1], grp[-1][2])); i += hit
        else:
            out.append(tokens[i]); i += 1
    return out


def chunks(tokens):
    units = merge_units(tokens)
    sents, cur = [], []
    for u in units:
        cur.append(u)
        ends = re.search(r"[.?!]['’\"]?$", u[0]) is not None
        colon = u[0].endswith(":") and len(cur) > 1
        if ends or colon: sents.append(cur); cur = []
    if cur: sents.append(cur)
    out = []
    for s in sents: out += split_even(s)
    return out


def split_even(s):
    n = len(s)
    if n <= 1: return [s]
    L = [len(u[0]) for u in s]
    def glen(i, j): return sum(L[i:j]) + (j - i - 1)
    def cost(i, j):
        c, k = glen(i, j), j - i
        pen = (c - MAX_CHARS) ** 2 if c > MAX_CHARS else (MAX_CHARS - c) * 0.6
        if k == 1 and " " not in s[i][0]: pen += 40 if s[i][0][-1:] in ",:" else 400
        if k > MAX_UNITS: pen += 300 * (k - MAX_UNITS)
        if c > MAX_CHARS + 8: pen += 500
        last = s[j - 1][0]
        if j < n and not re.search(r"[,.:;?!)]$", last) and re.sub(r"[^a-z']", "", last.lower()) in WEAK_END: pen += 60
        return pen
    best = [0.0] + [math.inf] * n; prev = [0] * (n + 1)
    for j in range(1, n + 1):
        for i in range(max(0, j - 7), j):
            v = best[i] + cost(i, j)
            if v < best[j]: best[j], prev[j] = v, i
    cuts, j = [], n
    while j > 0: cuts.append((prev[j], j)); j = prev[j]
    return [s[i:j] for i, j in reversed(cuts)]


def voice_runs(lead, thr=-45.0):
    import numpy as np
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", VOICE, "-ac", "1", "-ar", "16000", "-f", "f32le", "-"], capture_output=True, check=True).stdout
    x = np.frombuffer(raw, np.float32); n = (len(x) - 320) // 160
    fr = np.lib.stride_tricks.sliding_window_view(x, 320)[::160][:n].astype(np.float64)
    m = 10 * np.log10((fr ** 2).mean(axis=1) + 1e-12) > thr
    def runs(mask):
        out, i = [], 0
        while i < len(mask):
            j = i
            while j < len(mask) and mask[j] == mask[i]: j += 1
            out.append((bool(mask[i]), i, j)); i = j
        return out
    for v, i, j in runs(m):
        if not v and j - i < 8 and i > 0 and j < len(m): m[i:j] = True
    for v, i, j in runs(m):
        if v and j - i < 4: m[i:j] = False
    return [(lead + 0.01 + i * 0.01, lead + 0.01 + j * 0.01) for v, i, j in runs(m) if v]


def snap(toks, t0, VR):
    def run_at(t): return next(((a, b) for a, b in VR if a <= t < b), None)
    def next_onset(t): return next((a for a, b in VR if a >= t), None)
    out = list(toks)
    for k, (tok, s, e) in enumerate(out):
        nxt_s = out[k + 1][1] if k + 1 < len(out) else None
        r = run_at(s)
        if r is not None and r[1] - s < 0.12 and e > r[1] + 0.1: r = None
        if r is None:
            o = next_onset(s)
            if o is not None and o <= max(e, s) + 0.3: s = o if nxt_s is None else min(o, nxt_s - 0.05)
        else:
            prev_e = out[k - 1][2] if k else t0
            if s - r[0] >= 0.12 and prev_e <= r[0] + 0.05: s = r[0]
        out[k] = (tok, s, max(e, s + 0.05))
    return out, run_at


def spread(units, c1, run_at):
    u = [list(x) for x in units]
    def hl(k): return (u[k + 1][1] if k + 1 < len(u) else c1) - u[k][1]
    for _ in range(4):
        for k in range(len(u)):
            if hl(k) >= 0.095: continue
            j = k - 1 if k > 0 else (k + 1 if k + 1 < len(u) else None)
            if j is None: continue
            i0, i1 = (j, k) if j < k else (k, j)
            a = u[i0][1]; b = u[i1 + 1][1] if i1 + 1 < len(u) else c1
            r = run_at(a + 0.001) or run_at(b - 0.001)
            if r and i1 + 1 >= len(u): b = min(b, max(r[1], a + 0.2))
            L0, L1 = len(u[i0][0]), len(u[i1][0]); cut = a + (b - a) * L0 / (L0 + L1)
            u[i0][2] = min(u[i0][2], cut); u[i1][1] = cut; u[i1][2] = max(u[i1][2], cut + 0.05)
    return [tuple(x) for x in u]


def ass_time(t):
    t = max(0.0, t); h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def ass_escape(s): return s.replace("\\", "\\\\").replace("{", "(").replace("}", ")")


def captions():
    p = plan(); t = p["presenter_start"]
    sc = {s["sceneId"]: s for s in json.load(open(p["scenes"]))["scenes"]}
    events, review = [], []
    VR = voice_runs(p["presenter_start"])
    allc = []
    for seg in p["presenter"]:
        sid = os.path.splitext(os.path.basename(seg["clip"]))[0]
        a, b = seg["in"], seg["out"]
        wj = json.load(open(f"downloads/{SET}/{sid}.words.json"))
        words = [w for w in wj["words"] if a - 0.05 <= w["start"] < b]
        display = sc[sid].get("shown") or sc[sid]["dialogue"]
        toks = [(tok, t + s - a, t + e - a) for tok, s, e in align(display, words)]
        toks, run_at = snap(toks, t, VR)
        allc += [(sid, c, t + (b - a)) for c in chunks(toks)]
        t += b - a
    for n, (sid, c, clip_end) in enumerate(allc):
        c0 = c[0][1]; c1 = c[-1][2] + 0.35
        nxt = allc[n + 1][1][0][1] if n + 1 < len(allc) else clip_end
        if n + 1 < len(allc) and allc[n + 1][0] != sid: nxt = min(nxt, clip_end)
        txt = " ".join(x[0] for x in c)
        if n + 1 < len(allc) and (nxt - c1 < 0.25 or (not re.search(r"[.?!:]['’\"]?$", txt) and nxt - c1 < 1.2)):
            c1 = nxt
        c1 = max(c0 + 0.3, min(c1, nxt))
        c = spread(c, c1, run_at)
        review.append({"scene": sid, "start": round(c0, 2), "end": round(c1, 2), "text": txt})
        for k, (tok, s, e) in enumerate(c):
            es = c0 if k == 0 else s
            ee = c1 if k == len(c) - 1 else c[k + 1][1]
            if ee - es < 0.02: continue
            parts = []
            for j, (tj, _, _) in enumerate(c):
                tj = ass_escape(tj).replace("₹", "{\\fnHelvetica Neue\\b1}₹{\\fnAvenir Next Heavy\\b0}").replace("§", "{\\fnHelvetica Neue\\b1}§{\\fnAvenir Next Heavy\\b0}")
                parts.append("{\\c&H0000D4FF&}" + tj + "{\\c&H00FFFFFF&}" if j == k else tj)
            pop = "\\fscx86\\fscy86\\t(0,90,\\fscx100\\fscy100)" if k == 0 else ""
            events.append(f"Dialogue: 0,{ass_time(es)},{ass_time(ee)},Cap,,0,0,0,,{{\\an5\\pos({W // 2},{CAP_Y}){pop}}}" + " ".join(parts))
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Avenir Next Heavy,88,&H00FFFFFF,&H00FFFFFF,&H00141414,&H78000000,0,0,0,0,100,100,0,0,1,7,3,5,70,70,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    open(f"{OUT}/captions.ass", "w").write(head + "\n".join(events) + "\n")
    json.dump(review, open(f"{OUT}/captions.json", "w"), ensure_ascii=False, indent=1)
    print(f"[vertical] captions: {len(review)} captions, {len(events)} events -> {OUT}/captions.ass")


# ---------------------------------------------------------------- the automatic edit
RICH = {"section", "compare", "flow", "counters", "timeline", "equation", "verdicts", "checklist", "slots", "blocks", "bundle", "splitcard", "notequal"}
QUESTION = {"question", "stamp"}


def builds(c):
    """every build moment of a cue (its own at + the at of each item / row / step / point / node / term)"""
    ts = [c.get("at"), c.get("head_at"), c.get("title_at")]
    for key in ("items", "rows", "steps", "points", "nodes", "terms", "cols", "slots"):
        for it in c.get(key) or []:
            ts.append(it.get("at")); ts += list(it.get("cells_at") or [])
    for key in ("left", "right", "merge", "fold", "verdict", "note"):
        v = c.get(key)
        if isinstance(v, dict): ts.append(v.get("at"))
    return sorted(t for t in ts if isinstance(t, (int, float)))


def auto_edit():
    tl = timeline(); words = json.load(open(WORDS))
    t_start, t_end = sting_end(), card_start()
    # pauses where a cut may fall: the gap before a word that starts a sentence / a phrase (>= 0.16 s of silence)
    gaps = []
    for a, b in zip(words, words[1:]):
        g = b["start"] - a["end"]
        if g >= 0.16 or (a["word"][-1:] in ".?!:;," and g >= 0.06):
            strong = a["word"][-1:] in ".?!:" or g >= 0.35
            gaps.append((round(b["start"] - min(0.1, g / 2), 3), strong))
    starts = [w["start"] - 0.04 for w in words]                           # fallback cut points: just before a word (never mid-word)
    def near_gap(t, lo, hi, strong_first=True):
        c = [g for g in gaps if lo <= g[0] <= hi]
        if not c:
            ws = [s for s in starts if lo <= s <= hi]
            return min(ws, key=lambda s: abs(s - t)) if ws else None
        if strong_first and any(s for _, s in c): c = [g for g in c if g[1]]
        return min(c, key=lambda g: abs(g[0] - t))[0]
    # wanted look per 0.05 s slot: A by default, S while content is on screen, G around the builds of rich cues, A on questions,
    # chapter openers and the close
    n = int((t_end - t_start) / 0.05) + 1
    look = ["A"] * n
    def paint(a, b, L, over=None):
        for i in range(max(0, int((a - t_start) / 0.05)), min(n, int((b - t_start) / 0.05) + 1)):
            if over is None or look[i] in over: look[i] = L
    content = [c for c in tl["cues"] if c["type"] not in ("panel", "sting", "endcard", "lower_third", "kicker", "cite")]
    for c in content: paint(c["t0"], c["t1"], "S")
    last_g = -1e9
    for c in sorted(content, key=lambda c: (builds(c) or [c["t0"]])[0]):
        if c["type"] in RICH:
            b = builds(c)
            if not b: continue
            # the card's reveal only (owner 17-10: "sometimes the animation", not most of the time): from its first build for at most
            # ~3.6 s, then back to the split view while he talks it through; and never two full-screen reveals within 5 s of each
            # other (cards that follow closely build in the split view)
            if b[0] - 0.25 - last_g < 5.0: continue
            g0, g1 = b[0] - 0.25, min(c["t1"], b[0] + 3.6, b[-1] + 1.2)
            paint(g0, g1, "G"); last_g = g1
    for c in content:
        if c["type"] in QUESTION: paint(c.get("at", c["t0"]) - 0.2, c["t1"], "A")
    chips = next(c for c in tl["cues"] if c["type"] == "panel").get("scenes") or []
    for ch in chips[1:]:                                  # a new chapter opens on the presenter (first phrase)
        g = near_gap(ch["at"] + 2.2, ch["at"] + 1.2, ch["at"] + 3.4)
        if g: paint(ch["at"] - 0.1, g, "A")
    paint(t_end - 6.5, t_end, "A", over={"S"})            # the close, to camera
    # change points -> snapped to pauses; drop shots < 2 s; no look longer than 14 s without a change (A <-> S alternate)
    pts = [(t_start, look[0])]
    for i in range(1, n):
        if look[i] != look[i - 1]: pts.append((t_start + i * 0.05, look[i]))
    snapped = [(t_start, pts[0][1])]
    for t, L in pts[1:]:
        g = near_gap(t, t - 0.9, t + 0.6)
        if g is None or g <= snapped[-1][0] + 0.2: continue
        if L == snapped[-1][1]: continue
        snapped.append((g, L))
    out = []
    for k, (t, L) in enumerate(snapped):
        nxt = snapped[k + 1][0] if k + 1 < len(snapped) else t_end
        if out and nxt - t < 2.0 and k + 1 < len(snapped): continue          # too short: the previous look runs on
        if out and out[-1][1] == L: continue
        out.append((t, L))
    final_pts = []
    for k, (t, L) in enumerate(out):
        final_pts.append((t, L))
        nxt = out[k + 1][0] if k + 1 < len(out) else t_end
        # a long split or presenter stretch: bring him in full screen (or back to the split) on a pause every ~6-8 s, so no look
        # runs much longer than that (full presenter about a quarter of the video)
        if L in ("S", "A") and nxt - t > 10:
            u = t + (5.5 if L == "S" else 4.5)
            while nxt - u > 3.5:
                g = near_gap(u, u - 1.2, u + 2.0)
                if g is None or g - final_pts[-1][0] < 3.0: break
                L2 = "A" if final_pts[-1][1] == "S" else "S"
                final_pts.append((g, L2)); u = g + (4.5 if L2 == "A" else 6.5)
            if final_pts[-1][1] != L and nxt - final_pts[-1][0] < 2.0: final_pts.pop()
    json.dump([[round(t, 3), L] for t, L in final_pts], open(f"{OUT}/edit.json", "w"))
    tot = {L: 0.0 for L in "AGS"}
    for k, (t, L) in enumerate(final_pts):
        tot[L] += (final_pts[k + 1][0] if k + 1 < len(final_pts) else t_end) - t
    print(f"[vertical] edit: {len(final_pts)} shots, " + ", ".join(f"{L} {v:.0f} s" for L, v in tot.items()))
    return final_pts


G_Y, G_W = 250, 1080
G_CROP = (76, 1128)
G_H = int(round(1080 * G_W / G_CROP[1] / 2)) * 2
FEATHER_H = 140


def edit_spans():
    E = [tuple(x) for x in json.load(open(f"{OUT}/edit.json"))]
    spans = {"A": [], "G": [], "S": []}
    for k, (t, look) in enumerate(E):
        end = E[k + 1][0] if k + 1 < len(E) else card_start() + 0.3
        spans[look].append((t, end))
    return spans


def feather_pngs():
    from PIL import Image
    c = (0xf5, 0xf0, 0xe8)
    for name in ("top", "bot"):
        im = Image.new("RGBA", (W, FEATHER_H)); px = im.load()
        for y in range(FEATHER_H):
            u = y / (FEATHER_H - 1)
            a = int(round(255 * ((1 - u) ** 1.6 if name == "top" else u ** 1.6)))
            for x in range(W): px[x, y] = (*c, a)
        im.save(f"{OUT}/feather_{name}.png")


def final(t0=None, t1=None, out=None):
    total = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", FULL], capture_output=True, text=True).stdout)
    STING_END, CARD_START = sting_end(), card_start()
    out = out or f"{OUT}/{SET}_9x16.mp4"
    ss = ["-ss", f"{t0:.3f}"] if t0 else []
    dur = (t1 or total) - (t0 or 0.0)
    fsub = os.path.abspath(f"{OUT}/captions.ass").replace(":", "\\:")
    lt = "crop=450:170:1460:875,scale=383:144:flags=lanczos"
    feather_pngs()
    sp = edit_spans()
    on = lambda look: "+".join(f"between(t,{a:.3f},{b - 0.001:.3f})" for a, b in sp[look]) or "0"
    f = [
        "[0:v]fps=24,format=rgba,split=5[o1][o2][o3][o4][o5]",
        f"[o1]crop=1280:1080:0:0,scale={W}:{PANEL_H}:flags=lanczos[panel]",
        f"[o2]crop=1280:1080:320:0,scale={W}:{PANEL_H}:flags=lanczos[card]",
        f"[o3]{lt}[lt]",
        f"[o5]{lt}[lt2]",
        f"[o4]crop={G_CROP[1]}:1080:{G_CROP[0]}:0,scale={G_W}:{G_H}:flags=lanczos[gpanel]",
        f"color=c={CREAM}:s={W}x{H}:r={FPS}:d={total:.3f},format=yuv420p,split=3[c1][c2][c3]",
        "[c1][panel]overlay=0:0:format=auto[s1]",
        f"[s1][1:v]overlay=0:{PANEL_H}[s2]",
        "[s2][lt]overlay=24:960:format=auto,format=yuv420p[split0]",
        f"[c3][gpanel]overlay=0:{G_Y}:format=auto[g1]",
        f"[g1][4:v]overlay=0:{G_Y}:format=auto[g2]",
        f"[g2][5:v]overlay=0:{G_Y + G_H - FEATHER_H}:format=auto,format=yuv420p[gfull]",
        f"[3:v][lt2]overlay=24:420:format=auto,format=yuv420p[afull]",
        f"[split0][gfull]overlay=0:0:enable='{on('G')}'[m1]",
        f"[m1][afull]overlay=0:0:enable='{on('A')}',format=yuv420p[split]",
        f"[c2][card]overlay=0:{(H - PANEL_H) // 2}:format=auto,format=yuv420p,split=2[ca][cb]",
        f"[ca]trim=0:{STING_END + 0.3:.3f},setpts=PTS-STARTPTS[cardA]",
        f"[split]trim={STING_END:.3f}:{CARD_START + 0.3:.3f},setpts=PTS-STARTPTS[splitT]",
        f"[cb]trim={CARD_START:.3f}:{total:.3f},setpts=PTS-STARTPTS[cardB]",
        f"[cardA][splitT]xfade=transition=fade:duration=0.3:offset={STING_END:.3f}[x1]",
        f"[x1][cardB]xfade=transition=fade:duration=0.3:offset={CARD_START:.3f}[x2]",
        f"[x2]subtitles=filename='{fsub}',format=yuv420p[v]",
    ]
    cmd = ["ffmpeg", "-hide_banner", "-y",
           "-framerate", str(FPS), "-i", FRAMES,
           "-i", f"{OUT}/ptrack.mp4",
           "-i", FULL,
           "-i", f"{OUT}/ptrack_full.mp4",
           "-loop", "1", "-framerate", str(FPS), "-i", f"{OUT}/feather_top.png",
           "-loop", "1", "-framerate", str(FPS), "-i", f"{OUT}/feather_bot.png",
           "-filter_complex", ";".join(f),
           "-map", "[v]", "-map", "2:a", *ss, "-t", f"{dur:.3f}",
           "-c:v", "libx264", "-preset", "medium", "-crf", "17", "-pix_fmt", "yuv420p", "-r", str(FPS),
           "-c:a", "copy", "-movflags", "+faststart", out, "-stats_period", "10"]
    print("[vertical] final ->", out, f"({t0 or 0:.1f}-{(t1 or total):.1f} s)", {k: len(v) for k, v in sp.items()})
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    what = sys.argv[2] if len(sys.argv) > 2 else ""
    if what == "captions": captions()
    elif what == "ptrack": ptrack(sys.argv[3] if len(sys.argv) > 3 else "split")
    elif what == "edit": auto_edit()
    elif what == "final":
        args = sys.argv[3:]
        get = lambda k: float(args[args.index(k) + 1]) if k in args else None
        final(get("--t0"), get("--t1"), args[args.index("--out") + 1] if "--out" in args else None)
    else: raise SystemExit(__doc__)
