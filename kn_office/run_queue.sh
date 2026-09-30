#!/bin/zsh
# Kannada office clips, one Flow launch per clip. Before every launch: no reel stage that uses Flow is running and the Flow
# browser has been closed for 30 s. After every clip: Kannada speech check; a failed take is set aside and re-rendered (max 3 takes).
# q01 is the pilot: the queue stops after it until kn_office/GO exists.
cd "/Users/admin/Downloads/New short/product-explainer"
UD="/Users/admin/Downloads/New short/Google Flow AI Video/user_data"; D=downloads/office_kn
KEY=$(grep -E '^REEL_PIPELINE_API_KEY=' '/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/.env' | cut -d= -f2- | tr -d '"')
TSX="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/node_modules/.bin/tsx"; PIPE="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/services/reel-service/pipeline/index.ts"
export FLOW_USER_DATA_DIR="$UD" FLOW_ASSETS_DIR="/Users/admin/Downloads/New short/Google Flow AI Video/assets" FLOW_LOGS_DIR="$PWD/logs/flow"
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
    if pgrep -f "user-data-dir=$UD" >/dev/null || [ "$r" != "0" ]; then idle=0; [ $told -eq 0 ] && { echo "[queue] waiting: reel service is using Flow $(date +%H:%M:%S)"; told=1; }; else idle=$((idle+10)); fi
    sleep 10
  done
  ls "$UD" | grep -qi singleton && ! pgrep -f "user-data-dir=$UD" >/dev/null && rm -f "$UD"/Singleton*
}
mkdir -p $D/rejected
for id in q01 q02 q03 q04 q05 q06 q07 q08 q09 q10 q11 q12 q13 q14 q15 q16 q17 q18; do
  secs=$(python3 -c "import json; print([s['seconds'] for s in json.load(open('kn_office/kn_all_scenes.json'))['scenes'] if s['sceneId']=='$id'][0])")
  for take in 1 2 3; do
    if [ -f $D/$id.mp4 ] && [ -f $D/$id.words.json ] && python3 -c "import json,sys; d=json.load(open('$D/$id.words.json')); sys.exit(0 if d.get('ok') else 1)"; then break; fi
    [ -f $D/$id.mp4 ] && { mv $D/$id.mp4 $D/rejected/${id}_take$((take-1)).mp4; mv $D/$id.words.json $D/rejected/${id}_take$((take-1)).words.json 2>/dev/null; }
    gate; echo "[queue] $id take $take start $(date +%H:%M:%S)"
    "$TSX" "$PIPE" --config kn_office/kn_${secs}s.json --scene $id --no-merge --timeout 240000 > logs/kn_office_$id.log 2>&1
    grep -q -E "Policy Filter Triggered|prominent people" logs/kn_office_$id.log && echo "[queue] $id POLICY REFUSED (no charge)"
    grep -q "CLI Error" logs/kn_office_$id.log && echo "[queue] $id launch error: $(grep 'CLI Error' logs/kn_office_$id.log | head -1 | cut -c1-120)"
    if [ -f $D/$id.mp4 ]; then
      line=$(python3 kn_office/kn_words.py kn_office/kn_all_scenes.json $D/$id.mp4 2>&1 | tail -1); echo "[queue] $line"
      okv=$(echo "$line" | grep -q ": OK" && echo true || echo false)
      python3 -c "import json; p='$D/$id.words.json'; d=json.load(open(p)); d['ok']=$( [ $okv = true ] && echo True || echo False ); json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)"
    else echo "[queue] $id take $take produced no clip"; sleep 20; fi
  done
  [ "$id" = "q01" ] && { echo "[queue] PILOT q01 done — waiting for GO"; while [ ! -f kn_office/GO ]; do sleep 5; done; }
done
echo "[queue] ALL DONE $(date +%H:%M:%S)"
