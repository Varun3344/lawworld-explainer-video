#!/bin/zsh
# 31-10-2026 QA: vzj c08 verdict rows were drawn struck-through (ok=False) though they are the Court's findings; rows fixed to ok=True, rebuild.
cd "/Users/admin/Downloads/New short/product-explainer"
while [ $(pgrep -f "post_course.sh " | wc -l) -ge 2 ]; do sleep 20; done
echo "$(date +%H:%M:%S) post vzj (redo) start"
V_LAYOUT=judgment NO_DELIVER=1 OVERLAY_WORKERS=1 zsh split/post_course.sh vzj Kerala_WPC_34157_2022_Vizhinjam_expert_committee_conflict > logs/post_vzj.log 2>&1
echo "$(date +%H:%M:%S) post vzj (redo) post_course exit $?"
zsh split/finish_judgment_reel.sh vzj qa > logs/qa_vzj.log 2>&1; echo "$(date +%H:%M:%S) post vzj (redo) done (qa exit $?)"
