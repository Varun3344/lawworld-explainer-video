#!/bin/zsh
# 02-11-2026 set 2: pbs renders on the main account once shs's queue there is ALL DONE (never two queues on one profile).
cd "/Users/admin/Downloads/New short/product-explainer"; export PATH=/usr/local/bin:$PATH
until grep -q "ALL DONE" logs/queue_shs.log 2>/dev/null; do sleep 20; done
source split/pbs_env.sh; zsh split/run_queue.sh c01 c02 c03 c04 c05 c06 c07 c08 c09 c10 > logs/queue_pbs.log 2>&1
