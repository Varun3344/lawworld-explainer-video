#!/bin/zsh
# Kannada office video: wait for the clip queue, then plan -> overlay frames -> compose.
cd "/Users/admin/Downloads/New short/product-explainer"
while ! grep -q "queue\] ALL DONE" logs/kn_office_queue.log; do sleep 10; done
OUT=out/office_kg; mkdir -p $OUT
echo "== plan =="; python3 kanglish/build_kg_plan.py || exit 1
echo "== overlays =="; rm -rf $OUT/frames; ./node_modules/.bin/tsx scripts/render_overlays.ts --html overlays/overlay_brand.html --timeline $OUT/timeline.json --out $OUT/frames | tail -1
echo "== compose =="; python3 scripts/compose2.py $OUT/plan.json | tail -3
echo "[knpost] DONE $(date +%H:%M:%S)"
