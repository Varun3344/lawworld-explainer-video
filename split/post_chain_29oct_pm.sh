#!/bin/zsh
# 29-10-2026 afternoon: post-production for the five 4:30 pm reels, one at a time in the order their renders finish.
cd "/Users/admin/Downloads/New short/product-explainer"
typeset -A STEM; STEM=(gpk SC_Gopalakrishanan_2026INSC1172_DA_burden_of_proof csb SC_ChetanSabharwal_2026INSC1163_reopening_change_of_opinion scc Delhi_FAOOSCOMM_248_2026_Siddhivinayak_summary_suit_no_appeal czs KHC_CrlP_847_2025_CarlZeiss_CLRA_limitation gms Kerala_FAO_95_2026_Greenmount_v_Wipro_trademark)
for s in gpk scc csb czs gms; do
  until grep -q "ALL DONE" logs/queue_$s.log 2>/dev/null; do sleep 20; done
  if [ "$s" = "czs" ]; then export CAP_FONT="Kannada Sangam MN" QA_LANG=kn; else unset CAP_FONT QA_LANG; fi
  echo "$(date +%H:%M:%S) post $s start"
  V_LAYOUT=judgment NO_DELIVER=1 OVERLAY_WORKERS=1 zsh split/post_course.sh $s ${STEM[$s]} > logs/post_$s.log 2>&1
  python3 split/thumb_brand.py out/$s/thumb_brand.json > logs/thumb_$s.log 2>&1
  zsh split/finish_judgment_reel.sh $s qa > logs/qa_$s.log 2>&1
  echo "$(date +%H:%M:%S) post $s done (qa exit $?)"
done
echo "$(date +%H:%M:%S) ALL POSTS DONE"
