#!/bin/zsh
# One flatten worker for every course set (the Mac cannot run three plus the overlay renders): flattens the OLDEST kept clip
# (by its source file's time) whose flat copy is missing or older than the source, across all listed sets - first come, first
# served, so no set starves while another keeps rendering; exits when every listed set is complete.
# Usage: zsh split/flatten_all.sh cog cpb apl dfc cus bail plt trl   (two of them may run at once: each skips a clip the other has)
cd "/Users/admin/Downloads/New short/product-explainer"
while true; do
  next=$(python3 - "$@" <<'PY'
import json, os, subprocess, sys
busy = subprocess.run(["ps", "-axo", "command="], capture_output=True, text=True).stdout   # clips another worker is flattening now
todo, left = [], 0
for s in sys.argv[1:]:
    p = f"split/{s}_all_scenes.json"
    if not os.path.exists(p): continue
    for sc in json.load(open(p))["scenes"]:
        c = sc["sceneId"]; src, flat, w = f"downloads/{s}/{c}.mp4", f"downloads/{s}/flat/{c}.mp4", f"downloads/{s}/{c}.words.json"
        if os.path.exists(flat) and os.path.exists(src) and os.path.getmtime(flat) >= os.path.getmtime(src): continue
        left += 1
        try: keep = os.path.exists(src) and json.load(open(w)).get("keep")
        except Exception: keep = False
        if keep and f"flatten_bg.py --seam left {src}" not in busy: todo.append((os.path.getmtime(src), src))
print(sorted(todo)[0][1] if todo else ("DONE" if left == 0 else "WAIT"))
PY
)
  if [ "$next" = "DONE" ]; then echo "$(date +%H:%M:%S) all sets flat"; break; fi
  if [ "$next" = "WAIT" ]; then sleep 20; continue; fi
  # claim the clip atomically (mkdir): the ps check alone let both workers take the same new clip, and their outputs collided (19-10)
  lock="${next:h}/flat/.lock_${next:t:r}"; mkdir -p "${next:h}/flat"
  find "$lock" -maxdepth 0 -mmin +15 -exec rmdir {} \; 2>/dev/null      # a stale claim (killed worker) expires after 15 min
  if ! mkdir "$lock" 2>/dev/null; then sleep 5; continue; fi
  FLATTEN_PRESET=veryfast nice -n 10 python3 split/flatten_bg.py --seam left $next 2>&1 | grep -E "^\[flatten\]" | sed "s/^/$(date +%H:%M:%S) /" | cut -c1-260
  rmdir "$lock"
done
