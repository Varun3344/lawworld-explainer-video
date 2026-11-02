"""Reel thumbnail v2, DARK (owner 02-11-2026: "we need to change thumbnail design also, because we are not getting proper views
... that video also unable to see, make a darker view in the downside"). On the Facebook / Instagram grid every cream thumbnail
looked alike and the platform's white view count / play icon at the foot of the tile vanished on the cream.
This design keeps the brand palette (copper / terracotta, cream, ink) and fonts, never the presenter, but:
  - a dark ink page with the court building behind the bench, warm-toned and darkened;
  - a big bold sans headline (Manrope 800) that still reads at grid-tile size, the second line in copper;
  - the strips as copper / glass / cream cards on the dark;
  - the foot of the frame (the bottom ~300 px) plain near-black, where the apps draw the view count, play icon and progress bar.
Same config as split/thumb_brand.py (the classic cream design stays there, unchanged):
  {"head1", "head2", "accent", "strips": [[text, "copper"|"paper"|"ink", icon?] x3], "judges": [[photo, name], ...], "court",
   "badge", "kicker", "out"}
Usage: python3 split/thumb_dark.py <config.json>   (writes cfg["out"], or cfg["out_dark"] when set)"""
import html, json, os, subprocess, sys

cfg = json.load(open(sys.argv[1]))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BRAND = "../brand"   # relative: Chrome loads the woff2 fonts that way (absolute file:// URLs stayed unloaded)
e = html.escape


def head2():
    h, a = cfg["head2"], cfg.get("accent", "")
    if a and a in h:
        i = h.index(a)
        return e(h[:i]) + f'<em>{e(a)}</em>' + e(h[i + len(a):])
    return e(h)


ICON = {"copper": '<path d="M18 6 6 18M6 6l12 12"/>', "paper": '<path d="M9 12l2 2 4-4"/><circle cx="12" cy="12" r="9"/>',
        "ink": '<path d="m16 16 3-8 3 8c-2 1-4 1-6 0"/><path d="m2 16 3-8 3 8c-2 1-4 1-6 0"/><path d="M7 21h10M12 3v18M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2"/>'}
