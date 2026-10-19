"""QA for the 16:9 split explainer: python3 split/qa_split.py [out/split/split_sample.mp4 | out/split9/split_sample.mp4 | out/coa/coa_full.mp4]
                                     [--no-speech]
(plan, timeline and qa folder are read from the video's folder; the script file from plan["scenes"]; the presenter box from
plan["presenter_box"] {x, y, w, h}: left of the panel (v3, box x 0) or right of it (v4, box x 1280))
- streams, size, fps, frame count = round(total*24), A/V durations
- integrated loudness and true peak (ebur128)
- black frames and frozen stretches (blackdetect / freezedetect on the presenter box, wherever it is)
- one screen: at every seam between the presenter box and the panel (x = box x and/or box x + w, inside the frame), the
  presenter-side strip (38 px next to the seam, under the feather) against the panel-side strip (58 px), rows 12..151 (above
  the head), 8 times over the panel's span plus the middle of every presenter segment (each clip is checked)
- every clip span re-transcribed OUT OF THE FINAL MIX (gpt-4o-transcribe) and compared with the script, token recall
  (--no-speech skips this API step, e.g. for a layout-only check)
- first / last frame and a frame at every panel build time → out/split/qa/*.png + contact sheet
Never prints API keys."""
import json, os, re, subprocess, sys, difflib, importlib.util
_spec = importlib.util.spec_from_file_location("words", "scripts/words.py"); W = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(W)
ARGS = [a for a in sys.argv[1:] if not a.startswith("--")]; NO_SPEECH = "--no-speech" in sys.argv[1:]
F = ARGS[0] if ARGS else "out/split/split_sample.mp4"
OD = os.path.dirname(F) or "."; Q = f"{OD}/qa"; os.makedirs(Q, exist_ok=True)
plan = json.load(open(f"{OD}/plan.json")); tl = json.load(open(f"{OD}/timeline.json"))
SC = {s["sceneId"]: s.get("spoken", s.get("dialogue")) for s in json.load(open(plan.get("scenes", "split/split_all_scenes.json")))["scenes"]}
PB = plan.get("presenter_box") or {}
BX, BY, BW, BH = int(PB.get("x", 0)), int(PB.get("y", 0)), int(PB.get("w", 1056)), int(PB.get("h", 1080))   # presenter box (v2 default: x 0, w 1056)
def sh(a): return subprocess.run(a, capture_output=True, text=True)
def sh_b(a): return subprocess.run(a, capture_output=True).stdout
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
fz = sh(["ffmpeg", "-nostats", "-i", F, "-vf", f"crop={BW}:{BH}:{BX}:{BY},freezedetect=n=0.002:d=1.2", "-an", "-f", "null", "-"]).stderr
freezes = re.findall(r"freeze_start: ([\d.]+)", fz); print(f"[qa] presenter-box freezes >1.2 s at: {freezes}")
flag(all(float(x) >= plan["total"] - 4.0 for x in freezes), "no frozen presenter before the end card")
# 3b one screen: the presenter backdrop must meet the panel cream without a step at every seam inside the frame (box x 0: seam at
#    x = w, presenter left of it; box at the right edge: seam at x = box x, presenter right of it)
SEAMS = [(x, side) for x, side in ((BX, "right"), (BX + BW, "left")) if 0 < x < int(v["width"])]   # side = where the presenter is
pan = next((c for c in tl["cues"] if c["type"] == "panel"), None)
if SEAMS and pan:
    import numpy as np
    # 8 times evenly over the panel's span (as before) + the middle of EVERY presenter segment inside it: 8 samples over a
    # 3.6-minute, 36-clip video checked at most 8 clips, so one unflattened clip usually slipped through
    lo_t, hi_t = pan["t0"] + 0.8, pan["t1"] - 0.8; tt_ = {round(pan["t0"] + 0.8 + k * (pan["t1"] - pan["t0"] - 1.6) / 7, 3): "" for k in range(8)}
    ts_ = plan["presenter_start"]
    for seg in plan["presenter"]:
        L_ = seg["out"] - seg["in"]; tm = ts_ + L_ / 2; ts_ += L_
        if lo_t <= tm <= hi_t: tt_[round(tm, 3)] = os.path.basename(seg["clip"])[:-4]
    for xs, side in SEAMS:
        worst, wat = 0, ""; x0 = max(0, xs - 80) & ~1; cw = min(int(v["width"]), xs + 80) - x0
        for tt, cid in sorted(tt_.items()):
            raw = sh_b(["ffmpeg", "-v", "error", "-ss", f"{tt:.3f}", "-i", F, "-frames:v", "1", "-vf", f"crop={cw}:140:{x0}:12", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"])
            if len(raw) < 140 * cw * 3: flag(False, f"seam x={xs}: no frame at {tt:.2f}s"); continue
            a8 = np.frombuffer(raw, np.uint8)[:140 * cw * 3].reshape(140, cw, 3).astype(float); s0 = xs - x0     # rows 12..151: above the head
            pstrip = a8[:, s0 - 40:s0 - 2] if side == "left" else a8[:, s0 + 2:s0 + 40]            # presenter side, under the feather
            qstrip = a8[:, s0 + 2:s0 + 60] if side == "left" else a8[:, s0 - 60:s0 - 2]            # panel side
            L = pstrip.reshape(-1, 3).mean(0); R = qstrip.reshape(-1, 3).mean(0); d = float(np.abs(L - R).max())
            if d > worst: worst, wat = d, f" at {tt:.2f}s" + (f" ({cid})" if cid else "")
            print(f"[qa] seam x={xs} {tt:6.2f}s{(' ' + cid) if cid else ''}  presenter side {tuple(int(round(v_)) for v_ in L)}  panel side {tuple(int(round(v_)) for v_ in R)}  max step {d:.1f}")
        flag(worst <= 3.0, f"one screen: no colour step at the seam x={xs} (presenter {side} of it; {len(tt_)} frames, every clip; worst {worst:.1f}{wat} <= 3)")
# 4 speech out of the final mix, per clip span
if NO_SPEECH: print("[qa] speech check skipped (--no-speech)")
KEY = None if NO_SPEECH else next(l.split("=", 1)[1].strip().strip('"') for l in open("/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/.env") if l.startswith("OPENAI_API_KEY="))
def norm(s): return re.sub(r"[^a-z0-9 ]", " ", s.lower().replace("versus", "v").replace(" vs ", " v ")).split()
t = plan["presenter_start"]
for seg in ([] if NO_SPEECH else plan["presenter"]):
    cid = os.path.basename(seg["clip"])[:-4]; L = seg["out"] - seg["in"]
    w = f"{Q}/{cid}.wav"; sh(["ffmpeg", "-v", "error", "-y", "-ss", f"{max(0, t - 0.25):.3f}", "-t", f"{L + 0.5:.3f}", "-i", F, "-vn", "-ac", "1", "-ar", "16000", w])
    # whisper-1, no prompt: gpt-4o-transcribe dropped second sentences of correct clips and once answered in Devanagari (course
    # series, 19-10-2026); spoken numbers are normalised on both sides (scripts/words.py numify: "one seventy three" == "173")
    def stt(path):
        r = sh(["curl", "-s", "https://api.openai.com/v1/audio/transcriptions", "-H", f"Authorization: Bearer {KEY}", "-F", "model=whisper-1", "-F", "language=en", "-F", f"file=@{path}"])
        try: return json.loads(r.stdout).get("text", "")
        except ValueError: return ""
    def recall(heard):
        want_t = W.numify(norm(SC[cid].replace("eighteen eighty-eight", "1888").replace("A B C", "ABC").replace("A P", "AP").replace("-", " ")))
        got = W.numify(norm(heard.replace("A.B.C.", "ABC").replace("A.P.", "AP").replace("A B C", "ABC").replace("A P ", "AP ").replace("-", " ")))
        want_t = list("".join(want_t)); got = list("".join(got))                      # compare characters: "B N S S" == "BNSS"
        sm = difflib.SequenceMatcher(a=want_t, b=got, autojunk=False); return sum(b.size for b in sm.get_matching_blocks()) / max(1, len(want_t))
    heard = stt(w); rec = recall(heard)
    if rec < 0.9:
        # both transcribers sometimes stop after the first sentence of a clip with a pause in it (Video 8 c22, 19-10: the final mix
        # had the whole line, the second half alone transcribed perfectly): transcribe the two halves split at the longest pause
        import wave, numpy as np
        wv = wave.open(w); sr = wv.getframerate(); a = np.frombuffer(wv.readframes(wv.getnframes()), np.int16).astype(float); wv.close()
        hop = sr // 20; e = np.array([np.sqrt((a[k:k + hop] ** 2).mean() + 1) for k in range(0, len(a) - hop, hop)])
        es = np.convolve(e, np.ones(5) / 5, mode="same")
        for frac in (0.35, 0.5, 0.65):                 # a split near a third, the middle or two thirds, at the quietest moment (+-0.6 s)
            c_ = int(len(e) * frac); lo, hi = max(1, c_ - 12), min(len(e) - 1, c_ + 12)
            cut = (lo + int(np.argmin(es[lo:hi]))) * hop
            halves = []
            for k, (s0, s1) in enumerate(((0, cut), (cut, len(a)))):
                hp = f"{Q}/{cid}_h{k}.wav"; hw = wave.open(hp, "wb"); hw.setnchannels(1); hw.setsampwidth(2); hw.setframerate(sr)
                hw.writeframes(a[s0:s1].astype(np.int16).tobytes()); hw.close(); halves.append(stt(hp))
            h2 = " ".join(halves); r2 = recall(h2)
            print(f"[qa] {cid} whole-clip recall {rec:.2f} -> split at {cut / sr:.2f}s {r2:.2f}  ({heard!r} -> {h2!r})")
            if r2 > rec: rec, heard = r2, h2
            if rec >= 0.9: break
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
