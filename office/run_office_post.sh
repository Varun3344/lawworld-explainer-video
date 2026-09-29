#!/bin/zsh
cd "/Users/admin/Downloads/New short/product-explainer"
while ! grep -q "office\] DONE" logs/office_run.log 2>/dev/null; do sleep 10; done
OUT=out/office; mkdir -p $OUT
echo "== plan =="; python3 office/build_office_plan.py
echo "== overlays =="; rm -rf $OUT/frames; ./node_modules/.bin/tsx scripts/render_overlays.ts --html overlays/overlay_brand.html --timeline $OUT/timeline.json --out $OUT/frames | tail -1
echo "== compose =="; python3 scripts/compose2.py $OUT/plan.json | tail -1
echo "[opost] DONE $(date +%H:%M:%S)"
