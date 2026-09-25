#!/bin/zsh
# Wait for the presenter run to exit, make sure the profile is free, then generate the two 3D cut-away clips.
PID=$1
while kill -0 $PID 2>/dev/null; do sleep 5; done
sleep 8
UD="/Users/admin/Downloads/New short/Google Flow AI Video/user_data"
for i in {1..12}; do ls "$UD" | grep -qi singleton || break; sleep 5; done
cd "/Users/admin/Downloads/New short/product-explainer"
TSX="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/node_modules/.bin/tsx"
PIPE="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/services/reel-service/pipeline/index.ts"
echo "[broll-after] presenter run exited; starting 3D B-roll at $(date)"
FLOW_USER_DATA_DIR="$UD" FLOW_ASSETS_DIR="/Users/admin/Downloads/New short/Google Flow AI Video/assets" FLOW_LOGS_DIR="/Users/admin/Downloads/New short/product-explainer/logs/flow" \
  "$TSX" "$PIPE" --config "/Users/admin/Downloads/New short/product-explainer/storyboards/sample_broll3d.json" --broll --no-merge --timeout 300000
echo "[broll-after] B-roll run exited with $? at $(date)"
