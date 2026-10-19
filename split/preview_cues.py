"""One preview frame per content cue of a timeline (after its last build), tiled into contact sheets for a layout review.
Usage: python3 split/preview_cues.py <timeline.json> <outdir>"""
import json, os, subprocess, sys
tl = json.load(open(sys.argv[1])); out = sys.argv[2]; os.makedirs(out, exist_ok=True)
def builds(c):
    ts = [c.get("at"), c.get("head_at")]
    for key in ("items", "rows", "steps", "points", "nodes", "terms", "cols"):
        for it in c.get(key) or []: ts.append(it.get("at")); ts += list(it.get("cells_at") or []); ts.append(it.get("strike_at"))
    for key in ("left", "right", "verdict", "note", "merge", "fold"):
        v = c.get(key)
        if isinstance(v, dict): ts.append(v.get("at"))
    return [t for t in ts if isinstance(t, (int, float))]
times = []
for c in tl["cues"]:
    if c["type"] in ("panel", "sting", "endcard", "lower_third", "kicker", "cite"): continue
    b = builds(c); t = min(c["t1"] - 0.15, (max(b) if b else c["t0"]) + 0.9)
    times.append(round(t, 2))
times = sorted(set(times))
subprocess.run(["./node_modules/.bin/tsx", "scripts/render_overlays.ts", "--timeline", sys.argv[1], "--out", out, "--html", "overlays/split_panel.html",
                "--preview", ",".join(f"{t:.2f}" for t in times)], check=True, capture_output=True)
pngs = [os.path.join(out, f"preview_{t:.2f}.png") for t in times]
for k in range(0, len(pngs), 12):
    grp = pngs[k:k + 12]; args = []
    for p in grp: args += ["-i", p]
    n = len(grp); flt = "".join(f"color=c=0x6d7f8f:s=1920x1080[b{i}];[b{i}][{i}:v]overlay,crop=1280:1080:0:0,scale=640:-1,drawtext=text='{os.path.basename(grp[i])[8:-4]}':x=10:y=10:fontsize=28:fontcolor=red[v{i}];" for i in range(n))
    while n < 12: flt += f"color=c=black:s=640x540:d=1[v{n}];"; n += 1
    flt += "".join(f"[v{i}]" for i in range(12)) + "xstack=inputs=12:layout=0_0|w0_0|w0+w1_0|0_h0|w0_h0|w0+w1_h0|0_h0+h3|w0_h0+h3|w0+w1_h0+h3|0_h0+h3+h6|w0_h0+h3+h6|w0+w1_h0+h3+h6[o]"
    subprocess.run(["ffmpeg", "-v", "error", "-y", *args, "-filter_complex", flt, "-map", "[o]", "-frames:v", "1", os.path.join(out, f"sheet_{k // 12 + 1}.jpg")], check=True)
print(f"[preview] {len(times)} frames, sheets in {out}")
