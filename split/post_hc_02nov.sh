#!/bin/zsh
# 02-11-2026 High Court set in the HOOK format (owner: "make 1 set of video and post it ... with new reel style").
# Usage: zsh split/post_hc_02nov.sh <set> <file stem> <r2 slug>
# Waits for: every clip rendered + flat, the music choice (split/MUSIC_CHOICE_02nov holds the bed file the owner picked) and a free
# post lane (two post_course at most). Then: post_course (layout gate inside) -> darkfoot thumbnail -> QA -> ship.
cd "/Users/admin/Downloads/New short/product-explainer"; export PATH=/usr/local/bin:$PATH
SET=$1; STEM=$2; SLUG=$3
until grep -q "ALL DONE" logs/queue_$SET.log 2>/dev/null && (( $(ls downloads/$SET/flat/c*.mp4 2>/dev/null | wc -l | tr -d ' ') >= 10 )); do sleep 30; done
echo "$(date +%H:%M:%S) $SET clips ready"
until [ -s split/MUSIC_CHOICE_02nov ]; do sleep 20; done
BED=$(cat split/MUSIC_CHOICE_02nov)
grep -q '^MUSIC = ' split/cues/$SET.py || printf '\nMUSIC = {"file": "%s", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice\n' "$BED" >> split/cues/$SET.py
echo "$(date +%H:%M:%S) $SET music: $(grep '^MUSIC = ' split/cues/$SET.py)"
while (( $(pgrep -f "post_course.sh " | wc -l | tr -d ' ') >= 2 )); do sleep 20; done
echo "$(date +%H:%M:%S) $SET post start"
V_LAYOUT=judgment NO_DELIVER=1 OVERLAY_WORKERS=1 zsh split/post_course.sh $SET $STEM > logs/post_$SET.log 2>&1
rc=$?; echo "$(date +%H:%M:%S) $SET post_course exit $rc"; grep -E "LAYOUT|head check|HELD|FAIL" logs/post_$SET.log out/${SET}9x16/*.log 2>/dev/null | head -5
[ $rc -eq 0 ] || exit 1
python3 split/thumb_darkfoot.py out/$SET/thumb_brand.json > logs/thumb_$SET.log 2>&1
zsh split/finish_judgment_reel.sh $SET qa > logs/qa_$SET.log 2>&1; echo "$(date +%H:%M:%S) $SET qa exit $?"
zsh split/finish_judgment_reel.sh $SET ship $SLUG $STEM > logs/ship_$SET.log 2>&1; echo "$(date +%H:%M:%S) $SET ship exit $?"; tail -3 logs/ship_$SET.log
