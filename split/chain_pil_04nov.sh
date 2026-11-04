#!/bin/zsh
# 04-11-2026: account a3 freed for the owner's suo motu PIL reels (ape English, apk Kannada), then back to bur (ptn's chain_after follows bur).
cd "/Users/admin/Downloads/New short/product-explainer"; export PATH=/usr/local/bin:$PATH
for s in ape apk bur; do
  echo "[chain] starting $s $(date +%H:%M:%S)"
  ( source split/${s}_env.sh; python3 split/make_course_sb.py $s --new-project > logs/sb_$s.log 2>&1; touch split/GO$s; mkdir -p downloads/$s
    zsh split/run_queue.sh c01 c02 c03 c04 c05 c06 c07 c08 c09 c10 > logs/queue_$s.log 2>&1 )
  echo "[chain] $s done $(date +%H:%M:%S)"
done
