#!/bin/zsh
# 10-11-2026 evening: after <set>'s queue ends, recover (zero credits) only if some clip of length <d> is still missing.
# usage: zsh split/recover_if_missing_10nov.sh <set> <d>
cd "/Users/admin/Downloads/New short/product-explainer"; s=$1; d=$2
until grep -q "ALL DONE" logs/queue_$s.log; do sleep 30; done
miss=$(python3 - $s $d <<'PY'
import json, os, sys
s, d = sys.argv[1], int(sys.argv[2])
sc = json.load(open(f"split/{s}_all_scenes.json"))["scenes"]
print(" ".join(x["sceneId"] for x in sc if x["seconds"] == d and not (os.path.exists(f"downloads/{s}/{x['sceneId']}.words.json") and json.load(open(f"downloads/{s}/{x['sceneId']}.words.json")).get("keep"))))
PY
)
echo "$(date +%H:%M:%S) $s missing ${d}s clips: [$miss]"
[ -z "$miss" ] && exit 0
zsh split/recover_after_10nov.sh $s $d
echo "$(date +%H:%M:%S) now match: zsh split/match_recovered_10nov.sh $s <cid> for: $miss"
