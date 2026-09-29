"""Three-pass compositor (same plan.json as compose.py):
  1. audio: voice (static gain) + music (normalised, ducked) -> final_audio.wav
  2. base video: lead + presenter clips (studio colour matched, graded) + full-frame 3D cut-aways + end clip (dissolve) -> base.mp4
  3. final: base.mp4 + overlay PNG sequence + final_audio.wav -> out (x264 medium crf 17, aac)
Usage: python3 compose2.py <plan.json> [--draft]"""
import sys, os, json, subprocess, re
plan = json.load(open(sys.argv[1])); draft = "--draft" in sys.argv
FPS = plan["fps"]; W, H = 1080, 1920
out = plan["out"]; work = os.path.join(os.path.dirname(out), "work"); os.makedirs(work, exist_ok=True)
def run(args, log):
    with open(log, "w") as lf: r = subprocess.run(args + ["-stats_period", "5"], stdout=lf, stderr=subprocess.STDOUT, text=True)
    if r.returncode != 0: raise SystemExit(f"[compose2] failed ({log}):\n" + open(log).read()[-2500:])
def dur(f): return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f],capture_output=True,text=True).stdout.strip())
def lufs(f):
    err = subprocess.run(["ffmpeg","-hide_banner","-nostats","-i",f,"-af","ebur128=peak=true","-f","null","-"],capture_output=True,text=True).stderr
    m = re.findall(r"I:\s+(-?[\d.]+) LUFS", err); return float(m[-1]) if m else -23.0
def corner_rgb(path, t=1.0):
    raw = subprocess.run(["ffmpeg","-v","error","-ss",str(t),"-i",path,"-frames:v","1","-vf","crop=120:160:16:16,scale=1:1","-f","rawvideo","-pix_fmt","rgb24","-"],capture_output=True).stdout
    return tuple(int(b) for b in raw[:3]) if len(raw) >= 3 else None
ps = plan["presenter_start"]; total = float(plan["total"]); pres = plan["presenter"]
ptrack_dur = sum(p["out"] - p["in"] for p in pres)
NORM = f"scale={W}:{H}:flags=lanczos,fps={FPS},format=yuv420p,setsar=1"
GRADE_P = plan.get("grade_presenter") or "eq=contrast=1.04:saturation=0.97,unsharp=5:5:0.3:5:5:0"; GRADE_3D = "eq=contrast=1.04:saturation=1.06,unsharp=5:5:0.25:5:5:0"

# ---- pass 1: audio ----
voice = os.path.join(work, "voice.wav"); final_audio = os.path.join(work, "final_audio.wav")
segs = []; vin = []
for k, p in enumerate(pres): vin += ["-i", p["clip"]]; segs.append(f"[{k}:a]atrim={p['in']}:{p['out']},asetpts=PTS-STARTPTS[a{k}]")
run(["ffmpeg","-hide_banner","-y"]+vin+["-filter_complex", ";".join(segs)+";"+"".join(f"[a{k}]" for k in range(len(segs)))+f"concat=n={len(segs)}:v=0:a=1[v]","-map","[v]","-ac","2","-ar","48000",voice], os.path.join(work,"p1a.log"))
vg = plan["voice_lufs"] - lufs(voice); m = plan["music"]; mg = m["target_lufs"] - lufs(m["file"])
print(f"[compose2] voice gain {vg:+.1f} dB, music gain {mg:+.1f} dB")
ag = (f"[0:a]volume={vg:.2f}dB,adelay={int(ps*1000)}|{int(ps*1000)},apad=whole_dur={total:.3f},asplit[vmain][vkey];"
      f"[1:a]atrim=0:{total:.3f},asetpts=PTS-STARTPTS,volume={mg:.2f}dB,afade=t=in:st=0:d={m['fade_in']},afade=t=out:st={total-m['fade_out']:.3f}:d={m['fade_out']}[mus];"
      "[mus][vkey]sidechaincompress=threshold=0.015:ratio=5:attack=60:release=700:makeup=1:level_sc=1[musd];"
      "[vmain][musd]amix=inputs=2:normalize=0:duration=first:dropout_transition=0,alimiter=limit=0.89:attack=5:release=80,aresample=48000[aout]")
