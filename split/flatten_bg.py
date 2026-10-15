#!/usr/bin/env python3
"""Flatten the plain cream studio backdrop of 9:16 talking-head clips so that, after compose2.py, it lands as exactly the
panel cream #f5f0e8 of the 16:9 split layout (presenter box x 0..640 | animated panel x 640..1920 over flat #f5f0e8):
one screen, no seam.

Usage (from product-explainer/):
  python3 split/flatten_bg.py downloads/split9/c01.mp4 [more.mp4 ...] [--out-dir downloads/split9/flat] [--debug <dir>]
          [--no-verify] [--target-yuv Y,U,V]
  -> <out-dir>/<same name>.mp4 (default out-dir <clip dir>/flat; overwritten on every run, the sources are never touched)
     and ONE stats line per clip. Same frame count, fps, size and duration; audio copied bit-exact (-c:a copy, md5 checked);
     video libx264 crf 10 preset medium yuv420p with the source's colour tags. About 20-25 s per 8-10 s clip on this iMac,
     plus ~10 s for the verification. --debug <dir> writes <dir>/<clip>/*.png (median, fit, plate, backdrop masks, prior,
     weights, residual x4, frame before/after, mock composite before/after, 4x seam zoom, measured backdrop mask).

Method (deterministic: numpy + ffmpeg only, frames streamed through numpy):
  1. Plate. 24 frames spread through the clip -> per-pixel temporal median (hands and mouth move, the backdrop does not).
     Backdrop = median pixels close to a robust log-domain cubic surface (Tukey IRLS at 1/8 res): within 5 % chroma, or
     within 12 % when the change is warmer (shading only goes warmer) and > 24 px from anything clearly presenter; never more
     neutral/cooler than the backdrop seen along the frame border (this gate keeps white and light-blue shirts out);
     rows of one uniform surface running the full width from the top edge (cornice / moulding) count as backdrop too;
     opened, and kept only when connected to the top or side edges (or a pocket > ~44 px). Plate = the median's own colour
     there, a push-pull membrane under the presenter, the median itself at half res wherever it is clearly backdrop, and a
     full-res luma ratio for static structures (the split9 cornice line and the dark moulding of the full/ set vanish).
  2. Gain G = target / plate per channel (clamped 0.5..2.5).
  3. Per frame: soft backdrop weight w (chroma res) from the colour distance to plate*k (asymmetric: cooler/more neutral
     counts 1.6x) 1 below 0.04 -> 0 at 0.09; brightness 1 between 0.67x and 1.08x of the plate -> 0 at 0.52x / 1.17x;
     times the neutral-colour gate and a protective prior (union of all samples' backdrop dilated 16 px: face, shirt and
     torso interior are never touched); then max3 + 2x box3, so the 1-2 px mixed edge pixels are included (no rim, no hard
     edge). The frame's own residual against plate*k (soft moving shadows, local light; +-6 %, ~52 px windows, confident
     backdrop only) refines G. Exposure drift k: per-channel median ratio of confident backdrop to the plate, gaussian-
     smoothed over 8 frames. Output = pixel * (w*G + 1 - w), computed as a Y'CbCr delta on the clip's own planes (no
     YUV->RGB->YUV round trip of the picture): where w = 0 the presenter's bytes are untouched before x264; where the
     correction is active the rounding is dithered (deterministic +-0.5) so integer rounding cannot bias the backdrop mean.
     RGB maths use the tagged matrix (smpte170m / untagged -> BT.601, bt709 -> BT.709).

Calibration (measured 2026-10-15 on this Mac: ffmpeg 9.0.1, compose2.py box mode, grade "unsharp=5:5:0.5:5:5:0", match_bg false):
  - The panel's #f5f0e8 PNG lands in the final mp4 as Y'CbCr (223, 123, 131) [smpte170m, tv]; ffmpeg decodes that to
    RGB (245, 239, 230) (an exact float BT.601 decoder shows ~(246, 241, 231)). compose2's pad colour lands as (223, 124, 131)
    but is always under the opaque panel.
  - compose2 pass 3 (overlay ... format=auto) sends the base video through RGB and back with truncation: near Y 224 the
    presenter's luma drops 1.0-1.35 (staircase 223->222, 224->223, 225->224, 226->224); chroma passes (V +0.07 with noise).
    Pass 2 (lanczos, crop, zoom/push, unsharp, x264 crf 12) keeps the backdrop mean within ~0.1.
  - So the clip backdrop is aimed at TARGET_YUV = (224.2, 123.0, 130.95): it LANDS as (223, 123, 131), the panel's own
    value, and backdrop and panel decode identically in any player. Both read (245, 239, 230) in ffmpeg: that is "#f5f0e8
    as it appears in the final mp4" (the nominal 245,240,232 does not survive compose2 for the panel either).
  - Re-measure if compose2 changes (overlay format=yuv420, an eq/colour grade on the presenter, match_bg true: its
    colorchannelmixer round trip shifts the backdrop again); --target-yuv overrides the constant.

Verification (on by default): 10 frames of the source and of the result go through a mock of compose2 (cover-scale to
640x1080, crop y 35 %, yuv420p, unsharp, pad 1920x1080 0xf5f0e8, x264 crf 12; then overlay of an RGBA PNG opaque #f5f0e8
from x=640 with a 48 px transparent->cream feather over x 592..640, format=auto, x264 crf 17), decoded to RGB by ffmpeg.
Reported: the seam strip x 600..639 (rows where it is backdrop: above the shoulders / beside the body) against the panel
x 641..700, the box's top corners, the worst (and 99th percentile) 16x16 patch of what the viewer sees as backdrop anywhere
in the box (x < 592; everything except the presenter blob, i.e. weight < 0.5 connected to the bottom edge, plus 16 px, so
a structure the matte missed would be counted), and the presenter's face and shirt patches (clip domain) before vs after.
The stats line ends "QA ok" or "QA CHECK (n)", followed by one "[flatten] WARNING <clip>: ..." line per failed check: frame
count / duration, video frame times (sorted packet pts must equal the source's, else the copied audio drifts), audio not
bit-exact, seam strip vs panel > 2, a top corner > 4, worst 16 px backdrop patch > 4, a presenter patch changed by > 3.
The tool never stops on a warning (the clip is written; look at --debug before using it).
Checked end to end 2026-10-15 with the real compose2.py (box 640, fy 0.78, zoom 1/1.06, push 0.03, unsharp grade, cream_tail
end card): pass 2's xfade negotiates yuv444p, so every presenter frame goes 420 -> 444 -> 420 (chroma only, smpte170m tv kept,
flat backdrop unchanged); the backdrop lands as Y'CbCr (223.0, 123.0, 131.0) next to the panel's (223, 123, 131), seam step
<= 0.3 (qa_split.py), no frame-to-frame jump at the cuts.

Limitations: needs a plain, roughly uniform warm backdrop (cream/beige; a colour more neutral than the backdrop is never
treated as backdrop); a cream/beige garment touching the backdrop would be partly flattened; set structures other than
full-width rows at the top (door frames, room corners, objects) are left alone unless their colour is backdrop-like;
backdrop revealed > 16 px inside where no sampled frame showed it, or in pockets < ~44 px enclosed by the presenter, stays
uncorrected; moving shadows deeper than ~6 % are only partly flattened (static ones fully); very dark static structures
amplify their compression noise (up to ~1.9x in blue for the full/ moulding); hair strands get partial, soft correction."""
import argparse, json, os, shutil, subprocess, sys, tempfile, time
import numpy as np

