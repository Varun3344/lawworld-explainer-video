#!/bin/zsh
# 31-10-2026 rounds 2-3: post-production for each set once its queue says ALL DONE and its 10 clips are flat; at most 2 post_course at once.
cd "/Users/admin/Downloads/New short/product-explainer"
typeset -A STEM; STEM=(
 ssk KHC_WA_909_2026_Shashikiran_prison_land_acquisition_upheld
 bcr Madras_CRP_5206_2026_Bennett_ex_developer_still_RERA_allottee
 sbp SC_SouthBiharPower_2026INSC1165_who_extends_arbitral_mandate
 smt Kerala_WA_2222_2026_OBC_creamy_layer_direct_recruit_judge
 lgc KHC_ITA_338_2013_Logica_Infosys_Wipro_not_comparables
 omc SC_OrissaMining_2026INSC1171_no_143_2_notice_reassessment_fails
 ikc Madras_ArbOP_513_2026_Inderchand_forgery_plea_arbitrator_appointed)
post() { echo "$(date +%H:%M:%S) post $1 start"
  V_LAYOUT=judgment NO_DELIVER=1 OVERLAY_WORKERS=1 zsh split/post_course.sh $1 ${STEM[$1]} > logs/post_$1.log 2>&1
  echo "$(date +%H:%M:%S) post $1 post_course exit $?"
  python3 split/thumb_brand.py out/$1/thumb_brand.json > logs/thumb_$1.log 2>&1
  zsh split/finish_judgment_reel.sh $1 qa > logs/qa_$1.log 2>&1; echo "$(date +%H:%M:%S) post $1 done (qa exit $?)"; }
left=(${@:-ssk bcr sbp smt lgc omc ikc})
while (( ${#left} )); do
  for s in $left; do
    grep -q "ALL DONE" logs/queue_$s.log 2>/dev/null || continue
    [ $(ls downloads/$s/flat/c*.mp4 2>/dev/null | wc -l) -ge 10 ] || continue
    [ $(pgrep -f "post_course.sh " | wc -l) -lt 2 ] || continue
    left=(${left:#$s}); post $s & sleep 40
  done
  sleep 20
done
wait; echo "$(date +%H:%M:%S) ALL POSTS DONE"
