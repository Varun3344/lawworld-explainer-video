#!/bin/zsh
cd "/Users/admin/Downloads/New short/product-explainer"
UD="/Users/admin/Downloads/New short/Google Flow AI Video/user_data"
idle=0; while [ $idle -lt 90 ]; do if pgrep -f "user-data-dir=$UD" >/dev/null; then idle=0; else idle=$((idle+10)); fi; sleep 10; done
ls "$UD" | grep -qi singleton && rm -f "$UD"/Singleton*
echo "[office] o17 start $(date +%H:%M:%S)"
TSX="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/node_modules/.bin/tsx"; PIPE="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/services/reel-service/pipeline/index.ts"
FLOW_USER_DATA_DIR="$UD" FLOW_ASSETS_DIR="/Users/admin/Downloads/New short/Google Flow AI Video/assets" FLOW_LOGS_DIR="$PWD/logs/flow" "$TSX" "$PIPE" --config office/office_6s.json --no-merge --timeout 240000
python3 scripts/words.py office/office_all_scenes.json downloads/office/o17.mp4 | tail -1
echo "[office] DONE $(date +%H:%M:%S)"
