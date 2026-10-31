#!/bin/zsh
# 31-10-2026: post-production for the SC judgment reel cdp (2026 INSC 1177) once its renders finish.
cd "/Users/admin/Downloads/New short/product-explainer"
s=cdp; stem=SC_GirishbhaiPatel_2026INSC1177_consent_decree_nonparty_appeal
until grep -q "ALL DONE" logs/queue_$s.log 2>/dev/null; do sleep 20; done
echo "$(date +%H:%M:%S) post $s start"
V_LAYOUT=judgment NO_DELIVER=1 OVERLAY_WORKERS=1 zsh split/post_course.sh $s $stem > logs/post_$s.log 2>&1
echo "$(date +%H:%M:%S) post $s post_course exit $?"
python3 split/thumb_brand.py out/$s/thumb_brand.json > logs/thumb_$s.log 2>&1
zsh split/finish_judgment_reel.sh $s qa > logs/qa_$s.log 2>&1
echo "$(date +%H:%M:%S) post $s done (qa exit $?)"
