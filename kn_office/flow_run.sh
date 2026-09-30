#!/bin/zsh
# usage: flow_run.sh <storyboard.json> [extra pipeline args]   — waits for the reel service and the Flow browser to be idle first
cd "/Users/admin/Downloads/New short/product-explainer"
UD="/Users/admin/Downloads/New short/Google Flow AI Video/user_data"
KEY=$(grep -E '^REEL_PIPELINE_API_KEY=' '/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/.env' | cut -d= -f2- | tr -d '"')
idle=0
while [ $idle -lt 40 ]; do
  r=$(curl -s -m 8 -H "x-api-key: $KEY" "http://localhost:4600/jobs?status=running" | python3 -c "
import sys,json
js=json.load(sys.stdin)['data']['jobs']; print(sum(1 for j in js for s in j['stages'] if s['status']=='running' and s['name'] in ('broll','story','intro')))" 2>/dev/null || echo 1)
  if pgrep -f "user-data-dir=$UD" >/dev/null || [ "$r" != "0" ]; then idle=0; else idle=$((idle+10)); fi
  sleep 10
done
ls "$UD" | grep -qi singleton && ! pgrep -f "user-data-dir=$UD" >/dev/null && rm -f "$UD"/Singleton*
TSX="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/node_modules/.bin/tsx"; PIPE="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/services/reel-service/pipeline/index.ts"
echo "[flow] $1 start $(date +%H:%M:%S)"
FLOW_USER_DATA_DIR="$UD" FLOW_ASSETS_DIR="/Users/admin/Downloads/New short/Google Flow AI Video/assets" FLOW_LOGS_DIR="$PWD/logs/flow" "$TSX" "$PIPE" --config "$1" --no-merge --timeout 240000 "${@:2}"
echo "[flow] $1 exit $? $(date +%H:%M:%S)"
