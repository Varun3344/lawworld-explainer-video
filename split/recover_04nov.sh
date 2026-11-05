#!/bin/zsh
# 05-11-2026: zero-credit recovery of rendered-but-not-downloaded clips (Flow download path failed): --recover <project URL>.
# usage: zsh split/recover_04nov.sh <set>   (one at a time per Flow account)
cd "/Users/admin/Downloads/New short/product-explainer"; export PATH=/usr/local/bin:$PATH
s=$1; source split/${s}_env.sh
UD="${SPLIT_UD:-/Users/admin/Downloads/New short/Google Flow AI Video/user_data}"
TSX="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/node_modules/.bin/tsx"; PIPE="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/services/reel-service/pipeline/index.ts"
export FLOW_USER_DATA_DIR="$UD" FLOW_ASSETS_DIR="/Users/admin/Downloads/New short/Google Flow AI Video/assets" FLOW_LOGS_DIR="$PWD/logs/flow"
URL=$(python3 -c "import json;print(json.load(open('split/${s}_10s.json'))['flowProjectUrl'])")
echo "$(date +%H:%M:%S) recover $s $URL"
"$TSX" "$PIPE" --config split/${s}_10s.json --recover "$URL" --no-merge --timeout 240000 > logs/recover_$s.log 2>&1
echo "$(date +%H:%M:%S) recover $s exit $? -> $(ls downloads/$s/recovered/*/ 2>/dev/null | wc -l | tr -d ' ') files"
