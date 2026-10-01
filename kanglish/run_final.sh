#!/bin/zsh
cd "/Users/admin/Downloads/New short/product-explainer"; OUT=out/office_kg
echo "== plan =="; python3 kanglish/build_kg_plan.py || exit 1
echo "== overlays =="; rm -rf $OUT/frames; ./node_modules/.bin/tsx scripts/render_overlays.ts --html overlays/overlay_brand.html --timeline $OUT/timeline.json --out $OUT/frames | tail -1
echo "== compose =="; python3 scripts/compose2.py $OUT/plan.json | tail -2
echo "== qa =="; python3 kanglish/qa_final.py
echo "[knfinal] DONE $(date +%H:%M:%S)"
