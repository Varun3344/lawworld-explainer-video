#!/bin/zsh
# Post-production of one course video, from flattened clips to the two deliverables (no Flow credits):
#   size match (presenter_geom) -> plan + cues (build_course_plan) -> overlay frames (3 headless renderers) -> 16:9 (compose2)
#   -> QA -> 9:16 (build_vertical_course: captions, two presenter tracks, automatic edit, final) -> ~/Downloads
# Waits until every clip of the set is rendered (words.json keep) and flattened. Usage: zsh split/post_course.sh <set> <file stem>
# e.g. zsh split/post_course.sh cog LawWorld_Cognizable_vs_NonCognizable
set -u
cd "/Users/admin/Downloads/New short/product-explainer"
SET=$1; STEM=$2; O=out/$SET; mkdir -p $O
log() { echo "[post $SET] $(date +%H:%M:%S) $*"; }
ready() { python3 - "$SET" <<'PY'
import json, os, sys
s = sys.argv[1]; ids = [x["sceneId"] for x in json.load(open(f"split/{s}_all_scenes.json"))["scenes"]]
bad = []
for c in ids:
    src, flat, w = f"downloads/{s}/{c}.mp4", f"downloads/{s}/flat/{c}.mp4", f"downloads/{s}/{c}.words.json"
    if not (os.path.exists(src) and os.path.exists(w) and os.path.exists(flat) and os.path.getmtime(flat) >= os.path.getmtime(src)): bad.append(c); continue
    if not json.load(open(w)).get("keep"): bad.append(c)
if not bad:
    # every flat must be readable and as long as its source: a corrupt flat (two flattens of one clip, 19-10) is set aside so the
    # flatten workers redo it, instead of failing the size match later
    import subprocess, time
    def dur(p):
        r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p], capture_output=True, text=True).stdout.strip()
        try: return float(r)
        except ValueError: return None
    for c in ids:
        flat, src = f"downloads/{s}/flat/{c}.mp4", f"downloads/{s}/{c}.mp4"
        fd, sd = dur(flat), dur(src)
        if fd is None or sd is None or abs(fd - sd) > 0.1:
            os.makedirs("downloads/_old_style_19oct/corrupt_flats", exist_ok=True)
            os.replace(flat, f"downloads/_old_style_19oct/corrupt_flats/{s}_{c}_{int(time.time())}.mp4"); bad.append(c)
            print(f"[post {s}] corrupt flat {c} set aside for re-flattening", file=sys.stderr)
print(len(bad)); sys.exit(0 if not bad else 1)
PY
}
until ready >/dev/null; do sleep 60; done
log "all clips rendered and flattened"
python3 split/presenter_geom.py downloads/$SET/flat/c*.mp4 --anchor c01 --seam left --max-up 0.10 --out $O/geom.json --place-out $O/place.json > $O/geom.log 2>&1 || { log "geom FAILED"; tail -5 $O/geom.log; exit 1; }
grep -E "SIZE OUTLIER" $O/geom.log | sed "s/^/[post $SET] /"
# a size outlier (a clip framed closer than the rest) sets the common size when every clip still fits that way: no clip beyond
# 5 % past its native resolution (s <= 1.25 in the 640x1080 box; Video 2 needed 1.244 for four close-framed clips) and every presenter's reach 24 px inside the box; else it stays larger at
# its cuts, with the warning above (Video 1 c28, +12 %, 19-10-2026)
if grep -q "SIZE OUTLIER" $O/geom.log; then
  # try thresholds from 0.10 up (none = no outliers): keep the one with the smallest size jump left at the outliers' cuts, as long as
  # no clip goes past s 1.30 (~10 % past native in the 640x1080 box) and every presenter's reach stays 24 px inside the box
  # (Video 4, 19-10: 0.12 left jumps of <= 2.5 % at s 1.29; 0.10 left 7 %; none needed s 1.32)
  for m in 0.12 0.14 0.16 0.20 none; do
    python3 split/presenter_geom.py --place $O/geom.json --anchor c01 --out $O/place_$m.json --seam left --max-up $m > $O/place_$m.log 2>&1
  done
  python3 - $O <<'PY2'