TARGET_YUV = (224.2, 123.0, 130.95)      # clip-domain target (see Calibration) -> lands as PANEL_YUV
PANEL_YUV = (223.0, 123.0, 131.0)        # the panel's #f5f0e8 in the final mp4
PANEL_RGB_DECODED = (245, 239, 230)      # what ffmpeg decodes PANEL_YUV to

# ----------------------------------------------------------------------------------------------------------------------
# probing, decoding, colour maths, small image tools (numpy only)
def probe(path):
    o = subprocess.run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", path], capture_output=True, text=True)
    try:
        d = json.loads(o.stdout); v = next(s for s in d["streams"] if s["codec_type"] == "video")
    except (ValueError, StopIteration):
        raise SystemExit(f"[flatten] cannot read {path}")
    n = int(v.get("nb_frames") or 0)
    if not n:
        c = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-count_packets", "-show_entries", "stream=nb_read_packets",
                            "-of", "csv=p=0", path], capture_output=True, text=True).stdout.strip()
        n = int(c or 0)
    tags = {k: v.get(k) for k in ("color_space", "color_range", "color_primaries", "color_transfer")}
    return {"w": int(v["width"]), "h": int(v["height"]), "n": n, "fps": v.get("r_frame_rate", "24/1"), "pix_fmt": v.get("pix_fmt"),
            "tags": tags, "audio": any(s["codec_type"] == "audio" for s in d["streams"]), "dur": float(d["format"].get("duration", 0)),
            "vdur": float(v.get("duration") or 0), "vstart": float(v.get("start_time") or 0)}

