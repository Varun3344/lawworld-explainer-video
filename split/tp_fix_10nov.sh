#!/bin/zsh
# 10-11-2026: delivered concept videos measured a true peak above -1 dBTP (fir -0.6). Audio-only fix: two-pass loudnorm
# (linear) to -14 LUFS / -1.5 dBTP, video stream copied untouched, +faststart. The original is kept in the scratchpad.
# usage: zsh split/tp_fix_10nov.sh <file.mp4>
f=$1; B=/private/tmp/claude-501/-Users-admin-Downloads-New-short/07a60ea5-ec1b-45a8-81e7-227b19aba488/scratchpad/tp_orig; mkdir -p $B
j=$(ffmpeg -hide_banner -nostats -i "$f" -vn -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json -f null - 2>&1 | sed -n '/^{/,/^}/p')
mi=$(echo "$j" | python3 -c "import json,sys;d=json.load(sys.stdin);print(d['input_i'],d['input_tp'],d['input_lra'],d['input_thresh'],d['target_offset'])")
set -- ${=mi}
tmp="${f%.mp4}.tpfix.mp4"
ffmpeg -v error -y -i "$f" -map 0:v:0 -map 0:a:0 -c:v copy -af "loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=${1}:measured_TP=${2}:measured_LRA=${3}:measured_thresh=${4}:offset=${5}:linear=true" -ar 48000 -c:a aac -b:a 192k -movflags +faststart "$tmp" || exit 1
m=$(ffmpeg -hide_banner -nostats -i "$tmp" -vn -af ebur128=peak=true -f null - 2>&1 | grep -E "I:|Peak:" | tail -2 | tr -s ' ' | tr '\n' ' ')
dv=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f"); dn=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$tmp")
echo "$(basename $f): before I=${1} TP=${2} | after $m | dur $dv -> $dn"
mv "$f" "$B/" && mv "$tmp" "$f"
