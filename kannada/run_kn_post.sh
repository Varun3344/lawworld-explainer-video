#!/bin/zsh
set -e; cd "/Users/admin/Downloads/New short/product-explainer"
while pgrep -f run_kn_retries.sh >/dev/null; do sleep 5; done
OUT=out/kn; mkdir -p $OUT
echo "== words (kn) =="; for c in k02 k04; do [ -f downloads/kn/$c.mp4 ] && python3 scripts/words.py kannada/kn_all_scenes.json downloads/kn/$c.mp4 --lang kn --prompt "ಲಾವರ್ಲ್ಡ್, ಭಾರತೀಯ ನ್ಯಾಯ ಸಂಹಿತೆ, ಭಾರತೀಯ ಸಾಕ್ಷ್ಯ ಅಧಿನಿಯಮ" | tail -1; done
echo "== plan =="; python3 kannada/build_kn_plan.py
echo "== overlays =="; rm -rf $OUT/frames; ./node_modules/.bin/tsx scripts/render_overlays.ts --html overlays/overlay_brand.html --timeline $OUT/timeline.json --out $OUT/frames | tail -1
echo "== compose =="; python3 scripts/compose2.py $OUT/plan.json | tail -1
echo "== finalize =="; ./scripts/finalize.sh $OUT/kn_sample.mp4 $OUT/LawWorld_Kannada_SAMPLE.mp4 $OUT/kn_thumbnail.png
echo "[knpost] DONE $(date '+%H:%M:%S')"
