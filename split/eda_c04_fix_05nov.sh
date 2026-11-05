#!/bin/zsh
# 05-11-2026: eda c04 pushes in mid-take (head cut in the 9:16 band at 37-39 s) -> re-take c04 on main, flatten, re-post eda.
cd "/Users/admin/Downloads/New short/product-explainer"; export PATH=/usr/local/bin:$PATH
mkdir -p downloads/eda/rejected
mv downloads/eda/c04.mp4 downloads/eda/rejected/c04_pushin.mp4; mv downloads/eda/c04.words.json downloads/eda/rejected/c04_pushin.words.json; mv downloads/eda/flat/c04.mp4 downloads/eda/rejected/c04_pushin_flat.mp4 2>/dev/null
( source split/eda_env.sh && zsh split/run_queue.sh c04 ) > logs/queue_eda_c04.log 2>&1
grep -E "words\] c04" logs/queue_eda_c04.log | tail -1
python3 -c "import json,sys; sys.exit(0 if json.load(open('downloads/eda/c04.words.json')).get('keep') else 1)" || { echo "eda c04 retake NOT kept"; exit 1; }
FLATTEN_PRESET=veryfast python3 split/flatten_bg.py --seam left downloads/eda/c04.mp4 2>&1 | grep -E "^\[flatten\]" | cut -c1-200
stem=$(grep -P '^eda\t' split/batch2_04nov.tsv 2>/dev/null | cut -f2); [ -z "$stem" ] && stem=$(awk -F'\t' '$1=="eda"{print $2}' split/batch2_04nov.tsv); slug=$(awk -F'\t' '$1=="eda"{print $3}' split/batch2_04nov.tsv)
echo "$(date +%H:%M:%S) eda post start ($stem)"
V_LAYOUT=judgment NO_DELIVER=1 OVERLAY_WORKERS=1 zsh split/post_course.sh eda $stem > logs/post_eda.log 2>&1 || { echo "$(date +%H:%M:%S) eda POST FAILED"; tail -3 logs/post_eda.log; exit 1; }
python3 split/thumb_darkfoot.py out/eda/thumb_brand.json > logs/thumb_eda.log 2>&1
zsh split/finish_judgment_reel.sh eda qa > logs/qa_eda.log 2>&1
zsh split/finish_judgment_reel.sh eda ship $slug $stem > logs/ship_eda.log 2>&1 && echo "$(date +%H:%M:%S) eda SHIPPED" || echo "$(date +%H:%M:%S) eda SHIP FAILED"
