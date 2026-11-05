#!/bin/zsh
cd "/Users/admin/Downloads/New short/product-explainer"
until grep -qE "elt (RESHIPPED|RESHIP FAILED|RE-EDIT FAILED)" logs/reedit_final_05nov.log; do sleep 20; done
pkill -f "reedit_final_05nov.sh"; sleep 2
nohup zsh split/reedit_final_05nov_A.sh > logs/reedit_final_05nov_A.log 2>&1 &
nohup zsh split/reedit_final_05nov_B.sh > logs/reedit_final_05nov_B.log 2>&1 &
echo "$(date +%H:%M:%S) split into A + B"
