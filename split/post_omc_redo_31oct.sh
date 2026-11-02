#!/bin/zsh
# 31-10-2026: omc re-rendered in a dark suit (the warm-taupe one was flattened into the backdrop); post it once all 10 clips are flat.
cd "/Users/admin/Downloads/New short/product-explainer"
until grep -q "ALL DONE" logs/queue_omc_redo.log 2>/dev/null && (( $(ls downloads/omc/flat/c*.mp4 2>/dev/null | wc -l | tr -d ' ') >= 10 )); do sleep 30; done
while (( $(pgrep -f "post_course.sh " | wc -l | tr -d ' ') >= 2 )); do sleep 20; done
echo "$(date +%H:%M:%S) post omc (redo) start"
V_LAYOUT=judgment NO_DELIVER=1 OVERLAY_WORKERS=1 zsh split/post_course.sh omc SC_OrissaMining_2026INSC1171_no_143_2_notice_reassessment_fails > logs/post_omc.log 2>&1
echo "$(date +%H:%M:%S) post omc (redo) post_course exit $?"
python3 split/thumb_brand.py out/omc/thumb_brand.json > logs/thumb_omc.log 2>&1
zsh split/finish_judgment_reel.sh omc qa > logs/qa_omc.log 2>&1; echo "$(date +%H:%M:%S) post omc (redo) done (qa exit $?)"
