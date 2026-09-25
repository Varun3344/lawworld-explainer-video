"""Assemble the final 1080x1920 video from plan.json: sting lead, presenter clips (dead air trimmed, corner mark
removed, graded), full-frame 3D cut-aways, end card with a dissolve, overlay PNG sequence, ducked music, loudness.
Usage: python3 compose.py <plan.json> [--draft]"""
import sys, os, json, subprocess, math, tempfile, re

plan = json.load(open(sys.argv[1])); draft = "--draft" in sys.argv
FPS = plan["fps"]; W, H = 1080, 1920
def sh(args, capture=False):
    r = subprocess.run(args, capture_output=True, text=True)
    if r.returncode != 0: raise SystemExit(f"command failed:\n{' '.join(args)[:600]}\n{r.stderr[-3000:]}")
    return r.stderr if capture else None
def dur(f): return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f],capture_output=True,text=True).stdout.strip())
def lufs(f, af=""):
    err = subprocess.run(["ffmpeg","-hide_banner","-nostats","-i",f]+(["-af",af] if af else [])+["-filter:a" if False else "-af", (af+"," if af else "")+"ebur128=peak=true","-f","null","-"],capture_output=True,text=True).stderr
    m = re.findall(r"I:\s+(-?[\d.]+) LUFS", err); return float(m[-1]) if m else -23.0

d = plan.get("delogo"); DELOGO = (f"delogo=x={d['x']}:y={d['y']}:w={d['w']}:h={d['h']}" if d else "null")
GRADE_P = "eq=contrast=1.04:brightness=0.0:saturation=0.97,unsharp=5:5:0.3:5:5:0"
GRADE_3D = "eq=contrast=1.04:saturation=1.06,unsharp=5:5:0.25:5:5:0"
NORM = f"scale={W}:{H}:flags=lanczos,fps={FPS},format=yuv420p,setsar=1"

ps = plan["presenter_start"]
inputs = []; fc = []; idx = 0
def add_input(path, extra=None):
    global idx
    inputs.extend((extra or []) + ["-i", path]); idx += 1; return idx - 1

# --- voice pre-pass: concat the trimmed presenter audio, measure loudness, derive a static gain (no pumping) ---
tmp = tempfile.mkdtemp(); voice_wav = os.path.join(tmp, "voice.wav")
segs = []; vin = []
for k, p in enumerate(plan["presenter"]):
    vin += ["-i", p["clip"]]; segs.append(f"[{k}:a]atrim={p['in']}:{p['out']},asetpts=PTS-STARTPTS[a{k}]")
sh(["ffmpeg","-v","error","-y"]+vin+["-filter_complex", ";".join(segs)+";"+"".join(f"[a{k}]" for k in range(len(segs)))+f"concat=n={len(segs)}:v=0:a=1[v]", "-map","[v]","-ac","2","-ar","48000",voice_wav])
voice_gain = plan["voice_lufs"] - lufs(voice_wav)
music_gain = plan["music"]["target_lufs"] - lufs(plan["music"]["file"])
print(f"[compose] voice gain {voice_gain:+.1f} dB, music gain {music_gain:+.1f} dB")

# --- presenter video track (studio colour matched across takes) ---
def corner_rgb(path, t=1.0):
    raw = subprocess.run(["ffmpeg","-v","error","-ss",str(t),"-i",path,"-frames:v","1","-vf","crop=120:160:16:16,scale=1:1","-f","rawvideo","-pix_fmt","rgb24","-"],capture_output=True).stdout
    return tuple(int(b) for b in raw[:3]) if len(raw) >= 3 else None
