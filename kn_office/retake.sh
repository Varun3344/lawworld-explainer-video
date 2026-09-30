#!/bin/zsh
# retake.sh <clipId>: set the current take aside and re-render until speech AND room both pass (max 3 takes), then assemble.
cd "/Users/admin/Downloads/New short/product-explainer"; id=$1; D=downloads/office_kn
UD="/Users/admin/Downloads/New short/Google Flow AI Video/user_data"
KEY=$(grep -E '^REEL_PIPELINE_API_KEY=' '/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/.env' | cut -d= -f2- | tr -d '"')
TSX="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/node_modules/.bin/tsx"; PIPE="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/services/reel-service/pipeline/index.ts"
export FLOW_USER_DATA_DIR="$UD" FLOW_ASSETS_DIR="/Users/admin/Downloads/New short/Google Flow AI Video/assets" FLOW_LOGS_DIR="$PWD/logs/flow"
gate() {
  local idle=0
  while [ $idle -lt 30 ]; do
    r=$(curl -s -m 8 -H "x-api-key: $KEY" "http://localhost:4600/jobs?status=running" | python3 -c "
import sys,json,os
W='/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/services/reel-service/work/jobs'
n=0
for j in json.load(sys.stdin)['data']['jobs']:
    run=[s['name'] for s in j['stages'] if s['status']=='running']
    if any(x in ('broll','story','intro') for x in run): n+=1
    elif 'compose' in run:
        c=os.path.join(W,j['id'],'reel_work','cover')
        if not (os.path.isdir(c) and os.listdir(c)): n+=1
print(n)" 2>/dev/null || echo 1)
    if pgrep -f "user-data-dir=$UD" >/dev/null || [ "$r" != "0" ]; then idle=0; else idle=$((idle+10)); fi
    sleep 10
  done
  ls "$UD" | grep -qi singleton && ! pgrep -f "user-data-dir=$UD" >/dev/null && rm -f "$UD"/Singleton*
}
secs=$(python3 -c "import json; print([s['seconds'] for s in json.load(open('kn_office/kn_all_scenes.json'))['scenes'] if s['sceneId']=='$id'][0])")
good=0; n=$(ls $D/rejected 2>/dev/null | grep -c "^${id}_")
for take in 1 2 3; do
  [ -f $D/$id.mp4 ] && { n=$((n+1)); mv $D/$id.mp4 $D/rejected/${id}_r$n.mp4; mv $D/$id.words.json $D/rejected/${id}_r$n.words.json 2>/dev/null; }
  gate; echo "[retake] $id take $take start $(date +%H:%M:%S)"
  "$TSX" "$PIPE" --config kn_office/kn_${secs}s.json --scene $id --no-merge --timeout 240000 > logs/kn_office_$id.log 2>&1
  [ -f $D/$id.mp4 ] || { echo "[retake] $id take $take produced no clip"; sleep 15; continue; }
  line=$(python3 kn_office/kn_words.py kn_office/kn_all_scenes.json $D/$id.mp4 2>&1 | tail -1); room=$(python3 kn_office/room_check.py $D/$id.mp4); rc=$?
  echo "[retake] $line"; echo "[retake] $id room difference $room (limit 18)"
  if echo "$line" | grep -q ": OK" && [ $rc -eq 0 ]; then python3 -c "import json; p='$D/$id.words.json'; d=json.load(open(p)); d['ok']=True; json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)"; good=1; break; fi
done
[ $good -eq 1 ] && echo "[retake] $id ACCEPTED $(date +%H:%M:%S)" || echo "[retake] $id FAILED after 3 takes"
