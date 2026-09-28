#!/bin/zsh
cd "/Users/admin/Downloads/New short/product-explainer"
while pgrep -f run_kn_queue.sh >/dev/null; do sleep 5; done
UD="/Users/admin/Downloads/New short/Google Flow AI Video/user_data"; sleep 6; for i in {1..20}; do ls "$UD" | grep -qi singleton || break; sleep 5; done
TSX="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/node_modules/.bin/tsx"; PIPE="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/services/reel-service/pipeline/index.ts"
export FLOW_USER_DATA_DIR="$UD" FLOW_ASSETS_DIR="/Users/admin/Downloads/New short/Google Flow AI Video/assets" FLOW_LOGS_DIR="/Users/admin/Downloads/New short/product-explainer/logs/flow"
echo "[k03] start $(date '+%H:%M:%S')"; "$TSX" "$PIPE" --config kannada/kn_test_k03.json --no-merge --timeout 300000; echo "[k03] exit $? $(date '+%H:%M:%S')"
