#!/bin/zsh
# 05-11-2026 QA: cst c02 repeats "electricity company"; awg c10 framing jumps mid-take -> re-take both (a1, a3), flatten, full post (+ thumb, qa, ship).
cd "/Users/admin/Downloads/New short/product-explainer"; export PATH=/usr/local/bin:$PATH
heavy() { echo $(( $(pgrep -f "post_course.sh " | wc -l | tr -d ' ') + $(pgrep -f "build_vertical_course.py [a-z0-9]+ final" | wc -l | tr -d ' ') )); }
redo() { local s=$1 c=$2 stem=$(awk -F'\t' -v k=$1 '$1==k{print $2}' split/batch2_04nov.tsv) slug=$(awk -F'\t' -v k=$1 '$1==k{print $3}' split/batch2_04nov.tsv)
  mkdir -p downloads/$s/rejected
  mv downloads/$s/$c.mp4 downloads/$s/rejected/${c}_qa05nov.mp4; mv downloads/$s/$c.words.json downloads/$s/rejected/${c}_qa05nov.words.json; mv downloads/$s/flat/$c.mp4 downloads/$s/rejected/${c}_qa05nov_flat.mp4 2>/dev/null
  ( source split/${s}_env.sh && zsh split/run_queue.sh $c ) > logs/queue_${s}_$c.log 2>&1
  echo "$(date +%H:%M:%S) $s $c: $(grep -E "words\] $c" logs/queue_${s}_$c.log | tail -1 | cut -c1-160)"
  python3 -c "import json,sys; sys.exit(0 if json.load(open('downloads/$s/$c.words.json')).get('keep') else 1)" || { echo "$s $c retake NOT kept"; return 1; }
  FLATTEN_PRESET=veryfast python3 split/flatten_bg.py --seam left downloads/$s/$c.mp4 2>&1 | grep -E "^\[flatten\] $c" | cut -c1-120
  while (( $(heavy) >= 4 )); do sleep 20; done
  echo "$(date +%H:%M:%S) $s post start"
  V_LAYOUT=judgment NO_DELIVER=1 OVERLAY_WORKERS=2 zsh split/post_course.sh $s $stem > logs/post_$s.log 2>&1 || { echo "$(date +%H:%M:%S) $s POST FAILED"; tail -2 logs/post_$s.log; return 1; }
  python3 split/thumb_darkfoot.py out/$s/thumb_brand.json > logs/thumb_$s.log 2>&1
  zsh split/finish_judgment_reel.sh $s qa > logs/qa_$s.log 2>&1
  zsh split/finish_judgment_reel.sh $s ship $slug $stem > logs/ship_$s.log 2>&1 && echo "$(date +%H:%M:%S) $s SHIPPED" || echo "$(date +%H:%M:%S) $s SHIP FAILED"
}
redo cst c02 &
redo awg c10 &
wait; echo "$(date +%H:%M:%S) RETAKES DONE"
