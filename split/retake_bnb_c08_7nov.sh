#!/bin/zsh
# 07-11 22:20: bnb c08 says "Section one five one fifteen" (heard 15115; the words check tolerates digit forms). Re-take until
# the number scan is clean (<= 3 rounds), re-flatten it, then run bnb post-production after the chq/csr chain.
cd "/Users/admin/Downloads/New short/product-explainer"
source split/bnb_env.sh
NS=/private/tmp/claude-501/-Users-admin-Downloads-New-short/07a60ea5-ec1b-45a8-81e7-227b19aba488/scratchpad/yt7nov/numscan.py
D=downloads/bnb
for round in 1 2 3; do
  if [ -f $D/c08.mp4 ]; then
    if python3 $NS bnb | grep -q "^bnb c08:"; then
      mv $D/c08.mp4 $D/rejected/c08_stumble_r$round.mp4; mv $D/c08.words.json $D/rejected/c08_stumble_r$round.words.json
      echo "[retake] $(date +%H:%M:%S) c08 set aside (round $round)"
    else echo "[retake] $(date +%H:%M:%S) c08 number scan clean"; break; fi
  fi
  zsh split/run_queue.sh c08 >> logs/queue_bnb.log 2>&1
  tail -3 logs/queue_bnb.log | sed "s/^/[retake] /"
done
python3 $NS bnb | grep -q "^bnb c08:" && { echo "[retake] $(date +%H:%M:%S) c08 STILL stumbles after 3 rounds - check by hand"; exit 1; }
python3 -c "import json,sys; sys.exit(0 if json.load(open('$D/c08.words.json')).get('keep') else 1)" || { echo "[retake] c08 not kept - check by hand"; exit 1; }
echo "[retake] $(date +%H:%M:%S) flatten c08"; zsh split/flatten_all.sh bnb
while pgrep -f post_chain_7nov_b.sh >/dev/null; do sleep 60; done
echo "[chain] $(date +%H:%M:%S) start bnb (pass 3, c08 re-take)" >> logs/post_chain_7nov.log
zsh split/post_course.sh bnb LawWorld_Bailable_and_NonBailable_Offences > logs/post_bnb.log 2>&1; rc=$?
echo "[chain] $(date +%H:%M:%S) bnb exit $rc" >> logs/post_chain_7nov.log
