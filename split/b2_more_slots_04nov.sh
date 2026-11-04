#!/bin/zsh
# 04-11-2026: when every Flow queue of the night is done, let batch 2 run 3 post-productions at once (renders no longer use the CPU).
cd "/Users/admin/Downloads/New short/product-explainer"
until ! pgrep -f "run_queue.sh|chain_after.sh|chain_bur_c04" >/dev/null; do sleep 60; done
echo 3 > logs/b2_maxposts; echo "$(date +%H:%M:%S) Flow queues done -> 3 post slots"
