#!/bin/zsh
# usage: zsh split/match_recovered_10nov.sh <set> <clip id>  -> whisper-checks every recovered tile against that clip's line
cd "/Users/admin/Downloads/New short/product-explainer"; s=$1; c=$2; source split/${s}_env.sh
T=/private/tmp/claude-501/-Users-admin-Downloads-New-short/07a60ea5-ec1b-45a8-81e7-227b19aba488/scratchpad/match_$s; mkdir -p $T
for f in downloads/$s/recovered/*/tile_*.mp4; do
  k=$T/$(basename $f .mp4).done; [ -f $k ] && { cat $k; continue; }
  want=$(python3 -c "import json;print([x['seconds'] for x in json.load(open('split/${s}_all_scenes.json'))['scenes'] if x['sceneId']=='$c'][0])")
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $f); case $d in ${want}.*) ;; *) echo "$(basename $f) ${d}s skip (want ${want}s)" | tee $k; continue;; esac
  mkdir -p $T/w; cp $f $T/w/$c.mp4; r=$(python3 scripts/words.py $SPLIT_ALL $T/w/$c.mp4 --prompt "$SPLIT_VOCAB" 2>&1 | tail -1)
  echo "$(basename $f) $r" | cut -c1-200 | tee $k
done
