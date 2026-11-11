#!/bin/zsh
# 10-11-2026: inj c29 rendered 3x in Flow but the download step failed each time (menu mis-click + 302 on the stream URL).
# Zero-credit recovery from the inj 8s project once the inj queue has released the BeatAI profile.
cd "/Users/admin/Downloads/New short/product-explainer"; export PATH=/usr/local/bin:$PATH
until grep -q "ALL DONE" logs/queue_inj.log; do sleep 30; done; sleep 45
source split/inj_env.sh
UD="$SPLIT_UD"
TSX="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/node_modules/.bin/tsx"; PIPE="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/services/reel-service/pipeline/index.ts"
export FLOW_USER_DATA_DIR="$UD" FLOW_ASSETS_DIR="/Users/admin/Downloads/New short/Google Flow AI Video/assets" FLOW_LOGS_DIR="$PWD/logs/flow"
URL=$(python3 -c "import json;print(json.load(open('split/inj_8s.json'))['flowProjectUrl'])")
echo "$(date +%H:%M:%S) recover inj 8s $URL"
"$TSX" "$PIPE" --config split/inj_8s.json --recover "$URL" --no-merge --timeout 240000 > logs/recover_inj8.log 2>&1
echo "$(date +%H:%M:%S) recover exit $? -> $(ls downloads/inj/recovered/*/ 2>/dev/null | wc -l | tr -d ' ') files"
