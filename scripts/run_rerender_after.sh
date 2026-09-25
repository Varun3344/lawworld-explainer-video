#!/bin/zsh
# Wait for the B-roll run to exit, then re-render one presenter scene (bad take already moved aside).
SCENE=$1
UD="/Users/admin/Downloads/New short/Google Flow AI Video/user_data"
while pgrep -f "sample_broll3d.json --broll" >/dev/null; do sleep 5; done
sleep 8
for i in {1..12}; do ls "$UD" | grep -qi singleton || break; sleep 5; done
cd "/Users/admin/Downloads/New short/product-explainer"
TSX="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/node_modules/.bin/tsx"
PIPE="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/services/reel-service/pipeline/index.ts"
echo "[rerender] starting $SCENE at $(date)"
FLOW_USER_DATA_DIR="$UD" FLOW_ASSETS_DIR="/Users/admin/Downloads/New short/Google Flow AI Video/assets" FLOW_LOGS_DIR="/Users/admin/Downloads/New short/product-explainer/logs/flow" \
  "$TSX" "$PIPE" --config "/Users/admin/Downloads/New short/product-explainer/storyboards/sample_presenter.json" --scene $SCENE --no-merge
echo "[rerender] exited with $? at $(date)"
