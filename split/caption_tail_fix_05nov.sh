#!/bin/zsh
# 05-11-2026: last caption floated 1-3 frames after the presenter left (apk, hgd): captions + final + qa + ship.
cd "/Users/admin/Downloads/New short/product-explainer"; export PATH=/usr/local/bin:$PATH
heavy() { echo $(( $(pgrep -f "post_course.sh " | wc -l | tr -d ' ') + $(pgrep -f "build_vertical_course.py [a-z0-9]+ final" | wc -l | tr -d ' ') )); }
typeset -A STEM SLUG
STEM[apk]=KHC_SuoMotu_PIL_Advocates_safety_03_11_2026_Kannada; SLUG[apk]=suo-motu-pil-advocates-safety-khc-03-11-2026-kannada
STEM[hgd]=KHC_COMAP_446_2026_KSFC_guarantor_heirs_liable_only_to_estate; SLUG[hgd]=sridhara-babu-v-ksfc-2026-khc-59867
for s in apk hgd; do
  while (( $(heavy) >= 4 )); do sleep 20; done
  if [ $s = apk ]; then export CAP_FONT="Kannada Sangam MN" QA_LANG=kn; else unset CAP_FONT QA_LANG; fi
  echo "$(date +%H:%M:%S) $s captions + final"
  ( V_LAYOUT=judgment python3 split/build_vertical_course.py $s captions && V_LAYOUT=judgment python3 split/build_vertical_course.py $s final ) > logs/captail_$s.log 2>&1 || { echo "$(date +%H:%M:%S) $s FAILED"; continue; }
  zsh split/finish_judgment_reel.sh $s qa > logs/qa_$s.log 2>&1
  zsh split/finish_judgment_reel.sh $s ship ${SLUG[$s]} ${STEM[$s]} > logs/ship_$s.log 2>&1 && echo "$(date +%H:%M:%S) $s RESHIPPED" || echo "$(date +%H:%M:%S) $s RESHIP FAILED"
done
echo "$(date +%H:%M:%S) CAPTION TAIL FIX DONE"
