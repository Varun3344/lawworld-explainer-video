"""9:16 version of the full Cause of Action video, built only from what the 16:9 video already rendered (no Flow
credits): the 36 flattened presenter clips with the same per-clip size match, the 16:9 panel overlay frames, and the
16:9 final mix's audio. Owner 2026-10-17: "cause of action video ... without wasting any credits ... make 9:16 like
Vaibhav Sisinty videos" -> creator-reel layout: explanation panel on top, presenter below, big word-by-word captions.

    python3 split/build_vertical.py captions      # write out/coa9x16/captions.ass (+ captions.json for review)
    python3 split/build_vertical.py ptrack        # render out/coa9x16/ptrack.mp4 (presenter, bottom region)
    python3 split/build_vertical.py final [--t0 S --t1 S] [--out PATH]   # compose (a window for tests)

Layout (1080x1920): panel = overlay frames x 0..1280 scaled to 1080x912 at the top; presenter = the 640x1080 box
picture of compose2 (same scale/crop per clip) scaled by K and cut to 1080x1008 below it; the 16:9 sting and end card
are centred cards, so they are shown full screen (crop x 420..1500) at the start and end; captions over the chest.
"""
import json, math, os, re, shlex, subprocess, sys
from difflib import SequenceMatcher

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
OUT = "out/coa9x16"
PLAN = "out/coa/plan.json"
FULL = "out/coa/coa_full.mp4"
FRAMES = "out/coa/frames/f%05d.png"
CLIPDIR = "downloads/coa/flat"          # the review-fixed flats (no arm-slot flicker), not the pre-review snapshot
W, H, FPS = 1080, 1920, 24
PANEL_H = 912                           # 1280x1080 panel * 0.84375
K = 1.6875                              # box (640 wide) -> the full 1080 width: a hand that leaves the shot leaves the frame (no mid-frame edge)
BOX_W, BOX_H = 640, 1080
REG_H = H - PANEL_H                     # 1008: presenter region
HEAD_TOP_BOX = 177                      # measured on every clip of the 16:9 final (+-3 px)
HEAD_MARGIN = 60                        # head top this far below the region top
Y0 = int(round(HEAD_TOP_BOX * K - HEAD_MARGIN)) & ~1
CREAM, FILL = "0xf5f0e8", "0xf7f2e8"
CAP_Y = 1470                            # caption centre (over the chest, clear of Reels/Shorts UI at the bottom)
STING_END, CARD_START, TOTAL = 1.70, 262.30, None
os.makedirs(OUT, exist_ok=True)


def plan():
    return json.load(open(PLAN))


def base_chains():
    """Per-clip (trim, scale, crop, pad) of compose2's base pass, from its --print-cmds output."""
    out = subprocess.run([sys.executable, "scripts/compose2.py", PLAN, "--print-cmds"], capture_output=True, text=True).stdout
    line = next(l for l in out.splitlines() if l.startswith("ffmpeg") and "base.mp4" in l and "concat=n=36" in l)
    chains = []
    for m in re.finditer(r"\[(\d+):v\]trim=([\d.]+):([\d.]+),setpts=PTS-STARTPTS,scale=(\d+):(\d+):flags=lanczos,crop=(\d+):(\d+):(\d+):(\d+),(pad=640:1080:(\d+):(\d+):color=0x[0-9a-f]+,)?", line):
        i = int(m.group(1))
        if i >= 36: continue
        a, b = float(m.group(2)), float(m.group(3))
        SW, SH, cw, ch, cx, cy = (int(m.group(k)) for k in range(4, 10))
        px, py = (int(m.group(11)), int(m.group(12))) if m.group(10) else (0, 0)
        chains.append(dict(i=i, a=a, b=b, SW=SW, SH=SH, cw=cw, ch=ch, cx=cx, cy=cy, px=px, py=py))
    if len(chains) != 36: raise SystemExit(f"parsed {len(chains)} clip chains, expected 36")
    return sorted(chains, key=lambda c: c["i"])


TRACKS = {   # name: (K, region height, Y0 = first row of the K-scaled box shown); the box is centred across the 1080 width
    "split": (K, REG_H, Y0),                        # bottom region of the split layout, head 60 px below its top
    "full": (H / BOX_H, H, 0),                      # full-screen presenter: the whole box, 1920 tall (head top ~315 px)
}


