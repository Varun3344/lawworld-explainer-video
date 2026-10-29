#!/bin/zsh
# If <set> <clip> take 2 is REJECTED again, kill that set's queue before take 3, restore take 1 (verified correct by hand), restart the queue.
# usage: zsh split/restore_numeric_take.sh <set> <clip> <queue_pid>
S=$1; C=$2; QP=$3; cd "/Users/admin/Downloads/New short/product-explainer"
tail -n 0 -F logs/queue_$S.log | while read -r line; do
  case "$line" in
    *"$C: OK"*|*"[kn] $C: OK"*) echo "$(date +%H:%M:%S) $S $C take 2 OK - nothing to do"; break;;
    *"$C take 2 REJECTED"*)
      kill $QP 2>/dev/null; sleep 2
      [ -f downloads/$S/$C.mp4 ] && mv downloads/$S/$C.mp4 downloads/$S/rejected/${C}_take2b.mp4
      cp downloads/$S/rejected/${C}_take1.mp4 downloads/$S/$C.mp4
      python3 -c "import json; d=json.load(open('downloads/$S/rejected/${C}_take1.words.json')); d['keep']=True; d['manual']='take 1 verified by gpt-4o-transcribe 29-10: digits-only mismatch'; json.dump(d,open('downloads/$S/$C.words.json','w'),ensure_ascii=False,indent=1)"
      rm -f downloads/$S/frames/${C}_last.jpg
      ffmpeg -v error -y -sseof -0.05 -i downloads/$S/$C.mp4 -frames:v 1 downloads/$S/frames/${C}_last.jpg
      echo "$(date +%H:%M:%S) restored $S $C take 1; restarting queue"
      source split/${S}_env.sh; nohup zsh split/run_queue.sh $(python3 -c "import json; ids=[s['sceneId'] for s in json.load(open('split/${S}_all_scenes.json'))['scenes']]; print(' '.join(ids[ids.index('$C'):]))") >> logs/queue_$S.log 2>&1 &
      break;;
  esac
done
