#!/bin/zsh
# out/full/full.mp4 -> out/final/LawWorld_Explainer_FINAL.mp4 : first 2.0 s replaced by the logo-card still with a 2 % slow zoom (audio untouched), one video + one audio stream.
set -e; cd "/Users/admin/Downloads/New short/product-explainer"; mkdir -p out/final
IN=${1:-out/full/full.mp4}; OUTF=${2:-out/final/LawWorld_Explainer_FINAL.mp4}
T=${3:-out/final/thumbnail.png}; [ -f $T ] || ffmpeg -v error -y -i $IN -ss 2.0 -frames:v 1 $T
ffmpeg -hide_banner -y -i $IN -loop 1 -framerate 24 -t 2.0 -i $T -filter_complex "[1:v]scale=1080:1920,zoompan=z='1+0.02*on/48':x='(iw-iw/zoom)/2':y='(ih-ih/zoom)/2':d=1:s=1080x1920:fps=24,trim=0:2.0,setpts=PTS-STARTPTS,format=yuv420p[intro];[0:v]trim=2.0,setpts=PTS-STARTPTS,format=yuv420p[rest];[intro][rest]concat=n=2:v=1:a=0,fps=24[v]" -map "[v]" -map 0:a:0 -c:v libx264 -preset medium -crf 17 -pix_fmt yuv420p -r 24 -c:a copy -movflags +faststart $OUTF -stats_period 10 > out/final/finalize.log 2>&1
ffprobe -v error -select_streams v:0 -show_entries stream=nb_frames,duration -of csv=p=0 $OUTF