sfx = plan.get("sfx", [])
if sfx:
    sin = []; sg = []
    for k, e in enumerate(sfx):
        sin += ["-i", e["file"]]; sg.append(f"[{k+2}:a]volume={e.get('gain_db', -8):.1f}dB,adelay={int(e['at']*1000)}|{int(e['at']*1000)},apad=whole_dur={total:.3f}[sx{k}]")
    ag = ag.replace("[vmain][musd]amix=inputs=2:normalize=0:duration=first:dropout_transition=0,", "".join(sg[:0]) + ";".join(sg) + ";" + "".join(f"[sx{k}]" for k in range(len(sfx))) + f"amix=inputs={len(sfx)}:normalize=0:duration=first:dropout_transition=0[sfxmix];[vmain][musd][sfxmix]amix=inputs=3:normalize=0:duration=first:dropout_transition=0,")
    run(["ffmpeg","-hide_banner","-y","-i",voice,"-i",m["file"]]+sin+["-filter_complex",ag,"-map","[aout]","-t",f"{total:.3f}","-c:a","pcm_s16le",final_audio], os.path.join(work,"p1b.log"))
else:
    run(["ffmpeg","-hide_banner","-y","-i",voice,"-i",m["file"],"-filter_complex",ag,"-map","[aout]","-t",f"{total:.3f}","-c:a","pcm_s16le",final_audio], os.path.join(work,"p1b.log"))
print(f"[compose2] audio mix {dur(final_audio):.2f}s")

