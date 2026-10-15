"""QA for the 16:9 split explainer: python3 split/qa_split.py [out/split/split_sample.mp4]
- streams, size, fps, frame count = round(total*24), A/V durations
- integrated loudness and true peak (ebur128)
- black frames and frozen stretches (blackdetect / freezedetect)
- every clip span re-transcribed OUT OF THE FINAL MIX (gpt-4o-transcribe) and compared with the script, token recall
- first / last frame and a frame at every panel build time → out/split/qa/*.png + contact sheet
Never prints API keys."""
import json, os, re, subprocess, sys, difflib
F = sys.argv[1] if len(sys.argv) > 1 else "out/split/split_sample.mp4"
Q = "out/split/qa"; os.makedirs(Q, exist_ok=True)
plan = json.load(open("out/split/plan.json")); tl = json.load(open("out/split/timeline.json"))
SC = {s["sceneId"]: s["spoken"] for s in json.load(open("split/split_all_scenes.json"))["scenes"]}
def sh(a): return subprocess.run(a, capture_output=True, text=True)
ok = True
def flag(cond, msg):
    global ok
    print(("  OK   " if cond else "  FAIL ") + msg); ok = ok and cond
# 1 streams
pr = json.loads(sh(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", F]).stdout)
v = [s for s in pr["streams"] if s["codec_type"] == "video"][0]; a = [s for s in pr["streams"] if s["codec_type"] == "audio"]
frames = int(sh(["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v:0", "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0", F]).stdout.strip())
total = plan["total"]; want = round(total * 24)
print(f"[qa] {F}: {v['width']}x{v['height']} {v['r_frame_rate']} frames {frames} (want {want}) dur {float(pr['format']['duration']):.3f}")
flag(v["width"] == 1920 and v["height"] == 1080, "1920x1080")
flag(v["r_frame_rate"] == "24/1", "24 fps")
flag(abs(frames - want) <= 1, f"frame count {frames} ≈ {want}")
flag(len(a) == 1 and a[0].get("sample_rate") == "48000", "one 48 kHz audio stream")
flag(abs(float(a[0]["duration"]) - float(v["duration"])) < 0.08, f"A/V duration match ({a[0]['duration']} vs {v['duration']})")
# 2 loudness
e = sh(["ffmpeg", "-nostats", "-i", F, "-af", "ebur128=peak=true", "-f", "null", "-"]).stderr
I = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", e)[-1]); TP = float(re.findall(r"Peak:\s+(-?[\d.]+) dBFS", e)[-1])
print(f"[qa] loudness {I} LUFS, true peak {TP} dBFS"); flag(-15.5 <= I <= -12.5, "loudness about -14 LUFS"); flag(TP <= -0.9, "true peak <= -1 dBTP")
# 3 black / freeze
bd = sh(["ffmpeg", "-nostats", "-i", F, "-vf", "blackdetect=d=0.12:pix_th=0.08", "-an", "-f", "null", "-"]).stderr
blacks = re.findall(r"black_start:([\d.]+) black_end:([\d.]+)", bd); print(f"[qa] black stretches: {blacks}"); flag(not blacks, "no black stretches")
fz = sh(["ffmpeg", "-nostats", "-i", F, "-vf", "crop=1056:1080:0:0,freezedetect=n=0.002:d=1.2", "-an", "-f", "null", "-"]).stderr
freezes = re.findall(r"freeze_start: ([\d.]+)", fz); print(f"[qa] presenter-box freezes >1.2 s at: {freezes}")
flag(all(float(x) >= plan["total"] - 4.0 for x in freezes), "no frozen presenter before the end card")
# 4 speech out of the final mix, per clip span
KEY = next(l.split("=", 1)[1].strip().strip('"') for l in open("/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/.env") if l.startswith("OPENAI_API_KEY="))
def norm(s): return re.sub(r"[^a-z0-9 ]", " ", s.lower().replace("versus", "v").replace(" vs ", " v ")).split()
t = plan["presenter_start"]
for seg in plan["presenter"]:
    cid = os.path.basename(seg["clip"])[:-4]; L = seg["out"] - seg["in"]
    w = f"{Q}/{cid}.wav"; sh(["ffmpeg", "-v", "error", "-y", "-ss", f"{max(0, t - 0.25):.3f}", "-t", f"{L + 0.5:.3f}", "-i", F, "-vn", "-ac", "1", "-ar", "16000", w])
    r = sh(["curl", "-s", "https://api.openai.com/v1/audio/transcriptions", "-H", f"Authorization: Bearer {KEY}", "-F", "model=gpt-4o-transcribe", "-F", "language=en", "-F", f"file=@{w}"])
    heard = json.loads(r.stdout).get("text", "")
    want_t = norm(SC[cid].replace("eighteen eighty-eight", "1888").replace("A B C", "ABC").replace("A P", "AP")); got = norm(heard.replace("A.B.C.", "ABC").replace("A.P.", "AP").replace("A B C", "ABC").replace("A P ", "AP "))
    sm = difflib.SequenceMatcher(a=want_t, b=got, autojunk=False); rec = sum(b.size for b in sm.get_matching_blocks()) / max(1, len(want_t))
    print(f"[qa] {cid} {t:6.2f}-{t + L:6.2f}  recall {rec:.2f}  heard: {heard}")
    flag(rec >= 0.9, f"{cid} spoken text intact in the final mix")
    t += L
# 5 frames: first, last, every build
times = {"first": 0.0, "last": max(0, frames / 24 - 0.05)}
for ci, c in enumerate(tl["cues"]):
    for k in ("at", "title_at", "sub_at", "head_at", "strike_at", "one_at", "many_at", "gather_at"):
        if isinstance(c.get(k), (int, float)): times[f"{c['type']}{ci}_{k}"] = c[k] + 0.6
    for it in c.get("items", []) + c.get("terms", []): times[f"{c['type']}_{str(it.get('n', it.get('text', '')))[:10]}"] = it["at"] + 0.6
for name, tt in sorted(times.items(), key=lambda x: x[1]):
    sh(["ffmpeg", "-v", "error", "-y", "-ss", f"{tt:.3f}", "-i", F, "-frames:v", "1", "-vf", "scale=640:-1", f"{Q}/{tt:07.3f}_{re.sub('[^A-Za-z0-9_]', '', name)}.png"])
pngs = sorted(x for x in os.listdir(Q) if x.endswith(".png") and not x.startswith("sheet"))
for i in range(0, len(pngs), 12):
    lst = f"{Q}/list.txt"; open(lst, "w").write("".join(f"file '{os.path.abspath(Q)}/{p}'\n" for p in pngs[i:i + 12]))
    sh(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-vf", "tile=3x4", "-frames:v", "1", f"{Q}/sheet_{i // 12}.png"])
print(f"[qa] {len(pngs)} frames → {Q}/sheet_*.png")
print("[qa] RESULT:", "PASS" if ok else "FAIL")
