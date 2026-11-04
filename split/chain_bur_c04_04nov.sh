#!/bin/zsh
# 04-11-2026: after gvd finishes on a3, re-take bur c04 (date heard as "March twenty-five"), then start sfr on a3.
cd "/Users/admin/Downloads/New short/product-explainer"; export PATH=/usr/local/bin:$PATH
until grep -q "ALL DONE" logs/queue_gvd.log 2>/dev/null; do sleep 30; done
echo "[chain] gvd done, re-taking bur c04 $(date +%H:%M:%S)"
mkdir -p downloads/bur/rejected
mv downloads/bur/c04.mp4 downloads/bur/rejected/c04_march25.mp4; mv downloads/bur/c04.words.json downloads/bur/rejected/c04_march25.words.json
mv downloads/bur/flat/c04.mp4 downloads/bur/rejected/c04_march25_flat.mp4 2>/dev/null
( source split/bur_env.sh && python3 split/make_course_sb.py bur && zsh split/run_queue.sh c04 ) >> logs/queue_bur_retake.log 2>&1
grep -E "words\] c04" logs/queue_bur_retake.log | tail -1
echo "[chain] starting sfr $(date +%H:%M:%S)"
source split/sfr_env.sh; python3 split/make_course_sb.py sfr --new-project; touch split/GOsfr
zsh split/run_queue.sh c01 c02 c03 c04 c05 c06 c07 c08 c09 c10
