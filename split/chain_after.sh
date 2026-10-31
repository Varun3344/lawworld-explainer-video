#!/bin/zsh
# Start <set>'s Flow queue once <prev>'s queue on the same account says ALL DONE (31-10-2026 rounds). Usage: zsh split/chain_after.sh <prev> <set>
cd "/Users/admin/Downloads/New short/product-explainer"
until grep -q "ALL DONE" logs/queue_$1.log 2>/dev/null; do sleep 30; done
echo "[chain] $1 done, starting $2 $(date +%H:%M:%S)"
source split/$2_env.sh; python3 split/make_course_sb.py $2 --new-project; touch split/GO$2
zsh split/run_queue.sh c01 c02 c03 c04 c05 c06 c07 c08 c09 c10
