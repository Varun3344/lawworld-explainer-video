#!/bin/zsh
set -e; cd "/Users/admin/Downloads/New short/product-explainer"; OUT=out/sample2; mkdir -p $OUT
echo "== words =="; python3 scripts/words.py storyboards/full_all_scenes.json downloads/full/c01.mp4 downloads/full/c02.mp4 downloads/full/c03.mp4
echo "== plan =="; python3 scripts/build_sample2_plan.py
echo "== overlays =="; rm -rf $OUT/frames; ./node_modules/.bin/tsx scripts/render_overlays.ts --html overlays/overlay_brand.html --timeline $OUT/timeline.json --out $OUT/frames | tail -1
echo "== compose =="; python3 scripts/compose.py $OUT/plan.json ${1:-}
