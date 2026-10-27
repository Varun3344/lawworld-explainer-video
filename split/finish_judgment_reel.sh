#!/bin/zsh
# Finish a judgment reel in the concept format (owner 26/27-10-2026), after post_course.sh with V_LAYOUT=judgment NO_DELIVER=1.
#   zsh split/finish_judgment_reel.sh <set> qa                       edit list, one-screen colour samples, frame sheet, full transcript
#   zsh split/finish_judgment_reel.sh <set> ship <r2-slug> <file stem>   cover (thumbnail, 15 frames = 0.625 s at 24 fps) + the ORIGINAL
#       audio track remuxed (a concat leaves an audio seam), R2 upload under reels/concept/<slug>/, md5 check, copy to ~/Downloads
set -e
cd "/Users/admin/Downloads/New short/product-explainer"
SET=$1; WHAT=$2; V=out/${SET}9x16; SRC=$V/${SET}_9x16.mp4; QA=$V/qa; mkdir -p $QA
if [ "$WHAT" = "qa" ]; then
  echo "edit: $(cat $V/edit.json)"
  ffprobe -v error -show_entries format=duration:stream=nb_frames -of csv=p=0 $SRC | tr '\n' ' '; echo
  python3 - $SRC $QA <<'PY'
import subprocess, sys
from PIL import Image
src, qa = sys.argv[1:3]
dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", src], capture_output=True, text=True).stdout)
for t in (30, 60):   # one screen: background above the panel, panel foot, gap, presenter band
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", src, "-frames:v", "1", f"{qa}/tone.png"], check=True)
    im = Image.open(f"{qa}/tone.png").convert("RGB")
    print(f"tone t={t}:", [im.getpixel((60, y)) for y in (40, 1092, 1120, 1200)])
ts = [0.3, 3, 7, 13, 17, 20] + [round(25 + k * (dur - 33) / 11, 1) for k in range(12)] + [dur - 1.5, dur - 0.1]
outs = []
for i, t in enumerate(ts):
    o = f"{qa}/f{i:02d}.png"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", src, "-frames:v", "1", "-vf", "scale=200:-2", o], check=True); outs.append(o)
rows = []
for r in range(0, len(outs), 10):
    g = outs[r:r + 10]; g += [g[-1]] * (10 - len(g)); o = f"{qa}/row{r}.png"
    subprocess.run(["ffmpeg", "-v", "error", "-y"] + sum([["-i", x] for x in g], []) + ["-filter_complex", "".join(f"[{k}]" for k in range(10)) + "hstack=10", o], check=True); rows.append(o)
subprocess.run(["ffmpeg", "-v", "error", "-y"] + sum([["-i", x] for x in rows], []) + ["-filter_complex", "".join(f"[{k}]" for k in range(len(rows))) + f"vstack={len(rows)}", f"{qa}/sheet.jpg"], check=True)
print("sheet:", f"{qa}/sheet.jpg")
PY
  KEY=$(grep '^OPENAI_API_KEY=' "/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/.env" | cut -d= -f2- | tr -d '"')
  ffmpeg -v error -y -i $SRC -vn -ac 1 -ar 16000 -b:a 48k $QA/a.mp3
  echo "transcript: $(curl -s https://api.openai.com/v1/audio/transcriptions -H "Authorization: Bearer $KEY" -F file=@$QA/a.mp3 -F model=whisper-1 -F language=en | python3 -I -c 'import json,sys;print(json.load(sys.stdin).get("text"))')"
elif [ "$WHAT" = "ship" ]; then
  SLUG=$3; STEM=$4; O=$V/cover; mkdir -p $O; TH=out/$SET/thumb_brand.png
  ENC=(-c:v libx264 -preset veryfast -crf 17 -r 24 -pix_fmt yuv420p -c:a aac -b:a 192k -ar 48000 -ac 2)
  ffmpeg -loglevel error -loop 1 -t 0.625 -i $TH -t 0.625 -i $SRC -map 0:v -map 1:a -vf "scale=1080:1920,setsar=1" "${ENC[@]}" -shortest -y $O/q0.mp4
  ffmpeg -loglevel error -i $SRC -ss 0.625 "${ENC[@]}" -y $O/q1.mp4
  printf "file '%s/q0.mp4'\nfile '%s/q1.mp4'\n" "$PWD/$O" "$PWD/$O" > $O/list.txt
  ffmpeg -loglevel error -f concat -safe 0 -i $O/list.txt -c copy -y $O/v.mp4
  ffmpeg -loglevel error -i $O/v.mp4 -i $SRC -map 0:v -map 1:a -c copy -movflags +faststart -y $O/final.mp4
  echo "final: $(ffprobe -v error -show_entries stream=codec_type,nb_frames -of csv=p=0 $O/final.mp4 | tr '\n' ' ')"
  F="$PWD/$O/final.mp4"
  cd "/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/services/reel-service"
  U=$(npx tsx -e "
require('dotenv').config({ path: '../../.env' });
const { putFile, urlForKey } = require('./src/utils/r2');
(async () => {
  const stamp = new Date().toISOString().replace(/[-:]/g, '').replace(/\..*/, 'Z').replace('T', '-');
  const key = 'reels/concept/' + process.argv[2] + '/final-9x16-' + stamp + '.mp4';
  await putFile(key, process.argv[1], 'video/mp4'); console.log('URL', urlForKey(key)); process.exit(0);
})().catch(e => { console.error(e); process.exit(1); });" "$F" "$SLUG" 2>&1 | grep '^URL' | cut -d' ' -f2)
  echo "url: $U"
  [ "$(curl -s "$U" | md5 -q)" = "$(md5 -q "$F")" ] && echo "md5 OK" || { echo "md5 MISMATCH"; exit 1; }
  D=~/Downloads/LawWorld_reels_27oct; mkdir -p $D
  cp "$F" "$D/${STEM}_9x16.mp4"; cp "/Users/admin/Downloads/New short/product-explainer/out/$SET/thumb_brand.png" "$D/${STEM}_thumbnail.png"
  echo "copied to $D/${STEM}_9x16.mp4"
fi
