#!/bin/zsh
# Kannada suo motu PIL reel, owner fixes 04-11-2026: new c10 + c11 (proper ending), full presenter only at the start.
cd "/Users/admin/Downloads/New short/product-explainer"; export PATH=/usr/local/bin:$PATH
until grep -q "ALL DONE" logs/queue_apk_end.log 2>/dev/null; do sleep 15; done
echo "$(date +%H:%M:%S) apk clips done" >> logs/pil_fix_04nov.log
zsh split/flatten_all.sh apk > logs/flatten_apk_end.log 2>&1
echo "$(date +%H:%M:%S) apk flat" >> logs/pil_fix_04nov.log
export CAP_FONT="Kannada Sangam MN" QA_LANG=kn
V_LAYOUT=judgment NO_DELIVER=1 OVERLAY_WORKERS=2 zsh split/post_course.sh apk KHC_SuoMotu_PIL_Advocates_safety_03_11_2026_Kannada > logs/post_apk.log 2>&1 || { echo "$(date +%H:%M:%S) apk POST FAILED" >> logs/pil_fix_04nov.log; exit 1; }
python3 split/thumb_darkfoot.py out/apk/thumb_brand.json > logs/thumb_apk.log 2>&1
zsh split/finish_judgment_reel.sh apk qa > logs/qa_apk.log 2>&1
zsh split/finish_judgment_reel.sh apk ship suo-motu-pil-advocates-safety-khc-03-11-2026-kannada KHC_SuoMotu_PIL_Advocates_safety_03_11_2026_Kannada > logs/ship_apk.log 2>&1 && echo "$(date +%H:%M:%S) apk RESHIPPED" >> logs/pil_fix_04nov.log || echo "$(date +%H:%M:%S) apk reship FAILED" >> logs/pil_fix_04nov.log
