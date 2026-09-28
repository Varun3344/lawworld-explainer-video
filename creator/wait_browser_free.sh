#!/bin/zsh
# Start the creator clips when no Chrome holds the main Flow profile (the reel's compose stage may open Flow briefly for a cover).
cd "/Users/admin/Downloads/New short/product-explainer"
UD="/Users/admin/Downloads/New short/Google Flow AI Video/user_data"
while true; do
  pgrep -f "user-data-dir=$UD" >/dev/null && open=1 || open=0
  locked=$(ls "$UD" | grep -ci singleton)
  echo "[wait] $(date '+%H:%M:%S') chrome_open=$open locked=$locked"
  [ "$open" = "0" ] && [ "$locked" = "0" ] && break
  sleep 10
done
sleep 5; echo "[wait] browser free — starting creator clips $(date '+%H:%M:%S')"
./creator/run_creator_queue.sh
