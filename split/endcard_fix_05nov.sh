#!/bin/zsh
# 05-11-2026: end-card line was clipped (crs nib tcn gft drv awg): frames re-rendered for the end card only; now 9:16 final + qa + ship.
cd "/Users/admin/Downloads/New short/product-explainer"; export PATH=/usr/local/bin:$PATH
heavy() { echo $(( $(pgrep -f "post_course.sh " | wc -l | tr -d ' ') + $(pgrep -f "build_vertical_course.py [a-z0-9]+ final" | wc -l | tr -d ' ') )); }
fix() { local s=$1 stem=$(awk -F'\t' -v k=$1 '$1==k{print $2}' split/batch2_04nov.tsv) slug=$(awk -F'\t' -v k=$1 '$1==k{print $3}' split/batch2_04nov.tsv)
  echo "$(date +%H:%M:%S) $s final start"
  V_LAYOUT=judgment python3 split/build_vertical_course.py $s final > logs/endfix_$s.log 2>&1 || { echo "$(date +%H:%M:%S) $s FINAL FAILED"; return 1; }
  zsh split/finish_judgment_reel.sh $s qa > logs/qa_$s.log 2>&1
  zsh split/finish_judgment_reel.sh $s ship $slug $stem > logs/ship_$s.log 2>&1 && echo "$(date +%H:%M:%S) $s RESHIPPED" || echo "$(date +%H:%M:%S) $s RESHIP FAILED"
}
for s in crs nib tcn gft drv awg; do
  while (( $(heavy) >= 4 )); do sleep 20; done
  fix $s &
  sleep 30
done
wait; echo "$(date +%H:%M:%S) ENDCARD FIX DONE"
