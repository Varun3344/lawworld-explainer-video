"""Three-pass compositor (same plan.json as compose.py):
  1. audio: voice (static gain) + music (normalised, ducked) -> final_audio.wav
  2. base video: lead + presenter clips (studio colour matched, graded) + full-frame 3D cut-aways + end clip (dissolve) -> base.mp4
  3. final: base.mp4 + overlay PNG sequence + final_audio.wav -> out (x264 medium crf 17, aac)
Usage: python3 compose2.py <plan.json> [--draft] [--print-cmds]
  --print-cmds  print every ffmpeg command (one line each, on stdout) instead of running it; status lines go to stderr and
                nothing is written. Input measurements (music loudness, studio colours, voice levelling, clip sizes) still run,
                read-only. The voice gain needs pass 1a's output: it is measured on work/voice.wav from an earlier run when
                that file exists, otherwise -23 LUFS is assumed (lufs() fallback).
Layout keys (optional; a plan without them gives the original 1080x1920 commands byte for byte):
  size: [W, H]  canvas, default [1080, 1920]. Lead, cut-aways, end card and tail use it, and clips COVER it (scale keeping
                aspect, centre crop) instead of being stretched. size without presenter_box = presenter box on the whole canvas.
  presenter_box: {x, y, w, h, fx, fy, pad}  each presenter segment COVERS a w x h box (scale up keeping aspect, lanczos) and
                is cropped around the source focal point (fx, fy), 0..1 of the scaled source: across, the box is centred on fx
                (clamped to the frame edges); down, the fy line keeps its relative height (0.35 = eye line stays at 35 %).
                Colour match and grade as before, then the box is padded to W x H at (x, y) with pad ("0xRRGGBB").
                Defaults: x 0, y 0, w W, h H, fx 0.5, fy 0.35, pad "0xf5f0e8" (brand cream). x, y, w, h must be even.
  per presenter segment in box mode: "fx" / "fy" override the focal point, "box": {...} overrides box keys for that segment
                (e.g. a full-frame hook), "zoom" z punches in about the focal point (crop w/z x h/z, scale back to w x h),
                "push" p is a slow zoom from z to z*(1+p) over the segment (per-frame scale + crop, like the 9:16 push)."""
import sys, os, json, subprocess, re, shlex
plan = json.load(open(sys.argv[1])); draft = "--draft" in sys.argv; dry = "--print-cmds" in sys.argv
FPS = plan["fps"]; W, H = (int(v) for v in plan.get("size", (1080, 1920)))
out = plan["out"]; work = os.path.join(os.path.dirname(out), "work")
if not dry: os.makedirs(work, exist_ok=True)
def say(*a): print(*a, file=sys.stderr if dry else sys.stdout)
def run(args, log):
    if dry: print(shlex.join(args + ["-stats_period", "5"])); return
    with open(log, "w") as lf: r = subprocess.run(args + ["-stats_period", "5"], stdout=lf, stderr=subprocess.STDOUT, text=True)
    if r.returncode != 0: raise SystemExit(f"[compose2] failed ({log}):\n" + open(log).read()[-2500:])
def dur(f): return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f],capture_output=True,text=True).stdout.strip())
def lufs(f):
    err = subprocess.run(["ffmpeg","-hide_banner","-nostats","-i",f,"-af","ebur128=peak=true","-f","null","-"],capture_output=True,text=True).stderr
    m = re.findall(r"I:\s+(-?[\d.]+) LUFS", err); return float(m[-1]) if m else -23.0
def corner_rgb(path, t=1.0):
    raw = subprocess.run(["ffmpeg","-v","error","-ss",str(t),"-i",path,"-frames:v","1","-vf","crop=120:160:16:16,scale=1:1","-f","rawvideo","-pix_fmt","rgb24","-"],capture_output=True).stdout
    return tuple(int(b) for b in raw[:3]) if len(raw) >= 3 else None
def probe_wh(path):
    o = subprocess.run(["ffprobe","-v","error","-select_streams","v:0","-show_entries","stream=width,height","-of","csv=p=0",path],capture_output=True,text=True).stdout.strip().split("\n")[0].split(",")
    try: return int(o[0]), int(o[1])
    except (ValueError, IndexError): raise SystemExit(f"[compose2] cannot read the frame size of {path}")
