#!/bin/zsh
# Deliver a set that post_course HELD on a speech FAIL after the flagged clips were checked by hand (same copy steps as post_course).
# Usage: zsh split/deliver_held.sh <set> <file stem> "<reason>"
set -eu
cd "/Users/admin/Downloads/New short/product-explainer"
SET=$1; STEM=$2; WHY=$3; O=out/$SET; V=out/${SET}9x16
[ -f $O/${SET}_full.mp4 ] && [ -f $V/${SET}_9x16.mp4 ] || { echo "missing outputs"; exit 1; }
cp $O/${SET}_full.mp4 ~/Downloads/${STEM}_16x9.mp4
cp $V/${SET}_9x16.mp4 ~/Downloads/${STEM}_9x16.mp4
cp $O/captions.srt ~/Downloads/${STEM}_16x9.srt
ffmpeg -v error -y -i $O/${SET}_full.mp4 -frames:v 1 -q:v 2 ~/Downloads/${STEM}_16x9_cover.jpg
ffmpeg -v error -y -i $V/${SET}_9x16.mp4 -frames:v 1 -q:v 2 ~/Downloads/${STEM}_9x16_cover.jpg
echo "[post $SET] $(date +%H:%M:%S) DELIVERED by hand after review ($WHY): ~/Downloads/${STEM}_16x9.mp4 + _9x16.mp4 (md5 $(md5 -q ~/Downloads/${STEM}_16x9.mp4) / $(md5 -q ~/Downloads/${STEM}_9x16.mp4))" | tee -a logs/post_$SET.log