def ptrack(name="split"):
    p = plan(); chains = base_chains(); total = p["total"]
    k, rh, ytop = TRACKS[name]
    inputs, f = [], []
    for c in chains:
        clip = os.path.join(CLIPDIR, os.path.basename(p["presenter"][c["i"]]["clip"]))
        inputs += ["-i", clip]
        SWk, SHk = int(round(c["SW"] * k / 2)) * 2, int(round(c["SH"] * k / 2)) * 2
        bwk = BOX_W * k                                                      # the box's width after the scale (>= 1080)
        X = (c["cx"] - c["px"]) * k + (bwk - W) / 2; Yv = (c["cy"] - c["py"]) * k + ytop   # window in the k-scaled picture
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


# ---------------------------------------------------------------- captions
# Display text = the reviewed script, with legal references written the way a reader expects them. Timing comes from
# the clip's cached whisper words; the words themselves never do (whisper hears "plaint" as "plaintiff").
DISPLAY = {
    "c07": "Our Supreme Court adopted this in ABC Laminart versus AP Agencies.",
    "c13": "You need both, and against this defendant. Let's make it concrete. Ravi lends ₹5 lakh to Suresh.",
    "c15": "What must Ravi prove? 1. He gave the loan. 2. Suresh agreed to repay by that date.",
    "c16": "3. The date has passed. 4. The money is still unpaid.",
    "c23": "One: pleading. Order 7 Rule 1(e) requires every plaint to state the facts constituting the cause of action, and when it arose.",
    "c24": "Two: rejection. Under Order 7 Rule 11(a), a plaint that discloses no cause of action must be rejected.",
    "c27": "Three: jurisdiction. Besides where the defendant lives, Section 20(c) lets you sue where the cause of action arises, wholly or in part.",
    "c29": "Under Order 2 Rule 2, if Ravi sues for only ₹3 lakh, he cannot later sue for the other ₹2 lakh.",
}
NUM = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8",
       "nine": "9", "ten": "10", "eleven": "11", "twelve": "12", "twenty": "20"}


def canon(tok):
    t = tok.lower().replace("’", "'").replace("₹", "")
    t = re.sub(r"[^a-z0-9']", "", t)
    return NUM.get(t, t)


def scene_lines():
    sc = json.load(open(plan()["scenes"]))
    items = sc if isinstance(sc, list) else sc.get("scenes") or sc.get("clips") or [{"sceneId": k, **v} for k, v in sc.items()]
    return {s.get("sceneId") or s.get("id"): (s.get("dialogue") or s.get("text") or s.get("line")) for s in items}


def align(display, words):
    """[(display token, start, end)] — each display token gets the time of the whisper words it lines up with.
    '11(a)' is matched as '11' + 'a' so the spoken letter is not taken by the next article 'a' (c24)."""
    dt = display.split()
    wt = [w for w in words if w["word"].strip()]
    a, own = [], []
    for i, t in enumerate(dt):
        m = re.fullmatch(r"(\d+)\(([a-z])\)[,.]?", t)
        for c in ([m.group(1), m.group(2)] if m else [canon(t)]): a.append(c); own.append(i)
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
    # display tokens with no whisper counterpart: spread between their neighbours
    for i, t in enumerate(times):
        if t: continue
        prev = next((times[j][1] for j in range(i - 1, -1, -1) if times[j]), wt[0]["start"] if wt else 0.0)
        nxt = next((times[j][0] for j in range(i + 1, len(times)) if times[j]), wt[-1]["end"] if wt else prev + 0.3)
        times[i] = (prev, max(prev + 0.05, nxt))
    return [(tok, s, e) for tok, (s, e) in zip(dt, times)]


# Units a caption must never split: legal references, amounts, the date, case names.
UNITS = [r"Order \d+ Rule \d+(?:\([a-z]\))?[,.]?", r"Section \d+\([a-z]\)", r"₹\d+ lakh[.,]?", r"31st March 2025[.,]?",
         r"Read versus Brown,?", r"ABC Laminart", r"AP Agencies\.?", r"Chand Kour", r"Partab Singh", r"Krishna Iyer,?",
         r"Code of Civil Procedure", r"Supreme Court", r"Privy Council", r"Limitation Act", r"cause of action[.,?]?",
         r"written statement\.?", r"bundle of facts'?\.?", r"'bundle of facts'\.?"]
