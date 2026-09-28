#!/bin/zsh
# After the k03 test: for k01, k02, k04 try each wording variant in order until one renders (policy refusals cost nothing).
cd "/Users/admin/Downloads/New short/product-explainer"
while pgrep -f "run_kn_queue.sh|run_k03_test.sh" >/dev/null; do sleep 5; done
UD="/Users/admin/Downloads/New short/Google Flow AI Video/user_data"
TSX="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/node_modules/.bin/tsx"; PIPE="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/services/reel-service/pipeline/index.ts"
export FLOW_USER_DATA_DIR="$UD" FLOW_ASSETS_DIR="/Users/admin/Downloads/New short/Google Flow AI Video/assets" FLOW_LOGS_DIR="/Users/admin/Downloads/New short/product-explainer/logs/flow"
waitfree() { sleep 6; for i in {1..20}; do ls "$UD" | grep -qi singleton || return 0; sleep 5; done; }
for cid in k01 k02 k04; do
  for v in 0 1 2; do
    cfg=kannada/${cid}_v${v}.json; [ -f $cfg ] || continue
    [ -f downloads/kn/$cid.mp4 ] && { echo "[retry] $cid already rendered"; break; }
    waitfree; echo "[retry] $cid variant $v start $(date '+%H:%M:%S')"
    "$TSX" "$PIPE" --config $cfg --no-merge --timeout 240000 > logs/kn_${cid}_v${v}.log 2>&1; echo "[retry] $cid variant $v exit $? $(date '+%H:%M:%S')"
    grep -q "Policy Filter Triggered" logs/kn_${cid}_v${v}.log && echo "[retry] $cid variant $v REFUSED by policy" 
    [ -f downloads/kn/$cid.mp4 ] && { echo "[retry] $cid rendered with variant $v"; echo $v > downloads/kn/$cid.variant; break; }
  done
done
echo "[retry] DONE $(date '+%H:%M:%S')"
