#!/bin/zsh
set -e; cd "/Users/admin/Downloads/New short/product-explainer"
while ! grep -q "creator\] DONE" logs/creator_queue.log 2>/dev/null; do sleep 10; done
n=$(ls downloads/creator/h*.mp4 2>/dev/null | wc -l | tr -d ' '); echo "[cpost] clips present: $n"
OUT=out/creator; mkdir -p $OUT
echo "== plan =="; python3 creator/build_creator_plan.py
echo "== overlays =="; rm -rf $OUT/frames; ./node_modules/.bin/tsx scripts/render_overlays.ts --html overlays/overlay_brand.html --timeline $OUT/timeline.json --out $OUT/frames | tail -1
echo "== compose =="; python3 scripts/compose2.py $OUT/plan.json | tail -1
echo "== thumbnail =="; ffmpeg -v error -y -i $OUT/creator.mp4 -ss 1.25 -frames:v 1 $OUT/creator_thumbnail.png && ffmpeg -v error -y -i $OUT/creator_thumbnail.png -q:v 2 $OUT/creator_thumbnail.jpg
echo "[cpost] DONE $(date '+%H:%M:%S')"
