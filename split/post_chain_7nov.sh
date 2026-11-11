#!/bin/zsh
# 7-Nov concept videos: post-production one set at a time, each only after its cues were reviewed (split/CUESOK_<set>).
cd "/Users/admin/Downloads/New short/product-explainer"
for pair in "bnb LawWorld_Bailable_and_NonBailable_Offences" "chq LawWorld_Cheque_Dishonour_Law_and_Timelines" "csr LawWorld_Charge_Sheets_and_Closure_Reports"; do
  s=${pair%% *}; stem=${pair#* }
  until [ -f split/CUESOK_$s ]; do sleep 60; done
  echo "[chain] $(date +%H:%M:%S) start $s"; zsh split/post_course.sh $s $stem > logs/post_$s.log 2>&1; echo "[chain] $(date +%H:%M:%S) $s exit $?"
done
