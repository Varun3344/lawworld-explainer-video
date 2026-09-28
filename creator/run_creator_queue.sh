#!/bin/zsh
cd "/Users/admin/Downloads/New short/product-explainer"
UD="/Users/admin/Downloads/New short/Google Flow AI Video/user_data"
TSX="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/node_modules/.bin/tsx"; PIPE="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/services/reel-service/pipeline/index.ts"
export FLOW_USER_DATA_DIR="$UD" FLOW_ASSETS_DIR="/Users/admin/Downloads/New short/Google Flow AI Video/assets" FLOW_LOGS_DIR="/Users/admin/Downloads/New short/product-explainer/logs/flow"
for round in 1 2; do
  echo "[creator] round $round $(date '+%H:%M:%S')"; "$TSX" "$PIPE" --config creator/creator_presenter.json --no-merge --timeout 240000; echo "[creator] exit $? $(date '+%H:%M:%S')"
  sleep 6; for i in {1..20}; do ls "$UD" | grep -qi singleton || break; sleep 5; done
  bad=(); for c in downloads/creator/h*.mp4; do id=$(basename $c .mp4); line=$(python3 scripts/words.py creator/creator_all_scenes.json $c 2>&1 | tail -1); echo "  $line"; echo "$line" | grep -q CHECK && bad+=($id); done
  for id in h01 h02 h03 h04 h05; do [ -f downloads/creator/$id.mp4 ] || bad+=($id); done
  [ ${#bad} -eq 0 ] && { echo "[creator] all 5 verbatim"; break; }
  echo "[creator] retaking: $bad"; mkdir -p downloads/creator/rejected; for id in $bad; do for f in downloads/creator/$id.mp4 downloads/creator/$id.words.json; do [ -f $f ] && mv $f downloads/creator/rejected/r${round}_$(basename $f); done; done
done
echo "[creator] DONE $(date '+%H:%M:%S')"
