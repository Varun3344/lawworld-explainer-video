#!/bin/zsh
# Overnight 28/29-10-2026: post-production for the five 9 am reels, one at a time (post_course waits for each set's clips).
cd "/Users/admin/Downloads/New short/product-explainer"
typeset -A STEM; STEM=(nkp SC_UoI_v_NarenderKumar_2026INSC1166_war_injury_pension rcc SC_RoyalConstruction_2026INSC1167_award_execution ele Kerala_CrlMC_6502_2025_Krishnankutty_elephant_s406 mon KHC_WP_674_2026_Monika_maternity_leave_probation pan Delhi_WPC_9365_2025_Lalit_PAN_misuse_tax)
for s in nkp rcc ele mon pan; do
  if [ "$s" = "mon" ]; then export CAP_FONT="Kannada Sangam MN" QA_LANG=kn; else unset CAP_FONT QA_LANG; fi
  echo "$(date +%H:%M:%S) post $s start"
  V_LAYOUT=judgment NO_DELIVER=1 OVERLAY_WORKERS=1 zsh split/post_course.sh $s ${STEM[$s]} > logs/post_$s.log 2>&1
  python3 split/thumb_brand.py out/$s/thumb_brand.json > logs/thumb_$s.log 2>&1
  zsh split/finish_judgment_reel.sh $s qa > logs/qa_$s.log 2>&1
  echo "$(date +%H:%M:%S) post $s done (qa exit $?)"
done
echo "$(date +%H:%M:%S) ALL POSTS DONE"
