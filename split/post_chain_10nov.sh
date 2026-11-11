#!/bin/zsh
# 10-Nov concept videos (owner "make 2-3 concept videos"): post-production one set at a time, each only after its cues were reviewed (split/CUESOK_<set>).
cd "/Users/admin/Downloads/New short/product-explainer"
for pair in "fir LawWorld_FIR_Zero_FIR_and_eFIR" "qsh LawWorld_Quashing_under_Section_528_BNSS" "inj LawWorld_Temporary_Injunctions_Order_39_CPC"; do
  s=${pair%% *}; stem=${pair#* }
  until [ -f split/CUESOK_$s ]; do sleep 60; done
  echo "[chain] $(date +%H:%M:%S) start $s" >> logs/post_chain_10nov.log; zsh split/post_course.sh $s $stem > logs/post_$s.log 2>&1; echo "[chain] $(date +%H:%M:%S) $s exit $?" >> logs/post_chain_10nov.log
done
