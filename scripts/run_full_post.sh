#!/bin/zsh
# Full video post-production: word timings + verbatim gate -> plan -> brand overlays -> compose.
set -e
cd "/Users/admin/Downloads/New short/product-explainer"
OUT=out/full; mkdir -p $OUT
echo "== word timings + verbatim check (Flow voice, original audio) =="
python3 scripts/words.py storyboards/full_all_scenes.json downloads/full/c*.mp4 | tee $OUT/words_report.txt
if grep -q "CHECK" $OUT/words_report.txt; then echo "!! some clips are not verbatim — see $OUT/words_report.txt"; [ "$1" = "--force" ] || exit 2; fi
echo "== plan =="; python3 scripts/build_full_plan.py --clips downloads/full --broll downloads/full/broll_3d --music audio/bed_full_170s.mp3 --out $OUT
echo "== overlays =="; rm -rf $OUT/frames; ./node_modules/.bin/tsx scripts/render_overlays.ts --html overlays/overlay_brand.html --timeline $OUT/timeline.json --out $OUT/frames | tail -2
echo "== compose =="; python3 scripts/compose2.py $OUT/plan.json ${2:-}
