"""Report every window where the 16:9 panel body carries no content for longer than MINGAP seconds.
Usage: python3 split/qa_panel.py out/<set>/<set>_full.mp4 [more.mp4 ...]

The compose QA checks the seam, loudness, frame count and the presenter; it does not look at whether the panel
has anything on it. A card whose header is anchored on a word spoken LATER than its own points builds nothing
until that word arrives, so the left two thirds sit empty — 4.5 s of it in swp before the BNS 209 section was
re-anchored (29-10-2026). Run this on every course/concept 16:9 before delivery; build_course_plan's own
"gap ... held" lines do not catch it, because the cue span looks continuous while the drawing starts late.
"""
import subprocess, sys, numpy as np

W, H, FPS, MINGAP = 118, 85, 2, 2.0

def check(path):
    vf = f"crop=1180:860:60:150,fps={FPS},scale={W}:{H},format=gray"   # panel body, minus the chip header
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-vf", vf, "-f", "rawvideo", "-"],
                         capture_output=True).stdout
    a = np.frombuffer(raw, np.uint8)
    a = a[:len(a) // (W * H) * (W * H)].reshape(-1, H, W).astype(np.int16).reshape(-1, H * W)
    ink = ((a - np.median(a, axis=1, keepdims=True)) < -25).mean(axis=1)
    empty, runs, i = ink < 0.004, [], 0
    while i < len(empty):
        if empty[i]:
            j = i
            while j < len(empty) and empty[j]: j += 1
            if (j - i) / FPS >= MINGAP: runs.append((i / FPS, j / FPS))
            i = j
        else: i += 1
    print(f"[qa-panel] {path}: {len(a)/FPS:.0f}s, median ink {np.median(ink)*100:.1f}%")
    for s, e in runs: print(f"[qa-panel]   EMPTY PANEL {s:7.2f} -> {e:7.2f}  ({e-s:.1f} s)")
    if not runs: print(f"[qa-panel]   OK   no empty panel >= {MINGAP:.1f} s")
    return not runs

if __name__ == "__main__":
    sys.exit(0 if all([check(p) for p in sys.argv[1:]]) else 1)
