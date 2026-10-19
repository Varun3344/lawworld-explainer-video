#!/usr/bin/env python3
"""Presenter framing for the split explainers: measure where the presenter stands in each talking-head clip, and compute
compose2.py "place" params ({"s", "dx", "dy"}, box mode) so that every clip matches one anchor clip's framing: same head-top
height, same body centre, same shoulder width, at every cut (owner 15-10-2026: "avatar position jumping scene to scene").

Usage (from product-explainer/):
  measure  python3 split/presenter_geom.py downloads/coa/flat/c*.mp4 [--frames 24] [--out out/coa/geom.json] [--debug DIR]
                   [--start S] [--dur D] [--crop W:H:X:Y]
  place    python3 split/presenter_geom.py --place out/coa/geom.json --anchor c01 [--out out/coa/place.json] [--seam left]
                   [--box W:H] [--fx 0.5] [--fy 0.78] [--ref-ignore c06,...] [--max-up 0.06|none]
                   (defaults: box 640:1080, fx 0.5, fy 0.78; a clip > 6 % larger than the anchor never sets the size)
  both     python3 split/presenter_geom.py downloads/coa/flat/c*.mp4 --anchor c01 --seam left --out out/coa/geom.json
                   --place-out out/coa/place.json
  --start/--dur measure a time range only; --crop measures a region (e.g. --crop 640:1080:1280:0 = the presenter box of a
  composed 16:9 video, to check a render); --debug DIR writes DIR/<clip>.png (a frame with the measurements drawn) and
  DIR/sheet.png (all clips side by side, scaled 0.5). Place JSON = {cid: {"s", "dx", "dy"}} (what build_coa_plan.py reads
  from out/coa/place.json).
Import (a plan builder):
  spec = importlib.util.spec_from_file_location("presenter_geom", "split/presenter_geom.py")
  PG = importlib.util.module_from_spec(spec); spec.loader.exec_module(PG)
  geoms = PG.measure_clips({cid: f"{CLIPS}/{cid}.mp4" for cid in IDS}, cache=f"{OUT}/geom.json")   # re-measures changed files only
  place, rep = PG.place_params(geoms, "c01", box=plan_presenter_box, seam="left")
  print("\n".join("[place] " + l for l in rep["lines"]))                                         # segment["place"] = place[cid]

Measurement (source pixels, continuous coordinates: pixel i spans i..i+1; numpy + ffmpeg only, deterministic). Made for
FLATTENED clips (split/flatten_bg.py): a plain uniform backdrop.
  24 frames spread over the clip (or range), decoded as the clip's own yuv420p planes. Backdrop = median colour of the frame
  border (top rows, side columns). Presenter mask = |Y - Yb| > 14 or |U - Ub| > 6 or |V - Vb| > 6 (chroma upsampled), opened
  3x3 (no specks). Per frame:
    head top T     first row whose mask holds a compact object (4 px .. half the width, growing to >= 20 px eight rows down):
                   the crown; full-width rows (set lines, a flatten band) are skipped
    width profile  per row, the mask run containing the head / neck centre line (gaps < 10 px closed); head width HW = median
                   width of rows T+40..T+120; neck N = narrowest row in T+0.8HW..T+2.2HW; shoulder knee S = first row below
                   N at >= 2.3 HW (the trapezius slope ends); torso band = rows S+0.15HW..S+0.40HW (deltoids / upper arms:
                   hands and forearms in front of the body do not reach the outline there)
    body centre    midpoint of the torso band outline. Measured on split9: 3-5x steadier within a clip (MAD 0.5-1.6 px) than
                   the head centre (MAD 2-5 px: the head sways while he talks); the neck centre (N-15..N+10) and the head
                   centre (T+0.35HW..N) are kept too (centre_neck over the same frames as the body centre, centre_head)
    shoulders      band outline width
  Clip values = medians over the frames. Arm out (e.g. the presenting-to-the-left gesture) or body turned: each side's
  half-width is taken from the frame's own neck centre (an arm never moves the neck); the resting pose = the largest group of
  samples whose two half-widths agree within 3 %; a side more than 8 % off its resting value (wider: arm out; narrower: the
  far shoulder of a turned body) is dropped for that frame; centre and width use the frames with neither side dropped (>= 6,
  else neck + clean half-widths).
  Also: head width, margins (closest approach of the presenter mask to each frame edge over the sampled frames: 0 = touches
  it; the legs always touch the bottom), reach (the silhouette's horizontal extent), spreads (MAD), notes (arm out, frames
  not measurable, framing drifting WITHIN the clip, e.g. a camera push-in) and a confidence 0..1 = min(valid frames, head
  top / centre / width stability).
Place: see place_params(). compose2.py applies "place" after the cover-scale/crop: scale s about the box's bottom-centre
  (legs stay cut by the frame bottom), shift dx, dy; uncovered box area = presenter_box "fill" (default 0xf7f2e8 = the
  flattened backdrop); compose2 itself clamps anything that would show a source frame edge (checking every frame for it)."""
import argparse, json, os, subprocess, sys
import numpy as np

VERSION = 3                 # bump when the measurement changes (cached geom.json entries are re-measured)
T_Y, T_C = 14, 6            # presenter mask thresholds against the backdrop (luma, chroma code values)

# ---------------------------------------------------------------------------------------------------------------------
# decoding
def probe(path):
    o = subprocess.run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", path], capture_output=True, text=True)
    try:
        d = json.loads(o.stdout); v = next(s for s in d["streams"] if s["codec_type"] == "video")
    except (ValueError, StopIteration):
        raise SystemExit(f"[geom] cannot read {path}")
    n = int(v.get("nb_frames") or 0)
    if not n:
        c = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-count_packets", "-show_entries", "stream=nb_read_packets",
                            "-of", "csv=p=0", path], capture_output=True, text=True).stdout.strip()
        n = int(c or 0)
    num, den = (v.get("r_frame_rate") or "24/1").split("/")
    return {"w": int(v["width"]), "h": int(v["height"]), "n": n, "fps": float(num) / float(den or 1), "dur": float(d["format"].get("duration", 0)),
            "space": v.get("color_space"), "range": v.get("color_range")}

