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
print(len(bad)); sys.exit(0 if not bad else 1)
PY
}
until ready >/dev/null; do sleep 60; done
log "all clips rendered and flattened"
python3 split/presenter_geom.py downloads/$SET/flat/c*.mp4 --anchor c01 --seam left --max-up 0.10 --out $O/geom.json --place-out $O/place.json > $O/geom.log 2>&1 || { log "geom FAILED"; tail -5 $O/geom.log; exit 1; }
grep -E "SIZE OUTLIER" $O/geom.log | sed "s/^/[post $SET] /"
# a size outlier (a clip framed closer than the rest) sets the common size when every clip still fits that way: no clip beyond
# its native resolution (s <= 1.18 in the 640x1080 box) and every presenter's reach 24 px inside the box; else it stays larger at
# its cuts, with the warning above (Video 1 c28, +12 %, 19-10-2026)
if grep -q "SIZE OUTLIER" $O/geom.log; then
  python3 split/presenter_geom.py --place $O/geom.json --anchor c01 --out $O/place_none.json --seam left --max-up none > $O/place_none.log 2>&1 && \
  python3 - $O <<'PY2' && cp $O/place_none.json $O/place.json && log "size: the outlier sets the common size (every clip fits)"
import re, sys
o = sys.argv[1]; L = open(f"{o}/place_none.log").read()
s = [float(x) for x in re.findall(r"place s (-?[\d.]+)", L)]; r = [(int(a), int(b)) for a, b in re.findall(r"reach x (-?\d+)\.\.(-?\d+)", L)]
ok = bool(s) and bool(r) and max(s) <= 1.18 and min(a for a, _ in r) >= 24 and max(b for _, b in r) <= 616
print(f"[post] size outlier check: max s {max(s or [0]):.3f}, reach {min([a for a, _ in r] or [0])}..{max([b for _, b in r] or [0])} -> {'outlier sets the size' if ok else 'kept: outlier stays larger'}")
sys.exit(0 if ok else 1)
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
