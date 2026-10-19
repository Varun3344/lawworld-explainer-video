#!/bin/zsh
# Flattens every kept clip of a course set (downloads/<set>/cNN.mp4 + words.json keep=true) whose flat copy is missing or older than
# the source; exits once every clip of split/<set>_all_scenes.json has a fresh flat copy. One clip at a time (the Mac is also
# rendering Flow clips). Usage: zsh split/flatten_watch.sh <set>
cd "/Users/admin/Downloads/New short/product-explainer"
SET=$1
while true; do
  left=0
  for c in $(python3 -c "import json; print(' '.join(s['sceneId'] for s in json.load(open('split/${SET}_all_scenes.json'))['scenes']))"); do
    s=downloads/$SET/$c.mp4; f=downloads/$SET/flat/$c.mp4; w=downloads/$SET/$c.words.json
    if [ -f $f ] && [ -f $s ] && [ $f -nt $s ]; then continue; fi
    left=$((left+1))
    [ -f $s ] && [ -f $w ] && python3 -c "import json,sys; sys.exit(0 if json.load(open('$w')).get('keep') else 1)" 2>/dev/null || continue
    nice -n 5 python3 split/flatten_bg.py --seam left $s 2>&1 | grep -E "^\[flatten\]" | sed "s/^/$(date +%H:%M:%S) /"
  done
  [ $left -eq 0 ] && { echo "$(date +%H:%M:%S) all flat"; break; }
  sleep 30
done
