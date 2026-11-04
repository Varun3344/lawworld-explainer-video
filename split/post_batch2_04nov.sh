#!/bin/zsh
# 04-11-2026 batch 2 (the remaining fresh judgments): sets come from split/batch2_04nov.tsv (set TAB stem TAB slug), re-read every
# pass so new reels join without a restart. Per set, once its queue says ALL DONE and every clip is flat: post_course -> darkfoot
# thumbnail -> QA -> ship. At most 2 post_course runs on the Mac at once (shared with the batch-1 dispatchers). Keeps one flatten
# worker (two once the batch-1 workers are gone) running over the batch-2 sets that still have clips to flatten. Posting stays manual.
cd "/Users/admin/Downloads/New short/product-explainer"; export PATH=/usr/local/bin:$PATH
one() { local s=$1 stem=$2 slug=$3
  V_LAYOUT=judgment NO_DELIVER=1 OVERLAY_WORKERS=1 zsh split/post_course.sh $s $stem > logs/post_$s.log 2>&1 || { echo "$(date +%H:%M:%S) $s POST FAILED"; return 1; }
  python3 split/thumb_darkfoot.py out/$s/thumb_brand.json > logs/thumb_$s.log 2>&1
  zsh split/finish_judgment_reel.sh $s qa > logs/qa_$s.log 2>&1 || echo "$(date +%H:%M:%S) $s QA exit $?"
  zsh split/finish_judgment_reel.sh $s ship $slug $stem > logs/ship_$s.log 2>&1 && echo "$(date +%H:%M:%S) $s SHIPPED" || echo "$(date +%H:%M:%S) $s SHIP FAILED"
}
nclips() { python3 -c "import json;print(len(json.load(open('split/$1_all_scenes.json'))['scenes']))" 2>/dev/null || echo 99; }
nflat() { find downloads/$1/flat -maxdepth 1 -name 'c*.mp4' ! -name '*part*' 2>/dev/null | wc -l | tr -d ' '; }
while true; do
  sets=($(cut -f1 split/batch2_04nov.tsv | grep -v '^#'))
  # flatten workers for the batch-2 sets with clips left to flatten
  need=0; for s in $sets; do [ -f split/${s}_all_scenes.json ] && (( $(nflat $s) < $(nclips $s) )) && need=1; done
  b1=$(pgrep -f "flatten_all.sh ukd" | wc -l | tr -d ' '); b2=$(pgrep -f "flatten_all.sh B2" | wc -l | tr -d ' ')
  if (( need )) && (( b2 < (b1 > 0 ? 1 : 2) )); then
    nohup zsh -c "exec -a 'flatten_all.sh B2' zsh split/flatten_all.sh $sets" >> logs/flatten_b2.log 2>&1 &
    echo "$(date +%H:%M:%S) flatten worker started over: $sets"
  fi
  left=0
  while IFS=$'\t' read -r s stem slug; do
    [[ -z "$s" || "$s" == \#* ]] && continue
    [ -f logs/b2_started_$s ] && continue
    left=1
    [ -f logs/b2_hold ] && break   # 05-11: hold new batch-2 posts while a priority fix runs
    grep -q "ALL DONE" logs/queue_$s.log 2>/dev/null || continue
    (( $(nflat $s) >= $(nclips $s) )) || continue
    (( $(pgrep -f "post_course.sh " | wc -l | tr -d ' ') >= $(cat logs/b2_maxposts 2>/dev/null || echo 2) )) && break   # 04-11 22:55: limit from logs/b2_maxposts (3 once Flow renders are done)
    touch logs/b2_started_$s; echo "$(date +%H:%M:%S) $s post start"; one $s $stem $slug &
    sleep 20
  done < split/batch2_04nov.tsv
  [ -f logs/b2_STOP ] && { echo "$(date +%H:%M:%S) stop file"; break; }
  sleep 30
done
