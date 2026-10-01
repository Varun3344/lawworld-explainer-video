"""Delivery checks for the Kannada office video: streams, loudness, per-clip speech in the FINAL mix, frame sheets."""
import os, sys, json, subprocess, re, tempfile, importlib.util
os.chdir("/Users/admin/Downloads/New short/product-explainer")
spec = importlib.util.spec_from_file_location("kw", "kn_office/kn_words.py"); kw = importlib.util.module_from_spec(spec); spec.loader.exec_module(kw)
V = sys.argv[1] if len(sys.argv) > 1 else "out/office_kg/office_kg.mp4"
plan = json.load(open("out/office_kg/plan.json")); tl = json.load(open("out/office_kg/timeline.json"))
scenes = {s["sceneId"]: s["dialogue"] for s in json.load(open("kanglish/kg_all_scenes.json"))["scenes"]}
pr = lambda *a: subprocess.run(a, capture_output=True, text=True)
v = pr("ffprobe","-v","error","-select_streams","v","-show_entries","stream=width,height,nb_frames,duration","-of","csv=p=0",V).stdout.strip()
a = pr("ffprobe","-v","error","-select_streams","a","-show_entries","stream=duration","-of","csv=p=0",V).stdout.strip()
print("video:", v, "| audio:", a, "| expected frames:", round(plan["total"]*24))
e = pr("ffmpeg","-hide_banner","-nostats","-i",V,"-af","ebur128=peak=true","-f","null","-").stderr
print("loudness:", re.findall(r"I:\s+(-?[\d.]+) LUFS", e)[-1], "LUFS | true peak:", re.findall(r"Peak:\s+(-?[\d.]+) dBFS", e)[-1], "dBFS")
base = plan["presenter_start"]; worst = 1.0
for i, s in enumerate(plan["presenter"]):
    sid = os.path.basename(s["clip"]).split(".")[0]; L = s["out"] - s["in"]; tmp = tempfile.mkdtemp(); mp4 = os.path.join(tmp, sid + ".mp4")
    # 0.45 s of lead-in and tail: whisper drops the first word of a segment that starts exactly on speech
    subprocess.run(["ffmpeg","-v","error","-y","-ss",f"{max(0, base-0.45):.3f}","-t",f"{L+0.9:.3f}","-i",V,"-vn","-c:a","aac",mp4], check=True)
    d = kw.transcribe(mp4); heard = d.get("text", ""); toks = kw.want_tokens(scenes[sid], bool(re.search(r"\d", heard)))
    r = kw.recall("".join(kw.skel(t) for t in toks), "".join(kw.skel(x) for x in heard.split())); worst = min(worst, r)
    print(f"  {sid} at {base:6.2f}s recall in final mix {r:.2f}{'   <-- LOW' if r < 0.55 else ''}")
    base += L
print("lowest recall in the final mix:", round(worst, 2))
S = "/tmp/knfinal"; os.makedirs(S, exist_ok=True)
c = {}
for x in tl["cues"]: c.setdefault(x["type"], []).append(x)
pts = [0.9, c["lower_third"][0]["t0"]+1.2, c["slam"][0]["words"][2]["at"]+0.4, c["stat"][0]["t0"]+1.5, c["orbit"][0]["t0"]+1.8] + [(k["start"]+k["end"])/2 for k in plan["cutaways"]] \
      + [c["phone"][0]["t1"]-0.5, c["chips"][0]["t1"]-0.4, c["pricing"][0]["t0"]+5, c["pricing"][0]["t1"]-0.8, tl["duration"]-0.4, 0.0]
for i, t in enumerate(pts): subprocess.run(["ffmpeg","-v","error","-y","-i",V,"-ss",f"{t:.2f}","-frames:v","1","-vf","scale=144:256",f"{S}/p{i:02d}.png"], check=True)
n = len(pts); per = 8
for r in range((n + per - 1) // per):
    fs = [f"{S}/p{i:02d}.png" for i in range(r*per, min(n, (r+1)*per))]
    subprocess.run(["ffmpeg","-v","error","-y"] + sum([["-i", f] for f in fs], []) + ["-filter_complex", f"hstack=inputs={len(fs)}" if len(fs) > 1 else "null", f"{S}/row{r}.png"], check=True)
print("frame rows:", (n + per - 1) // per, "in", S)
