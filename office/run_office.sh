#!/bin/zsh
cd "/Users/admin/Downloads/New short/product-explainer"
UD="/Users/admin/Downloads/New short/Google Flow AI Video/user_data"
TSX="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/node_modules/.bin/tsx"; PIPE="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/services/reel-service/pipeline/index.ts"
export FLOW_USER_DATA_DIR="$UD" FLOW_ASSETS_DIR="/Users/admin/Downloads/New short/Google Flow AI Video/assets" FLOW_LOGS_DIR="$PWD/logs/flow"
KEY=$(grep -E '^REEL_PIPELINE_API_KEY=' '/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/.env' | cut -d= -f2- | tr -d '"')
free() { while true; do r=$(curl -s -m 8 -H "x-api-key: $KEY" "http://localhost:4600/jobs?status=running" | python3 -c "import sys,json; print(len(json.load(sys.stdin)['data']['jobs']))" 2>/dev/null || echo 1); pgrep -f "user-data-dir=$UD" >/dev/null && o=1 || o=0; [ "$r" = "0" ] && [ "$o" = "0" ] && break; sleep 10; done; sleep 4; ls "$UD" | grep -qi singleton && rm -f "$UD"/Singleton*; }
for sb in office/office_10s.json office/office_8s.json office/office_6s.json; do free; echo "[office] $sb start $(date +%H:%M:%S)"; "$TSX" "$PIPE" --config $sb --no-merge --timeout 240000; echo "[office] $sb exit $? $(date +%H:%M:%S)"; done
echo "== check =="; for c in downloads/office/o*.mp4; do python3 scripts/words.py office/office_all_scenes.json $c | tail -1; done
echo "[office] DONE $(date +%H:%M:%S)"