ps = plan["presenter_start"]; total = float(plan["total"]); pres = plan["presenter"]
ptrack_dur = sum(p["out"] - p["in"] for p in pres)
NORM = f"scale={W}:{H}:flags=lanczos,fps={FPS},format=yuv420p,setsar=1"
SIZED = "size" in plan; BOXED = SIZED or "presenter_box" in plan
if SIZED: NORM = f"scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos,crop={W}:{H},fps={FPS},format=yuv420p,setsar=1"
GRADE_P = plan.get("grade_presenter") or "eq=contrast=1.04:saturation=0.97,unsharp=5:5:0.3:5:5:0"; GRADE_3D = "eq=contrast=1.04:saturation=1.06,unsharp=5:5:0.25:5:5:0"
if BOXED:
    if W % 2 or H % 2: raise SystemExit(f"[compose2] size {W}x{H} must be even")
    f0 = [f for f in (os.path.join(plan["overlays"]["dir"], f"f{n:05d}.png") for n in (0, 1)) if os.path.exists(f)]
    if not f0: say(f"[compose2] warning: no overlay frames in {plan['overlays']['dir']} yet")
    elif (osz := probe_wh(f0[0])) != (W, H):
        msg = f"[compose2] overlay frames are {osz[0]}x{osz[1]} but the canvas is {W}x{H}"
        if not dry: raise SystemExit(msg)
        say("warning: " + msg)

# ---- pass 1: audio ----
voice = os.path.join(work, "voice.wav"); final_audio = os.path.join(work, "final_audio.wav")
segs = []; vin = []
def mean_db(clip, a, b):
    o = subprocess.run(["ffmpeg","-hide_banner","-nostats","-ss",f"{a:.3f}","-t",f"{b-a:.3f}","-i",clip,"-vn","-af","volumedetect","-f","null","-"],capture_output=True,text=True).stderr
    m = re.search(r"mean_volume: (-?[\d.]+) dB", o); return float(m.group(1)) if m else None
