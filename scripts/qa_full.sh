#!/bin/zsh
# Delivery checks for a finished cut: stream durations/frame counts, loudness, frame sheets, transcript of the mix.
V=$1; S=/private/tmp/claude-501/-Users-admin-Downloads-New-short/8f2b0605-28fa-45d1-a69f-5fd2e6b48b14/scratchpad
cd "/Users/admin/Downloads/New short/product-explainer"
echo "== streams =="; ffprobe -v error -select_streams v -show_entries stream=width,height,duration,nb_frames,r_frame_rate -of default=nw=1 $V; ffprobe -v error -select_streams a -show_entries stream=duration,sample_rate -of default=nw=1 $V
echo "== loudness =="; ffmpeg -hide_banner -nostats -i $V -af "ebur128=peak=true" -f null - 2>&1 | grep -E "I:|Peak:" | tail -2
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $V)
echo "== frame sheets (24 points) =="
i=0; for t in 0.04 1.5 5 9 15 21 24 30 37 45 55 63 72 80 90 98 105 113 121 130 140 150 160 170; do i=$((i+1)); ffmpeg -v error -y -i $V -ss $t -frames:v 1 -vf scale=180:320 "$S/q_$(printf %02d $i).png"; done
ffmpeg -v error -y -i $V -ss $(python3 -c "print(max(0,$D-0.05))") -frames:v 1 -vf scale=180:320 "$S/q_last.png"
for r in 1 2 3; do a=$(( (r-1)*8+1 )); args=(); for k in $(seq $a $((a+7))); do args+=(-i "$S/q_$(printf %02d $k).png"); done; ffmpeg -v error -y "${args[@]}" -filter_complex "[0][1][2][3][4][5][6][7]hstack=inputs=8" "$S/qa_sheet_$r.png"; done
echo "== transcript of the mix =="; OK=$(grep -E "^OPENAI_API_KEY=" "/Users/admin/Downloads/New short/Google Flow AI Video/.env" | cut -d= -f2- | tr -d '"'); ffmpeg -v error -y -i $V -vn -ac 1 -ar 16000 -b:a 64k -f mp3 /tmp/qa_mix.mp3 2>/dev/null; curl -s -m 180 https://api.openai.com/v1/audio/transcriptions -H "Authorization: Bearer $OK" -F file=@/tmp/qa_mix.mp3 -F model=whisper-1 -F response_format=text -F language=en -F "prompt=LawWorld, Ravishankar, advocate, AI chatbot, e-courts, DPDP Act, Pay-as-you-go, GST."