LIST_MARK = re.compile(r"^\d\.$")
MAX_CHARS, MAX_UNITS = 17, 5
WEAK_END = {"the", "a", "an", "to", "of", "in", "for", "he", "she", "it", "that", "and", "or", "with", "by", "at", "on",
            "your", "his", "every", "any", "can", "is", "was", "not", "no", "as", "if", "we", "how"}


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
    """Captions of 2-5 words (about 18 characters), split evenly inside each sentence, never across one; legal
    references, amounts and the date stay whole; '1.' starts a list item instead of ending a sentence."""
    units = merge_units(tokens)
    sents, cur = [], []
    for k, u in enumerate(units):
        cur.append(u)
        ends = re.search(r"[.?!]['’\"]?$", u[0]) is not None and not LIST_MARK.match(u[0])
        colon = u[0].endswith(":") and len(cur) > 1          # "The first question is:" ends; "One:" runs on into "pleading."
        if ends or colon: sents.append(cur); cur = []
    if cur: sents.append(cur)
    out = []
    for s in sents: out += split_even(s)
    return out


def split_even(s):
    """Best contiguous partition of one sentence: groups near MAX_CHARS, no one-word group unless unavoidable."""
    n = len(s)
    if n <= 1: return [s]
    L = [len(u[0]) for u in s]
    def glen(i, j): return sum(L[i:j]) + (j - i - 1)
    def cost(i, j):
        c, k = glen(i, j), j - i
        pen = (c - MAX_CHARS) ** 2 if c > MAX_CHARS else (MAX_CHARS - c) * 0.6
        if k == 1 and " " not in s[i][0]: pen += 40 if s[i][0][-1:] in ",:" else 400   # a lone word, unless it is "Surprisingly,"
        if k > MAX_UNITS: pen += 300 * (k - MAX_UNITS)
        if c > MAX_CHARS + 8: pen += 500
        last = s[j - 1][0]
        if j < n and not re.search(r"[,.:;?!)]$", last) and re.sub(r"[^a-z']", "", last.lower()) in WEAK_END: pen += 60   # never "the", "he", "for"…
        return pen
    best = [0.0] + [math.inf] * n; prev = [0] * (n + 1)
    for j in range(1, n + 1):
        for i in range(max(0, j - 7), j):
            v = best[i] + cost(i, j)
            if v < best[j]: best[j], prev[j] = v, i
    cuts, j = [], n
    while j > 0: cuts.append((prev[j], j)); j = prev[j]
    return [s[i:j] for i, j in reversed(cuts)]


# Explicit caption lines where the even split breaks a name/term or leaves a dangling word. Joined with spaces each
# list must equal the clip's display line (checked below).
BREAKS = {
    "c02": ["The first question is:", "do you have", "a cause of action?", "Get this wrong,", "and your suit",
            "can be thrown out", "before the defendant", "even files", "a written statement."],
    "c03": ["So in the next", "five minutes:", "what a cause of action is,", "how to spot one,", "and why it matters",
            "at every stage of a suit."],
    "c06": ["A cause of action", "is every fact", "the plaintiff", "would have to prove,", "if it were denied,",
            "to win judgment."],
    "c08": ["And put it simply:", "a bundle of facts", "which, with the law", "that applies to them,",
            "gives the plaintiff", "a right to relief", "against the defendant."],
    "c11": ["Second,", "an act or omission", "of the defendant", "that infringes that right."],
    "c13": ["You need both,", "and against", "this defendant.", "Let's make it concrete.", "Ravi lends",
            "₹5 lakh to Suresh."],
    "c15": ["What must Ravi prove?", "1. He gave the loan.", "2. Suresh agreed", "to repay by that date."],
    "c16": ["3. The date has passed.", "4. The money", "is still unpaid."],
    "c17": ["Each of these", "is part of the bundle.", "Together, they are", "Ravi's cause of action."],
    "c18": ["It arose", "on 31st March 2025,", "the due date he missed.", "Remember that date.", "We'll need it."],
    "c20": ["The Privy Council", "said in Chand Kour", "versus Partab Singh", "that it refers entirely",
            "to the grounds", "set out in the plaint."],
    "c23": ["One: pleading.", "Order 7 Rule 1(e)", "requires every plaint", "to state the facts", "constituting",
            "the cause of action,", "and when it arose."],
    "c24": ["Two: rejection.", "Under Order 7 Rule 11(a),", "a plaint that discloses", "no cause of action",
            "must be rejected."],
    "c26": ["And as", "Justice Krishna Iyer", "put it,", "if clever drafting", "creates only an illusion",
            "of a cause of action,", "nip it in the bud."],
    "c27": ["Three: jurisdiction.", "Besides where", "the defendant lives,", "Section 20(c)", "lets you sue where",
            "the cause of action arises,", "wholly or in part."],
    "c28": ["In Ravi's case,", "that can include", "where the loan", "was given,", "or where repayment", "was due.",
            "Four: one suit", "for the whole claim."],
    "c29": ["Under Order 2 Rule 2,", "if Ravi sues", "for only ₹3 lakh,", "he cannot later sue",
            "for the other ₹2 lakh."],
    "c30": ["And a relief", "he leaves out", "without the court's leave", "is lost for good."],
    "c31": ["Five: limitation.", "For many suits,", "the limitation clock", "starts when",
            "the cause of action arises."],
    "c32": ["The Limitation Act", "fixes the exact", "starting point", "for each kind of suit.",
            "That's why we pinned", "31st March 2025."],
    "c33": ["So before you draft", "any plaint,", "ask three questions.", "What right", "does my client have?"],
    "c35": ["If you can answer", "all three", "with facts you can prove,", "you have", "a cause of action."],
    "c36": ["If you can't,", "no amount of drafting", "will save the suit.", "See you", "in the next episode."],
}