gains = {}
if plan.get("match_bg", True) and len(plan["presenter"]) > 1:
    cols = {p["clip"]: corner_rgb(p["clip"], min(1.0, p["out"] - 0.2)) for p in plan["presenter"]}
    ok = [v for v in cols.values() if v]
    if ok:
        target = tuple(sorted(v[ch] for v in ok)[len(ok)//2] for ch in range(3))
        for clip, v in cols.items():
            if v: gains[clip] = tuple(max(0.88, min(1.12, target[ch] / max(1, v[ch]))) for ch in range(3))
        print(f"[compose] studio colour target {target}; per-clip gains " + ", ".join(f"{os.path.basename(c)}:{tuple(round(x,3) for x in g)}" for c, g in gains.items()))
pv = []
for k, p in enumerate(plan["presenter"]):
    i = add_input(p["clip"]); g = gains.get(p["clip"])
    mix = f"colorchannelmixer=rr={g[0]:.4f}:gg={g[1]:.4f}:bb={g[2]:.4f}," if g else ""
    fc.append(f"[{i}:v]trim={p['in']}:{p['out']},setpts=PTS-STARTPTS,{DELOGO},{NORM},{mix}{GRADE_P}[pv{k}]")
    pv.append(f"[pv{k}]")
fc.append("".join(pv)+f"concat=n={len(pv)}:v=1:a=0[ptrack]")
ptrack_dur = sum(p["out"]-p["in"] for p in plan["presenter"])
fc.append(f"color=c=black:s={W}x{H}:r={FPS}:d={ps:.3f},format=yuv420p[lead]")
tail = float(plan.get("tail_black") or 0)
if tail > 0:
    fc.append(f"color=c=0xf5f0e8:s={W}x{H}:r={FPS}:d={tail:.3f},format=yuv420p[tailv]")
    fc.append("[lead][ptrack][tailv]concat=n=3:v=1:a=0,settb=1/24,setpts=N/24/TB[base]")
else:
    fc.append("[lead][ptrack]concat=n=2:v=1:a=0,settb=1/24,setpts=N/24/TB[base]")
main = "[base]"; main_dur = ps + ptrack_dur + tail

# --- end card clip with a dissolve ---
ec = plan.get("endcard")
if ec:
    i = add_input(ec["clip"])
    fc.append(f"[{i}:v]trim={ec['offset']}:{ec['offset']+ec['dur']},setpts=PTS-STARTPTS,{DELOGO},{NORM},{GRADE_3D},settb=1/24,setpts=N/24/TB[ev]")
    off = main_dur - ec["xfade"]
    fc.append(f"{main}[ev]xfade=transition=fade:duration={ec['xfade']}:offset={off:.3f}[mx]")
    main = "[mx]"; main_dur = off + ec["dur"]
total = plan.get("total") or main_dur

# --- full-frame 3D cut-aways over the presenter, with soft alpha edges ---
for n, c in enumerate(plan.get("cutaways", [])):
    i = add_input(c["clip"]); L = c["end"] - c["start"]; f = c.get("fade", 0.2)
    fc.append(f"[{i}:v]trim={c['offset']}:{c['offset']+L:.3f},setpts=PTS-STARTPTS,{DELOGO},{NORM},{GRADE_3D},format=yuva420p,"
              f"fade=t=in:st=0:d={f}:alpha=1,fade=t=out:st={L-f:.3f}:d={f}:alpha=1,setpts=PTS+{c['start']:.3f}/TB[cv{n}]")
    fc.append(f"{main}[cv{n}]overlay=0:0:eof_action=pass:enable='between(t,{c['start']:.3f},{c['end']:.3f})'[mc{n}]"); main = f"[mc{n}]"

# --- overlay PNG sequence ---
ov = plan["overlays"]; frames = os.path.join(ov["dir"], "f%05d.png")
if os.path.exists(os.path.join(ov["dir"], "f00000.png")):
    i = add_input(frames, ["-framerate", str(ov["fps"])])
    fc.append(f"[{i}:v]format=rgba[ovl]"); fc.append(f"{main}[ovl]overlay=0:0:eof_action=pass:format=auto[mo]"); main = "[mo]"
else: print("[compose] WARNING: no overlay frames found, composing without overlays")
fc.append(f"{main}fade=t=out:st={total-0.7:.3f}:d=0.7,format=yuv420p[vout]")

# --- audio: voice (static gain) + music (normalised, ducked under speech) ---
vi = add_input(voice_wav); mi = add_input(plan["music"]["file"])
m = plan["music"]
fc.append(f"[{vi}:a]volume={voice_gain:.2f}dB,adelay={int(ps*1000)}|{int(ps*1000)},apad=whole_dur={total:.3f},asplit[vmain][vkey]")
fc.append(f"[{mi}:a]atrim=0:{total:.3f},asetpts=PTS-STARTPTS,volume={music_gain:.2f}dB,afade=t=in:st=0:d={m['fade_in']},afade=t=out:st={total-m['fade_out']:.3f}:d={m['fade_out']}[mus]")
if m.get("duck", True):
    fc.append("[mus][vkey]sidechaincompress=threshold=0.015:ratio=5:attack=60:release=700:makeup=1:level_sc=1[musd]")
else: fc.append("[vkey]anullsink;[mus]acopy[musd]")
fc.append("[vmain][musd]amix=inputs=2:normalize=0:duration=first:dropout_transition=0,alimiter=limit=0.89:attack=5:release=80,aresample=48000[aout]")

out = plan["out"]; os.makedirs(os.path.dirname(out), exist_ok=True)
enc = ["-c:v","libx264","-preset","veryfast" if draft else "medium","-crf","22" if draft else "17","-pix_fmt","yuv420p","-r",str(FPS),
       "-c:a","aac","-b:a","192k","-ar","48000","-movflags","+faststart","-t",f"{total:.3f}"]
cmd = ["ffmpeg","-hide_banner","-y"]+inputs+["-filter_complex",";".join(fc),"-map","[vout]","-map","[aout]"]+enc+[out]
open(os.path.join(os.path.dirname(out), "ffmpeg_cmd.txt"), "w").write(" ".join(cmd))
print(f"[compose] rendering {total:.2f}s -> {out}")
logf = os.path.join(os.path.dirname(out), "ffmpeg.log")
with open(logf, "w") as lf: r = subprocess.run(cmd + ["-stats_period", "5"], stdout=lf, stderr=subprocess.STDOUT, text=True)
if r.returncode != 0: raise SystemExit("[compose] ffmpeg failed, see " + logf + "\n" + open(logf).read()[-3000:])
print(f"[compose] done: {dur(out):.2f}s, {os.path.getsize(out)/1e6:.1f} MB")
