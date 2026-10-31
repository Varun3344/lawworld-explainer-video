#!/bin/zsh
# 31-10-2026: kmv c03 re-rendered (the first take skipped "K M V Projects"): flatten it, wait for a free post lane (max 2), rebuild kmv.
cd "/Users/admin/Downloads/New short/product-explainer"
zsh split/flatten_all.sh kmv
echo "$(date +%H:%M:%S) kmv c03 flat"
while [ $(pgrep -f "post_course.sh " | wc -l) -ge 2 ]; do sleep 20; done
echo "$(date +%H:%M:%S) post kmv (redo) start"
V_LAYOUT=judgment NO_DELIVER=1 OVERLAY_WORKERS=1 zsh split/post_course.sh kmv KHC_COMAP_87_2025_KMV_Projects_price_escalation_clause_deleted > logs/post_kmv.log 2>&1
echo "$(date +%H:%M:%S) post kmv (redo) post_course exit $?"
python3 split/thumb_brand.py out/kmv/thumb_brand.json > logs/thumb_kmv.log 2>&1
zsh split/finish_judgment_reel.sh kmv qa > logs/qa_kmv.log 2>&1; echo "$(date +%H:%M:%S) post kmv (redo) done (qa exit $?)"
