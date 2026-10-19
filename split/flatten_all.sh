#!/bin/zsh
# One flatten worker for every course set (the Mac cannot run three plus the overlay renders): flattens each kept clip whose flat
# copy is missing or older than the source, oldest set first; exits when every listed set is complete.
# Usage: zsh split/flatten_all.sh cog cpb apl dfc cus bail plt trl
cd "/Users/admin/Downloads/New short/product-explainer"
while true; do
  left=0; did=0
  for SET in "$@"; do
    [ -f split/${SET}_all_scenes.json ] || continue
    for c in $(python3 -c "import json; print(' '.join(s['sceneId'] for s in json.load(open('split/${SET}_all_scenes.json'))['scenes']))"); do
      s=downloads/$SET/$c.mp4; f=downloads/$SET/flat/$c.mp4; w=downloads/$SET/$c.words.json
      if [ -f $f ] && [ -f $s ] && [ $f -nt $s ]; then continue; fi
      left=$((left+1))
      [ -f $s ] && [ -f $w ] && python3 -c "import json,sys; sys.exit(0 if json.load(open('$w')).get('keep') else 1)" 2>/dev/null || continue
      pgrep -f "flatten_bg.py --seam left $s" >/dev/null && continue          # an earlier worker is still on it
      FLATTEN_PRESET=veryfast nice -n 10 python3 split/flatten_bg.py --seam left $s 2>&1 | grep -E "^\[flatten\]" | sed "s/^/$(date +%H:%M:%S) /" | cut -c1-260
      did=1; break
    done
    [ $did -eq 1 ] && break
  done
  [ $left -eq 0 ] && { echo "$(date +%H:%M:%S) all sets flat"; break; }
  [ $did -eq 0 ] && sleep 20
done
