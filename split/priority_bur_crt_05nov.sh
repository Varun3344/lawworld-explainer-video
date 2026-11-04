#!/bin/zsh
# 05-11-2026 00:15: priority over batch 2 (logs/b2_hold): bur re-post (c04 re-take, the date fix) and crt (last batch-1 reel). Then release batch 2.
cd "/Users/admin/Downloads/New short/product-explainer"; export PATH=/usr/local/bin:$PATH
heavy() { echo $(( $(pgrep -f "post_course.sh " | wc -l | tr -d ' ') + $(pgrep -f "build_vertical_course.py [a-z0-9]+ final" | wc -l | tr -d ' ') )); }
for s in bur crt; do
  while (( $(heavy) >= 3 )); do sleep 30; done
  echo "$(date +%H:%M:%S) $s post start (priority)"; zsh split/post_one_04nov.sh $s >> logs/priority_05nov.log 2>&1 &
  sleep 60
done
rm -f logs/b2_hold; echo "$(date +%H:%M:%S) batch 2 released"
wait; echo "$(date +%H:%M:%S) PRIORITY DONE"
