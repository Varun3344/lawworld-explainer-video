#!/bin/zsh
# 02-11-2026: the first HOOK-format judgment reel (kps, SC 2026 INSC 1154). Post it once all 10 clips are rendered and flat.
cd "/Users/admin/Downloads/New short/product-explainer"
export PATH=/usr/local/bin:$PATH
until grep -q "ALL DONE" logs/queue_kps.log 2>/dev/null && (( $(ls downloads/kps/flat/c*.mp4 2>/dev/null | wc -l | tr -d ' ') >= 10 )); do sleep 30; done
echo "$(date +%H:%M:%S) post kps start"
V_LAYOUT=judgment NO_DELIVER=1 OVERLAY_WORKERS=1 zsh split/post_course.sh kps SC_BankOfIndia_v_KamalPasha_2026INSC1154_CoC_cannot_withdraw_approved_plan > logs/post_kps.log 2>&1
echo "$(date +%H:%M:%S) post kps post_course exit $?"
python3 split/thumb_darkfoot.py out/kps/thumb_brand.json > logs/thumb_kps.log 2>&1
zsh split/finish_judgment_reel.sh kps qa > logs/qa_kps.log 2>&1; echo "$(date +%H:%M:%S) post kps done (qa exit $?)"
