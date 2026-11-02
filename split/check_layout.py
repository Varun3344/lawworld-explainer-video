"""Card layout check for a course / judgment reel timeline (owner 02-11-2026, after the kps case bar was hidden under c04's step boxes:
"dont make those type of faults again").
For every content cue (not the panel chrome, sting, end card, name tag or kicker), at the moment it is fully built (its last build
+ 0.6 s, inside its span), each cue on screen at that moment is rendered ALONE by the real overlay page (overlays/split_panel.html,
the same __init / __seek the frame renderer uses) and their opaque pixels are compared:
  OVERLAP   two cards on screen together cover the same pixels (> 300 px at alpha > 110: shadows and soft edges don't count)
  CUT       a card's opaque pixels fall outside what the 9:16 judgment reel shows of the panel (frame x 76..1204, y < 1076)
Prints one line per problem and "LAYOUT OK" / "LAYOUT FAIL n". Exit 0 when OK, 1 on any fault.
Usage: V_LAYOUT=judgment python3 split/check_layout.py <set> [--mock]        (--mock: out/<set>_mock/timeline.json, before any clip is rendered)"""
import json, os, subprocess, sys, tempfile
from PIL import Image

SET = sys.argv[1]; MOCK = "--mock" in sys.argv
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TL = os.path.join(ROOT, "out", f"{SET}_mock" if MOCK else SET, "timeline.json")
HTML = os.path.join(ROOT, "overlays", "split_panel.html")
X0, X1, YMAX = 76, 1204, 1076          # build_vertical_course.py G_CROP (76, 1128): the 9:16 judgment panel column
JUDG = os.environ.get("V_LAYOUT") == "judgment"   # the CUT test applies to judgment reels (course videos show the whole panel)
ALPHA, MIN_OVER, MIN_CUT = 110, 300, 200
tmp = tempfile.mkdtemp(prefix=f"layout_{SET}_")

JS = r"""
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const [html, tlPath, outDir] = process.argv.slice(1);
(async () => {
  const tl = JSON.parse(fs.readFileSync(tlPath, 'utf8'));
  const b = await chromium.launch({ headless: true, channel: 'chrome' });
  const p = await b.newPage({ viewport: { width: tl.width ?? 1920, height: tl.height ?? 1080 }, deviceScaleFactor: 1 });
  await p.goto('file://' + html); await p.evaluate(() => document.fonts.ready);
  await p.evaluate((t) => window.__init(t), tl);
  const plan = await p.evaluate(() => {
    const SKIP = ['panel', 'sting', 'endcard', 'lower_third', 'kicker'];
    const builds = (c) => { const ts = [c.at, c.head_at, c.track_at];
      for (const k of ['items', 'rows', 'steps', 'points', 'nodes', 'terms', 'cols', 'judges']) for (const it of (c[k] || [])) {
        ts.push(it.at, it.strike_at); for (const v of (it.cells_at || [])) ts.push(v); }
      for (const k of ['left', 'right', 'verdict', 'note', 'merge', 'fold']) { const v = c[k]; if (v && typeof v === 'object') ts.push(v.at); }
      return ts.filter((x) => typeof x === 'number'); };
    const label = (c) => String(c.head || c.text || c.tag || c.title || ((c.steps || c.nodes || c.items || c.rows || [])[0] || {}).label
      || ((c.items || c.rows || [])[0] || {}).text || '').slice(0, 60);
    return EL.map((x, i) => ({ i, type: x.c.type, t0: x.c.t0, t1: (x.end ?? x.c.t1), b: builds(x.c), label: label(x.c) }))
             .filter((o) => !SKIP.includes(o.type));
  });
  const checks = [];
  for (const o of plan) {
    let t = Math.max(o.t0 + 0.6, o.b.length ? Math.max(...o.b) + 0.6 : o.t0 + 0.6);
    t = Math.min(t, o.t1 - 0.08);
    const active = plan.filter((q) => q.t0 <= t && t <= q.t1).map((q) => q.i);
    const files = {};
    for (const i of active) {
      await p.evaluate(([t, i]) => { window.__seek(t);
        EL.forEach((x, k) => { if (k !== i) { x.el.style.visibility = 'hidden'; if (x.el2) x.el2.style.visibility = 'hidden'; } }); }, [t, i]);
      const f = path.join(outDir, `c${o.i}_at${t.toFixed(2)}_cue${i}.png`);
      await p.screenshot({ path: f, omitBackground: true, type: 'png' }); files[i] = f;
    }
    checks.push({ cue: o.i, type: o.type, label: o.label, t: +t.toFixed(2), files });
  }
  fs.writeFileSync(path.join(outDir, 'checks.json'), JSON.stringify({ plan, checks }));
  await b.close();
})().catch((e) => { console.error(e); process.exit(1); });
"""
r = subprocess.run(["node", "-e", JS, HTML, TL, tmp], cwd=ROOT, capture_output=True, text=True)
if r.returncode: sys.exit(f"[layout] renderer failed: {r.stderr.strip()[-600:]}")
data = json.load(open(os.path.join(tmp, "checks.json"))); info = {o["i"]: o for o in data["plan"]}
masks = {}
def mask(f):
    if f not in masks: masks[f] = Image.open(f).getchannel("A").point(lambda a: 255 if a > ALPHA else 0)
    return masks[f]
def count(m): return m.histogram()[255]
faults, seen = [], set()
for ch in data["checks"]:
    me = ch["cue"]; files = {int(k): v for k, v in ch["files"].items()}
    m = mask(files[me]); w, h = m.size
    cut = count(m.crop((0, 0, X0, h))) + count(m.crop((X1, 0, w, h))) + count(m.crop((X0, YMAX, X1, h)))
    if JUDG and cut > MIN_CUT: faults.append(f"CUT      t {ch['t']:6.2f}  {ch['type']:9} '{ch['label']}': {cut} px outside the 9:16 panel column")
    for other, f in files.items():
        # every pair is measured at EVERY card's fully-built moment (a pair first met while one card was still building - kps
        # c04's step boxes vs the case bar - must not be skipped later); a failing pair is reported once
        if other == me or (min(me, other), max(me, other)) in seen: continue
        from PIL import ImageChops
        n = count(ImageChops.multiply(m, mask(f)))
        if n > MIN_OVER:
            seen.add((min(me, other), max(me, other)))
            o = info[other]
            faults.append(f"OVERLAP  t {ch['t']:6.2f}  {ch['type']:9} '{ch['label']}'  x  {o['type']} '{o['label']}': {n} px")
for f in faults: print("[layout]", f)
if os.environ.get("LAYOUT_DEBUG"): print("[layout] frames in", tmp)
print(f"[layout] {SET}: {len(data['checks'])} cards checked, " + ("LAYOUT OK" if not faults else f"LAYOUT FAIL {len(faults)}"))
sys.exit(1 if faults else 0)