def chunks_from(toks, lines):
    out, i = [], 0
    for ln in lines:
        n = len(ln.split()); out.append(merge_units(toks[i:i + n])); i += n
    if i != len(toks) or " ".join(t[0] for t in toks) != " ".join(lines): raise SystemExit(f"BREAKS do not match: {lines}")
    return out


# Whisper-1 puts a word that follows a pause at the end of the previous word (captions up to 0.77 s early) and
# sometimes starts the first word after a pause late or gives it zero length. Snap word starts to the real voice.
VOICE = "out/coa/work/voice.wav"        # compose2's voice stem; timeline = voice time + presenter_start


def voice_runs(lead, thr=-45.0):
    import numpy as np
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", VOICE, "-ac", "1", "-ar", "16000", "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
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
        if not v and j - i < 8 and i > 0 and j < len(m): m[i:j] = True        # close gaps < 80 ms
    for v, i, j in runs(m):
        if v and j - i < 4: m[i:j] = False                                    # drop blips < 40 ms
    return [(lead + 0.01 + i * 0.01, lead + 0.01 + j * 0.01) for v, i, j in runs(m) if v]


# first word after a pause that whisper glued to the previous phrase (clip seconds, measured on voice.wav)
WORD_START_FIX = {"c11": {8: 3.80}, "c23": {18: 8.40}, "c26": {14: 6.59}}


def snap(toks, t0, VR):
    def run_at(t): return next(((a, b) for a, b in VR if a <= t < b), None)
    def next_onset(t): return next((a for a, b in VR if a >= t), None)
    out = list(toks)
    for k, (tok, s, e) in enumerate(out):
        nxt_s = out[k + 1][1] if k + 1 < len(out) else None
        r = run_at(s)
        if r is not None and r[1] - s < 0.12 and e > r[1] + 0.1: r = None       # start sits on the previous word's tail
        if r is None:                                                          # start in a pause -> the voice onset
            o = next_onset(s)
            if o is not None and o <= max(e, s) + 0.3: s = o if nxt_s is None else min(o, nxt_s - 0.05)
        else:                                                                  # first word after a pause, start late
            prev_e = out[k - 1][2] if k else t0
            if s - r[0] >= 0.12 and prev_e <= r[0] + 0.05: s = r[0]
        out[k] = (tok, s, max(e, s + 0.05))
    return out, run_at


def spread(units, c1, run_at):
    """Every highlighted unit gets >= ~0.1 s: a zero-length whisper word shares its neighbour's time by length."""
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


def ass_escape(s):
    return s.replace("\\", "\\\\").replace("{", "(").replace("}", ")")


