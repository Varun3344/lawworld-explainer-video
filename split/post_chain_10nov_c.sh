#!/bin/zsh
# 10-Nov evening concept videos (owner "make 2-3 more"): post-production one set at a time, whichever is READY first
# (every clip kept + flattened, and cues reviewed: split/CUESOK_<set>). GEOM_EXTRA=--frames 48 (inj c15 lesson); build_course_plan has the vdur fix.
cd "/Users/admin/Downloads/New short/product-explainer"
typeset -A STEM; STEM=(exd LawWorld_Setting_Aside_an_Ex_Parte_Decree elv LawWorld_Electronic_Evidence_Section_63_BSA mnt LawWorld_Maintenance_Section_144_BNSS)
left=(exd elv mnt)
export GEOM_EXTRA="--frames 48"
while (( ${#left} )); do
  pick=""
  for s in $left; do
    [ -f split/CUESOK_$s ] || continue
    ok=$(python3 - $s <<'PY'
import json, os, sys
s = sys.argv[1]; ids = [x["sceneId"] for x in json.load(open(f"split/{s}_all_scenes.json"))["scenes"]]
bad = [c for c in ids if not (os.path.exists(f"downloads/{s}/{c}.words.json") and json.load(open(f"downloads/{s}/{c}.words.json")).get("keep")
        and os.path.exists(f"downloads/{s}/flat/{c}.mp4") and os.path.getmtime(f"downloads/{s}/flat/{c}.mp4") >= os.path.getmtime(f"downloads/{s}/{c}.mp4"))]
print("yes" if not bad else "no")
PY
)
    [ "$ok" = yes ] && { pick=$s; break; }
  done
  if [ -z "$pick" ]; then sleep 60; continue; fi
  echo "[chain] $(date +%H:%M:%S) start $pick" >> logs/post_chain_10nov.log
  zsh split/post_course.sh $pick ${STEM[$pick]} > logs/post_$pick.log 2>&1
  echo "[chain] $(date +%H:%M:%S) $pick exit $?" >> logs/post_chain_10nov.log
  left=(${left:#$pick})
done