# ---- pass 2: base video ----
gains = {}
if plan.get("match_bg", True) and len(pres) > 1:
    cols = {p["clip"]: corner_rgb(p["clip"], min(1.0, p["out"] - 0.2)) for p in pres}; ok = [v for v in cols.values() if v]
    if ok:
        target = tuple(sorted(v[ch] for v in ok)[len(ok)//2] for ch in range(3))
        for clip, v in cols.items():
            if v: gains[clip] = tuple(max(0.88, min(1.12, target[ch] / max(1, v[ch]))) for ch in range(3))
        print(f"[compose2] studio colour target {target}")
inputs = []; fc = []; idx = 0
def add(path, extra=None):
    global idx; inputs.extend((extra or []) + ["-i", path]); idx += 1; return idx - 1
pv = []
for k, p in enumerate(pres):
    i = add(p["clip"]); g = gains.get(p["clip"]); mix = f"colorchannelmixer=rr={g[0]:.4f}:gg={g[1]:.4f}:bb={g[2]:.4f}," if g else ""
    z = float(p.get("zoom", 1.0)); zf = f"crop=iw/{z:.4f}:ih/{z:.4f}:(iw-iw/{z:.4f})/2:(ih-ih/{z:.4f})*0.35," if z > 1.001 else ""
    push = float(p.get("push", 0.0))
    if push > 0:
        L = max(0.1, p["out"] - p["in"])
        zf = (f"scale=w='trunc(1080*(1+{push:.4f}*t/{L:.3f})/2)*2':h='trunc(1920*(1+{push:.4f}*t/{L:.3f})/2)*2':eval=frame:flags=bicubic,"
              f"crop=1080:1920:x='(iw-1080)/2':y='(ih-1920)*0.35',")
    fc.append(f"[{i}:v]trim={p['in']}:{p['out']},setpts=PTS-STARTPTS,scale=1080:1920:flags=lanczos,{zf}{NORM},{mix}{GRADE_P}[pv{k}]"); pv.append(f"[pv{k}]")
fc.append(f"color=c=black:s={W}x{H}:r={FPS}:d={ps:.3f},format=yuv420p[lead]")
fc.append("".join(pv)+f"concat=n={len(pv)}:v=1:a=0[ptrack]")
fc.append("[lead][ptrack]concat=n=2:v=1:a=0,settb=1/24,setpts=N/24/TB[base0]"); main = "[base0]"; main_dur = ps + ptrack_dur
ec = plan.get("endcard")
if ec:
    i = add(ec["clip"]); off = main_dur - ec["xfade"]
    fc.append(f"[{i}:v]trim={ec['offset']}:{ec['offset']+ec['dur']},setpts=PTS-STARTPTS,{NORM},{GRADE_3D},settb=1/24,setpts=N/24/TB[ev]")
    fc.append(f"{main}[ev]xfade=transition=fade:duration={ec['xfade']}:offset={off:.3f}[mx]"); main = "[mx]"; main_dur = off + ec["dur"]
tail = float(plan.get("tail_black") or 0)
if tail > 0:
    fc.append(f"color=c=0xf5f0e8:s={W}x{H}:r={FPS}:d={tail:.3f},format=yuv420p,settb=1/24[tl]"); fc.append(f"{main}[tl]concat=n=2:v=1:a=0[mt]"); main = "[mt]"; main_dur += tail
for n, c in enumerate(plan.get("cutaways", [])):
    i = add(c["clip"]); L = c["end"] - c["start"]; f = c.get("fade", 0.2)
    fc.append(f"[{i}:v]trim={c['offset']}:{c['offset']+L:.3f},setpts=PTS-STARTPTS,{NORM},{GRADE_3D},format=yuva420p,fade=t=in:st=0:d={f}:alpha=1,fade=t=out:st={L-f:.3f}:d={f}:alpha=1,setpts=PTS+{c['start']:.3f}/TB[cv{n}]")
    fc.append(f"{main}[cv{n}]overlay=0:0:eof_action=pass:enable='between(t,{c['start']:.3f},{c['end']:.3f})'[mc{n}]"); main = f"[mc{n}]"
fc.append(f"{main}format=yuv420p[vbase]")
base = os.path.join(work, "base.mp4")
run(["ffmpeg","-hide_banner","-y"]+inputs+["-filter_complex",";".join(fc),"-map","[vbase]","-an","-c:v","libx264","-preset","veryfast","-crf","12","-pix_fmt","yuv420p","-r",str(FPS),"-t",f"{total:.3f}",base], os.path.join(work,"p2.log"))
print(f"[compose2] base video {dur(base):.2f}s")

# ---- pass 3: overlays + audio ----
ov = plan["overlays"]; frames = os.path.join(ov["dir"], "f%05d.png")
# both inputs normalised to CFR before the overlay and again after it; without this the encoder drops frames and the picture drifts from the sound (measured: 64-114 dropped frames per 35 s)
g3 = (f"[0:v]fps={FPS}[b];[1:v]fps={FPS},format=rgba[o];"
      f"[b][o]overlay=0:0:eof_action=pass:format=auto,fps={FPS},fade=t=out:st={total-0.7:.3f}:d=0.7,format=yuv420p[vout]")
enc = ["-c:v","libx264","-preset","veryfast" if draft else "medium","-crf","22" if draft else "17","-pix_fmt","yuv420p","-r",str(FPS),"-c:a","aac","-b:a","192k","-ar","48000","-movflags","+faststart","-t",f"{total:.3f}"]
run(["ffmpeg","-hide_banner","-y","-i",base,"-framerate",str(ov["fps"]),"-i",frames,"-i",final_audio,"-filter_complex",g3,"-map","[vout]","-map","2:a"]+enc+[out], os.path.join(work,"p3.log"))
vd = subprocess.run(["ffprobe","-v","error","-select_streams","v","-show_entries","stream=duration,nb_frames","-of","csv=p=0",out],capture_output=True,text=True).stdout.strip()
print(f"[compose2] done: {out} {dur(out):.2f}s {os.path.getsize(out)/1e6:.1f} MB; video stream (duration,frames) = {vd}; base frames = {subprocess.run(['ffprobe','-v','error','-select_streams','v','-show_entries','stream=nb_frames','-of','csv=p=0',base],capture_output=True,text=True).stdout.strip()}")
