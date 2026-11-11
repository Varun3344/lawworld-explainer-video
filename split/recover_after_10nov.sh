#!/bin/zsh
# 10-11-2026: zero-credit recovery of clips that rendered in Flow but failed to download (3 takes each).
# Waits until the set's queue has finished (its Flow profile is free), then downloads every clip of the <set>_<d>s project.
# usage: zsh split/recover_after_10nov.sh <set> <seconds 6|8|10>
cd "/Users/admin/Downloads/New short/product-explainer"; export PATH=/usr/local/bin:$PATH
s=$1; d=$2
until grep -q "ALL DONE" logs/queue_$s.log; do sleep 30; done; sleep 45
source split/${s}_env.sh
TSX="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/node_modules/.bin/tsx"; PIPE="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/services/reel-service/pipeline/index.ts"
export FLOW_USER_DATA_DIR="$SPLIT_UD" FLOW_ASSETS_DIR="/Users/admin/Downloads/New short/Google Flow AI Video/assets" FLOW_LOGS_DIR="$PWD/logs/flow"
URL=$(python3 -c "import json;print(json.load(open('split/${s}_${d}s.json'))['flowProjectUrl'])")
echo "$(date +%H:%M:%S) recover $s ${d}s $URL"
"$TSX" "$PIPE" --config split/${s}_${d}s.json --recover "$URL" --no-merge --timeout 240000 > logs/recover_${s}${d}.log 2>&1
echo "$(date +%H:%M:%S) recover exit $? -> $(ls downloads/$s/recovered/*/ 2>/dev/null | wc -l | tr -d ' ') files"
