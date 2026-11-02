#!/bin/zsh
# 02-11-2026: kps rebuilt after the c04 card overlap (no Flow: clips unchanged), new thumbnail, QA, ship.
cd "/Users/admin/Downloads/New short/product-explainer"; export PATH=/usr/local/bin:$PATH
echo "$(date +%H:%M:%S) kps rebuild start"
V_LAYOUT=judgment NO_DELIVER=1 OVERLAY_WORKERS=2 zsh split/post_course.sh kps SC_BankOfIndia_v_KamalPasha_2026INSC1154_CoC_cannot_withdraw_approved_plan > logs/post_kps.log 2>&1; echo "$(date +%H:%M:%S) post_course exit $?"
python3 split/thumb_darkfoot.py out/kps/thumb_brand.json > logs/thumb_kps.log 2>&1
zsh split/finish_judgment_reel.sh kps qa > logs/qa_kps.log 2>&1; echo "$(date +%H:%M:%S) qa exit $?"
zsh split/finish_judgment_reel.sh kps ship bank-of-india-v-kamal-pasha-2026-insc-1154 SC_BankOfIndia_v_KamalPasha_2026INSC1154_CoC_cannot_withdraw_approved_plan > logs/ship_kps.log 2>&1; echo "$(date +%H:%M:%S) ship exit $?"; tail -3 logs/ship_kps.log
