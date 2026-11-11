#!/bin/zsh
# 7-Nov concept videos, second pass after the layout-gate fixes (21:55): post-production one set at a time.
cd "/Users/admin/Downloads/New short/product-explainer"
for pair in "bnb LawWorld_Bailable_and_NonBailable_Offences" "chq LawWorld_Cheque_Dishonour_Law_and_Timelines" "csr LawWorld_Charge_Sheets_and_Closure_Reports"; do
  s=${pair%% *}; stem=${pair#* }
  echo "[chain] $(date +%H:%M:%S) start $s (pass 2)" >> logs/post_chain_7nov.log
  zsh split/post_course.sh $s $stem > logs/post_$s.log 2>&1; rc=$?
  echo "[chain] $(date +%H:%M:%S) $s exit $rc" >> logs/post_chain_7nov.log
done
