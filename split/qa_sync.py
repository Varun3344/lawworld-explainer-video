"""Lip-sync check of a composed course video (owner 19-10-2026: "match proper lip syncing"). For every presenter segment of the plan:
  sound    the final's audio at the segment's place, cross-correlated with the source clip's own audio -> sound offset
  picture  the final's presenter box (x 1280..1920) at the segment's middle, against the source clip's frames passed through the
           exact filter chain compose2 used for that segment (from its --print-cmds), at -4..+4 frames -> picture offset
Lips stay in sync when picture - sound is within one frame (42 ms) everywhere; plus a frame-count check of the base video.
Usage: python3 split/qa_sync.py <set> [--every N]"""
import json, re, subprocess, sys, numpy as np
SET = sys.argv[1]; EVERY = int(sys.argv[sys.argv.index("--every") + 1]) if "--every" in sys.argv else 1
PLAN = f"out/{SET}/plan.json"; P = json.load(open(PLAN)); FULL = P["out"]; FPS = 24; SR = 8000
cmds = subprocess.run([sys.executable, "scripts/compose2.py", PLAN, "--print-cmds"], capture_output=True, text=True).stdout
base_cmd = next(l for l in cmds.splitlines() if l.startswith("ffmpeg") and "base.mp4" in l)
chains = {int(m.group(1)): m.group(2) for m in re.finditer(r"\[(\d+):v\]trim=[\d.]+:[\d.]+,setpts=PTS-STARTPTS,(.*?)\[pv\d+\]", base_cmd)}
def audio(path, ss, dur):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{ss:.3f}", "-t", f"{dur:.3f}", "-i", path, "-vn", "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True).stdout
    return np.frombuffer(raw, np.float32)
def gray(path, ss, n, vf):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{ss:.4f}", "-i", path, "-frames:v", str(n), "-vf", vf + ",scale=80:135,format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
    k = len(raw) // (80 * 135); return np.frombuffer(raw[:k * 80 * 135], np.uint8).reshape(k, 135, 80).astype(np.float32)
def lag_of(a, b, maxlag):
    ea, eb = np.abs(a), np.abs(b); n = min(len(ea), len(eb)); ea, eb = ea[:n] - ea[:n].mean(), eb[:n] - eb[:n].mean(); best, bl = -9, 0
    for lag in range(-maxlag, maxlag + 1, 2):
        x = ea[max(0, lag):n + min(0, lag)]; y = eb[max(0, -lag):n - max(0, lag)]
        c = float(np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y) + 1e-9))
        if c > best: best, bl = c, lag
    return bl / SR, best
t = P["presenter_start"]; rows = []; worst = 0.0; nf_exp = round(t * FPS)
for k, seg in enumerate(P["presenter"]):
    L = seg["out"] - seg["in"]; nf_exp += int(np.ceil(seg["out"] * FPS - 1e-9) - np.ceil(seg["in"] * FPS - 1e-9))
    if k % EVERY == 0 and L > 2.0 and k in chains:
        a_off, c = lag_of(audio(seg["clip"], seg["in"], L), audio(FULL, t, L), int(0.2 * SR))
        a_off = -a_off
        mid = round((t + L / 2) * FPS) / FPS; n = 10
        fin = gray(FULL, mid, n, "crop=640:1080:1280:0")
        chain = re.sub(r",pad=1920:1080:\d+:\d+:color=0x[0-9a-f]+", "", chains[k]).split(",format=yuv420p")[0]   # the 640x1080 box itself
        src = gray(seg["clip"], seg["in"] + (mid - t) - 4 / FPS, n + 8, chain)
        errs = [(float(np.mean(np.abs(fin[:min(n, len(src) - j)] - src[j:j + min(n, len(src) - j)]))), j - 4) for j in range(0, 9) if len(src) - j >= n // 2]
        best = min(errs) if errs else (float("nan"), 0); v_off = best[1] / FPS
        d = v_off - a_off; worst = max(worst, abs(d))
        rows.append((seg["clip"].split("/")[-1][:-4], round(t, 2), round(a_off * 1000), round(v_off * 1000), round(d * 1000), round(c, 2), round(best[0], 1)))
    t += L
for r in rows: print(f"[sync] {r[0]} at {r[1]:7.2f}s  sound {r[2]:+4d} ms  picture {r[3]:+4d} ms  lips {r[4]:+4d} ms  (audio corr {r[5]}, frame diff {r[6]})")
bf = subprocess.run(["ffprobe", "-v", "error", "-count_packets", "-select_streams", "v", "-show_entries", "stream=nb_read_packets", "-of", "csv=p=0",
                     f"out/{SET}/work/base.mp4"], capture_output=True, text=True).stdout.strip()
print(f"[sync] base video frames {bf} (presenter part expected {nf_exp}, + end card)")
print(f"[sync] {SET}: {len(rows)} segments, worst picture-vs-sound {worst * 1000:.0f} ms -> " + ("OK" if worst <= 0.045 else "CHECK"))