def decode(path, w, h, frames=None):
    """stream the clip's own yuv420p planes (no conversion: exactly what the decoder produced); `frames`: only those indices"""
    vf = ["-vf", "select='" + "+".join(f"eq(n\\,{i})" for i in sorted(frames)) + "'"] if frames else []
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", path, "-map", "0:v:0"] + vf + ["-fps_mode", "passthrough", "-f", "rawvideo",
                          "-pix_fmt", "yuv420p", "-"], stdout=subprocess.PIPE)
    ny, nc = w * h, (w // 2) * (h // 2)
    try:
        while True:
            b = p.stdout.read(ny + 2 * nc)
            if len(b) < ny + 2 * nc: break
            a = np.frombuffer(b, np.uint8)
            yield a[:ny].reshape(h, w), a[ny:ny + nc].reshape(h // 2, w // 2), a[ny + nc:].reshape(h // 2, w // 2)
    finally:
        p.stdout.close(); p.wait()

class Matrix:
    """Y'CbCr <-> R'G'B' (0..255 floats): bt709 tag -> BT.709, anything else (smpte170m, bt470bg, untagged) -> BT.601"""
    def __init__(self, space, rng):
        kr, kb = (0.2126, 0.0722) if space == "bt709" else (0.299, 0.114)
        kg = 1 - kr - kb; full = rng in ("pc", "jpeg")
        self.name = ("BT.709" if space == "bt709" else "BT.601") + (" full" if full else " limited")
        self.yo, self.ys, self.cs = (0.0, 1.0, 1.0) if full else (16.0, 255 / 219, 255 / 224)
        self.k = np.array([kr, kg, kb], np.float32); self.kr, self.kb = kr, kb
        self.rv = 2 * (1 - kr) * self.cs; self.bu = 2 * (1 - kb) * self.cs
        self.gu = 2 * (1 - kb) * kb / kg * self.cs; self.gv = 2 * (1 - kr) * kr / kg * self.cs
    def chroma(self, U, V):
        u = np.asarray(U, np.float32) - 128; v = np.asarray(V, np.float32) - 128
        return np.stack([self.rv * v, -self.gu * u - self.gv * v, self.bu * u], -1)
    def to_rgb(self, Y, U, V):
        return ((np.asarray(Y, np.float32) - self.yo) * self.ys)[..., None] + self.chroma(U, V)
    def delta_uv(self, d):
        yl = d @ self.k
        return (d[..., 2] - yl) / (2 * (1 - self.kb)) / self.cs, (d[..., 0] - yl) / (2 * (1 - self.kr)) / self.cs

def _pad1(a, ax):
    return np.concatenate([np.take(a, [0], ax), a, np.take(a, [a.shape[ax] - 1], ax)], ax)

def box3(a):
    """3x3 box blur, edge-replicated"""
    p = _pad1(a, 0); a = (p[:-2] + p[1:-1] + p[2:]) * np.float32(1 / 3)
    p = _pad1(a, 1); return (p[:, :-2] + p[:, 1:-1] + p[:, 2:]) * np.float32(1 / 3)

def max3(a):
    """3x3 max filter, edge-replicated"""
    p = _pad1(a, 0); a = np.maximum(np.maximum(p[:-2], p[1:-1]), p[2:])
    p = _pad1(a, 1); return np.maximum(np.maximum(p[:, :-2], p[:, 1:-1]), p[:, 2:])

def dilate(m, r):
    for _ in range(r): m = max3(m)
    return m

def erode(m, r):
    return ~dilate(~m, r) if m.dtype == bool else -dilate(-m, r)

def box(a, r):
    """box blur radius r (cumsum, edge-replicated) on the first two axes"""
    if r <= 0: return a
    k = 2 * r + 1; a = a.astype(np.float32, copy=False)
    for ax in (0, 1):
        p = np.pad(a, [(r + 1, r) if i == ax else (0, 0) for i in range(a.ndim)], mode="edge")
        c = np.cumsum(p, axis=ax, dtype=np.float64); n = a.shape[ax]
        hi = c[k:k + n] if ax == 0 else c[:, k:k + n]; lo = c[:n] if ax == 0 else c[:, :n]
        a = ((hi - lo) / k).astype(np.float32)
    return a

def up2_lin(a):
    """bilinear 2x upsample of a 2-D or (h,w,c) array, pixel centres aligned, edge-replicated"""
    if a.ndim == 3: return np.stack([up2_lin(a[..., c]) for c in range(a.shape[2])], -1)
    a = a.astype(np.float32, copy=False); h, w = a.shape; q = 0.25 * a; t = 0.75 * a; o = np.empty((2 * h, 2 * w), np.float32)
    for r, dst in ((t + np.concatenate([q[:1], q[:-1]], 0), o[0::2]), (t + np.concatenate([q[1:], q[-1:]], 0), o[1::2])):
        rq = 0.25 * r; r *= 0.75
        np.add(r, np.concatenate([rq[:, :1], rq[:, :-1]], 1), out=dst[:, 0::2]); np.add(r, np.concatenate([rq[:, 1:], rq[:, -1:]], 1), out=dst[:, 1::2])
    return o

def half(a):
    """2x2 block mean (float32)"""
    h, w = a.shape[0] // 2 * 2, a.shape[1] // 2 * 2; a = a[:h, :w]
    s = a[0::2, 0::2].astype(np.float32); s += a[1::2, 0::2]; s += a[0::2, 1::2]; s += a[1::2, 1::2]; s *= 0.25
    return s

def bmean(a, f):
    """block mean by an integer factor (powers of two by repeated halving)"""
    if f & (f - 1) == 0:
        a = np.asarray(a)
        while f > 1: a = half(a); f //= 2
        return a.astype(np.float32, copy=False)
    h, w = a.shape[0] // f, a.shape[1] // f
    return a[:h * f, :w * f].reshape(h, f, w, f, *a.shape[2:]).mean(axis=(1, 3), dtype=np.float32)

def resize(a, H, W):
    """bilinear resample (h,w[,c]) -> (H,W[,c]), pixel centres aligned"""
    h, w = a.shape[:2]
    ys = np.clip((np.arange(H) + 0.5) * h / H - 0.5, 0, h - 1); xs = np.clip((np.arange(W) + 0.5) * w / W - 0.5, 0, w - 1)
    y0 = np.floor(ys).astype(int); x0 = np.floor(xs).astype(int); y1 = np.minimum(y0 + 1, h - 1); x1 = np.minimum(x0 + 1, w - 1)
    fy = (ys - y0).astype(np.float32).reshape((-1,) + (1,) * (a.ndim - 1)); fx = (xs - x0).astype(np.float32).reshape((1, -1) + (1,) * (a.ndim - 2))
    a = a.astype(np.float32, copy=False); r0 = a[y0]; r1 = a[y1]
    return (r0[:, x0] * (1 - fx) + r0[:, x1] * fx) * (1 - fy) + (r1[:, x0] * (1 - fx) + r1[:, x1] * fx) * fy

def reconstruct(seed, mask):
    """the parts of `mask` 8-connected to `seed`"""
    cur = seed & mask
    while True:
        nxt = max3(cur) & mask
        if (nxt == cur).all(): return cur
        cur = nxt

def smoothstep(e0, e1, x):
    t = np.clip((x - e0) * np.float32(1 / (e1 - e0)), 0, 1); return t * t * (3 - 2 * t)

def tukey(x, s):
    u = np.clip(np.abs(x) / s, 0, 1); return (1 - u * u) ** 2

def logratio(rgb, logref):
    """chroma distance (max change of log R/G, log B/G) and log G ratio of a colour image to a reference (log) colour field"""
    r = np.log(np.maximum(rgb, 1.0)) - logref
    return np.maximum(np.abs(r[..., 0] - r[..., 1]), np.abs(r[..., 2] - r[..., 1])), r[..., 1]

COOL = 1.6   # a change toward cooler / more neutral (less red, more blue than the backdrop) counts 1.6x: shading only goes warmer
def chroma_dist(r):
    """asymmetric chroma distance of log ratios r (...,3) to the backdrop"""
    cr = r[..., 0] - r[..., 1]; cb = r[..., 2] - r[..., 1]
    return np.maximum(np.where(cr < 0, -COOL * cr, cr), np.where(cb > 0, COOL * cb, -cb))

def gate(rgb, g, is_log=False):
    """1 unless the colour is more neutral / cooler than any backdrop seen in the frame border (log R/G below its 1st
    percentile or log B/G above its 99th, by more than 0.02; 0 beyond 0.05). Warmer is allowed: shading goes warmer."""
    l = rgb if is_log else np.log(np.maximum(rgb, 1.0)); cr = l[..., 0] - l[..., 1]; cb = l[..., 2] - l[..., 1]
    return 1 - smoothstep(0.02, 0.05, np.maximum(g[0] - cr, cb - g[3]))

def push_pull(v, m):
    """fill v (h,w,c) where the weight m (h,w) is low with a smooth membrane from the known surroundings"""
    levels = [(v * m[..., None], m.astype(np.float32))]
    while min(levels[-1][1].shape) > 2:
        s, w = levels[-1]; h2, w2 = (s.shape[0] + 1) // 2, (s.shape[1] + 1) // 2
        s = np.pad(s, ((0, h2 * 2 - s.shape[0]), (0, w2 * 2 - s.shape[1]), (0, 0))); w = np.pad(w, ((0, h2 * 2 - w.shape[0]), (0, w2 * 2 - w.shape[1])))
        levels.append((s.reshape(h2, 2, w2, 2, -1).sum((1, 3)), w.reshape(h2, 2, w2, 2).sum((1, 3))))
    s, w = levels[-1]; est = np.broadcast_to(s.sum((0, 1)) / max(w.sum(), 1e-6), s.shape).astype(np.float32)
    for li in range(len(levels) - 2, -1, -1):
        s, w = levels[li]; up = resize(est, s.shape[0], s.shape[1])
        a = np.clip(w / (4.0 ** li) * 2, 0, 1)[..., None]
        est = a * (s / np.maximum(w, 1e-6)[..., None]) + (1 - a) * up
    return est.astype(np.float32)

def polyfit_robust(L, m0, deg=3, iters=10, sc=0.08, sl=0.30):
    """robust (Tukey IRLS) log-domain polynomial surface per channel; L (h,w,3) log colour, m0 initial weights"""
    h, w = L.shape[:2]; yy, xx = np.mgrid[0:h, 0:w]; xn = (xx + 0.5) / w * 2 - 1; yn = (yy + 0.5) / h * 2 - 1
    A = np.stack([xn ** i * yn ** j for i in range(deg + 1) for j in range(deg + 1 - i)], -1).reshape(h * w, -1)
    Lf = L.reshape(-1, 3).astype(np.float64); wt = m0.reshape(-1).astype(np.float64); keep = wt > 0
    for _ in range(iters):
        sw = np.sqrt(wt)[:, None]; beta = np.linalg.lstsq(A * sw, Lf * sw, rcond=None)[0]; r = Lf - A @ beta
        dc = np.maximum(np.abs(r[:, 0] - r[:, 1]), np.abs(r[:, 2] - r[:, 1]))
        wt = tukey(dc, sc) * tukey(r[:, 1], sl) * keep
    return (A @ beta).reshape(h, w, 3).astype(np.float32)

def save_png(path, img):
    img = np.asarray(img, np.float32); h, w = img.shape[:2]
    if img.ndim == 2: img = np.repeat(img[..., None], 3, -1)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w}x{h}", "-i", "-", path],
                   input=np.clip(img + 0.5, 0, 255).astype(np.uint8).tobytes(), check=True)

