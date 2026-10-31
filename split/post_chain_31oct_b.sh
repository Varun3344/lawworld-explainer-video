#!/bin/zsh
# 31-10-2026 afternoon: post-production of the four 4 pm reels, one at a time in the order their renders finish.
cd "/Users/admin/Downloads/New short/product-explainer"
typeset -A STEM; STEM=(dvc SC_DVC_v_MaithanAlloys_2026INSC1178_review_cannot_reopen_settled_point kmv KHC_COMAP_87_2025_KMV_Projects_price_escalation_clause_deleted vzj Kerala_WPC_34157_2022_Vizhinjam_expert_committee_conflict arm Madras_WP_30908_2024_ArunaMills_GST_refund_no_DRC04)
left=(dvc kmv vzj arm)
while (( ${#left} )); do
  s=""; for x in $left; do grep -q "ALL DONE" logs/queue_$x.log 2>/dev/null && { s=$x; break; }; done
  [ -z "$s" ] && { sleep 20; continue; }
  left=(${left:#$s})
  echo "$(date +%H:%M:%S) post $s start"
  V_LAYOUT=judgment NO_DELIVER=1 OVERLAY_WORKERS=1 zsh split/post_course.sh $s ${STEM[$s]} > logs/post_$s.log 2>&1
  echo "$(date +%H:%M:%S) post $s post_course exit $?"
  python3 split/thumb_brand.py out/$s/thumb_brand.json > logs/thumb_$s.log 2>&1
  zsh split/finish_judgment_reel.sh $s qa > logs/qa_$s.log 2>&1
  echo "$(date +%H:%M:%S) post $s done (qa exit $?)"
done
echo "$(date +%H:%M:%S) ALL POSTS DONE"
