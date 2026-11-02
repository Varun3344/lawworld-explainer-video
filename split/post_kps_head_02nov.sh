#!/bin/zsh
# 02-11-2026: kps 9:16 rebuilt with the measured head line (owner: "head is cutting ... looks as two parts"); 16:9 and overlays unchanged.
cd "/Users/admin/Downloads/New short/product-explainer"; export PATH=/usr/local/bin:$PATH; export V_LAYOUT=judgment
echo "$(date +%H:%M:%S) kps 9:16 rebuild start"
python3 split/build_vertical_course.py kps ptrack split > out/kps/v_ptrack.log 2>&1 || { echo "ptrack FAILED"; tail -3 out/kps/v_ptrack.log; exit 1; }
grep -E "head" out/kps/v_ptrack.log
python3 split/build_vertical_course.py kps edit && python3 split/build_vertical_course.py kps final > out/kps/v_final.log 2>&1 || { echo "final FAILED"; tail -3 out/kps/v_final.log; exit 1; }
zsh split/finish_judgment_reel.sh kps qa > logs/qa_kps.log 2>&1; echo "$(date +%H:%M:%S) qa exit $?"
zsh split/finish_judgment_reel.sh kps ship bank-of-india-v-kamal-pasha-2026-insc-1154 SC_BankOfIndia_v_KamalPasha_2026INSC1154_CoC_cannot_withdraw_approved_plan > logs/ship_kps.log 2>&1; echo "$(date +%H:%M:%S) ship exit $?"; tail -3 logs/ship_kps.log