# ----------------------------------------------------------------------------------------------------------------------
# 1) analysis: plate (clean backdrop), protective prior, exposure drift
def set_rows(rgb_q, top=0.12):
    """rows of one uniform set surface running the full width from the top edge down (cornice, moulding, ceiling line):
    pixels within 8 % chroma / 25 % brightness of their row's median, in rows where >= 80 % of the pixels are"""
    out = np.zeros(rgb_q.shape[:2], bool)
    for y in range(max(1, int(top * rgb_q.shape[0]))):
        l = np.log(np.maximum(rgb_q[y], 1.0)); r = l - np.median(l, 0)
        close = (np.maximum(np.abs(r[:, 0] - r[:, 1]), np.abs(r[:, 2] - r[:, 1])) < 0.08) & (np.abs(r[:, 1]) < 0.25)
        if close.mean() < 0.8: break
        out[y] = close
    return out

def classify_backdrop(rgb_q, logref_q, g, sr=None):
    """backdrop mask (1/4 res) against a reference backdrop colour field: sure, or loosely beige (warmer only) and far from
    the presenter, always inside the backdrop's own chroma range, plus set rows; opened (no specks) and kept only when
    connected to the top/side edges or a pocket > ~44 px across"""
    r = np.log(np.maximum(rgb_q, 1.0)) - logref_q; dl = r[..., 1]; dc = chroma_dist(r)
    sr = np.zeros(dl.shape, bool) if sr is None else sr
    ok = gate(rgb_q, g) > 0.5
    sure = (dc < 0.05) & (dl > -0.40) & (dl < 0.12) & ok
    definite = ((dc > 0.16) | (dl < -0.8) | (dl > 0.25)) & ~sr
    loose = (dc < 0.12) & (r[..., 2] - r[..., 1] < 0.01) & (dl > -0.6) & (dl < 0.15) & ok & ~dilate(definite, 6)
    cand = sure | loose | sr
    bd = dilate(erode(cand, 1), 1) & cand
    border = np.zeros_like(bd); border[0, :] = border[:, 0] = border[:, -1] = True   # top and sides (the bottom is the presenter's)
    return bd & (reconstruct(border, bd) | dilate(erode(bd, 5), 5))

