#!/bin/zsh
# Render one overlay timeline with several headless renderers at once (scripts/render_overlays.ts --from/--to), then check
# that every frame f00000..f(N-1) was written exactly once, by this run.
# Usage (from anywhere): split/render_parallel.sh <page.html> <timeline.json> <outdir> <workers>     [env FPS=24 NICE=10]
#   N = ceil(timeline.duration x FPS) frames (render_overlays.ts's own count), split into <workers> contiguous ranges; each
#   worker is one Playwright Chrome headless with its own temporary profile (no Flow profile is touched), run under
#   nice -n $NICE (the Mac also renders Flow clips); logs <outdir>/.render_w<k>.log. Paths may be relative to the caller's folder.
# Verification (exit 1 on any failure, 0 = all good):
#   - every worker exited 0 and logged "done: range A-B of N" for exactly the range it was given;
#   - the ranges tile 0..N-1 with no gap and no overlap (each frame belongs to exactly one worker);
#   - every f%05d.png 0..N-1 exists, is a PNG and was written during this run (mtime after the start), so a frame left over
#     from an earlier render cannot pass for a missing one;
#   - frames numbered >= N (left over from an older, longer timeline) are listed as a warning (compose2 reads -t total).
set -u
[ $# -eq 4 ] || { echo "usage: $0 <page.html> <timeline.json> <outdir> <workers>" >&2; exit 2; }
html=${1:A}; tl=${2:A}; out=${3:A}; n=$4; fps=${FPS:-24}; nic=${NICE:-10}       # absolute before the cd below
ROOT="${0:A:h:h}"; cd "$ROOT" || exit 1
[[ $n == <1-> ]] || { echo "[parallel] workers must be a positive integer, not '$n'" >&2; exit 2; }
[ -f "$html" ] && [ -f "$tl" ] || { echo "[parallel] missing $html or $tl" >&2; exit 2; }
TSX=./node_modules/.bin/tsx
total=$(python3 -c "import json,math,sys; print(math.ceil(json.load(open(sys.argv[1]))['duration']*float(sys.argv[2])))" "$tl" "$fps") || exit 2
(( total > 0 )) || { echo "[parallel] timeline has no frames" >&2; exit 2; }
(( n > total )) && n=$total
chunk=$(( (total + n - 1) / n ))
mkdir -p "$out"; marker="$out/.render_start"; : > "$marker"; sleep 1      # mtimes of this run's frames are >= the marker's
t0=$(date +%s); pids=(); ranges=()
for (( k = 0; k < n; k++ )); do
  a=$(( k * chunk )); b=$(( a + chunk - 1 )); (( b > total - 1 )) && b=$(( total - 1 ))
  (( a > b )) && break
  ranges+=("$a-$b")
  nice -n $nic $TSX scripts/render_overlays.ts --html "$html" --timeline "$tl" --out "$out" --fps $fps --from $a --to $b > "$out/.render_w$k.log" 2>&1 &
  pids+=($!)
done
echo "[parallel] $total frames, ${#pids} workers: ${ranges[*]}"
rcs=()
for pid in $pids; do wait $pid; rcs+=($?); done
python3 - "$out" "$total" "$marker" "${rcs[*]}" $ranges <<'EOF'
import os, re, sys, glob
out, total, marker, rcs, ranges = sys.argv[1], int(sys.argv[2]), sys.argv[3], [int(x) for x in sys.argv[4].split()], sys.argv[5:]
start = os.path.getmtime(marker); bad = []
rg = [tuple(int(v) for v in r.split("-")) for r in ranges]
for k, ((a, b), rc) in enumerate(zip(rg, rcs)):
    log = open(f"{out}/.render_w{k}.log").read()
    m = re.search(r"done: range (\d+)-(\d+) of (\d+): (\d+) frames", log)
    errl = [l for l in log.splitlines() if "Error" in l or "error" in l]
    if rc != 0: bad.append(f"worker {k} ({a}-{b}) exited {rc}: {(errl[0] if errl else (log.strip().splitlines() or ['no output'])[-1]).strip()[:200]}")
    elif not m: bad.append(f"worker {k} ({a}-{b}) logged no 'done: range' line")
    elif (int(m[1]), int(m[2]), int(m[3]), int(m[4])) != (a, b, total, b - a + 1): bad.append(f"worker {k} rendered {m[0]!r}, was given {a}-{b} of {total}")
cover = [0] * total
for a, b in rg:
    for i in range(a, b + 1): cover[i] += 1
gaps = [i for i, c in enumerate(cover) if c == 0]; dup = [i for i, c in enumerate(cover) if c > 1]
if gaps: bad.append(f"{len(gaps)} frames in no worker's range (first {gaps[0]})")
if dup: bad.append(f"{len(dup)} frames in more than one range (first {dup[0]})")
missing, notpng, stale = [], [], []
for i in range(total):
    p = f"{out}/f{i:05d}.png"
    if not os.path.isfile(p): missing.append(i); continue
    with open(p, "rb") as fh:
        if fh.read(8) != b"\x89PNG\r\n\x1a\n": notpng.append(i)
    if os.path.getmtime(p) < start: stale.append(i)
for name, lst in (("missing", missing), ("not a PNG", notpng), ("not written by this run (older file)", stale)):
    if lst: bad.append(f"{len(lst)} frames {name} (first f{lst[0]:05d}.png)")
extra = sorted(int(os.path.basename(f)[1:-4]) for f in glob.glob(f"{out}/f[0-9][0-9][0-9][0-9][0-9].png") if int(os.path.basename(f)[1:-4]) >= total)
if extra: print(f"[parallel] WARNING {len(extra)} older frames past the end of this timeline (f{extra[0]:05d}..f{extra[-1]:05d}.png): delete them if this folder is reused")
for b_ in bad: print("[parallel] FAIL " + b_)
print(f"[parallel] {'OK' if not bad else 'FAILED'}: frames 0..{total - 1}, each written once by this run" if not bad else "[parallel] FAILED")
sys.exit(1 if bad else 0)
EOF
rc=$?
echo "[parallel] $(( $(date +%s) - t0 ))s"
exit $rc
