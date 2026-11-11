#!/bin/zsh
# 10-Nov concept videos, after fir was delivered (15:46): inj is complete (c29 recovered), qsh still waits for c32 - so inj first, then qsh.
cd "/Users/admin/Downloads/New short/product-explainer"
for pair in "inj LawWorld_Temporary_Injunctions_Order_39_CPC" "qsh LawWorld_Quashing_under_Section_528_BNSS"; do
  s=${pair%% *}; stem=${pair#* }
  until [ -f split/CUESOK_$s ]; do sleep 60; done
  echo "[chain] $(date +%H:%M:%S) start $s" >> logs/post_chain_10nov.log; zsh split/post_course.sh $s $stem > logs/post_$s.log 2>&1; echo "[chain] $(date +%H:%M:%S) $s exit $?" >> logs/post_chain_10nov.log
done