def chroma_range(Ml):
    """log R/G, log B/G range of the backdrop seen in the frame border (top 12 % rows, outer 10 % columns), 1-99 %"""
    hh, ww = Ml.shape[:2]; band = np.zeros((hh, ww), bool)
    band[: max(1, int(0.12 * hh))] = True; band[:, : max(1, int(0.1 * ww))] = True; band[:, -max(1, int(0.1 * ww)):] = True
    ref = np.median(Ml[: max(2, hh // 8)].reshape(-1, 3), 0); dc, dl = logratio(Ml, np.log(np.maximum(ref, 1.0)))
    ok = band & (dc < 0.15) & (dl > -0.6) & (dl < 0.2)
    if ok.sum() < 20: ok = band
    l = np.log(np.maximum(Ml[ok], 1.0)); cr = l[:, 0] - l[:, 1]; cb = l[:, 2] - l[:, 1]
    return (float(np.percentile(cr, 1)), float(np.percentile(cr, 99)), float(np.percentile(cb, 1)), float(np.percentile(cb, 99)))

def analyze(path, info, mx, nsamp=24):
    w, h, n = info["w"], info["h"], info["n"]
    idx = set(np.linspace(0, max(n - 1, 0), min(nsamp, max(n, 1))).round().astype(int).tolist())
    SY, SU, SV, low = [], [], [], []
    for i, (Y, U, V) in enumerate(decode(path, w, h)):
        if i in idx: SY.append(Y.copy()); SU.append(U.copy()); SV.append(V.copy())
        low.append(mx.to_rgb(Y[3::8, 3::8], U[1::4, 1::4], V[1::4, 1::4]))   # point samples, 1/8 res: exposure drift only
    if len(SY) < 3: raise SystemExit(f"[flatten] too few frames decoded from {path}")
    MY = np.median(np.stack(SY), 0).astype(np.float32); MU = np.median(np.stack(SU), 0).astype(np.float32); MV = np.median(np.stack(SV), 0).astype(np.float32)
    Mh = mx.to_rgb(bmean(MY, 2), MU, MV)                              # temporal median at chroma resolution
    Mq = bmean(Mh, 2); Ml = bmean(Mh, 4)
    g = chroma_range(Ml)                                              # the backdrop's own chroma range (frame border)
    sr = set_rows(Mq)                                                 # cornice / moulding rows at the top edge
    ref = np.median(Ml[: max(2, Ml.shape[0] // 8)].reshape(-1, 3), 0)   # top rows: (almost) always backdrop
    dc0, dl0 = logratio(Ml, np.log(np.maximum(ref, 1.0)))
    F = np.exp(polyfit_robust(np.log(np.maximum(Ml, 1.0)), tukey(dc0, 0.15) * ((dl0 > -0.6) & (dl0 < 0.2)) * (gate(Ml, g) > 0.5)))
    bd = classify_backdrop(Mq, np.log(resize(F, Mq.shape[0], Mq.shape[1])), g, sr)
    if bd.mean() < 0.05: raise SystemExit(f"[flatten] {path}: no plain backdrop found ({100 * bd.mean():.1f} % of the frame)")
    Pq = box(push_pull(Mq, erode(bd, 1).astype(np.float32)), 1)
    Ph = resize(Pq, h // 2, w // 2)
    rf = np.log(np.maximum(Mh, 1.0)) - np.log(np.maximum(Ph, 1.0)); dlf = rf[..., 1]
    cf = (1 - smoothstep(0.08, 0.15, chroma_dist(rf))) * smoothstep(-0.6, -0.4, dlf) * (1 - smoothstep(0.08, 0.15, dlf))
    cf = box3(box3(np.maximum(cf * resize(erode(bd, 2).astype(np.float32), h // 2, w // 2), resize((sr & bd).astype(np.float32), h // 2, w // 2))))
    Ph = Ph + cf[..., None] * (Mh - Ph)
    # full-res luma detail of static backdrop structures (moulding lines, steep corners) the half-res plate cannot hold
    Dl = (MY - mx.yo) / np.maximum(up2_lin(half(MY)) - mx.yo, 1.0)
    D = 1 + up2_lin(cf) * np.clip(Dl - 1, -0.3, 0.3)
    lq = np.log(np.maximum(bmean(Ph, 2), 1.0)); un = bd.copy()
    for Y, U, V in zip(SY, SU, SV):
        un |= classify_backdrop(mx.to_rgb(bmean(Y, 4), bmean(U, 2), bmean(V, 2)), lq, g, sr)
    prior_h = np.clip(resize(box(dilate(un.astype(np.float32), 4), 2), h // 2, w // 2), 0, 1)
    k, kraw = drift(low, Ph, bd)
    return {"Ph": Ph, "prior_h": prior_h, "k": k, "kraw": kraw, "bd": bd, "union": un, "M": Mh, "F": F, "cf": cf, "nlow": len(low), "gate": g,
            "D": D.astype(np.float32)}

def drift(low, Ph, bd_q):
    """per-frame (per channel) ratio of the visible backdrop to the plate, gaussian-smoothed over time (sigma 8 frames)"""
    Pl = bmean(Ph, 4); hl, wl = Pl.shape[:2]; lp = np.log(np.maximum(Pl, 1.0))
    m = resize(erode(bd_q, 2).astype(np.float32), hl, wl) > 0.99
    ks = []
    for L in low:
        r = np.log(np.maximum(L[:hl, :wl], 1.0)) - lp
        dc = np.maximum(np.abs(r[..., 0] - r[..., 1]), np.abs(r[..., 2] - r[..., 1]))
        ok = m & (dc < 0.03) & (np.abs(r[..., 1]) < 0.10)
        ks.append(np.median(r[ok], 0) if ok.sum() > 50 else np.full(3, np.nan))
    k = np.array(ks, np.float64)
    for c in range(3):
        bad = ~np.isfinite(k[:, c])
        if bad.all(): k[:, c] = 0.0
        elif bad.any(): k[bad, c] = np.interp(np.flatnonzero(bad), np.flatnonzero(~bad), k[~bad, c])
    s = 8.0; r = int(3 * s); g = np.exp(-0.5 * (np.arange(-r, r + 1) / s) ** 2); g /= g.sum()
    kp = np.pad(k, ((r, r), (0, 0)), mode="reflect" if len(k) > r else "edge")
    ks = np.stack([np.convolve(kp[:, c], g, mode="valid") for c in range(3)], -1)
    return np.exp(np.clip(ks, -0.15, 0.15)).astype(np.float32), np.exp(k)

# ----------------------------------------------------------------------------------------------------------------------
# 2) render
def weight_and_residual(rgbh, logPk, prior_h, prior_q, g):
    """soft backdrop weight (chroma res) and the frame's own smooth log residual against plate*k (+-6 %, returned at chroma res)"""
    l = np.log(np.maximum(rgbh, 1.0)); lr = l - logPk
    dc = chroma_dist(lr); dl = lr[..., 1]
    wr = (1 - smoothstep(0.04, 0.09, dc)) * smoothstep(-0.65, -0.40, dl) * (1 - smoothstep(0.08, 0.16, dl)) * prior_h * gate(l, g, True)
    wt = box3(box3(max3(wr)))
    # residual: soft shadows / local light changes on the backdrop (within +-6 %), measured on confident backdrop only (1/4 res)
    lq = half(lr); dq = chroma_dist(lq)
    cq = ((dq < 0.03) & (np.abs(lq).max(-1) < 0.06)).astype(np.float32) * prior_q
    num = box(box(lq * cq[..., None], 6), 6); den = box(box(cq, 6), 6)
    res = num / np.maximum(den, 1e-3)[..., None] * np.clip(den / 0.25, 0, 1)[..., None]
    return wt, up2_lin(np.clip(res, -0.06, 0.06))

def render(path, out, info, mx, A, target_rgb, keep=()):
    w, h = info["w"], info["h"]; Ph = A["Ph"]; logPh = np.log(np.maximum(Ph, 1.0)); prior_h = A["prior_h"]; k = A["k"]
    prior_q = (bmean(prior_h, 2) > 0.999).astype(np.float32)
    lG0 = np.log(np.clip(target_rgb / np.maximum(Ph, 1.0), 0.5, 2.5)).astype(np.float32)   # dark mouldings need up to ~1.9x blue
    rng = np.random.default_rng(20261015)                        # deterministic dither fields, shifted per frame
    DY = (rng.random((h + 64, w + 64), np.float32) - 0.5); DU = (rng.random((h // 2 + 64, w // 2 + 64), np.float32) - 0.5)
    DV = (rng.random((h // 2 + 64, w // 2 + 64), np.float32) - 0.5)
    # a video stream that starts after 0 (edit list) keeps its start, so the copied audio stays in sync
    off = ["-itsoffset", f"{info['vstart']:.6f}"] if info.get("vstart", 0.0) > 1e-4 else []   # (other cases: the pts check warns)
    enc = ["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "yuv420p", "-s", f"{w}x{h}", "-framerate", info["fps"]] + off + ["-i", "-",
           "-i", path, "-map", "0:v:0", "-map", "1:a?", "-c:v", "libx264", "-preset", "medium", "-crf", "10", "-pix_fmt", "yuv420p"]
    # the source's colour tags, set on the frames (ffmpeg 9 lets untagged frames override -color_primaries / -color_trc)
    sp = [f"{opt}={info['tags'][tag]}" for tag, opt in (("color_space", "colorspace"), ("color_range", "range"), ("color_primaries", "color_primaries"),
                                                         ("color_transfer", "color_trc")) if info["tags"].get(tag) not in (None, "", "unknown")]
    if sp: enc += ["-vf", "setparams=" + ":".join(sp)]
    tmp = out + ".part.mp4"; enc += ["-c:a", "copy", "-movflags", "+faststart", tmp]
    pe = subprocess.Popen(enc, stdin=subprocess.PIPE)
    wsum = np.zeros((h // 2, w // 2), np.float32); nf = 0; snaps = {}; rmax = 0.0; iys = np.float32(1 / mx.ys)
    invD = (1 / A["D"]).astype(np.float32); omD = (1 - A["D"]).astype(np.float32)
    try:
        for i, (Y, U, V) in enumerate(decode(path, w, h)):
            lk = np.log(k[min(i, len(k) - 1)])
            ch = mx.chroma(U, V); rgbh = ((half(Y) - mx.yo) * mx.ys)[..., None] + ch
            wt, res = weight_and_residual(rgbh, logPh + lk, prior_h, prior_q, A["gate"])
            a = np.exp(lG0 - lk - res); a -= 1; a *= wt[..., None]      # w*(G-1), G = target / (plate * k * residual)
            dU, dV = mx.delta_uv(rgbh * a)
            # luma delta on the full grid, with the static full-res detail D: dY = ((Y - yo)*(s1 + w(1 - D)) + s2/ys) / D
            s1 = up2_lin(a @ mx.k); s2 = up2_lin((a * ch) @ mx.k); s1 += up2_lin(wt) * omD
            dY = Y * s1; dY += s2 * iys - mx.yo * s1; dY *= invD
            oy, ox = (i * 37) % 64, (i * 23) % 64; on = wt > 0       # dithered rounding where (and only where) it changes
            np.add(dY, DY[oy:oy + h, ox:ox + w], out=dY, where=s1 != 0)
            dU += DU[oy // 2:oy // 2 + h // 2, ox // 2:ox // 2 + w // 2] * on; dV += DV[oy // 2:oy // 2 + h // 2, ox // 2:ox // 2 + w // 2] * on
            dY += Y; np.rint(dY, out=dY); np.clip(dY, 0, 255, out=dY); Yo = dY.astype(np.uint8)
            Uo = np.clip(np.rint(U + dU), 0, 255).astype(np.uint8); Vo = np.clip(np.rint(V + dV), 0, 255).astype(np.uint8)
            pe.stdin.write(Yo.tobytes()); pe.stdin.write(Uo.tobytes()); pe.stdin.write(Vo.tobytes())
            wsum += wt; nf += 1; rmax = max(rmax, float(np.abs(res).max()))
            if i in keep: snaps[i] = wt
    finally:
        pe.stdin.close(); rc = pe.wait()
    if rc != 0: raise SystemExit(f"[flatten] encoder failed for {path}")
    os.replace(tmp, out)
    return {"frames": nf, "wmean": wsum / max(nf, 1), "snaps": snaps, "resmax": rmax}

# ----------------------------------------------------------------------------------------------------------------------
# 3) verification: mock of compose2 (box mode 640x1080 at x 0, panel from x 640 with a 48 px feather)
BOX_W, BOX_H, FY, CANVAS = 640, 1080, 0.35, (1920, 1080)
def box_geometry(w, h):
    """compose2 box_chain for fx 0.5, fy 0.35, zoom 1: cover scale size and crop offset (crop offsets are even for yuv420p)"""
    sw, sh = max(BOX_W, int(BOX_H * w / h + 0.5)), max(BOX_H, int(BOX_W * h / w + 0.5))
    x0 = int(min(max(0.5 * sw - BOX_W // 2, 0), sw - BOX_W)) // 2 * 2; y0 = int((sh - BOX_H) * FY) // 2 * 2
    return sw / w, x0, y0

def test_overlay(path):
    W, H = CANVAS; img = np.zeros((H, W, 4), np.uint8); img[:, 592:, :3] = (245, 240, 232)
    img[:, 592:640, 3] = np.round((np.arange(48) + 0.5) / 48 * 255).astype(np.uint8)[None, :]; img[:, 640:, 3] = 255
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{W}x{H}", "-i", "-", path], input=img.tobytes(), check=True)

def mock_composite(clip, frames, tmpdir, tag, png):
    W, H = CANVAS; sel = "+".join(f"eq(n\\,{i})" for i in frames)
    base = os.path.join(tmpdir, f"{tag}_base.mp4"); fin = os.path.join(tmpdir, f"{tag}_final.mp4")
    vf = (f"select='{sel}',setpts=N/24/TB,scale={BOX_W}:{BOX_H}:force_original_aspect_ratio=increase:flags=lanczos,"
          f"crop={BOX_W}:{BOX_H}:x='clip(0.5000*iw-{BOX_W // 2},0,iw-{BOX_W})':y='(ih-{BOX_H})*{FY:.4f}',fps=24,format=yuv420p,setsar=1,"
          f"unsharp=5:5:0.5:5:5:0,pad={W}:{H}:0:0:color=0xf5f0e8")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", clip, "-vf", vf, "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "12",
                    "-pix_fmt", "yuv420p", "-r", "24", base], check=True)
    g3 = "[0:v]fps=24[b];[1:v]fps=24,format=rgba[o];[b][o]overlay=0:0:eof_action=pass:shortest=1:format=auto,fps=24,format=yuv420p[v]"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", base, "-loop", "1", "-framerate", "24", "-i", png, "-filter_complex", g3,
                    "-map", "[v]", "-c:v", "libx264", "-preset", "medium", "-crf", "17", "-pix_fmt", "yuv420p", "-r", "24", fin], check=True)
    b = subprocess.run(["ffmpeg", "-v", "error", "-i", fin, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True).stdout
    n = W * H * 3   # frames stay uint8 (views of b): 20 float32 1080p frames were ~0.5 GB of the tool's 0.7 GB peak
    return [np.frombuffer(b, np.uint8, n, j * n).reshape(H, W, 3) for j in range(len(b) // n)]

def verify(src, out, info, mx, A, R, frames, dbg=None):
    w, h = info["w"], info["h"]; W, H = CANVAS
    sc, x0, y0 = box_geometry(w, h)
    # what the viewer sees as backdrop in each verified frame, in box coordinates: everything except the presenter (pixels
    # with weight < 0.5 connected to the bottom edge) and 16 px around it (stray hair). Anything the matte missed (a
    # moulding, a pocket) is therefore measured too.
    by, bx = np.mgrid[0:BOX_H, 0:BOX_W]
    sy = np.clip(((by + y0 + 0.5) / sc - 0.5) / 4, 0, h // 4 - 1).astype(int); sx = np.clip(((bx + x0 + 0.5) / sc - 0.5) / 4, 0, w // 4 - 1).astype(int)
    def seen(wt):
        p = half(wt) < 0.5; seed = np.zeros_like(p); seed[-1, :] = True
        return ~dilate(reconstruct(seed, p), 4)
    masks = [seen(R["snaps"][f])[sy, sx] for f in frames]
    tmpdir = tempfile.mkdtemp(prefix=".verify_", dir=os.path.dirname(os.path.abspath(out)))   # removed below
    try:
        png = os.path.join(tmpdir, "panel.png"); test_overlay(png)
        before = mock_composite(src, frames, tmpdir, "before", png); after = mock_composite(out, frames, tmpdir, "after", png)
        if dbg and before and after:
            j = len(before) // 2; save_png(f"{dbg}/mock_before.png", before[j]); save_png(f"{dbg}/mock_after.png", after[j])
            z = lambda im: np.repeat(np.repeat(im[0:200, 540:740], 4, 0), 4, 1)             # 4x zoom of the top of the seam
            save_png(f"{dbg}/mock_seam_zoom4x.png", np.concatenate([z(before[j]), np.full((800, 8, 3), 255, np.float32), z(after[j])], 1))
            m = masks[j]; ov = after[j][:, :BOX_W].copy(); ov[~m] = ov[~m] * 0.35; save_png(f"{dbg}/mock_backdrop_mask.png", ov)
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)
    nb = min(len(before), len(after), len(masks))
    if nb == 0: return None
    def region(frames_rgb, x0_, x1_, y0_, y1_, need_full_rows=False):
        acc, cnt = np.zeros(3), 0
        for f, m in zip(frames_rgb[:nb], masks[:nb]):
            mm = m[y0_:y1_, x0_:min(x1_, BOX_W)]
            if need_full_rows: mm = np.repeat(mm.all(1, keepdims=True), x1_ - x0_, 1)
            px = f[y0_:y1_, x0_:x1_][mm] if x1_ <= BOX_W else None
            if px is not None and len(px): acc += px.sum(0); cnt += len(px)
        return acc / cnt if cnt else None, cnt
    def rows_panel(frames_rgb):
        acc, cnt = np.zeros(3), 0
        for f, m in zip(frames_rgb[:nb], masks[:nb]):
            rows = m[:, 600:640].all(1)
            if rows.any(): px = f[rows][:, 641:701].reshape(-1, 3); acc += px.sum(0); cnt += len(px)
        return acc / cnt if cnt else None
    st = {}
    for tag, fr in (("before", before), ("after", after)):
        st[tag] = {"seam": region(fr, 600, 640, 0, BOX_H, True)[0], "TL": region(fr, 8, 128, 8, 168)[0], "TR": region(fr, 470, 590, 8, 168)[0],
                   "panel": rows_panel(fr)}
        devs = []; pan = np.array(PANEL_RGB_DECODED, float)
        for f, m in zip(fr[:nb], masks[:nb]):                # 16x16 patch means vs the panel, box x < 592 (left of the feather)
            pm = f[:BOX_H // 16 * 16, :592].reshape(BOX_H // 16, 16, 37, 16, 3).mean((1, 3))
            ok = m[:BOX_H // 16 * 16, :592].reshape(BOX_H // 16, 16, 37, 16).all((1, 3))
            devs += np.abs(pm - pan).max(-1)[ok].tolist()
        st[tag]["worst"] = max(devs) if devs else float("nan"); st[tag]["p99"] = float(np.percentile(devs, 99)) if devs else float("nan")
    # presenter patches in the clip domain: face (skin cluster of the median) and shirt (bright, neutral-to-blue, under the face)
    M = A["M"]; hh, ww = M.shape[:2]; yy, xx = np.mgrid[0:hh, 0:ww]
    notbd = ~(resize(A["bd"].astype(np.float32), hh, ww) > 0.5); Rr, Gg, Bb = M[..., 0], M[..., 1], M[..., 2]
    skin = notbd & (Rr > Gg) & (Gg > Bb) & (Rr - Bb > 40) & (Rr - Gg > 15) & (Rr > 90) & (Rr < 250) & (yy < 0.5 * hh)
    patches = {}
    if skin.sum() > 50:
        cy, cx = int(np.median(yy[skin])), int(np.median(xx[skin])); patches["face"] = (cy - 12, cy + 12, cx - 12, cx + 12)
        shirt = notbd & (Bb >= Rr - 8) & (Gg > 120) & (yy > cy + 0.12 * hh) & (yy < cy + 0.45 * hh) & (np.abs(xx - cx) < 0.12 * ww)
        if shirt.sum() > 30:
            sy_, sx_ = int(np.median(yy[shirt])), int(np.median(xx[shirt])); patches["shirt"] = (sy_ - 10, sy_ + 10, sx_ - 10, sx_ + 10)
    pres = {k_: [np.zeros(3), np.zeros(3), 0] for k_ in patches}
    for (Ys, Us, Vs), (Yo, Uo, Vo) in zip(decode(src, w, h, frames), decode(out, w, h, frames)):
        a_ = mx.to_rgb(bmean(Ys.astype(np.float32), 2), Us, Vs); b_ = mx.to_rgb(bmean(Yo.astype(np.float32), 2), Uo, Vo)
        for k_, (p0, p1, q0, q1) in patches.items():
            pres[k_][0] += a_[p0:p1, q0:q1].reshape(-1, 3).mean(0); pres[k_][1] += b_[p0:p1, q0:q1].reshape(-1, 3).mean(0); pres[k_][2] += 1
    st["presenter"] = {k_: (v[0] / v[2], v[1] / v[2]) for k_, v in pres.items() if v[2]}
    st["patch_pos"] = {k_: (2 * (p[0] + p[1]) // 2, 2 * (p[2] + p[3]) // 2) for k_, p in patches.items()}
    return st

# ----------------------------------------------------------------------------------------------------------------------
def audio_md5(path):
    o = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-map", "0:a:0", "-c", "copy", "-f", "md5", "-"], capture_output=True, text=True).stdout.strip()
    return o or None

def video_pts(path):
    """sorted video packet pts (seconds, no decode): the output must keep the source's frame times, or the picture drifts
    from the copied audio (e.g. a source whose video starts after 0 through an edit list)"""
    o = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "packet=pts_time", "-of", "csv=p=0", path],
                       capture_output=True, text=True).stdout.split()
    return sorted(round(float(x), 4) for x in o if x not in ("", "N/A"))

def fmt(v): return "(" + ",".join(f"{x:.0f}" for x in v) + ")" if v is not None else "(n/a)"
def fmtd(a, b): return "(" + ",".join(f"{x - y:+.1f}" for x, y in zip(a, b)) + ")" if a is not None and b is not None else "(n/a)"

def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("clips", nargs="+"); ap.add_argument("--out-dir", help="default: <clip dir>/flat"); ap.add_argument("--debug", help="debug image dir")
    ap.add_argument("--no-verify", action="store_true", help="skip the compose2 mock measurement")
    ap.add_argument("--target-yuv", help="override the clip-domain target Y,U,V (default %s)" % ",".join(map(str, TARGET_YUV)))
    a = ap.parse_args()
    tgt = tuple(float(v) for v in a.target_yuv.split(",")) if a.target_yuv else TARGET_YUV
    for c in a.clips:
        t0 = time.time(); info = probe(c)
        if info["w"] % 2 or info["h"] % 2: raise SystemExit(f"[flatten] {c}: odd frame size {info['w']}x{info['h']}")
        mx = Matrix(info["tags"].get("color_space"), info["tags"].get("color_range"))
        T = Matrix(info["tags"].get("color_space"), "tv").to_rgb(np.float32(tgt[0]), np.float32(tgt[1]), np.float32(tgt[2]))   # target is limited-range
        od = a.out_dir or os.path.join(os.path.dirname(os.path.abspath(c)), "flat"); os.makedirs(od, exist_ok=True)
        name = os.path.basename(c); out = os.path.join(od, name)
        if os.path.abspath(out) == os.path.abspath(c): raise SystemExit(f"[flatten] refusing to overwrite the source {c}")
        dbg = os.path.join(a.debug, os.path.splitext(name)[0]) if a.debug else None
        if dbg: os.makedirs(dbg, exist_ok=True)
        A = analyze(c, info, mx); t1 = time.time()
        vf = sorted(set(np.linspace(info["n"] * 0.04, info["n"] * 0.96 - 1, 10).round().astype(int).tolist()))
        R = render(c, out, info, mx, A, T, keep=set(vf) | {A["nlow"] // 2}); t2 = time.time()
        oi = probe(out); same_a = (audio_md5(c) == audio_md5(out)) if info["audio"] else None
        warn = []
        if oi["n"] != info["n"] or abs(oi["dur"] - info["dur"]) > 0.03: warn.append(f"frames {oi['n']} vs {info['n']}, duration {oi['dur']:.3f} vs {info['dur']:.3f}")
        ps, po = video_pts(c), video_pts(out)
        if len(ps) != len(po) or (ps and max(abs(x - y) for x, y in zip(ps, po)) > 0.002):
            warn.append(f"video frame times differ from the source (first {ps[:1]} vs {po[:1]}): A/V sync not guaranteed")
        if info["audio"] and not same_a: warn.append("audio is not bit-exact")
        if dbg:
            h, w = info["h"], info["w"]
            save_png(f"{dbg}/median.png", resize(A["M"], h, w)); save_png(f"{dbg}/plate.png", resize(A["Ph"], h, w)); save_png(f"{dbg}/fit.png", resize(A["F"], h, w))
            save_png(f"{dbg}/backdrop_median.png", resize(A["bd"].astype(np.float32), h, w) * 255)
            save_png(f"{dbg}/backdrop_union.png", resize(A["union"].astype(np.float32), h, w) * 255)
            save_png(f"{dbg}/prior.png", resize(A["prior_h"], h, w) * 255); save_png(f"{dbg}/weight_mean.png", resize(R["wmean"], h, w) * 255)
            mid = A["nlow"] // 2; save_png(f"{dbg}/weight_{mid:04d}.png", resize(R["snaps"][mid], h, w) * 255)
            save_png(f"{dbg}/residual_x4.png", resize(np.clip(128 + 4 * (A["M"] - A["Ph"]), 0, 255), h, w))
            for tag, p in (("before", c), ("after", out)):
                subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", p, "-vf", f"select=eq(n\\,{mid})", "-frames:v", "1", f"{dbg}/frame_{tag}.png"], check=True)
        line = (f"[flatten] {name} -> {out} | {R['frames']}/{info['n']} frames {oi['dur']:.2f}s, audio {'bit-exact' if same_a else ('none' if same_a is None else 'CHANGED')}, "
                f"{mx.name}, backdrop TL {fmt(A['Ph'][8:88, 8:68].reshape(-1, 3).mean(0))}, drift k {A['k'].min():.3f}..{A['k'].max():.3f}")
        if not a.no_verify:
            st = verify(c, out, info, mx, A, R, vf, dbg)
            if st:
                b_, a_ = st["before"], st["after"]
                line += (f" | final mp4 RGB (panel #f5f0e8 lands as {fmt(a_['panel'])}): seam x600-639 {fmt(b_['seam'])}->{fmt(a_['seam'])} d{fmtd(a_['seam'], a_['panel'])},"
                         f" top-left {fmt(b_['TL'])}->{fmt(a_['TL'])} d{fmtd(a_['TL'], a_['panel'])}, top-right {fmt(b_['TR'])}->{fmt(a_['TR'])} d{fmtd(a_['TR'], a_['panel'])},"
                         f" 16px backdrop patches |d| max {b_['worst']:.1f}->{a_['worst']:.1f} (p99 {b_['p99']:.1f}->{a_['p99']:.1f}) | presenter " +
                         ", ".join(f"{k_} {fmt(p0)}->{fmt(p1)} d{fmtd(p1, p0)}" for k_, (p0, p1) in st["presenter"].items()))
                # the brief's limits: seam step <= 2 per channel, visible backdrop <= 4, presenter colours change only a few units
                dmax = lambda p, q: float(np.max(np.abs(np.asarray(p, float) - np.asarray(q, float)))) if p is not None and q is not None else 0.0
                if dmax(a_["seam"], a_["panel"]) > 2: warn.append(f"seam strip differs from the panel by {dmax(a_['seam'], a_['panel']):.1f} (> 2)")
                for k_ in ("TL", "TR"):
                    if dmax(a_[k_], a_["panel"]) > 4: warn.append(f"backdrop {k_} corner differs from the panel by {dmax(a_[k_], a_['panel']):.1f} (> 4)")
                if a_["worst"] > 4: warn.append(f"a 16 px backdrop patch differs from the panel by {a_['worst']:.1f} (> 4): check {dbg or '--debug'}")
                for k_, (p0, p1) in st["presenter"].items():
                    if dmax(p0, p1) > 3: warn.append(f"presenter {k_} colour changed by {dmax(p0, p1):.1f} (> 3): a backdrop-coloured garment or skin?")
            else:
                warn.append("verification measured nothing")
        line += f" | {t2 - t0:.1f}s" + ("" if a.no_verify else f" + verify {time.time() - t2:.1f}s") + (f" | QA CHECK ({len(warn)})" if warn else " | QA ok")
        print(line, flush=True)
        for m_ in warn: print(f"[flatten] WARNING {name}: {m_}", flush=True)

if __name__ == "__main__":
    main()