lv = {}
if plan.get("level_voice"):
    ms = [mean_db(p["clip"], p["in"], p["out"]) for p in pres]; okm = sorted(x for x in ms if x is not None)
    if okm:
        med = okm[len(okm)//2]; lv = {k: max(-6.0, min(6.0, med - x)) for k, x in enumerate(ms) if x is not None}
        say("[compose2] per-clip voice levelling (dB): " + " ".join(f"{v:+.1f}" for v in lv.values()))
for k, p in enumerate(pres):
    L = p["out"] - p["in"]; vin += ["-i", p["clip"]]
    # 20-30 ms fades at every cut: no clicks where two takes meet
    segs.append(f"[{k}:a]atrim={p['in']}:{p['out']},asetpts=PTS-STARTPTS,volume={lv.get(k, 0.0):.2f}dB,afade=t=in:st=0:d=0.02,afade=t=out:st={max(0, L-0.03):.3f}:d=0.03[a{k}]")
run(["ffmpeg","-hide_banner","-y"]+vin+["-filter_complex", ";".join(segs)+";"+"".join(f"[a{k}]" for k in range(len(segs)))+f"concat=n={len(segs)}:v=0:a=1[v]","-map","[v]","-ac","2","-ar","48000",voice], os.path.join(work,"p1a.log"))
if dry: say("[compose2] dry run: voice loudness " + (f"measured on the existing {voice}" if os.path.exists(voice) else "not measured (pass 1a not run), -23.0 LUFS assumed"))
vg = plan["voice_lufs"] - lufs(voice); m = plan["music"]; mg = m["target_lufs"] - lufs(m["file"])
say(f"[compose2] voice gain {vg:+.1f} dB, music gain {mg:+.1f} dB")
ag = (f"[0:a]volume={vg:.2f}dB,adelay={int(ps*1000)}|{int(ps*1000)},apad=whole_dur={total:.3f},asplit[vmain][vkey];"
      f"[1:a]atrim=0:{total:.3f},asetpts=PTS-STARTPTS,volume={mg:.2f}dB,afade=t=in:st=0:d={m['fade_in']},afade=t=out:st={total-m['fade_out']:.3f}:d={m['fade_out']}[mus];"
      "[mus][vkey]sidechaincompress=threshold=0.015:ratio=5:attack=60:release=700:makeup=1:level_sc=1[musd];"
      "[vmain][musd]amix=inputs=2:normalize=0:duration=first:dropout_transition=0,alimiter=limit=" + str(plan.get('limit', 0.89)) + (":level=0" if "limit" in plan else "") + ":attack=5:release=80,aresample=48000[aout]")
sfx = plan.get("sfx", [])
if sfx:
    sin = []; sg = []
    for k, e in enumerate(sfx):
        sin += ["-i", e["file"]]; sg.append(f"[{k+2}:a]volume={e.get('gain_db', -8):.1f}dB,adelay={int(e['at']*1000)}|{int(e['at']*1000)},apad=whole_dur={total:.3f}[sx{k}]")
    ag = ag.replace("[vmain][musd]amix=inputs=2:normalize=0:duration=first:dropout_transition=0,", "".join(sg[:0]) + ";".join(sg) + ";" + "".join(f"[sx{k}]" for k in range(len(sfx))) + f"amix=inputs={len(sfx)}:normalize=0:duration=first:dropout_transition=0[sfxmix];[vmain][musd][sfxmix]amix=inputs=3:normalize=0:duration=first:dropout_transition=0,")
    run(["ffmpeg","-hide_banner","-y","-i",voice,"-i",m["file"]]+sin+["-filter_complex",ag,"-map","[aout]","-t",f"{total:.3f}","-c:a","pcm_s16le",final_audio], os.path.join(work,"p1b.log"))
else:
    run(["ffmpeg","-hide_banner","-y","-i",voice,"-i",m["file"],"-filter_complex",ag,"-map","[aout]","-t",f"{total:.3f}","-c:a","pcm_s16le",final_audio], os.path.join(work,"p1b.log"))
if not dry: say(f"[compose2] audio mix {dur(final_audio):.2f}s")

# ---- pass 2: base video ----
gains = {}
if plan.get("match_bg", True) and len(pres) > 1:
    cols = {p["clip"]: corner_rgb(p["clip"], min(1.0, p["out"] - 0.2)) for p in pres}; ok = [v for v in cols.values() if v]
    if ok:
        target = tuple(sorted(v[ch] for v in ok)[len(ok)//2] for ch in range(3))
        for clip, v in cols.items():
            if v: gains[clip] = tuple(max(0.88, min(1.12, target[ch] / max(1, v[ch]))) for ch in range(3))
        say(f"[compose2] studio colour target {target}")
inputs = []; fc = []; idx = 0
def add(path, extra=None):
    global idx; inputs.extend((extra or []) + ["-i", path]); idx += 1; return idx - 1
BOX = {"x": 0, "y": 0, "w": W, "h": H, "fx": 0.5, "fy": 0.35, "pad": "0xf5f0e8", **(plan.get("presenter_box") or {})}
def box_chain(p):
    """box mode: filters that fit one presenter segment into its box (cover scale, focal crop, zoom or push) + the pad filter"""
    b = {**BOX, **(p.get("box") or {})}; bx, by, bw, bh = (int(b[c]) for c in "xywh")
    fx = float(p.get("fx", b["fx"])); fy = float(p.get("fy", b["fy"])); z = float(p.get("zoom", 1.0)); push = float(p.get("push", 0.0))
    if (bx | by | bw | bh) % 2 or bw < 2 or bh < 2 or bx < 0 or by < 0 or bx + bw > W or by + bh > H or not (0 <= fx <= 1 and 0 <= fy <= 1):
        raise SystemExit(f"[compose2] bad presenter box {b} (fx {fx}, fy {fy}) for {p['clip']}: x, y, w, h even and inside {W}x{H}; fx, fy in 0..1")
    iw, ih = probe_wh(p["clip"])
    sw, sh = max(bw, int(bh * iw / ih + 0.5)), max(bh, int(bw * ih / iw + 0.5))   # size after scale=bw:bh:force_original_aspect_ratio=increase
    x0 = min(max(fx * sw - bw / 2, 0), sw - bw); rx = (fx * sw - x0) / bw          # focal point inside the box: rx across, fy down
    f = (f"scale={bw}:{bh}:force_original_aspect_ratio=increase:flags=lanczos,"
         f"crop={bw}:{bh}:x='clip({fx:.4f}*iw-{bw // 2},0,iw-{bw})':y='(ih-{bh})*{fy:.4f}',")
    if push > 0:   # slow zoom about the focal point, z -> z*(1+push) over the segment
        # crop's iw/ih keep the FIRST frame's size when scale resizes per frame (ffmpeg 9: measured top-left pivot), so x/y recompute the size from t
        L = max(0.1, p["out"] - p["in"]); k = (f"{z:.4f}*" if z > 1.001 else "") + f"(1+{push:.4f}*t/{L:.3f})"
        zw, zh = f"trunc({bw}*{k}/2)*2", f"trunc({bh}*{k}/2)*2"
        f += (f"scale=w='{zw}':h='{zh}':eval=frame:flags=bicubic,"
              f"crop={bw}:{bh}:x='({zw}-{bw})*{rx:.4f}':y='({zh}-{bh})*{fy:.4f}',")
    elif z > 1.001:   # punch-in about the focal point
        f += f"crop=iw/{z:.4f}:ih/{z:.4f}:(iw-iw/{z:.4f})*{rx:.4f}:(ih-ih/{z:.4f})*{fy:.4f},scale={bw}:{bh}:flags=lanczos,"
    pad = f",pad={W}:{H}:{bx}:{by}:color={b['pad']}" if (bx, by, bw, bh) != (0, 0, W, H) else ""
    say(f"[compose2] box {os.path.basename(p['clip'])}: {iw}x{ih} covers {sw}x{sh}, {bw}x{bh} at {bx},{by}; focal {fx:.3f},{fy:.3f} -> {rx:.3f},{fy:.3f} of the box; zoom {z:g} push {push:g}")
    return f, pad
pv = []
for k, p in enumerate(pres):
    i = add(p["clip"]); g = gains.get(p["clip"]); mix = f"colorchannelmixer=rr={g[0]:.4f}:gg={g[1]:.4f}:bb={g[2]:.4f}," if g else ""
    if BOXED:
        geo, pad = box_chain(p)
        fc.append(f"[{i}:v]trim={p['in']}:{p['out']},setpts=PTS-STARTPTS,{geo}fps={FPS},format=yuv420p,setsar=1,{mix}{GRADE_P}{pad}[pv{k}]"); pv.append(f"[pv{k}]")
        continue
    z = float(p.get("zoom", 1.0)); zf = f"crop=iw/{z:.4f}:ih/{z:.4f}:(iw-iw/{z:.4f})/2:(ih-ih/{z:.4f})*0.35," if z > 1.001 else ""
    push = float(p.get("push", 0.0))
    if push > 0:
        L = max(0.1, p["out"] - p["in"])
        zf = (f"scale=w='trunc({W}*(1+{push:.4f}*t/{L:.3f})/2)*2':h='trunc({H}*(1+{push:.4f}*t/{L:.3f})/2)*2':eval=frame:flags=bicubic,"
              f"crop={W}:{H}:x='(iw-{W})/2':y='(ih-{H})*0.35',")
    fc.append(f"[{i}:v]trim={p['in']}:{p['out']},setpts=PTS-STARTPTS,scale={W}:{H}:flags=lanczos,{zf}{NORM},{mix}{GRADE_P}[pv{k}]"); pv.append(f"[pv{k}]")
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
if not dry: say(f"[compose2] base video {dur(base):.2f}s")

# ---- pass 3: overlays + audio ----
ov = plan["overlays"]; frames = os.path.join(ov["dir"], "f%05d.png")
# both inputs normalised to CFR before the overlay and again after it; without this the encoder drops frames and the picture drifts from the sound (measured: 64-114 dropped frames per 35 s)
g3 = (f"[0:v]fps={FPS}[b];[1:v]fps={FPS},format=rgba[o];"
      f"[b][o]overlay=0:0:eof_action=pass:format=auto,fps={FPS},fade=t=out:st={total-0.7:.3f}:d=0.7,format=yuv420p[vout]")
enc = ["-c:v","libx264","-preset","veryfast" if draft else "medium","-crf","22" if draft else "17","-pix_fmt","yuv420p","-r",str(FPS),"-c:a","aac","-b:a","192k","-ar","48000","-movflags","+faststart","-t",f"{total:.3f}"]
run(["ffmpeg","-hide_banner","-y","-i",base,"-framerate",str(ov["fps"]),"-i",frames,"-i",final_audio,"-filter_complex",g3,"-map","[vout]","-map","2:a"]+enc+[out], os.path.join(work,"p3.log"))
if dry: say("[compose2] dry run: commands printed, nothing run or written"); sys.exit(0)
vd = subprocess.run(["ffprobe","-v","error","-select_streams","v","-show_entries","stream=duration,nb_frames","-of","csv=p=0",out],capture_output=True,text=True).stdout.strip()
print(f"[compose2] done: {out} {dur(out):.2f}s {os.path.getsize(out)/1e6:.1f} MB; video stream (duration,frames) = {vd}; base frames = {subprocess.run(['ffprobe','-v','error','-select_streams','v','-show_entries','stream=nb_frames','-of','csv=p=0',base],capture_output=True,text=True).stdout.strip()}")
