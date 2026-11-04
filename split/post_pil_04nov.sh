#!/bin/zsh
# Post-production for ape (English) and apk (Kannada: CAP_FONT + QA_LANG), each once its 10 clips are rendered and flat; ships to ~/Downloads.
cd "/Users/admin/Downloads/New short/product-explainer"; export PATH=/usr/local/bin:$PATH
typeset -A STEM SLUG; STEM=(ape KHC_SuoMotu_PIL_Advocates_safety_03_11_2026_English apk KHC_SuoMotu_PIL_Advocates_safety_03_11_2026_Kannada)
SLUG=(ape suo-motu-pil-advocates-safety-khc-03-11-2026-english apk suo-motu-pil-advocates-safety-khc-03-11-2026-kannada)
for s in ${@:-ape apk}; do
  until grep -q "ALL DONE" logs/queue_$s.log 2>/dev/null && (( $(ls downloads/$s/flat/c*.mp4 2>/dev/null | grep -v part | wc -l | tr -d ' ') >= 10 )); do sleep 30; done
  while (( $(pgrep -f "post_course.sh " | wc -l | tr -d ' ') >= 2 )); do sleep 20; done
  echo "$(date +%H:%M:%S) $s post start"
  if [ $s = apk ]; then export CAP_FONT="Kannada Sangam MN" QA_LANG=kn; else unset CAP_FONT QA_LANG; fi
  V_LAYOUT=judgment NO_DELIVER=1 OVERLAY_WORKERS=1 zsh split/post_course.sh $s ${STEM[$s]} > logs/post_$s.log 2>&1 || { echo "$(date +%H:%M:%S) $s POST FAILED"; continue; }
  python3 split/thumb_darkfoot.py out/$s/thumb_brand.json > logs/thumb_$s.log 2>&1
  zsh split/finish_judgment_reel.sh $s qa > logs/qa_$s.log 2>&1 || echo "$(date +%H:%M:%S) $s QA exit $?"
  zsh split/finish_judgment_reel.sh $s ship ${SLUG[$s]} ${STEM[$s]} > logs/ship_$s.log 2>&1 && echo "$(date +%H:%M:%S) $s SHIPPED" || echo "$(date +%H:%M:%S) $s SHIP FAILED"
done
