#!/bin/zsh
cd "/Users/admin/Downloads/New short/product-explainer"
UD="/Users/admin/Downloads/New short/Google Flow AI Video/user_data"
TSX="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/node_modules/.bin/tsx"
PIPE="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/services/reel-service/pipeline/index.ts"
export FLOW_USER_DATA_DIR="$UD" FLOW_ASSETS_DIR="/Users/admin/Downloads/New short/Google Flow AI Video/assets" FLOW_LOGS_DIR="/Users/admin/Downloads/New short/product-explainer/logs/flow"
waitfree() { sleep 6; for i in {1..20}; do ls "$UD" | grep -qi singleton || return 0; sleep 5; done; }
mkdir -p downloads/full/rejected; for f in downloads/full/c02.mp4 downloads/full/c02.words.json; do [ -f $f ] && mv $f downloads/full/rejected/silent_$(basename $f); done
echo "[s2] c02 retake start $(date '+%H:%M:%S')"; "$TSX" "$PIPE" --config storyboards/full_presenter_10s.json --scene c02 --no-merge; echo "[s2] c02 exit $? $(date '+%H:%M:%S')"; waitfree
echo "[s2] broll start $(date '+%H:%M:%S')"; "$TSX" "$PIPE" --config storyboards/sample2_broll3d.json --broll --no-merge --timeout 300000; echo "[s2] broll exit $? $(date '+%H:%M:%S')"
echo "[s2] DONE $(date '+%H:%M:%S')"