def decode(path, w, h, frames, crop=None):
    """the clip's own yuv420p planes of the given frame indices (optionally a crop W,H,X,Y of the frame)"""
    sel = "select='" + "+".join(f"eq(n\\,{i})" for i in sorted(frames)) + "'"
    vf = sel + (f",crop={crop[0]}:{crop[1]}:{crop[2]}:{crop[3]}" if crop else "")
    if crop: w, h = crop[0], crop[1]
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-map", "0:v:0", "-vf", vf, "-fps_mode", "passthrough", "-f", "rawvideo",
                          "-pix_fmt", "yuv420p", "-"], capture_output=True).stdout
    ny, nc = w * h, (w // 2) * (h // 2); fs = ny + 2 * nc; out = []
    for j in range(len(raw) // fs):
        a = np.frombuffer(raw, np.uint8, fs, j * fs)
        out.append((a[:ny].reshape(h, w), a[ny:ny + nc].reshape(h // 2, w // 2), a[ny + nc:].reshape(h // 2, w // 2)))
    return out

def rgb_frame(path, index, crop=None):
    """one frame as RGB (ffmpeg's own conversion), for debug drawings"""
    vf = f"select='eq(n\\,{index})'" + (f",crop={crop[0]}:{crop[1]}:{crop[2]}:{crop[3]}" if crop else "")
    p = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-map", "0:v:0", "-vf", vf, "-frames:v", "1", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                       capture_output=True).stdout
    return p

# ---------------------------------------------------------------------------------------------------------------------
# per-frame measurement
def _shift_or(m, r, axis):
    """boolean dilation by r along one axis (edge = False)"""
    out = m.copy()
    for k in range(1, r + 1):
        if axis == 1: out[:, k:] |= m[:, :-k]; out[:, :-k] |= m[:, k:]
        else: out[k:] |= m[:-k]; out[:-k] |= m[k:]
    return out

def _shift_and(m, r, axis):
    """boolean erosion by r along one axis (outside the frame counts as True, so edges do not erode)"""
    out = m.copy()
    for k in range(1, r + 1):
        if axis == 1: out[:, k:] &= m[:, :-k]; out[:, :-k] &= m[:, k:]
        else: out[k:] &= m[:-k]; out[:-k] &= m[k:]
    return out

def presenter_mask(Y, U, V, bd):
    Yi = Y.astype(np.int16); Ui = np.repeat(np.repeat(U.astype(np.int16), 2, 0), 2, 1); Vi = np.repeat(np.repeat(V.astype(np.int16), 2, 0), 2, 1)
    m = (np.abs(Yi - bd[0]) > T_Y) | (np.abs(Ui - bd[1]) > T_C) | (np.abs(Vi - bd[2]) > T_C)
    return _shift_or(_shift_or(_shift_and(_shift_and(m, 1, 0), 1, 1), 1, 0), 1, 1)          # 3x3 opening: no specks

def backdrop_colour(frames):
    """median Y, U, V of the frame border (top 6 % rows, outer 3 % columns of the upper 40 %), over the frames"""
    vals = []
    for Y, U, V in frames:
        h2, w2 = U.shape; t = max(2, int(0.06 * h2)); s = max(2, int(0.03 * w2)); hh = max(t + 1, int(0.4 * h2))
        ys = np.concatenate([Y[:2 * t:2, ::2].ravel(), Y[:2 * hh:2, :2 * s:2].ravel(), Y[:2 * hh:2, -2 * s::2].ravel()])
        us = np.concatenate([U[:t].ravel(), U[:hh, :s].ravel(), U[:hh, -s:].ravel()])
        vs = np.concatenate([V[:t].ravel(), V[:hh, :s].ravel(), V[:hh, -s:].ravel()])
        vals.append((np.median(ys), np.median(us), np.median(vs)))
    return tuple(float(np.median([v[c] for v in vals])) for c in range(3))

def _run(closed_row, c, look=40):
    """[left, right] (inclusive columns) of the True run containing column c, or nearest within `look` px; None if none"""
    w = len(closed_row)
    if not closed_row[c]:
        xs = np.flatnonzero(closed_row[max(0, c - look):min(w, c + look + 1)])
        if not len(xs): return None
        c = max(0, c - look) + int(xs[np.argmin(np.abs(xs + max(0, c - look) - c))])
    f = np.flatnonzero(~closed_row[:c]); l = int(f[-1]) + 1 if len(f) else 0
    g = np.flatnonzero(~closed_row[c:]); r = c + int(g[0]) - 1 if len(g) else w - 1
    return l, r

def measure_frame(m):
    """head top, centre, head width, neck, shoulder knee, band half-widths of one presenter mask (None if no presenter)"""
    h, w = m.shape; rc = m.sum(1)
    cand = np.flatnonzero((rc >= 4) & (rc <= 0.5 * w))          # full-width rows are set structure / a flatten band, never the crown
    T = next((int(r) for r in cand if r + 8 < h and 20 <= rc[r + 8] <= 0.5 * w), None)
    if T is None: return None
    ys, xs = np.nonzero(m[T:T + 60]); c0 = int(np.median(xs)) if len(xs) else w // 2
    closed = _shift_and(_shift_or(m, 5, 1), 5, 1)              # horizontal closing: gaps < ~10 px
    rows = range(T, min(h, T + 900)); runs = {}; c = c0
    for r in rows:
        rr = _run(closed[r], min(max(c, 0), w - 1))
        if rr is None:
            if r - T > 60: break
            continue
        runs[r] = rr
        if r - T < 300: c = int(round(0.7 * c + 0.3 * (rr[0] + rr[1]) / 2))   # follow the head / neck centre line
    wid = {r: b - a + 1 for r, (a, b) in runs.items()}
    hw_rows = [wid[r] for r in range(T + 40, T + 121) if r in wid]
    if len(hw_rows) < 40: return None
    HW = float(np.median(hw_rows))
    a, b = T + int(0.8 * HW), T + int(2.2 * HW)
    prof = np.array([wid.get(r, np.nan) for r in range(a, b + 1)], float)
    if np.isnan(prof).all(): return None
    sm = np.array([np.nanmedian(prof[max(0, i - 2):i + 3]) for i in range(len(prof))])
    N = a + int(np.nanargmin(sm))
    S = next((r for r in range(N, min(h, N + int(2.0 * HW))) if wid.get(r, 0) >= 2.3 * HW and wid.get(r + 2, 0) >= 2.3 * HW), None)
    mid = lambda a, b: [(runs[r][0] + runs[r][1] + 1) / 2 for r in range(a, b) if r in runs]
    mids = mid(T + int(0.35 * HW), N + 1); necks = mid(N - 15, N + 11)
    if len(mids) < 10 or len(necks) < 8: return None
    C = float(np.median(mids)); CN = float(np.median(necks))
    out = {"T": float(T), "C": C, "CN": CN, "HW": HW, "N": float(N), "S": None, "lo": None, "ro": None, "band": None}
    if S is not None:
        b0, b1 = S + int(round(0.15 * HW)), S + int(round(0.40 * HW))
        band = [runs[r] for r in range(b0, b1 + 1) if r in runs]
        if len(band) >= 0.6 * (b1 - b0 + 1):    # outline of the torso band: left x and right x (continuous px; pixel i spans i..i+1)
            out.update(S=float(S), lo=float(np.median([l for l, r in band])), ro=float(np.median([r + 1 for l, r in band])), band=(b0, b1))
    y0 = max(0, T - 4); ys, xs = np.nonzero(m[y0:]); ys = ys + y0      # nothing above the crown is the presenter (set line, flatten band)
    out["edge"] = (int(xs.min()), int(w - 1 - xs.max()), int(ys.min()), int(h - 1 - ys.max()))      # left, right, top, bottom margins
    return out

# ---------------------------------------------------------------------------------------------------------------------
# per-clip measurement
def _mad(v): v = np.asarray(v, float); return float(np.median(np.abs(v - np.median(v)))) if len(v) else float("nan")

def _resting_pose(Ls, Rs, tol=0.03):
    """the presenter's resting pose in one clip: the largest group of band samples whose left AND right half-widths (from the
    neck) both agree within tol with one sample's -> (median left, median right, group size). An arm out widens one side, a
    turned body narrows the far side and widens the near one; both scatter, the facing-front resting pose repeats. Fewer than
    3 in the best group: the medians of all samples."""
    near = (np.abs(Ls[None, :] - Ls[:, None]) <= tol * Ls[:, None]) & (np.abs(Rs[None, :] - Rs[:, None]) <= tol * Rs[:, None])
    cnt = near.sum(1); j = int(np.argmax(cnt))
    if cnt[j] < 3: return float(np.median(Ls)), float(np.median(Rs)), int(cnt[j])
    return float(np.median(Ls[near[j]])), float(np.median(Rs[near[j]])), int(cnt[j])

def sample_indices(info, nsamp, start=None, dur=None):
    n = info["n"]; fps = info["fps"] or 24.0
    a = int(round((start or 0.0) * fps)); b = n if dur is None else min(n, int(round(((start or 0.0) + dur) * fps)))
    a = max(0, min(a, n - 1)); b = max(a + 1, b); span = b - a
    lo, hi = a + 0.02 * span, b - 1 - 0.02 * span
    return sorted(set(np.linspace(lo, max(lo, hi), min(nsamp, span)).round().astype(int).tolist()))

def measure_clip(path, nsamp=24, start=None, dur=None, crop=None, keep_frames=False):
    info = probe(path); w, h = (crop[0], crop[1]) if crop else (info["w"], info["h"])
    idx = sample_indices(info, nsamp, start, dur)
    frames = decode(path, info["w"], info["h"], idx, crop)
    if len(frames) < 3: raise SystemExit(f"[geom] {path}: only {len(frames)} frames decoded")
    bd = backdrop_colour(frames); per = []
    for i, (Y, U, V) in zip(idx, frames):
        fm = measure_frame(presenter_mask(Y, U, V, bd))
        per.append((i, fm))
    ok = [(i, f) for i, f in per if f]
    res = {"version": VERSION, "clip": path, "w": w, "h": h, "fps": info["fps"], "frames": len(frames), "range": [start, dur] if start is not None or dur is not None else None,
           "crop": list(crop) if crop else None, "backdrop_yuv": [round(x, 1) for x in bd], "valid": len(ok)}
    try: st = os.stat(path); res["file"] = {"size": st.st_size, "mtime": round(st.st_mtime, 3)}
    except OSError: pass
    if len(ok) < 3:
        res.update(conf=0.0, notes=["presenter not found in enough frames"]); return res
    T = [f["T"] for _, f in ok]; C = [f["C"] for _, f in ok]; CN = [f["CN"] for _, f in ok]; HW = [f["HW"] for _, f in ok]; Nk = [f["N"] for _, f in ok]
    B = [f for _, f in ok if f["lo"] is not None]
    notes = []; ctr = sw = L = R = S = band = None; c_mad = sw_mad = float("nan"); cn = float(np.median(CN))
    if len(B) >= 3:
        # half-widths from the frame's own NECK centre (an arm never moves the neck); a side more than 8 % off that side's
        # resting-pose value (_resting_pose) is dropped for that frame: wider = an arm held out (e.g. presenting to the left),
        # narrower = the body turned (the far shoulder foreshortened). (v2 compared with the lower quartile and so kept the
        # turned frames and dropped the facing-front ones whenever a quarter of the samples were turned: coa c24 centre +19 px.)
        Ls = np.array([f["CN"] - f["lo"] for f in B]); Rs = np.array([f["ro"] - f["CN"] for f in B])
        Lr, Rr, _ = _resting_pose(Ls, Rs)
        keepL = np.abs(Ls - Lr) <= 0.08 * Lr; keepR = np.abs(Rs - Rr) <= 0.08 * Rr; both = keepL & keepR
        if (~keepL).any() or (~keepR).any():
            nw = int((Ls > 1.08 * Lr).sum() + (Rs > 1.08 * Rr).sum()); nn = int((~keepL).sum() + (~keepR).sum()) - nw
            notes.append(f"arm out / body turned in {int((~keepL).sum())} left / {int((~keepR).sum())} right band samples (dropped: {nw} wider, {nn} narrower than the resting pose)")
        lo = np.array([f["lo"] for f in B]); ro = np.array([f["ro"] for f in B])
        L, R = float(np.median(Ls[keepL])), float(np.median(Rs[keepR]))
        if both.sum() >= 6:    # body centre = torso band midpoint, shoulder width = band width, on the frames with no arm out
            ctr = float(np.median((lo + ro)[both] / 2)); sw = float(np.median((ro - lo)[both]))
            c_mad = _mad((lo + ro)[both] / 2); sw_mad = _mad((ro - lo)[both])
            # the neck centre of the SAME frames: place_params compares centre_x - centre_neck across the set; over all frames a
            # clip where he steps sideways while turned (coa c20: neck x 365 -> 461 -> 360) got a 5 px wrong offset and centre
            cn = float(np.median(np.array([f["CN"] for f in B])[both]))
        else:                   # an arm out most of the clip: rebuild from the clean half-widths around the neck
            ctr = float(np.median(CN)) + (R - L) / 2; sw = L + R; c_mad = _mad(CN); sw_mad = _mad(Ls + Rs)
            notes.append("few clean band frames: centre and width from the neck and the clean half-widths")
        S = float(np.median([f["S"] for f in B])); band = [int(np.median([f["band"][0] for f in B])), int(np.median([f["band"][1] for f in B]))]
    else:
        notes.append("shoulder band not found")
    edges = np.array([f["edge"] for _, f in ok])
    lefts = np.array([f["edge"][0] for _, f in ok]); rights = np.array([w - 1 - f["edge"][1] for _, f in ok])
    rd = lambda v, k=2: None if v is None else round(float(v), k)
    res.update({
        "head_top": rd(np.median(T)), "centre_x": rd(ctr), "shoulder_w": rd(sw),
        "centre_head": rd(np.median(C)), "centre_neck": rd(cn), "half_w": [rd(L), rd(R)] if L is not None else None,
        "head_w": rd(np.median(HW)), "neck_y": rd(np.median(Nk), 1), "shoulder_y": S, "band": band,
        "spread": {"head_top": rd(_mad(T)), "centre_x": rd(c_mad), "shoulder_w": rd(sw_mad), "head_w": rd(_mad(HW)), "centre_head": rd(_mad(C))},
        "margins": {"left": int(edges[:, 0].min()), "right": int(edges[:, 1].min()), "top": int(edges[:, 2].min()), "bottom": int(edges[:, 3].min())},
        "reach": {"left": int(lefts.min()), "left_p10": rd(np.percentile(lefts, 10), 1), "right": int(rights.max()), "right_p90": rd(np.percentile(rights, 90), 1)},
        "per_frame": [[i, f["T"], round(f["C"], 1), round(f["CN"], 1), None if f["lo"] is None else round((f["lo"] + f["ro"]) / 2, 1),
                       None if f["lo"] is None else round(f["ro"] - f["lo"], 1)] for i, f in ok],
    })
    bad_i = [i for i, f in per if not f]
    if bad_i: notes.append(f"{len(bad_i)}/{len(per)} frames not measurable (frames {bad_i[0]}..{bad_i[-1]}): check them by eye")
    if len(ok) >= 9:                       # the presenter moving or the camera pushing in WITHIN the clip: a static place cannot follow
        k = len(ok) // 3; a_, b_ = [f for _, f in ok[:k]], [f for _, f in ok[-k:]]
        dHW = np.median([f["HW"] for f in b_]) / np.median([f["HW"] for f in a_]) - 1; dT = np.median([f["T"] for f in b_]) - np.median([f["T"] for f in a_])
        dC = np.median([f["CN"] for f in b_]) - np.median([f["CN"] for f in a_])
        if abs(dHW) > 0.04 or abs(dT) > 10 or abs(dC) > 15:
            notes.append(f"framing drifts within the clip (first -> last third: head width {100 * dHW:+.1f} %, head top {dT:+.0f} px, neck x {dC:+.0f} px)")
    c_valid = len(ok) / len(frames)
    c_T = max(0.0, 1 - _mad(T) / 8); c_C = max(0.0, 1 - c_mad / 8) if sw else 0.0
    c_W = max(0.0, 1 - (sw_mad / sw) / 0.03) if sw else 0.0
    res["conf"] = round(min(c_valid, c_T, c_C, c_W), 3); res["notes"] = notes
    if keep_frames: res["_frames"] = (idx, frames, bd, per)
    return res

def measure_clips(clips, cache=None, nsamp=24, verbose=True):
    """clips: {cid: path} (or a list of paths: cid = file stem). With cache (a geom.json path), clips whose file size/mtime
    and settings are unchanged are taken from it; the cache is rewritten with the current set."""
    if not isinstance(clips, dict): clips = {os.path.splitext(os.path.basename(p))[0]: p for p in clips}
    old = {}
    if cache and os.path.exists(cache):
        try: old = json.load(open(cache)).get("clips", {})
        except ValueError: old = {}
    out = {}
    for cid, p in clips.items():
        st = os.stat(p); o = old.get(cid)
        if o and o.get("version") == VERSION and o.get("clip") == p and o.get("file") == {"size": st.st_size, "mtime": round(st.st_mtime, 3)} and o.get("frames", 0) >= min(nsamp, 3):
            out[cid] = o; continue
        out[cid] = measure_clip(p, nsamp)
        if verbose: print(summary_line(cid, out[cid]), file=sys.stderr, flush=True)
    if cache:
        os.makedirs(os.path.dirname(os.path.abspath(cache)), exist_ok=True)
        json.dump({"version": VERSION, "clips": out}, open(cache, "w"), indent=1)
    return out

def summary_line(cid, g):
    if g.get("shoulder_w") is None: return f"[geom] {cid}: NOT MEASURED ({'; '.join(g.get('notes', []))})"
    s = g["spread"]; m = g["margins"]
    return (f"[geom] {cid}: head top {g['head_top']:7.2f} (±{s['head_top']:.1f})  centre {g['centre_x']:7.2f} (±{s['centre_x']:.1f}; neck {g['centre_neck']:.1f}, "
            f"head {g['centre_head']:.1f} ±{s['centre_head']:.1f})  shoulders {g['shoulder_w']:7.2f} (±{s['shoulder_w']:.1f})  head w {g['head_w']:.1f}  "
            f"margins L{m['left']} R{m['right']} T{m['top']} B{m['bottom']}  conf {g['conf']:.2f}" + (f"  [{'; '.join(g['notes'])}]" if g["notes"] else ""))

# ---------------------------------------------------------------------------------------------------------------------
# geometry shared with compose2.py box mode (keep in step with box_chain / place_window there)
def box_geometry(iw, ih, bw, bh, fx=0.5, fy=0.35):
    """compose2 box mode without a place: cover-scale size (sw, sh), crop offsets (x0, y0) as ffmpeg applies them (lrint,
    then even for yuv420p) and the source -> box scale factors (kx, ky)"""
    sw, sh = max(bw, int(bh * iw / ih + 0.5)), max(bh, int(bw * ih / iw + 0.5))
    fx, fy = float(f"{fx:.4f}"), float(f"{fy:.4f}")                                 # compose2 writes them with 4 decimals
    x0 = int(round(min(max(fx * sw - bw // 2, 0), sw - bw))) & ~1
    y0 = int(round((sh - bh) * fy)) & ~1
    return {"iw": iw, "ih": ih, "sw": sw, "sh": sh, "x0": x0, "y0": y0, "kx": sw / iw, "ky": sh / ih}

def even(v):
    """nearest even integer (compose2's rounding of the place window offsets)"""
    return int(np.floor(v / 2 + 0.5)) * 2

def place_window(iw, ih, bw, bh, fx, fy, s, dx, dy):
    """compose2's place: the source scaled ONCE to (SW, SH) = cover size x s (even), and the even crop offset (CX, CY) of
    the box window in it, so that the unplaced box's bottom-centre lands at (bw/2 + dx, bh + dy) of the box.
    exp: box px uncovered at each side (> 0 = that source frame edge lies inside the box)."""
    g = box_geometry(iw, ih, bw, bh, fx, fy)
    SW = int(round(g["sw"] * s / 2)) * 2; SH = int(round(g["sh"] * s / 2)) * 2
    CX = (g["x0"] + bw / 2) * SW / g["sw"] - bw / 2 - dx; CY = (g["y0"] + bh) * SH / g["sh"] - bh - dy
    CXi, CYi = even(CX), even(CY)
    return {**g, "SW": SW, "SH": SH, "CX": CXi, "CY": CYi, "CXf": CX, "CYf": CY, "KX": SW / iw, "KY": SH / ih,
            "exp": {"left": -CXi, "right": CXi + bw - SW, "top": -CYi, "bottom": CYi + bh - SH}}

def in_box(g, win):
    """a clip's measurements (source px) -> box px through a place window (or a box_geometry: no place)"""
    KX, KY = win.get("KX", win["kx"]), win.get("KY", win["ky"]); CX, CY = win.get("CX", win["x0"]), win.get("CY", win["y0"])
    return {"top": g["head_top"] * KY - CY, "centre": g["centre_x"] * KX - CX, "width": g["shoulder_w"] * KX,
            "reach": (g["reach"]["left"] * KX - CX, (g["reach"]["right"] + 1) * KX - CX)}

def place_params(geoms, anchor, box=None, size_tol=0.005, edge_safety=4, fx=None, seam=None, feather=48, ref_ignore=(), max_up=0.06):
    """Per-clip compose2 "place" params ({"s", "dx", "dy"}) so every clip matches the anchor clip's head-top height, body
    centre and shoulder width (zoom 1.0, no push anywhere), within ~1 % / ~4 px (residuals: even crop offsets, +-1 px).
      geoms    {cid: measure_clip() result} of the clips compose2 will read (the flattened ones), source px
      anchor   cid whose framing is the target
      box      the plan's presenter_box {"w", "h", "fx", "fy"} (default 640 x 1080, fx 0.5, fy 0.78)
      fx       optional {cid: fx} for segments that override the focal point
      seam     "left" (presenter right of the panel: Cause of Action v4) or "right" (v3): flags hands reaching under the
               feather px seam feather
      ref_ignore  cids that may not set the reference size (a size outlier waiting for a retake): they keep s 1 and stay
               larger (reported) instead of every other clip being scaled up to them
      max_up   a clip whose presenter is more than this fraction larger than the anchor's (default 0.06) is a SIZE OUTLIER:
               added to ref_ignore automatically, with a report line (a retake that came back framed tighter, e.g. coa c31
               +17 %, would otherwise zoom EVERY clip in by that much and cut more hands at the box edges). None = no cap.
    Rules
      - never scale below 1 (the legs would lift off the frame bottom). If a clip's presenter is more than size_tol larger
        than the anchor's, the LARGEST presenter (outliers excepted, see max_up) sets the size and the anchor is scaled up
        too (report line "reference size").
      - scaling is about the box's bottom-centre, so a scaled-up presenter's head rises and is shifted back down to the target.
      - a clip can only be lifted (dy < 0) as far as the source rows below the box bottom allow (~14 box px for 720x1280 in
        640x1080 at fy 0.78); when one needs more, the common head-top target is lowered for every clip (report line).
      - a sideways shift beyond the scaled image's slack uncovers a strip at one side (filled with the pad colour = the
        flattened backdrop): only where the presenter keeps >= edge_safety source px clear of that frame edge in the
        measured frames, else dx stops at the slack (residual reported). Same for the top edge; never the bottom edge.
      - set cross-checks (same person in every clip): a clip whose torso-band centre is > 5 px off the set's torso-to-neck
        offset uses neck + offset (an arm out most of the clip); one whose shoulders/head-width ratio is > 3 % off the set
        uses head width x the set ratio when its shoulders look disturbed (arm out / unstable), else it is only flagged.
    Returns (place, report): place {cid: {"s", "dx", "dy"}} for every measured clip (s 1 / dx 0 / dy 0 = unchanged);
    report {"lines", "ref", "target": {top, centre, width}, "clips": {cid: {...}}, "unplaced": [...]}; box px throughout."""
    b = {"w": 640, "h": 1080, "fx": 0.5, "fy": 0.78, **(box or {})}; bw, bh = int(b["w"]), int(b["h"]); fy = float(b["fy"])
    fxc = lambda c: float((fx or {}).get(c, b["fx"]))
    if anchor not in geoms: raise SystemExit(f"[geom] anchor {anchor} not measured")
    # Straight-to-camera clips (course series, 19-10-2026): the hands talk in front of the chest the whole clip, so no frame has a
    # clean torso band and the shoulders / body centre come back NaN. Then size from the head width x the set's shoulders/head
    # ratio (Cause of Action: 2.63, 36 clips, 2.61..2.65) and centre on the neck - both measured to +-1 px on every clip.
    ok_r = [g["shoulder_w"] / g["head_w"] for g in geoms.values() if g.get("shoulder_w") is not None and np.isfinite(g["shoulder_w"]) and g.get("head_w")]
    mr0 = float(np.median(ok_r)) if ok_r else 2.63
    geoms = {c: dict(g) for c, g in geoms.items()}
    for c, g in geoms.items():
        fixed = []
        if g.get("centre_x") is None or not np.isfinite(g["centre_x"]): g["centre_x"] = g["centre_neck"]; fixed.append("centre = neck")
        if g.get("shoulder_w") is None or not np.isfinite(g["shoulder_w"]): g["shoulder_w"] = g["head_w"] * mr0; fixed.append(f"width = head x {mr0:.2f}")
        if fixed: g["notes"] = list(g.get("notes", [])) + ["no clean torso band (hands in front): " + ", ".join(fixed)]
    bad = [c for c, g in geoms.items() if g.get("shoulder_w") is None or g.get("centre_x") is None]
    if anchor in bad: raise SystemExit(f"[geom] anchor {anchor} has no usable measurement: {geoms[anchor].get('notes')}")
    use = {c: dict(g) for c, g in geoms.items() if c not in bad}; notes = {c: [] for c in use}; lines = []
    if len(use) >= 4:
        offs = {c: g["centre_x"] - g["centre_neck"] for c, g in use.items()}; mo = float(np.median(list(offs.values())))
        rat = {c: g["shoulder_w"] / g["head_w"] for c, g in use.items()}; mr = float(np.median(list(rat.values())))
        for c, g in use.items():
            if abs(offs[c] - mo) > 5.0:
                notes[c].append(f"torso centre {offs[c] - mo:+.1f} px off the set's torso-to-neck offset (arm out?): centre = neck {mo:+.1f}")
                g["centre_x"] = g["centre_neck"] + mo
            if abs(rat[c] / mr - 1) > 0.03:
                if any("arm out" in n for n in g.get("notes", [])) or g["spread"]["shoulder_w"] > 0.01 * g["shoulder_w"]:
                    notes[c].append(f"shoulders/head {100 * (rat[c] / mr - 1):+.1f} % off the set (arm out): size from the head width")
                    g["shoulder_w"] = g["head_w"] * mr
                else:
                    notes[c].append(f"shoulders/head {100 * (rat[c] / mr - 1):+.1f} % off the set: check the size by eye")
    win1 = {c: place_window(g["w"], g["h"], bw, bh, fxc(c), fy, 1.0, 0, 0) for c, g in use.items()}
    at1 = {c: in_box(g, win1[c]) for c, g in use.items()}                           # framing as composed today (s 1)
    ign = [c for c in ref_ignore if c in use and c != anchor]
    wa = at1[anchor]["width"]; auto = []
    if max_up is not None:
        auto = sorted((c for c in use if c != anchor and c not in ign and at1[c]["width"] > wa * (1 + max_up)), key=lambda c: -at1[c]["width"])
        for c in auto:
            lines.append(f"SIZE OUTLIER {c}: presenter {100 * (at1[c]['width'] / wa - 1):+.1f} % larger than the anchor {anchor} (max_up {100 * max_up:g} %): it does not "
                         f"set the size (every other clip would be zoomed in up to that much); it keeps s 1 and stays larger at its cuts: retake it "
                         f"(max_up=None / --max-up none lets it set the size)")
        ign += auto
    big = max((c for c in use if c not in ign), key=lambda c: at1[c]["width"]); W = max(wa, at1[big]["width"] / (1 + size_tol))
    for c in ign:
        if at1[c]["width"] > W * (1 + size_tol):
            notes[c].append(("SIZE OUTLIER (max_up): " if c in auto else "kept out of the reference size (ref_ignore): ") + f"stays {100 * (at1[c]['width'] / W - 1):+.1f} % larger")
    ref = anchor
    if W > wa * 1.0005:
        ref = big
        lines.append(f"reference size: the anchor {anchor}'s presenter ({wa:.1f} px shoulders in the box) is smaller than {big}'s ({at1[big]['width']:.1f} px), "
                     f"so the largest presenter sets the size ({W:.1f} px) and the anchor is scaled up by {W / wa:.4f} too (no clip is ever scaled below 1)")
    sc = {c: max(1.0, W / at1[c]["width"]) for c in use}
    Yt, Xt = at1[anchor]["top"], at1[anchor]["centre"]
    hi = {}
    for c, g in use.items():                                                        # highest reachable head top per clip
        w0 = place_window(g["w"], g["h"], bw, bh, fxc(c), fy, sc[c], 0, 0); hi[c] = in_box(g, w0)["top"] - (w0["SH"] - w0["CY"] - bh)
    need = max(hi.values())
    if need > Yt + 0.5:
        who = max(hi, key=hi.get)
        lines.append(f"head-top target lowered from y {Yt:.1f} to {need:.1f}: {who}'s presenter stands too low in its frame to be lifted further "
                     f"without showing the frame's bottom edge (every clip, the anchor included, follows the lower target)")
        Yt = need
    place, rep = {}, {}
    for c, g in use.items():
        s = sc[c]; w0 = place_window(g["w"], g["h"], bw, bh, fxc(c), fy, s, 0, 0)
        # the even window offset that puts the centre / head top nearest the target, and the integer shift that yields it
        dxi = int(round(w0["CXf"] - even(g["centre_x"] * w0["KX"] - Xt))); dyi = int(round(w0["CYf"] - even(g["head_top"] * w0["KY"] - Yt)))
        mg = g["margins"]; nt = notes[c]
        for _ in range(6):                                                          # even rounding + edge rules
            win = place_window(g["w"], g["h"], bw, bh, fxc(c), fy, s, dxi, dyi); e = win["exp"]; ch = False
            if e["bottom"] > 0:
                if e["bottom"] > 2: nt.append(f"dy limited by {e['bottom']} px: the frame's bottom edge would show")
                dyi += e["bottom"]; ch = True
            if e["left"] > 0 and mg["left"] < edge_safety:
                nt.append(f"dx limited by {e['left']} px: the presenter touches the left frame edge (margin {mg['left']} px)"); dxi -= e["left"]; ch = True
            if e["right"] > 0 and mg["right"] < edge_safety:
                nt.append(f"dx limited by {e['right']} px: the presenter touches the right frame edge (margin {mg['right']} px)"); dxi += e["right"]; ch = True
            if e["top"] > 0 and mg["top"] < edge_safety:
                nt.append(f"dy limited by {e['top']} px: the presenter touches the top frame edge"); dyi -= e["top"]; ch = True
            if not ch: break
        a = in_box(g, win); ex = {k: v for k, v in win["exp"].items() if v > 0}
        if ex: nt.append("uncovers " + ", ".join(f"{k} {v} px" for k, v in ex.items()) + " (fill = flattened backdrop; presenter clear of that edge by "
                         + ", ".join(f"{mg[k]} px" for k in ex) + ")")
        if seam == "left" and a["reach"][0] < feather: nt.append(f"silhouette reaches box x {a['reach'][0]:.0f}, under the {feather} px seam feather")
        if seam == "right" and a["reach"][1] > bw - feather: nt.append(f"silhouette reaches box x {a['reach'][1]:.0f}, under the {feather} px seam feather")
        if a["reach"][0] < 0 or a["reach"][1] > bw: nt.append(f"silhouette leaves the box (x {a['reach'][0]:.0f}..{a['reach'][1]:.0f}): cut by the box edge")
        place[c] = {"s": round(s, 4), "dx": dxi, "dy": dyi}
        rep[c] = {"s1": {k: round(v, 1) for k, v in at1[c].items() if k != "reach"}, "after": {k: round(v, 1) for k, v in a.items() if k != "reach"},
                  "err": {"top": round(a["top"] - Yt, 1), "centre": round(a["centre"] - Xt, 1), "width_pct": round(100 * (a["width"] / W - 1), 2)},
                  "reach_box": [round(a["reach"][0], 1), round(a["reach"][1], 1)], "window": {k: win[k] for k in ("SW", "SH", "CX", "CY")},
                  "exposed": ex, "conf": g.get("conf"), "notes": nt}
    lines.append(f"target (box px, {bw}x{bh} box): head top y {Yt:.1f}, centre x {Xt:.1f}, shoulders {W:.1f} px  [anchor {anchor}" + (f", size from {ref}]" if ref != anchor else "]"))
    for c in sorted(rep):
        r = rep[c]; p = place[c]
        lines.append(f"{c}: before top {r['s1']['top']:6.1f} centre {r['s1']['centre']:6.1f} width {r['s1']['width']:6.1f} | place s {p['s']:.4f} dx {p['dx']:+4d} dy {p['dy']:+4d}"
                     f" | after top {r['after']['top']:6.1f} centre {r['after']['centre']:6.1f} width {r['after']['width']:6.1f}"
                     f" (err {r['err']['top']:+.1f} px, {r['err']['centre']:+.1f} px, {r['err']['width_pct']:+.2f} %) | reach x {r['reach_box'][0]:.0f}..{r['reach_box'][1]:.0f}"
                     f" | conf {r['conf']:.2f}" + (f" | NOTE {'; '.join(r['notes'])}" if r["notes"] else ""))
    for c in bad: lines.append(f"{c}: NOT PLACED (measurement failed: {'; '.join(geoms[c].get('notes', []))})")
    return place, {"lines": lines, "ref": ref, "target": {"top": Yt, "centre": Xt, "width": W}, "clips": rep, "unplaced": bad, "outliers": auto}

# ---------------------------------------------------------------------------------------------------------------------
# debug drawing
def _line(img, x0, y0, x1, y1, col, t=3):
    h, w = img.shape[:2]; x0, x1 = sorted((int(round(x0)), int(round(x1)))); y0, y1 = sorted((int(round(y0)), int(round(y1))))
    img[max(0, y0 - t // 2):min(h, y1 + t - t // 2), max(0, x0 - t // 2):min(w, x1 + t - t // 2)] = col

def draw_debug(path, res, out_png, crop=None, target=None):
    """the sampled frame nearest the clip's medians with: mask outline (cyan), head top (red), body centre = torso band
    midpoint (green, full height), head centre (thin red) and neck centre (thin yellow), neck row (yellow), shoulder knee
    (orange), torso band and the measured shoulder width centred on the body centre (blue), silhouette reach over all
    sampled frames (magenta); target (optional {top, centre, width}, same px): dashed white lines"""
    idx, frames, bd, per = res["_frames"]; w, h = res["w"], res["h"]
    best = min((k for k, (i, f) in enumerate(per) if f and f["lo"] is not None),
               key=lambda k: abs(per[k][1]["T"] - res["head_top"]) + abs((per[k][1]["lo"] + per[k][1]["ro"]) / 2 - res["centre_x"]), default=len(per) // 2)
    i = idx[best]; Y, U, V = frames[best]
    raw = rgb_frame(res["clip"], i, crop); img = np.frombuffer(raw, np.uint8)[:w * h * 3].reshape(h, w, 3).copy()
    m = presenter_mask(Y, U, V, bd); edge = m & ~_shift_and(_shift_and(m, 1, 0), 1, 1)
    img[edge] = (0, 220, 255)
    T, C, W = res["head_top"], res["centre_x"], res["shoulder_w"]
    _line(img, C - 130, T, C + 130, T, (255, 0, 0))
    _line(img, C, T - 40, C, h - 1, (0, 200, 0))
    _line(img, res["centre_head"], T + 10, res["centre_head"], res["neck_y"] - 30, (255, 60, 60), 1)
    _line(img, res["centre_neck"], res["neck_y"] - 25, res["centre_neck"], res["neck_y"] + 25, (255, 220, 0), 1)
    _line(img, C - 90, res["neck_y"], C + 90, res["neck_y"], (255, 220, 0))
    if res["band"]:
        b0, b1 = res["band"]; xl, xr = C - W / 2, C + W / 2
        _line(img, xl, res["shoulder_y"], xl + 40, res["shoulder_y"], (255, 140, 0)); _line(img, xr - 40, res["shoulder_y"], xr, res["shoulder_y"], (255, 140, 0))
        for y in (b0, b1): _line(img, xl, y, xr, y, (40, 80, 255), 2)
        _line(img, xl, b0 - 25, xl, b1 + 25, (40, 80, 255)); _line(img, xr, b0 - 25, xr, b1 + 25, (40, 80, 255))
    for x in (res["reach"]["left"], res["reach"]["right"]): _line(img, x, 0, x, h - 1, (255, 0, 255), 2)
    if target:
        for x in range(0, w, 16): _line(img, x, target["top"], x + 8, target["top"], (255, 255, 255), 1)
        for y in range(0, h, 16): _line(img, target["centre"], y, target["centre"], y + 8, (255, 255, 255), 1)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w}x{h}", "-i", "-", out_png], input=img.tobytes(), check=True)
    return i

def sheet(pngs, out_png, scale=0.5):
    if not pngs: return
    ins = sum((["-i", p] for p in pngs), [])
    fc = "".join(f"[{k}:v]scale=iw*{scale}:-2[v{k}];" for k in range(len(pngs))) + "".join(f"[v{k}]" for k in range(len(pngs))) + f"hstack=inputs={len(pngs)}[o]" if len(pngs) > 1 else f"[0:v]scale=iw*{scale}:-2[o]"
    subprocess.run(["ffmpeg", "-v", "error", "-y"] + ins + ["-filter_complex", fc, "-map", "[o]", "-frames:v", "1", out_png], check=True)

# ---------------------------------------------------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("clips", nargs="*"); ap.add_argument("--frames", type=int, default=24)
    ap.add_argument("--out", help="measure mode: geom JSON; --place mode: place JSON"); ap.add_argument("--debug")
    ap.add_argument("--start", type=float); ap.add_argument("--dur", type=float); ap.add_argument("--crop", help="W:H:X:Y region to measure")
    ap.add_argument("--place", metavar="GEOM_JSON", help="compute place params from these measurements (needs --anchor)")
    ap.add_argument("--anchor"); ap.add_argument("--place-out", help="measure mode with --anchor: write the place JSON here")
    ap.add_argument("--box", default="640:1080"); ap.add_argument("--fx", type=float, default=0.5); ap.add_argument("--fy", type=float, default=0.78)
    ap.add_argument("--seam", choices=("left", "right"), help="seam side of the presenter box (left = presenter right of the panel)")
    ap.add_argument("--ref-ignore", default="", help="comma list of clips that may not set the reference size (size outliers)")
    ap.add_argument("--max-up", default="0.06", help="a clip more than this fraction larger than the anchor is a size outlier and never sets the "
                    "reference size (default 0.06; 'none' = the largest clip always sets it)")
    a = ap.parse_args()
    crop = tuple(int(v) for v in a.crop.split(":")) if a.crop else None
    if a.place:
        if not a.anchor: ap.error("--place needs --anchor")
        geoms = json.load(open(a.place))["clips"]; dst = a.out or a.place_out
    else:
        if not a.clips: ap.error("clips or --place required")
        geoms = {}; pngs = []; dst = a.place_out
        if a.debug: os.makedirs(a.debug, exist_ok=True)
        for p in a.clips:
            cid = os.path.splitext(os.path.basename(p))[0]
            r = measure_clip(p, a.frames, a.start, a.dur, crop, keep_frames=bool(a.debug))
            print(summary_line(cid, r), flush=True)
            if a.debug and r.get("shoulder_w") is not None:
                png = os.path.join(a.debug, f"{cid}.png"); draw_debug(p, r, png, crop); pngs.append(png)
            r.pop("_frames", None); geoms[cid] = r
        if a.debug: sheet(pngs, os.path.join(a.debug, "sheet.png"))
        if a.out:
            os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True); json.dump({"version": VERSION, "clips": geoms}, open(a.out, "w"), indent=1)
    if a.anchor:
        bw, bh = (int(v) for v in a.box.split(":"))
        place, rep = place_params(geoms, a.anchor, {"w": bw, "h": bh, "fx": a.fx, "fy": a.fy}, seam=a.seam,
                                  ref_ignore=[c for c in a.ref_ignore.split(",") if c],
                                  max_up=None if a.max_up.strip().lower() in ("none", "") else float(a.max_up))
        print("\n".join("[place] " + l for l in rep["lines"]))
        if dst:
            os.makedirs(os.path.dirname(os.path.abspath(dst)), exist_ok=True); json.dump(place, open(dst, "w"), indent=1)
            print(f"[place] wrote {dst}")

if __name__ == "__main__":
    main()
