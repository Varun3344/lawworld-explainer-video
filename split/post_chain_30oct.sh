#!/bin/zsh
# 30-10-2026: post-production for today's two judgment reels (SC srb English, Karnataka mda Kannada), one at a time as renders finish.
cd "/Users/admin/Downloads/New short/product-explainer"
typeset -A STEM; STEM=(srb SC_ShreeramBuilders_2026INSC1176_arbitrators_cannot_rewrite_contract mda KHC_WP_43457_2015_MandyaUDA_registration_not_application)
for s in srb mda; do
  until grep -q "ALL DONE" logs/queue_$s.log 2>/dev/null; do sleep 20; done
  if [ "$s" = "mda" ]; then export CAP_FONT="Kannada Sangam MN" QA_LANG=kn; else unset CAP_FONT QA_LANG; fi
  echo "$(date +%H:%M:%S) post $s start"
  V_LAYOUT=judgment NO_DELIVER=1 OVERLAY_WORKERS=1 zsh split/post_course.sh $s ${STEM[$s]} > logs/post_$s.log 2>&1
  echo "$(date +%H:%M:%S) post $s post_course exit $?"
  python3 split/thumb_brand.py out/$s/thumb_brand.json > logs/thumb_$s.log 2>&1
  zsh split/finish_judgment_reel.sh $s qa > logs/qa_$s.log 2>&1
  echo "$(date +%H:%M:%S) post $s done (qa exit $?)"
done
echo "$(date +%H:%M:%S) ALL POSTS DONE"
