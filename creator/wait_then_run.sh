#!/bin/zsh
# Start the creator clips only when the reel service has no running job and the Flow profile is free.
cd "/Users/admin/Downloads/New short/product-explainer"
KEY=$(grep -E '^REEL_PIPELINE_API_KEY=' '/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/.env' | cut -d= -f2- | tr -d '"')
UD="/Users/admin/Downloads/New short/Google Flow AI Video/user_data"
while true; do
  running=$(curl -s -m 8 -H "x-api-key: $KEY" "http://localhost:4600/jobs?status=running" | python3 -c "import sys,json; print(len(json.load(sys.stdin)['data']['jobs']))" 2>/dev/null || echo 1)
  busy=$(curl -s -m 5 http://localhost:4600/health | python3 -c "import sys,json; print(json.load(sys.stdin)['data']['flow']['busy'])" 2>/dev/null || echo True)
  locked=$(ls "$UD" | grep -ci singleton)
  echo "[wait] $(date '+%H:%M:%S') running_jobs=$running busy=$busy profile_locked=$locked"
  [ "$busy" != "True" ] && [ "$locked" = "0" ] && break   # a job parked at review still counts as running, so gate on the browser only
  sleep 10
done
sleep 3; echo "[wait] reel service idle — starting creator clips $(date '+%H:%M:%S')"
./creator/run_creator_queue.sh
