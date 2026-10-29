#!/bin/zsh
# one afternoon reel: wait for its render, edit, thumbnail, QA. usage: zsh split/post_one_29oct.sh <set> <stem>
cd "/Users/admin/Downloads/New short/product-explainer"; s=$1; stem=$2
until grep -q "ALL DONE" logs/queue_$s.log 2>/dev/null; do sleep 20; done
if [ "$s" = "czs" ]; then export CAP_FONT="Kannada Sangam MN" QA_LANG=kn; fi
echo "$(date +%H:%M:%S) post $s start" >> logs/post_chain_29oct_pm.log
V_LAYOUT=judgment NO_DELIVER=1 OVERLAY_WORKERS=1 zsh split/post_course.sh $s $stem > logs/post_$s.log 2>&1
python3 split/thumb_brand.py out/$s/thumb_brand.json > logs/thumb_$s.log 2>&1
zsh split/finish_judgment_reel.sh $s qa > logs/qa_$s.log 2>&1
echo "$(date +%H:%M:%S) post $s done (qa exit $?)" >> logs/post_chain_29oct_pm.log
