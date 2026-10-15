#!/usr/bin/env python3
"""Estimate the presenter's horizontal centre (0..1 of the frame width) in a talking-head clip. No OpenCV: ffmpeg + numpy.

Usage: python3 split/face_x.py <clip.mp4> [--fps 2] [--width 192] [--start S] [--dur D] [--debug out.png] [-v]
Prints one number (e.g. 0.497) for presenter_box.fx / a segment's "fx" in compose2.py plans.

Method: ffmpeg decodes grayscale frames at 2 fps, 192 px wide. A static set does not change and a slow camera drift or light
ramp changes steadily, while a talking presenter (mouth, head, hands) changes direction, so the motion energy per pixel is
the mean absolute SECOND temporal difference |f[t+1] - 2 f[t] + f[t-1]|, after removing each difference image's median
(noise floor, flicker). Energy is summed per column over the top 85 % of the frame (desk / lower third left out), the
background level (30th-percentile column) is subtracted, and a mean-shift window 35 % of the width wide, started at the
smoothed peak, settles on the presenter's centre of mass. -v prints the confidence (share of the motion inside the window)
and the 10-90 % motion extent; --debug writes a mid-clip frame over the motion map with the estimate drawn in red."""
import sys, json, argparse, subprocess
import numpy as np

def probe(path):
    o = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height:format=duration",
                        "-of", "json", path], capture_output=True, text=True)
    try:
        d = json.loads(o.stdout); s = d["streams"][0]; return int(s["width"]), int(s["height"]), float(d["format"]["duration"])
    except (ValueError, KeyError, IndexError):
        raise SystemExit(f"face_x: cannot read {path}")

def gray_frames(path, fps, width, start, dur):
    w0, h0, d0 = probe(path); h = max(2, int(round(width * h0 / w0 / 2)) * 2)
    cmd = ["ffmpeg", "-v", "error"] + (["-ss", str(start)] if start else []) + (["-t", str(dur)] if dur else []) + \
          ["-i", path, "-vf", f"fps={fps},scale={width}:{h}:flags=area,format=gray", "-f", "rawvideo", "-"]
    raw = subprocess.run(cmd, capture_output=True).stdout; n = len(raw) // (width * h)
    return np.frombuffer(raw[:n * width * h], np.uint8).reshape(n, h, width).astype(np.float32), (w0, h0, d0)

def estimate(F, bottom=0.85, win=0.35, base_pct=30):
    n, h, w = F.shape
    if n < 2: raise SystemExit("face_x: need at least 2 frames (clip too short?)")
    D = np.abs(F[2:] - 2 * F[1:-1] + F[:-2]) if n >= 3 else np.abs(F[1:] - F[:-1])
    D = np.clip(D - np.median(D.reshape(len(D), -1), axis=1)[:, None, None], 0, None)
    E = D.mean(axis=0)                                    # motion energy map, h x w
    col = E[: max(1, int(bottom * h))].sum(axis=0)
    c = np.clip(col - np.percentile(col, base_pct), 0, None)
    if c.sum() <= 1e-6: return 0.5, 0.0, (0.0, 1.0), E   # nothing moves: centre
    k = max(3, int(w * 0.08) | 1); sm = np.convolve(c, np.ones(k) / k, mode="same")
    xs = np.arange(w, dtype=np.float64); x = float(np.argmax(sm)); half = win * w / 2
    for _ in range(30):                                   # mean shift on the column profile
        m = (xs >= x - half) & (xs <= x + half); nx = float((xs[m] * c[m]).sum() / max(c[m].sum(), 1e-9))
        if abs(nx - x) < 0.01: x = nx; break
        x = nx
    m = (xs >= x - half) & (xs <= x + half); conf = float(c[m].sum() / c.sum())
    cum = np.cumsum(c[m]) / max(c[m].sum(), 1e-9); xm = xs[m]
    ext = (float(xm[np.searchsorted(cum, 0.1)] + 0.5) / w, float(xm[min(len(xm) - 1, np.searchsorted(cum, 0.9))] + 0.5) / w)
    return (x + 0.5) / w, conf, ext, E

def debug_png(path, clip, t, fx, E):
    em = (255 * np.clip(E / (np.percentile(E, 99.5) + 1e-6), 0, 1)).astype(np.uint8); eh, ew = em.shape; X = int(round(fx * 640))
    line = f"drawbox=x={X - 1}:y=0:w=3:h=ih:color=red@0.9:t=fill"
    g = (f"[0:v]scale=640:-2,format=rgb24,{line}[a];[1:v]scale=640:-2:flags=neighbor,format=rgb24,{line}[b];[a][b]vstack")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", clip, "-f", "rawvideo", "-pix_fmt", "gray",
                    "-s", f"{ew}x{eh}", "-i", "-", "-filter_complex", g, "-frames:v", "1", path], input=em.tobytes(), check=True)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="presenter horizontal centre (0..1) of a talking-head clip")
    ap.add_argument("clip"); ap.add_argument("--fps", type=float, default=2.0); ap.add_argument("--width", type=int, default=192)
    ap.add_argument("--start", type=float, default=0.0); ap.add_argument("--dur", type=float, default=0.0)
    ap.add_argument("--debug"); ap.add_argument("-v", "--verbose", action="store_true")
    a = ap.parse_args()
    F, (w0, h0, d0) = gray_frames(a.clip, a.fps, a.width, a.start, a.dur)
    fx, conf, ext, E = estimate(F)
    if a.verbose or conf < 0.5:
        print(f"face_x: {a.clip} {w0}x{h0} {d0:.2f}s, {len(F)} frames; centre {fx:.3f}, confidence {conf:.2f}, "
              f"motion 10-90% across {ext[0]:.3f}-{ext[1]:.3f}" + ("  (LOW confidence: check with --debug)" if conf < 0.5 else ""), file=sys.stderr)
    if a.debug: debug_png(a.debug, a.clip, a.start + (a.dur or d0 - a.start) / 2, fx, E)
    print(f"{fx:.3f}")
