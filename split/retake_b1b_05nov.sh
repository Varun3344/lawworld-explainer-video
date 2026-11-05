#!/bin/zsh
# 05-11-2026 07:00: second re-take with reworded lines - rnt c09 ("agreed that a High Court"), ptn c04 ("protected by the Telangana Tenancy Act"). Both on main.
# flatten, full post + thumb + qa + ship (post_one_04nov.sh, batch-1 maps). adt on a3; rnt then ptn on main.
cd "/Users/admin/Downloads/New short/product-explainer"; export PATH=/usr/local/bin:$PATH
heavy() { echo $(( $(pgrep -f "post_course.sh " | wc -l | tr -d ' ') + $(pgrep -f "build_vertical_course.py [a-z0-9]+ final" | wc -l | tr -d ' ') )); }
take() { local s=$1 c=$2
  mkdir -p downloads/$s/rejected
  mv downloads/$s/$c.mp4 downloads/$s/rejected/${c}_qa9b.mp4; mv downloads/$s/$c.words.json downloads/$s/rejected/${c}_qa9b.words.json; mv downloads/$s/flat/$c.mp4 downloads/$s/rejected/${c}_qa9b_flat.mp4 2>/dev/null
  ( source split/${s}_env.sh && zsh split/run_queue.sh $c ) > logs/queue_${s}_${c}_qa9b.log 2>&1
  echo "$(date +%H:%M:%S) $s $c: $(grep -E "words\] $c" logs/queue_${s}_${c}_qa9b.log | tail -1 | cut -c1-200)"
}
post() { local s=$1 c=$2
  python3 -c "import json,sys; sys.exit(0 if json.load(open('downloads/$s/$c.words.json')).get('keep') else 1)" || { echo "$s $c retake NOT kept - check by hand"; return 1; }
  FLATTEN_PRESET=veryfast python3 split/flatten_bg.py --seam left downloads/$s/$c.mp4 2>&1 | grep -E "^\[flatten\] $c" | cut -c1-100
  while (( $(heavy) >= 4 )); do sleep 20; done
  echo "$(date +%H:%M:%S) $s post start"; zsh split/post_one_04nov.sh $s
}

( take rnt c09; take ptn c04; post rnt c09 & post ptn c04; wait ) &
wait; echo "$(date +%H:%M:%S) B1 RETAKES 2 DONE"
