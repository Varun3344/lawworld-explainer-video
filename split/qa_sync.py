"""Lip-sync check of a composed course video (owner 19-10-2026: "match proper lip syncing"): for every presenter segment of the plan,
(1) the SOUND in the final at the segment's place is cross-correlated with the source clip's own sound -> audio offset, and
(2) the PICTURE of the presenter box in the final is matched against the source clip's frames -> video offset;
lips stay in sync when both offsets agree (picture minus sound within one frame, 42 ms, everywhere).
Usage: python3 split/qa_sync.py <set> [--every N]   (default: every clip)"""
import json, subprocess, sys, numpy as np
SET = sys.argv[1]; EVERY = int(sys.argv[sys.argv.index("--every") + 1]) if "--every" in sys.argv else 1
P = json.load(open(f"out/{SET}/plan.json")); FULL = P["out"]; FPS = 24; SR = 8000
def audio(path, ss, dur):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{ss:.3f}", "-t", f"{dur:.3f}", "-i", path, "-vn", "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True).stdout
    return np.frombuffer(raw, np.float32)
def frames(path, ss, n, crop=None, scale="64:108"):
    vf = (f"crop={crop}," if crop else "") + f"scale={scale},format=gray"
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{ss:.3f}", "-i", path, "-frames:v", str(n), "-vf", vf, "-f", "rawvideo", "-"], capture_output=True).stdout
    w, h = map(int, scale.split(":")); k = len(raw) // (w * h)
    return np.frombuffer(raw[:k * w * h], np.uint8).reshape(k, h, w).astype(np.float32)
def xcorr_lag(a, b, maxlag):
    """lag (samples) of b relative to a that maximises the correlation of envelopes"""
    ea = np.abs(a); eb = np.abs(b); n = min(len(ea), len(eb)); ea, eb = ea[:n] - ea[:n].mean(), eb[:n] - eb[:n].mean()
    best, bl = -1e9, 0
    for lag in range(-maxlag, maxlag + 1, 4):
        x = ea[max(0, lag):n + min(0, lag)]; y = eb[max(0, -lag):n - max(0, lag)]
        if len(x) < SR: continue
        c = float(np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y) + 1e-9))
        if c > best: best, bl = c, lag
    return bl, best
t = P["presenter_start"]; worst = 0.0; rows = []
for k, seg in enumerate(P["presenter"]):
    L = seg["out"] - seg["in"]
    if k % EVERY == 0 and L > 2.0:
        # sound: the final at [t, t+L] vs the clip at [in, out]
        lag, c = xcorr_lag(audio(seg["clip"], seg["in"], L), audio(FULL, t, L), int(0.25 * SR))
        a_off = -lag / SR
        # picture: 12 frames of the final's presenter box vs the clip's own frames around the same moment (the best frame shift)
        mid = t + L / 2; n = 12
        fin = frames(FULL, mid, n, crop="640:1080:1280:0")
        src = frames(seg["clip"], seg["in"] + L / 2 - 3 / FPS, n + 6, scale="64:108")
        errs = []
        for sh in range(0, 7):
            m = min(len(fin), len(src) - sh)
            if m < 6: continue
            d = fin[:m] - fin[:m].mean(axis=(1, 2), keepdims=True); s = src[sh:sh + m] - src[sh:sh + m].mean(axis=(1, 2), keepdims=True)
            errs.append((float(np.mean(np.abs(np.diff(d, axis=0) - np.diff(s, axis=0)))), sh))
        v_off = (min(errs)[1] - 3) / FPS if errs else float("nan")
        diff = v_off - a_off; worst = max(worst, abs(diff))
        rows.append((seg["clip"].split("/")[-1][:-4], round(t, 2), round(a_off * 1000), round(v_off * 1000), round(diff * 1000), round(c, 2)))
    t += L
for r in rows: print(f"[sync] {r[0]} at {r[1]:7.2f}s  sound {r[2]:+4d} ms  picture {r[3]:+4d} ms  lips {r[4]:+4d} ms  (corr {r[5]})")
print(f"[sync] {SET}: {len(rows)} segments checked, worst picture-vs-sound {worst * 1000:.0f} ms -> " + ("OK" if worst <= 0.045 else "CHECK"))
