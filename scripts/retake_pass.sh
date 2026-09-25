#!/bin/zsh
# After the main queue: transcript-check every presenter clip, move failures aside, regenerate (short watchdog).
# c20 special case: Flow's policy filter refused the exact line; round 1 retries it verbatim, later rounds use minimal rewordings.
cd "/Users/admin/Downloads/New short/product-explainer"
UD="/Users/admin/Downloads/New short/Google Flow AI Video/user_data"
TSX="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/node_modules/.bin/tsx"
PIPE="/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/services/reel-service/pipeline/index.ts"
export FLOW_USER_DATA_DIR="$UD" FLOW_ASSETS_DIR="/Users/admin/Downloads/New short/Google Flow AI Video/assets" FLOW_LOGS_DIR="/Users/admin/Downloads/New short/product-explainer/logs/flow"
mkdir -p downloads/full/rejected
SCENES=storyboards/full_all_scenes.json; [ -f downloads/full/c20.altused ] && SCENES=storyboards/full_all_scenes_c20alt$(cat downloads/full/c20.altused).json
waitfree() { sleep 6; for i in {1..20}; do ls "$UD" | grep -qi singleton || return 0; sleep 5; done; }
for round in 1 2 3; do
  echo "[retake] round $round check $(date '+%H:%M:%S') (scenes: $SCENES)"
  bad=()
  for c in downloads/full/c*.mp4; do
    id=$(basename $c .mp4)
    line=$(python3 scripts/words.py $SCENES $c 2>&1 | tail -1); echo "  $line"
    echo "$line" | grep -q "CHECK" && bad+=($id)
  done
  for id in c01 c02 c03 c04 c05 c06 c07 c08 c09 c10 c11 c12 c13 c14 c15 c16 c17 c18 c19 c20; do [ -f downloads/full/$id.mp4 ] || bad+=($id); done
  [ ${#bad} -eq 0 ] && { echo "[retake] all 20 clips verbatim"; break; }
  echo "[retake] regenerating: $bad"
  for id in $bad; do for f in downloads/full/$id.mp4 downloads/full/$id.words.json; do [ -f $f ] && mv $f downloads/full/rejected/r${round}_$(basename $f); done; done
  for sb in storyboards/full_presenter_10s.json storyboards/full_presenter_8s.json storyboards/full_presenter_6s.json; do
    ids=(); for id in $bad; do grep -q "\"$id\"" $sb && ids+=($id); done
    [ ${#ids} -eq 0 ] && continue
    for id in $ids; do
      cfg=$sb
      if [ "$id" = "c20" ] && [ $round -ge 2 ]; then n=$((round-1)); cfg=storyboards/c20_alt$n.json; echo "$n" > downloads/full/c20.altused; SCENES=storyboards/full_all_scenes_c20alt$n.json; fi
      waitfree; echo "[retake] run $cfg --scene $id $(date '+%H:%M:%S')"
      "$TSX" "$PIPE" --config $cfg --scene $id --no-merge --timeout 240000; echo "[retake] exit $? $(date '+%H:%M:%S')"
    done
  done
done
echo "[retake] DONE $(date '+%H:%M:%S')"
