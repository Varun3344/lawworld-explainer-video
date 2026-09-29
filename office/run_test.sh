#!/bin/zsh
cd "/Users/admin/Downloads/New short/product-explainer"
KEY=$(grep -E '^REEL_PIPELINE_API_KEY=' '/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/.env' | cut -d= -f2- | tr -d '"')
UD="/Users/admin/Downloads/New short/Google Flow AI Video/user_data"
while true; do
  r=$(curl -s -m 8 -H "x-api-key: $KEY" "http://localhost:4600/jobs?status=running" | python3 -c "import sys,json; print(len(json.load(sys.stdin)['data']['jobs']))" 2>/dev/null || echo 1)
  pgrep -f "user-data-dir=$UD" >/dev/null && o=1 || o=0
  [ "$r" = "0" ] && [ "$o" = "0" ] && break; sleep 10
done
sleep 5; ls "$UD" | grep -qi singleton && ! pgrep -f "user-data-dir=$UD" >/dev/null && rm -f "$UD"/Singleton*
echo "[test] start $(date +%H:%M:%S)"
TSX="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/node_modules/.bin/tsx"; PIPE="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/services/reel-service/pipeline/index.ts"
FLOW_USER_DATA_DIR="$UD" FLOW_ASSETS_DIR="/Users/admin/Downloads/New short/Google Flow AI Video/assets" FLOW_LOGS_DIR="$PWD/logs/flow" "$TSX" "$PIPE" --config office/test_o01.json --no-merge --timeout 240000
echo "[test] exit $? $(date +%H:%M:%S)"
