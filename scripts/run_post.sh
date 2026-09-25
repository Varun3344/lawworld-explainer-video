#!/bin/zsh
# Post-production for the sample: voice → word timings/QA → plan → overlay frames → compose.
set -e
cd "/Users/admin/Downloads/New short/product-explainer"
D=downloads/sample; OUT=out/sample
CLIPS=($D/p01_hello.mp4 $D/p02_introduce.mp4 $D/p03_caseprep.mp4)
for c in $CLIPS; do [ -f "$c" ] || { echo "missing $c"; exit 1; }; done
echo "== voice (ElevenLabs speech-to-speech) =="; python3 scripts/voice_sts.py $CLIPS
RAVI=($D/p01_hello.ravi.mp4 $D/p02_introduce.ravi.mp4 $D/p03_caseprep.ravi.mp4)
echo "== word timings + verbatim check =="; python3 scripts/words.py storyboards/sample_presenter.json $RAVI
B01=$D/broll_3d/b01_features_broll.mp4; B02=$D/broll_3d/b02_caseprep_broll.mp4
ARGS=(); [ -f "$B01" ] && ARGS+=(--b01 "$B01"); [ -f "$B02" ] && ARGS+=(--b02 "$B02")
echo "== plan =="; python3 scripts/build_plan.py --sb storyboards/sample_presenter.json --clips $RAVI $ARGS --music audio/bed_sample_40s.mp3 --out $OUT
echo "== overlays =="; rm -rf $OUT/frames; ./node_modules/.bin/tsx scripts/render_overlays.ts --timeline $OUT/timeline.json --out $OUT/frames | tail -2
echo "== compose =="; python3 scripts/compose.py $OUT/plan.json ${1:-}
