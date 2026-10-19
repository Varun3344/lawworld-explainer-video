#!/bin/zsh
# Start the next course set's Flow queue on an account once the previous queue on that account has finished.
# Usage: zsh split/chain_queue.sh <wait_for_queue_log> <next_set> [extra ids of the previous set to render first ...]
# e.g. zsh split/chain_queue.sh logs/apl_queue.log cus apl:c55 apl:c56
cd "/Users/admin/Downloads/New short/product-explainer"
WAIT=$1; NEXT=$2; shift 2
until grep -q "ALL DONE" "$WAIT" 2>/dev/null; do sleep 30; done
echo "[chain] $(date +%H:%M:%S) $WAIT finished"
for x in "$@"; do                                   # leftovers of the previous set (clips added after its queue started)
  s=${x%%:*}; id=${x#*:}
  ( source split/${s}_env.sh && zsh split/run_queue.sh $id ) >> logs/${s}_queue_extra.log 2>&1
done
source split/${NEXT}_env.sh
IDS=$(python3 -c "import json; print(' '.join(s['sceneId'] for s in json.load(open('split/${NEXT}_all_scenes.json'))['scenes']))")
echo "[chain] $(date +%H:%M:%S) starting $NEXT: $(echo $IDS | wc -w) clips"
zsh split/run_queue.sh ${=IDS} > logs/${NEXT}_queue.log 2>&1
echo "[chain] $(date +%H:%M:%S) $NEXT done"