def captions():
    p = plan(); lines = scene_lines(); t = p["presenter_start"]
    events, review = [], []
    VR = voice_runs(p["presenter_start"])
    allc = []                                   # (sid, units) for the whole video, so a caption can hold to the next one
    for seg in p["presenter"]:
        sid = os.path.splitext(os.path.basename(seg["clip"]))[0]
        a, b = seg["in"], seg["out"]
        wj = json.load(open(f"downloads/coa/{sid}.words.json"))
        words = [w for w in wj["words"] if a - 0.05 <= w["start"] < b]
        display = DISPLAY.get(sid, lines[sid])
        toks = [(tok, t + s - a, t + e - a) for tok, s, e in align(display, words)]
        for i, cs_ in WORD_START_FIX.get(sid, {}).items():
            tok, s_, e_ = toks[i]; ns = t + cs_ - a; toks[i] = (tok, ns, max(e_, ns + 0.05))
        toks, run_at = snap(toks, t, VR)
        cs = chunks_from(toks, BREAKS[sid]) if sid in BREAKS else chunks(toks)
        allc += [(sid, c, t + (b - a)) for c in cs]
        t += b - a
    for n, (sid, c, clip_end) in enumerate(allc):
        c0 = c[0][1]; c1 = c[-1][2] + 0.35
        nxt = allc[n + 1][1][0][1] if n + 1 < len(allc) else clip_end
        if n + 1 < len(allc) and allc[n + 1][0] != sid: nxt = min(nxt, clip_end)   # never across a clip cut
        txt = " ".join(x[0] for x in c)
        if n + 1 < len(allc) and (nxt - c1 < 0.25 or (not re.search(r"[.?!:]['’\"]?$", txt) and nxt - c1 < 1.2)):
            c1 = nxt                                # no 1-6 frame flicker, no blank screen inside a sentence
        c1 = max(c0 + 0.3, min(c1, nxt))
        c = spread(c, c1, run_at)
        review.append({"scene": sid, "start": round(c0, 2), "end": round(c1, 2), "text": txt})
        for k, (tok, s, e) in enumerate(c):
            es = c0 if k == 0 else s
            ee = c1 if k == len(c) - 1 else c[k + 1][1]
            if ee - es < 0.02: continue
            parts = []
            for j, (tj, _, _) in enumerate(c):
                tj = ass_escape(tj).replace("₹", "{\\fnHelvetica Neue\\b1}₹{\\fnAvenir Next Heavy\\b0}")   # Avenir Next has no ₹
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


# ---------------------------------------------------------------- compose
# ---------------------------------------------------------------- the edit (owner 2026-10-17)
# "not only like this — sometimes the full avatar has to show and sometimes the animation part": three looks, cut on
# the pause before a sentence. A = presenter full screen (the hook, the turns, the close), G = the animation full screen
# (a new card / stamp / equation / timeline / reason builds), S = split (he walks through a list while it fills in).
EDIT = [
    (1.70, "A"),    # c01 hook, to camera
    (10.10, "G"),   # "do you have a cause of action?" -> question card
    (12.55, "A"),   # "Get this wrong, and your suit can be"
    (14.45, "G"),   # stamp: NO CAUSE OF ACTION = PLAINT REJECTED
    (17.96, "S"),   # c03 the list fills in; c04 CPC: no definition (one line: split); c05 Read v. Brown
    (39.98, "G"),   # c06 the classic definition ... "have to prove,"
    (45.03, "S"),   # "if it were denied, to win judgment." / c07 A.B.C. Laminart / c08 the equation builds
    (62.88, "A"),   # c09 "Notice the words 'bundle of facts'..." (the bundle is only a ring here)
    (68.62, "S"),   # "Open the bundle, and you will usually find two things." (it opens on top)
    (73.20, "G"),   # RIGHT, BREACH, they merge into CAUSE OF ACTION
    (81.76, "S"),   # c12 verdicts; c13 "You need both..." while the right row lights (89.76)
    (92.90, "A"),   # "Let's make it concrete."
    (94.50, "G"),   # "Ravi lends ₹5 lakh to Suresh." -> the LOAN node
    (97.14, "S"),   # c14 due date, ₹0 repaid
    (104.08, "A"),  # "What must Ravi prove?"
    (106.10, "S"),  # the checklist ticks 1-4, c17 it folds into Ravi's cause of action
    (122.56, "G"),  # c18 the date pin lands
    (128.40, "A"),  # "Remember that date. We'll need it." + "Two common mistakes. First,"
    (132.99, "G"),  # cause of action != the defence (builds 133.08 / 134.52)
    (135.94, "S"),  # c20 Chand Kour v. Partab Singh
    (144.35, "G"),  # != the relief (144.42), relief vs cause of action
    (148.76, "S"),  # "The cause of action is why you are entitled to it."
    (152.60, "A"),  # "So why does this matter so much? Five reasons."
    (155.92, "S"),  # "One: pleading." Order 7 Rule 1(e)
    (165.58, "A"),  # "Two: rejection."
    (167.45, "S"),  # Order 7 Rule 11(a)
    (173.26, "G"),  # the court reads only the plaint
    (178.14, "S"),  # Krishna Iyer J.: nip it in the bud
    (187.54, "G"),  # "Three: jurisdiction." the map
    (189.50, "S"),  # Section 20(c)
    (197.30, "G"),  # the map: where the loan was given / repayment was due
    (204.30, "S"),  # "Four: one suit for the whole claim."
    (207.04, "G"),  # Order 2 Rule 2, the claim bar
    (214.60, "A"),  # "lost for good"
    (220.12, "G"),  # reason 5, the clock
    (225.92, "S"),  # the Limitation Act
    (231.85, "G"),  # the date pin flies into the clock
    (235.46, "A"),  # "So before you draft any plaint, ask three questions."
    (239.40, "S"),  # the three questions fill in; c35 "All three, with facts you can prove"
    (253.96, "A"),  # the close, to camera
]
G_Y, G_W = 250, 1080                      # full-screen animation: panel x 76..1204 scaled to 1080 wide, top at y 250
G_CROP = (76, 1128)
G_H = int(round(1080 * G_W / G_CROP[1] / 2)) * 2   # 1034
FEATHER_H = 140


