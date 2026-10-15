#!/bin/zsh
# Flattens every kept full-video clip (downloads/coa/cNN.mp4 + words.json keep=true) whose flat copy is missing or older than the
# source; exits once all 36 flat clips are present and fresh. One clip at a time (the Mac is also rendering Flow clips).
# --seam left: the Cause of Action layout (presenter box RIGHT of the panel) for the verification; the whole stats line and every
# WARNING line are shown (no cut).
cd "/Users/admin/Downloads/New short/product-explainer"
while true; do
  left=0
  for i in {1..36}; do
    c=$(printf "c%02d" $i); s=downloads/coa/$c.mp4; f=downloads/coa/flat/$c.mp4; w=downloads/coa/$c.words.json
    if [ -f $f ] && [ -f $s ] && [ $f -nt $s ]; then continue; fi
    left=$((left+1))
    [ -f $s ] && [ -f $w ] && python3 -c "import json,sys; sys.exit(0 if json.load(open('$w')).get('keep') else 1)" 2>/dev/null || continue
    python3 split/flatten_bg.py --seam left $s 2>&1 | grep -E "^\[flatten\]" | sed "s/^/$(date +%H:%M:%S) /"
  done
  [ $left -eq 0 ] && { echo "$(date +%H:%M:%S) all 36 flat"; break; }
  sleep 30
done
