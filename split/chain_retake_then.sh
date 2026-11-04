#!/bin/zsh
# chain_retake_then.sh <set> <clip> <next_set>: when <set>'s queue says ALL DONE, re-render <clip> on the same account, then start <next_set>'s queue
# (like chain_after.sh). Keeps one queue per Flow profile at a time. 04-11-2026 (mhr c01: avatar inserted a Hindi "ki").
cd "/Users/admin/Downloads/New short/product-explainer"; export PATH=/usr/local/bin:$PATH
SET=$1; CLIP=$2; NEXT=$3
until grep -q "ALL DONE" logs/queue_$SET.log 2>/dev/null; do sleep 30; done
echo "[chain] $SET done, re-taking $SET $CLIP $(date +%H:%M:%S)"
( source split/${SET}_env.sh && zsh split/run_queue.sh $CLIP ) >> logs/queue_${SET}_retake.log 2>&1
grep -E "words\] $CLIP" logs/queue_${SET}_retake.log | tail -1
echo "[chain] starting $NEXT $(date +%H:%M:%S)"
source split/${NEXT}_env.sh; python3 split/make_course_sb.py $NEXT --new-project; touch split/GO$NEXT
zsh split/run_queue.sh c01 c02 c03 c04 c05 c06 c07 c08 c09 c10
