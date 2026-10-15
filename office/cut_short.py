"""Cut a shorter version of a composed office video from whole presenter clips, with a fresh continuous music bed.

Usage (from product-explainer/):
  python3 office/cut_short.py <master.mp4> <plan.json> <out.mov> o01 o02 o03 o15 o16 o17 [--sfx-from=<other plan.json>]

--sfx-from takes the sfx list from another plan with the same presenter timeline, for a master mixed from an earlier
plan: LawWorld_Product_Video_Office.mp4 is the 019e388 build (pops on Better/Faster/Cheaper, no orbit riser), while
out/office/plan.json is the Premium build. Regenerate the old plan by running 019e388's office/build_office_plan.py in a
scratch checkout (downloads/ symlinked, an empty scripts/envkeys.py stub).

Picture: frame-exact runs of the composed master (the hook before o01 and the end card after the last clip come along
when the first / last clip is kept). Sentences stay whole because cuts fall only on clip boundaries.
Sound: rebuilt with compose2's pass-1 recipe from work/voice.wav (voice stem of the same run) and the plan's sfx,
re-timed per run, over one continuous bed, so the music does not jump at the cuts. Gains are the full video's
(read from compose_run.log) so the short and the full cut sound alike.
Output is an intermediate .mov (x264 crf 10 + PCM) for open_on_card.py.
"""
import json
import math
import os
import re
import subprocess
import sys

FPS = 24


def main():
    master, plan_path, out = sys.argv[1:4]
    keep = [a for a in sys.argv[4:] if not a.startswith("--")]
    plan = json.load(open(plan_path))
    for a in sys.argv[4:]:
        if a.startswith("--sfx-from="):
            other = json.load(open(a.split("=", 1)[1]))
            if [(p["clip"], p["in"], p["out"]) for p in other["presenter"]] != [(p["clip"], p["in"], p["out"]) for p in plan["presenter"]]:
                raise SystemExit("--sfx-from plan has a different presenter timeline")
            plan["sfx"] = other["sfx"]
    root = os.path.dirname(os.path.dirname(os.path.abspath(plan_path)))  # out/<name>/plan.json -> out/
    work = os.path.join(os.path.dirname(plan_path), "work")
    log = open(os.path.join(os.path.dirname(plan_path), "compose_run.log")).read()
    vg, mg = (float(x) for x in re.search(r"voice gain ([+-][\d.]+) dB, music gain ([+-][\d.]+) dB", log).groups())

    ps, total = plan["presenter_start"], plan["total"]
    t, clips = ps, []
    for p in plan["presenter"]:
        cid = os.path.basename(p["clip"])[:-4]
        clips.append((cid, t, t + p["out"] - p["in"]))
        t += p["out"] - p["in"]
    pend = t
    ids = [c[0] for c in clips]
    unknown = [k for k in keep if k not in ids]
    if unknown:
        raise SystemExit(f"unknown clips {unknown}")

    # contiguous runs of kept clips, in master seconds
    runs = []
    for cid, s, e in clips:
        if cid not in keep:
            continue
        if runs and abs(runs[-1][1] - s) < 1e-6:
            runs[-1][1] = e
        else:
            runs.append([s, e])
    if runs and abs(runs[0][0] - ps) < 1e-6:
        runs[0][0] = 0.0  # keep the hook card that plays before the first clip
    if runs and abs(runs[-1][1] - pend) < 1e-6:
        runs[-1][1] = total  # keep the end card
    # frame-exact: a run owns the frames whose start time lies in [s, e)
    fr = [(math.ceil(s * FPS - 1e-6), math.ceil(e * FPS - 1e-6)) for s, e in runs]
    n_master = round(total * FPS)
    fr[-1] = (fr[-1][0], min(fr[-1][1], n_master))
    new_total = sum(b - a for a, b in fr) / FPS
    print("runs (frames):", fr, f"-> {new_total:.3f} s")

    # ---- sound ----
    inputs, graph, mixin = ["-i", os.path.join(work, "voice.wav"), "-i", os.path.join(root, "..", plan["music"]["file"])], [], []
    pos = 0.0
    sfx_inputs = []
    for k, (a, b) in enumerate(fr):
        s, e = a / FPS, b / FPS
        vs, ve = max(s, ps) - ps, min(e, pend) - ps
        if ve > vs:
            at = pos + (max(s, ps) - s)
            graph.append(f"[0:a]atrim={vs:.4f}:{ve:.4f},asetpts=PTS-STARTPTS,afade=t=in:st=0:d=0.01,"
                         f"volume={vg:.2f}dB,adelay={round(at * 1000)}:all=1[v{k}]")
            mixin.append(f"[v{k}]")
        for ev in plan.get("sfx", []):
            if s - 0.2 <= ev["at"] < e:
                sfx_inputs.append((ev, pos + ev["at"] - s))
        pos += e - s
    graph.append(f"{''.join(mixin)}amix=inputs={len(mixin)}:normalize=0:duration=longest,apad=whole_dur={new_total:.4f},asplit[vmain][vkey]")
    m = plan["music"]
    graph.append(f"[1:a]atrim=0:{new_total:.4f},asetpts=PTS-STARTPTS,volume={mg:.2f}dB,afade=t=in:st=0:d={m['fade_in']},"
                 f"afade=t=out:st={new_total - m['fade_out']:.4f}:d={m['fade_out']}[mus]")
    graph.append("[mus][vkey]sidechaincompress=threshold=0.015:ratio=5:attack=60:release=700:makeup=1:level_sc=1[musd]")
    sx = []
    for k, (ev, at) in enumerate(sfx_inputs):
        inputs += ["-i", os.path.join(root, "..", ev["file"])]
        d = round(max(0.0, at) * 1000)
        graph.append(f"[{k + 2}:a]volume={ev.get('gain_db', -8):.1f}dB,adelay={d}|{d},apad=whole_dur={new_total:.4f}[sx{k}]")
        sx.append(f"[sx{k}]")
    limiter = f"alimiter=limit={plan.get('limit', 0.89)}" + (":level=0" if "limit" in plan else "") + ":attack=5:release=80,aresample=48000[aout]"
    if sx:
        graph.append(f"{''.join(sx)}amix=inputs={len(sx)}:normalize=0:duration=first:dropout_transition=0[sfxmix]")
        graph.append(f"[vmain][musd][sfxmix]amix=inputs=3:normalize=0:duration=first:dropout_transition=0,{limiter}")
    else:
        graph.append(f"[vmain][musd]amix=inputs=2:normalize=0:duration=first:dropout_transition=0,{limiter}")
    wav = out[:-4] + "_audio.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(graph), "-map", "[aout]",
                    "-t", f"{new_total:.4f}", "-ac", "2", "-c:a", "pcm_s16le", wav], check=True)
    print(f"sound: {len(mixin)} voice runs, {len(sx)} sfx, voice {vg:+.1f} dB, music {mg:+.1f} dB")

    # ---- picture ----
    vg_ = ";".join(f"[0:v]trim=start_frame={a}:end_frame={b},setpts=PTS-STARTPTS[p{k}]" for k, (a, b) in enumerate(fr))
    vg_ += ";" + "".join(f"[p{k}]" for k in range(len(fr))) + f"concat=n={len(fr)}:v=1:a=0[vo]"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", master, "-i", wav, "-filter_complex", vg_, "-map", "[vo]", "-map", "1:a",
                    "-c:v", "libx264", "-preset", "fast", "-crf", "10", "-pix_fmt", "yuv420p", "-r", str(FPS),
                    "-c:a", "pcm_s16le", out], check=True)
    print(out)


if __name__ == "__main__":
    main()
