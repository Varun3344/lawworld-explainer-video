#!/bin/zsh
# 31-10-2026: the 4 pm reels in two lanes (renders all finished): lane A = dvc (already running as its own post_course) then vzj,
# lane B = kmv then arm. Each set writes only under out/<set>, so two lanes are safe; OVERLAY_WORKERS=1 keeps memory low.
cd "/Users/admin/Downloads/New short/product-explainer"
typeset -A STEM; STEM=(dvc SC_DVC_v_MaithanAlloys_2026INSC1178_review_cannot_reopen_settled_point kmv KHC_COMAP_87_2025_KMV_Projects_price_escalation_clause_deleted vzj Kerala_WPC_34157_2022_Vizhinjam_expert_committee_conflict arm Madras_WP_30908_2024_ArunaMills_GST_refund_no_DRC04)
finish() { python3 split/thumb_brand.py out/$1/thumb_brand.json > logs/thumb_$1.log 2>&1
           zsh split/finish_judgment_reel.sh $1 qa > logs/qa_$1.log 2>&1; echo "$(date +%H:%M:%S) post $1 done (qa exit $?)"; }
post() { echo "$(date +%H:%M:%S) post $1 start"
         V_LAYOUT=judgment NO_DELIVER=1 OVERLAY_WORKERS=1 zsh split/post_course.sh $1 ${STEM[$1]} > logs/post_$1.log 2>&1
         echo "$(date +%H:%M:%S) post $1 post_course exit $?"; finish $1; }
laneA() { while pgrep -f "post_course.sh dvc " >/dev/null; do sleep 15; done
          echo "$(date +%H:%M:%S) post dvc post_course finished (earlier chain)"; finish dvc; post vzj; }
laneB() { post kmv; post arm; }
laneA & laneB & wait
echo "$(date +%H:%M:%S) ALL POSTS DONE"