import re, shutil, sys
o = sys.argv[1]; best = None
for m in ("0.12", "0.14", "0.16", "0.20", "none"):
    try: L = open(f"{o}/place_{m}.log").read()
    except OSError: continue
    s = [float(x) for x in re.findall(r"place s (-?[\d.]+)", L)]; r = [(int(a), int(b)) for a, b in re.findall(r"reach x (-?\d+)\.\.(-?\d+)", L)]
    left = max([float(x) for x in re.findall(r"stays \+([\d.]+) % larger", L)] or [0.0])
    ok = bool(s) and bool(r) and max(s) <= 1.30 and min(a for a, _ in r) >= 24 and max(b for _, b in r) <= 616
    print(f"[post] size: max_up {m}: max s {max(s or [0]):.3f}, outliers stay up to +{left:.1f} %{'' if ok else ' (rejected)'}")
    if ok and (best is None or left < best[1] - 0.05): best = (m, left)
if best:
    shutil.copy(f"{o}/place_{best[0]}.json", f"{o}/place.json"); print(f"[post] size: using max_up {best[0]} (outliers stay up to +{best[1]:.1f} %)")
else: print("[post] size: kept max_up 0.10 (outliers stay larger)")
PY2
fi
python3 split/build_course_plan.py --set $SET || { log "plan FAILED"; exit 1; }
log "overlay frames"
rm -rf $O/frames; zsh split/render_parallel.sh overlays/split_panel.html $O/timeline.json $O/frames ${OVERLAY_WORKERS:-2} > $O/frames.log 2>&1 || { log "overlays FAILED"; tail -5 $O/frames.log; exit 1; }
log "16:9 compose"
python3 scripts/compose2.py $O/plan.json > $O/compose.log 2>&1 || { log "compose FAILED"; tail -5 $O/compose.log; exit 1; }
tail -1 $O/compose.log
python3 split/qa_split.py $O/${SET}_full.mp4 > $O/qa.log 2>&1; grep -iE "FAIL|WARN|recall|loud|frames" $O/qa.log | head -12 | sed "s/^/[post $SET] qa: /"
python3 split/qa_sync.py $SET > $O/sync.log 2>&1; tail -1 $O/sync.log | sed "s/^/[post $SET] /"
log "9:16"
V=out/${SET}9x16
python3 split/build_vertical_course.py $SET captions > $O/v_captions.log 2>&1 && \
python3 split/build_vertical_course.py $SET ptrack split > $O/v_ptrack.log 2>&1 && \
python3 split/build_vertical_course.py $SET ptrack full > $O/v_ptrack_full.log 2>&1 && \
python3 split/build_vertical_course.py $SET edit && \
python3 split/build_vertical_course.py $SET final > $O/v_final.log 2>&1 || { log "9:16 FAILED"; tail -5 $O/v_*.log; exit 1; }
# a clip whose words did not survive into the final mix may be a wrong fact: hold the pair for review (every other QA flag is
# cosmetic and is delivered with its warning, owner rule 23-09: hold only for a wrong fact)
if grep -q "FAIL .*spoken text intact" $O/qa.log; then log "qa: speech FAIL - HELD for review, not copied to ~/Downloads ($(grep -c "FAIL .*spoken text intact" $O/qa.log) clip(s); 16:9 $O/${SET}_full.mp4, 9:16 $V/${SET}_9x16.mp4)"; exit 0; fi
[ -n "${NO_DELIVER:-}" ] && { log "test run: not copied to ~/Downloads"; exit 0; }
cp $O/${SET}_full.mp4 ~/Downloads/${STEM}_16x9.mp4
cp $V/${SET}_9x16.mp4 ~/Downloads/${STEM}_9x16.mp4
cp $O/captions.srt ~/Downloads/${STEM}_16x9.srt
ffmpeg -v error -y -i $O/${SET}_full.mp4 -frames:v 1 -q:v 2 ~/Downloads/${STEM}_16x9_cover.jpg
ffmpeg -v error -y -i $V/${SET}_9x16.mp4 -frames:v 1 -q:v 2 ~/Downloads/${STEM}_9x16_cover.jpg
log "DELIVERED ~/Downloads/${STEM}_16x9.mp4 + _9x16.mp4 (md5 $(md5 -q ~/Downloads/${STEM}_16x9.mp4) / $(md5 -q ~/Downloads/${STEM}_9x16.mp4))"
