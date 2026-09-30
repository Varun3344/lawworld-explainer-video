#!/bin/zsh
# tail_check.sh <clip>: last words + level in the final 0.6 s (a complete final word decays to silence before the end)
c=$1; d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $c)
python3 -c "import json; d=json.load(open('${c%.mp4}.words.json')); print(d['text'][-70:]); print([(w['word'],w['start'],w['end']) for w in d['words'][-2:]])"
for k in 6 5 4 3 2 1; do t=$(python3 -c "print(round($d-0.1*$k,2))"); printf "$t: "; ffmpeg -hide_banner -nostats -ss $t -t 0.1 -i $c -af volumedetect -f null - 2>&1 | grep mean_volume | sed 's/.*mean_volume: //'; done
