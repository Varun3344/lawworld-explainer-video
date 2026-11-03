#!/bin/zsh
# 03-11-2026 one hook-format reel: wait for every clip (rendered + flat) -> post_course (layout gate inside) -> darkfoot thumbnail -> QA.
# No ship here: the finished reel is reviewed first (transcript, frames, cover), then shipped by hand.
# Usage: zsh split/post_one_03nov.sh <set> <file stem>
cd "/Users/admin/Downloads/New short/product-explainer"; export PATH=/usr/local/bin:$PATH
SET=$1; STEM=$2
until grep -q "ALL DONE" logs/queue_$SET.log 2>/dev/null && (( $(ls downloads/$SET/flat/c*.mp4 2>/dev/null | wc -l | tr -d ' ') >= 10 )); do sleep 30; done
echo "$(date +%H:%M:%S) $SET clips ready"
while (( $(pgrep -f "post_course.sh " | wc -l | tr -d ' ') >= 2 )); do sleep 20; done
echo "$(date +%H:%M:%S) $SET post start"
V_LAYOUT=judgment NO_DELIVER=1 OVERLAY_WORKERS=1 zsh split/post_course.sh $SET $STEM > logs/post_$SET.log 2>&1
rc=$?; echo "$(date +%H:%M:%S) $SET post_course exit $rc"; grep -E "LAYOUT|head check|HELD|FAIL" logs/post_$SET.log 2>/dev/null | head -5
[ $rc -eq 0 ] || exit 1
python3 split/thumb_darkfoot.py out/$SET/thumb_brand.json > logs/thumb_$SET.log 2>&1; echo "$(date +%H:%M:%S) $SET thumb exit $?"
zsh split/finish_judgment_reel.sh $SET qa > logs/qa_$SET.log 2>&1; echo "$(date +%H:%M:%S) $SET qa exit $?"
echo "$(date +%H:%M:%S) $SET READY FOR REVIEW"
