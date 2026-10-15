#!/bin/zsh
# 16:9 split-screen explainer clips (Cause of Action, first minute), one Flow launch per clip on the main account.
# Before every launch: no reel stage that uses Flow is running and the Flow browser has been closed for 30 s (gate from
# kanglish/run_queue.sh). After every clip: English speech check (scripts/words.py). A take far from the script (match < 0.90)
# is set aside and re-rendered (max 3 takes); 0.90-0.97 is kept for a manual listen (versus / 1888 / A B C spellings).
# c01 is the pilot and the anchor of every later clip: the queue stops after it until split/GO exists.
cd "/Users/admin/Downloads/New short/product-explainer"
UD="/Users/admin/Downloads/New short/Google Flow AI Video/user_data"; D=${SPLIT_D:-downloads/split}; SB=${SPLIT_SB:-split/split}; ALLJ=${SPLIT_ALL:-split/split_all_scenes.json}; GOF=${SPLIT_GO:-split/GO}
KEY=$(grep -E '^REEL_PIPELINE_API_KEY=' '/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/.env' | cut -d= -f2- | tr -d '"')
TSX="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/node_modules/.bin/tsx"; PIPE="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/services/reel-service/pipeline/index.ts"
export FLOW_USER_DATA_DIR="$UD" FLOW_ASSETS_DIR="/Users/admin/Downloads/New short/Google Flow AI Video/assets" FLOW_LOGS_DIR="$PWD/logs/flow"
VOCAB="LawWorld, cause of action, Code of Civil Procedure, Read versus Brown, A B C Laminart, A P Agencies, plaintiff, defendant, plaint, written statement, Supreme Court"
gate() {
  local idle=0 told=0
  while [ $idle -lt 30 ]; do
    r=$(curl -s -m 8 -H "x-api-key: $KEY" "http://localhost:4600/jobs?status=running" | python3 -c "
import sys,json,os
W='/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/services/reel-service/work/jobs'
n=0
for j in json.load(sys.stdin)['data']['jobs']:
    run=[s['name'] for s in j['stages'] if s['status']=='running']
    if any(x in ('broll','story','intro') for x in run): n+=1
    elif 'compose' in run:
        c=os.path.join(W,j['id'],'reel_work','cover')   # compose opens Flow once, for the cover portrait
        if not (os.path.isdir(c) and os.listdir(c)): n+=1
print(n)" 2>/dev/null || echo 1)
    if [ "$r" = "1" ] && [ "$(curl -s -m 3 -o /dev/null -w '%{http_code}' http://localhost:4600/health)" != "200" ]; then
      pgrep -f "user-data-dir=$HOME/Library/Application Support/LawWorld/flow-accounts" >/dev/null && r=1 || r=0
    fi
    if pgrep -f "user-data-dir=$UD" >/dev/null || [ "$r" != "0" ]; then idle=0; [ $told -eq 0 ] && { echo "[queue] waiting: reel service is using Flow $(date +%H:%M:%S)"; told=1; }; else idle=$((idle+10)); fi
    sleep 10
  done
  ls "$UD" | grep -qi singleton && ! pgrep -f "user-data-dir=$UD" >/dev/null && rm -f "$UD"/Singleton*
}
mkdir -p $D/rejected
if [ $# -gt 0 ]; then IDS=($@); else IDS=(c01 c02 c03 c04 c05 c06 c07 c08 c09); fi
for id in $IDS; do
  secs=$(python3 -c "import json; print([s['seconds'] for s in json.load(open('$ALLJ'))['scenes'] if s['sceneId']=='$id'][0])")
  for take in 1 2 3; do
    if [ -f $D/$id.mp4 ] && [ -f $D/$id.words.json ] && python3 -c "import json,sys; d=json.load(open('$D/$id.words.json')); sys.exit(0 if d.get('keep') else 1)"; then break; fi
    if [ -f $D/$id.mp4 ]; then
      mv $D/$id.mp4 $D/rejected/${id}_take$((take-1)).mp4; mv $D/$id.words.json $D/rejected/${id}_take$((take-1)).words.json 2>/dev/null
      rm -f $D/frames/${id}_last.jpg
    fi
    gate; echo "[queue] $id take $take start $(date +%H:%M:%S)"
    "$TSX" "$PIPE" --config ${SB}_${secs}s.json --scene $id --no-merge --timeout 240000 > logs/$(basename $SB)_$id.log 2>&1
    grep -q -E "Policy Filter Triggered|prominent people" logs/$(basename $SB)_$id.log && echo "[queue] $id POLICY REFUSED (no charge)"
    grep -q "CLI Error" logs/$(basename $SB)_$id.log && echo "[queue] $id launch error: $(grep 'CLI Error' logs/$(basename $SB)_$id.log | head -1 | cut -c1-140)"
    if [ -f $D/$id.mp4 ]; then
      line=$(python3 scripts/words.py $ALLJ $D/$id.mp4 --prompt "$VOCAB" 2>&1 | tail -1); echo "[queue] $line"
      ratio=$(python3 -c "import json; print(json.load(open('$D/$id.words.json')).get('match_ratio',0))" 2>/dev/null || echo 0)
      keep=$(python3 -c "print('True' if float('$ratio')>=0.90 else 'False')")
      python3 -c "import json; p='$D/$id.words.json'; d=json.load(open(p)); d['keep']=$keep; json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)"
      [ "$keep" = "False" ] && echo "[queue] $id take $take REJECTED (match $ratio) — re-rendering"
    else echo "[queue] $id take $take produced no clip"; sleep 20; fi
  done
  [ "$id" = "c01" ] && [ ! -f $GOF ] && { echo "[queue] PILOT c01 done — waiting for $GOF $(date +%H:%M:%S)"; while [ ! -f $GOF ]; do sleep 5; done; }
done
echo "[queue] ALL DONE $(date +%H:%M:%S)"
