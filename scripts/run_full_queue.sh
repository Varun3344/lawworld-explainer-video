#!/bin/zsh
# Sequential Flow generation for the full video: 10 s clips -> 8 s clips -> 6 s clip -> 3D B-roll. One browser at a time.
cd "/Users/admin/Downloads/New short/product-explainer"
UD="/Users/admin/Downloads/New short/Google Flow AI Video/user_data"
TSX="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/node_modules/.bin/tsx"
PIPE="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/services/reel-service/pipeline/index.ts"
export FLOW_USER_DATA_DIR="$UD" FLOW_ASSETS_DIR="/Users/admin/Downloads/New short/Google Flow AI Video/assets" FLOW_LOGS_DIR="/Users/admin/Downloads/New short/product-explainer/logs/flow"
waitfree() { sleep 6; for i in {1..20}; do ls "$UD" | grep -qi singleton || return 0; sleep 5; done; }
run() { echo "[queue] === $1 start $(date '+%H:%M:%S') ==="; "$TSX" "$PIPE" --config "$1" "${@:2}" --no-merge; echo "[queue] === $1 exit $? $(date '+%H:%M:%S') ==="; waitfree; }
run storyboards/full_presenter_10s.json
run storyboards/full_presenter_8s.json
run storyboards/full_presenter_6s.json
[ -f storyboards/full_broll3d.json ] && run storyboards/full_broll3d.json --broll --timeout 300000
echo "[queue] ALL DONE $(date '+%H:%M:%S')"