ICON_ALT = {"x": ICON["copper"], "check": ICON["paper"], "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>', "scale": ICON["ink"]}
strips = "".join(
    f'<div class="st {s[1]}"><div class="ic"><svg viewBox="0 0 24 24">{ICON_ALT[s[2]] if len(s) > 2 else ICON[s[1]]}</svg></div><div class="tx">{e(s[0])}</div></div>'
    for s in cfg["strips"])
judges = "".join(
    f'<div class="jd" style="transform:rotate({a}deg)"><div class="fr"><img src="file://{e(p)}"></div><div class="nm">{e(n)}</div></div>'
    for (p, n), a in zip(cfg["judges"], (3, -3, 3)))
court = (f'<div class="court" style="background-image:url(file://{e(cfg["court"])})"></div>' if cfg.get("court") else "")
page = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:"Instrument Serif";font-style:normal;src:url({BRAND}/fonts/Instrument_Serif_jizBRFtNs2ka5fXjeivQ4LroWlx-6zUTjnTLgNs.woff2) format("woff2");}}
@font-face{{font-family:"Instrument Serif";font-style:italic;src:url({BRAND}/fonts/Instrument_Serif_jizHRFtNs2ka5fXjeivQ4LroWlx-6zAjjH7Motmp5g.woff2) format("woff2");}}
@font-face{{font-family:"Manrope";font-weight:200 800;src:url({BRAND}/fonts/Manrope_xn7gYHE41ni1AdIRggexSvfedN4.woff2) format("woff2");}}
:root{{--ink:#15120f;--night:#0b0908;--cream:#f5f0e8;--paper:#fffcf6;--accent:#e08a66;--deep:#b3573f;
      --copper:linear-gradient(135deg,#e8946f 0%,#d97757 40%,#b3573f 100%);}}
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:1080px;height:1920px;overflow:hidden;background:var(--ink);font-family:Manrope,sans-serif;color:var(--cream);-webkit-font-smoothing:antialiased;}}
body{{position:relative;}}
/* warm glow behind the headline, the court band behind the bench, and the plain near-black foot for the apps' view count / play bar */
.glow{{position:absolute;inset:0;background:radial-gradient(900px 700px at 50% 22%,rgba(217,119,87,.22),transparent 70%),
       radial-gradient(1200px 900px at 50% 60%,rgba(255,255,255,.04),transparent 70%);}}
.court{{position:absolute;left:0;width:1080px;background-size:cover;background-position:center 30%;
        filter:sepia(.55) saturate(.85) brightness(.42) contrast(1.08);
        -webkit-mask-image:linear-gradient(to bottom,transparent 0,#000 22%,#000 66%,transparent 100%);}}
.foot{{position:absolute;left:0;right:0;bottom:0;height:520px;background:linear-gradient(to bottom,rgba(11,9,8,0) 0,rgba(11,9,8,.86) 34%,var(--night) 52%);}}
.wrap{{position:absolute;left:0;right:0;top:0;height:1600px;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:0 60px;z-index:2;}}
.top{{display:flex;justify-content:center;align-items:center;gap:20px;}}
.top img.mk{{width:70px;height:70px;filter:drop-shadow(0 8px 18px rgba(0,0,0,.5));}}
.top img.wm{{height:58px;}}
.kick{{margin-top:30px;}}
.kick span{{display:inline-block;background:var(--copper);color:#fff;font-weight:800;font-size:28px;letter-spacing:5px;padding:14px 30px;border-radius:40px;box-shadow:0 14px 30px rgba(179,87,63,.35);}}
h1{{margin-top:30px;width:960px;text-align:center;font-weight:800;letter-spacing:-2px;}}
h1 .l{{display:block;line-height:1.02;text-wrap:balance;}}
h1 .l1{{font-size:118px;color:#fff;text-shadow:0 6px 30px rgba(0,0,0,.45);}}
h1 .l2{{margin-top:14px;font-size:96px;color:var(--accent);}}
h1 em{{font-family:"Instrument Serif",serif;font-style:italic;font-weight:400;font-size:1.22em;letter-spacing:0;color:#f3a37f;}}
.strips{{margin-top:38px;width:920px;display:flex;flex-direction:column;gap:18px;}}
.st{{display:flex;align-items:center;gap:24px;padding:20px 30px;border-radius:26px;font-weight:800;font-size:41px;line-height:1.1;}}
.st .ic{{width:60px;height:60px;border-radius:20px;flex:none;display:flex;align-items:center;justify-content:center;}}
.st svg{{width:38px;height:38px;fill:none;stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round;}}
.st.copper{{background:var(--copper);color:#fff;box-shadow:0 20px 44px rgba(179,87,63,.40);}}
.st.copper .ic{{background:rgba(255,255,255,.2);}} .st.copper svg{{stroke:#fff;}}
.st.paper{{background:rgba(255,255,255,.08);color:#fff;box-shadow:inset 0 0 0 2px rgba(255,255,255,.16);}}
.st.paper .ic{{background:rgba(224,138,102,.22);}} .st.paper svg{{stroke:#f3a37f;}}
.st.ink{{background:var(--cream);color:var(--ink);box-shadow:0 20px 44px rgba(0,0,0,.35);}}
.st.ink .ic{{background:#f5dfd0;}} .st.ink svg{{stroke:var(--deep);}}
.bench{{margin-top:46px;display:flex;justify-content:center;gap:64px;position:relative;z-index:2;}}
.jd{{display:flex;flex-direction:column;align-items:center;gap:20px;}}
.fr{{width:262px;height:330px;padding:12px;background:#fff;border-radius:6px;box-shadow:0 30px 70px rgba(0,0,0,.55);}}
.fr img{{width:100%;height:100%;object-fit:cover;object-position:50% 18%;display:block;border-radius:2px;}}
.bench.j3{{gap:30px;}} .bench.j3 .fr{{width:236px;height:298px;}} .bench.j3 .nm{{font-size:34px;}}
.nm{{font-family:"Instrument Serif",serif;font-size:42px;line-height:1;color:var(--ink);background:rgba(245,240,232,.95);padding:8px 22px 10px;border-radius:30px;}}
.badge{{margin-top:38px;position:relative;z-index:3;}}
.badge span{{display:inline-block;color:#f3a37f;font-weight:800;font-size:32px;letter-spacing:4px;padding:16px 38px;border-radius:44px;box-shadow:inset 0 0 0 3px rgba(224,138,102,.75);background:rgba(11,9,8,.55);}}
</style></head><body>
<div class="glow"></div>{court}<div class="foot"></div>
<div class="wrap">
<div class="top"><img class="mk" src="{BRAND}/site_logo_mark.png"><img class="wm" src="{BRAND}/wordmark_white.png"></div>
<div class="kick"><span>{e(cfg.get("kicker", "JUDGMENT EXPLAINED"))}</span></div>
<h1><span class="l l1">{e(cfg["head1"])}</span><span class="l l2">{head2()}</span></h1>
<div class="strips">{strips}</div>
<div class="bench{" j3" if len(cfg["judges"]) >= 3 else ""}">{judges}</div>
<div class="badge"><span>{e(cfg["badge"])}</span></div>
</div>
<script>window.__layout = () => {{ const c = document.querySelector(".court"), b = document.querySelector(".bench"); if (!c) return;
  const r = b.getBoundingClientRect(); c.style.top = (r.top - 260) + "px"; c.style.height = (r.height + 420) + "px"; }};</script>
</body></html>"""

tmp = os.path.join(ROOT, "overlays", "_thumb_dark.html")
open(tmp, "w").write(page)
out = os.path.abspath(cfg.get("out_dark") or cfg["out"])
js = """
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ headless: true, channel: 'chrome' });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  await p.goto('file://' + process.argv[1]);
  await p.evaluate(async () => { await document.fonts.ready;
    // the headline lines wrap to at most two lines each; shrink a line until it fits two lines inside 960 px
    for (const l of document.querySelectorAll('h1 .l')) { let fs = parseFloat(getComputedStyle(l).fontSize);
      const lh = () => parseFloat(getComputedStyle(l).lineHeight) || fs * 1.02;
      while ((l.scrollWidth > 960 || l.getBoundingClientRect().height > 2.1 * fs * 1.02) && fs > 56) { fs -= 2; l.style.fontSize = fs + 'px'; } }
    // the whole stack must end above the dark foot (y 1600): shrink the bench photos if it does not
    const w = document.querySelector('.wrap'), bd = document.querySelector('.badge');
    for (let k = 0; k < 8 && bd.getBoundingClientRect().bottom > 1560; k++) {
      for (const f of document.querySelectorAll('.fr')) { f.style.width = (f.offsetWidth * 0.93) + 'px'; f.style.height = (f.offsetHeight * 0.93) + 'px'; } }
    if (window.__layout) window.__layout();
    await Promise.all([...document.images].map(i => i.decode().catch(() => {}))); });
  const box = await p.evaluate(() => { const r = document.querySelector('.badge').getBoundingClientRect(); return Math.round(r.bottom); });
  const fams = await p.evaluate(() => [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family + ' ' + f.style));
  await p.screenshot({ path: process.argv[2] });
  console.log('fonts loaded:', fams.join(', '), '| stack ends at y', box); await b.close();
})().catch(e => { console.error(e); process.exit(1); });
"""
r = subprocess.run(["node", "-e", js, tmp, out], cwd=ROOT, capture_output=True, text=True)
print(r.stdout.strip(), r.stderr.strip()[-400:]); r.check_returncode()
print("saved", out)
