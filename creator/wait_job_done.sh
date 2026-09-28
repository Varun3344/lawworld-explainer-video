#!/bin/zsh
cd "/Users/admin/Downloads/New short/product-explainer"
KEY=$(grep -E '^REEL_PIPELINE_API_KEY=' '/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/.env' | cut -d= -f2- | tr -d '"')
UD="/Users/admin/Downloads/New short/Google Flow AI Video/user_data"
while true; do
  running=$(curl -s -m 8 -H "x-api-key: $KEY" "http://localhost:4600/jobs?status=running" | python3 -c "import sys,json; print(len(json.load(sys.stdin)['data']['jobs']))" 2>/dev/null || echo 1)
  pgrep -f "user-data-dir=$UD" >/dev/null && open=1 || open=0
  echo "[wait] $(date '+%H:%M:%S') running_jobs=$running chrome_open=$open"
  [ "$running" = "0" ] && [ "$open" = "0" ] && break
  sleep 10
done
sleep 5; echo "[wait] reel job finished, browser free — starting creator clips $(date '+%H:%M:%S')"
./creator/run_creator_queue.sh
