#!/bin/zsh
# 31-10-2026: round-2 post-production in two fixed lanes (chain d never started a post; replaced). Lane A: ssk then sbp; lane B: bcr then smt.
cd "/Users/admin/Downloads/New short/product-explainer"
typeset -A STEM; STEM=(ssk KHC_WA_909_2026_Shashikiran_prison_land_acquisition_upheld bcr Madras_CRP_5206_2026_Bennett_ex_developer_still_RERA_allottee sbp SC_SouthBiharPower_2026INSC1165_who_extends_arbitral_mandate smt Kerala_WA_2222_2026_OBC_creamy_layer_direct_recruit_judge)
post() { echo "$(date +%H:%M:%S) post $1 start"
  V_LAYOUT=judgment NO_DELIVER=1 OVERLAY_WORKERS=1 zsh split/post_course.sh $1 ${STEM[$1]} > logs/post_$1.log 2>&1
  echo "$(date +%H:%M:%S) post $1 post_course exit $?"
  python3 split/thumb_brand.py out/$1/thumb_brand.json > logs/thumb_$1.log 2>&1
  zsh split/finish_judgment_reel.sh $1 qa > logs/qa_$1.log 2>&1; echo "$(date +%H:%M:%S) post $1 done (qa exit $?)"; }
{ post ssk; post sbp; } &
{ post bcr; post smt; } &
wait; echo "$(date +%H:%M:%S) ALL POSTS DONE"