def edit_spans():
    spans = {"A": [], "G": [], "S": []}
    for k, (t, look) in enumerate(EDIT):
        end = EDIT[k + 1][0] if k + 1 < len(EDIT) else CARD_START + 0.3
        spans[look].append((t, end))
    return spans


def feather_pngs():
    """cream strips that melt the full-screen animation's top / bottom edge into the canvas (no hard band)"""
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
    p = plan(); total = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", FULL], capture_output=True, text=True).stdout)
    out = out or f"{OUT}/coa_9x16.mp4"
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
        f"[o2]crop=1280:1080:320:0,scale={W}:{PANEL_H}:flags=lanczos[card]",   # the centred sting / end card, whole
        f"[o3]{lt}[lt]",
        f"[o5]{lt}[lt2]",
        f"[o4]crop={G_CROP[1]}:1080:{G_CROP[0]}:0,scale={G_W}:{G_H}:flags=lanczos[gpanel]",
        f"color=c={CREAM}:s={W}x{H}:r={FPS}:d={total:.3f},format=yuv420p,split=3[c1][c2][c3]",
        # S: panel on top, presenter below (+ the name tag beside his head)
        "[c1][panel]overlay=0:0:format=auto[s1]",
        f"[s1][1:v]overlay=0:{PANEL_H}[s2]",
        "[s2][lt]overlay=24:960:format=auto,format=yuv420p[split0]",
        # G: the animation full screen, its top / bottom edges melted into the cream
        f"[c3][gpanel]overlay=0:{G_Y}:format=auto[g1]",
        f"[g1][4:v]overlay=0:{G_Y}:format=auto[g2]",
        f"[g2][5:v]overlay=0:{G_Y + G_H - FEATHER_H}:format=auto,format=yuv420p[gfull]",
        # A: the presenter full screen (+ the name tag beside his head)
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
           "-framerate", str(FPS), "-i", FRAMES,                                       # 0 animation frames (16:9, RGBA)
           "-i", f"{OUT}/ptrack.mp4",                                                 # 1 presenter, split region
           "-i", FULL,                                                                # 2 the 16:9 final (audio)
           "-i", f"{OUT}/ptrack_full.mp4",                                            # 3 presenter, full screen
           "-loop", "1", "-framerate", str(FPS), "-i", f"{OUT}/feather_top.png",      # 4
           "-loop", "1", "-framerate", str(FPS), "-i", f"{OUT}/feather_bot.png",      # 5
           "-filter_complex", ";".join(f),
           "-map", "[v]", "-map", "2:a", *ss, "-t", f"{dur:.3f}",
           "-c:v", "libx264", "-preset", "medium", "-crf", "17", "-pix_fmt", "yuv420p", "-r", str(FPS),
           "-c:a", "copy", "-movflags", "+faststart", out, "-stats_period", "10"]
    print("[vertical] final ->", out, f"({t0 or 0:.1f}-{(t1 or total):.1f} s)", {k: len(v) for k, v in sp.items()})
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else ""
    if what == "captions": captions()
    elif what == "ptrack": ptrack(sys.argv[2] if len(sys.argv) > 2 else "split")
    elif what == "final":
        args = sys.argv[2:]
        get = lambda k: float(args[args.index(k) + 1]) if k in args else None
        final(get("--t0"), get("--t1"), args[args.index("--out") + 1] if "--out" in args else None)
    else: raise SystemExit(__doc__)
