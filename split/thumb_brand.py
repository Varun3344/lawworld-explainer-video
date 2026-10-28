"""Reel thumbnail in the LawWorld video palette (owner 26-10-2026: "for that thumbnail also use our colour palette theme").
Same layout as reel-service work/review/thumb_2judges.py (headline, three strips, the bench as framed official photos, badge; never
the presenter), drawn as an HTML page with the concept videos' own fonts and colours (cream, terracotta / copper, ink; Instrument
Serif + Manrope) and screenshotted by headless Chrome at 1080x1920.
Usage: python3 split/thumb_brand.py <config.json>
config: {"head1", "head2", "accent" (words of head2 set in italic copper), "strips": [[text, "copper"|"paper"|"ink"], x3],
         "judges": [[photo, name], ...], "court" (building photo, optional), "badge", "kicker", "out"}"""
import html, json, os, subprocess, sys

cfg = json.load(open(sys.argv[1]))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BRAND = "../brand"   # relative, as overlays/split_panel.html does: Chrome loads the woff2 fonts that way (absolute file:// URLs stayed unloaded)
e = html.escape


KN = "kn" if any("\u0C80" <= ch <= "\u0CFF" for ch in cfg["head1"] + cfg["head2"]) else ""


def head2():
    h, a = cfg["head2"], cfg.get("accent", "")
    if a and a in h:
        i = h.index(a)
        return e(h[:i]) + f'<em>{e(a)}</em>' + e(h[i + len(a):])
    return e(h)


ICON = {"copper": '<path d="M18 6 6 18M6 6l12 12"/>', "paper": '<path d="M9 12l2 2 4-4"/><circle cx="12" cy="12" r="9"/>',
        "ink": '<path d="m16 16 3-8 3 8c-2 1-4 1-6 0"/><path d="m2 16 3-8 3 8c-2 1-4 1-6 0"/><path d="M7 21h10M12 3v18M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2"/>'}
# optional 3rd item: an icon override, e.g. ["Cheque acknowledges the debt", "copper", "arrow"] (28-10-2026: the copper strip's x
# read as "not" on a strip that states the holding)
ICON_ALT = {"x": ICON["copper"], "check": ICON["paper"], "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>', "scale": ICON["ink"]}
strips = "".join(
    f'<div class="st {s[1]}"><div class="ic"><svg viewBox="0 0 24 24">{ICON_ALT[s[2]] if len(s) > 2 else ICON[s[1]]}</svg></div><div class="tx">{e(s[0])}</div></div>'
    for s in cfg["strips"])
judges = "".join(
    f'<div class="jd" style="transform:rotate({a}deg)"><div class="fr"><img src="file://{e(p)}"></div><div class="nm">{e(n)}</div></div>'
    for (p, n), a in zip(cfg["judges"], (3, -3)))

court = (f'<div class="court" style="background-image:url(file://{e(cfg["court"])})"></div>' if cfg.get("court") else "")
page = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:"Instrument Serif";font-style:normal;src:url({BRAND}/fonts/Instrument_Serif_jizBRFtNs2ka5fXjeivQ4LroWlx-6zUTjnTLgNs.woff2) format("woff2");}}
@font-face{{font-family:"Instrument Serif";font-style:italic;src:url({BRAND}/fonts/Instrument_Serif_jizHRFtNs2ka5fXjeivQ4LroWlx-6zAjjH7Motmp5g.woff2) format("woff2");}}
@font-face{{font-family:"Manrope";font-weight:200 800;src:url({BRAND}/fonts/Manrope_xn7gYHE41ni1AdIRggexSvfedN4.woff2) format("woff2");}}
@font-face{{font-family:"Noto Serif Kannada";font-weight:400;src:url({BRAND}/fonts/Noto_Serif_Kannada_400.woff2) format("woff2");}}
@font-face{{font-family:"Noto Serif Kannada";font-weight:700;src:url({BRAND}/fonts/Noto_Serif_Kannada_700.woff2) format("woff2");}}
@font-face{{font-family:"Noto Sans Kannada";font-weight:400;src:url({BRAND}/fonts/Noto_Sans_Kannada_400.woff2) format("woff2");}}
@font-face{{font-family:"Noto Sans Kannada";font-weight:700;src:url({BRAND}/fonts/Noto_Sans_Kannada_700.woff2) format("woff2");}}
:root{{--cream:#f5f0e8;--paper:#fffcf6;--ink:#1f1e1d;--muted:#6b6660;--rule:#e0d7c6;--accent:#cc785c;--deep:#b3573f;--wash:#f5dfd0;
      --copper:linear-gradient(135deg,#de8a6a 0%,#d97757 38%,#b3573f 100%);}}
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:1080px;height:1920px;overflow:hidden;background:var(--cream);font-family:Manrope,"Noto Sans Kannada",sans-serif;color:var(--ink);-webkit-font-smoothing:antialiased;}}
body{{display:flex;flex-direction:column;align-items:center;justify-content:center;padding:0 70px 150px;}}   /* owner 26-10: everything in the middle (player bar / app UI cover the foot) */
.top{{display:flex;justify-content:center;align-items:center;gap:22px;}}
.top img.mk{{width:76px;height:76px;filter:drop-shadow(0 8px 16px rgba(120,60,30,.25));}}
.top img.wm{{height:64px;}}
.kick{{margin-top:30px;}}
.kick span{{display:inline-block;background:var(--wash);color:var(--deep);font-weight:800;font-size:28px;letter-spacing:4px;padding:14px 30px;border-radius:40px;box-shadow:inset 0 0 0 2px rgba(179,87,63,.18);}}
h1{{margin-top:24px;width:940px;text-align:center;font-family:"Instrument Serif","Noto Serif Kannada",serif;font-weight:400;letter-spacing:-1px;}}
h1 .l{{display:block;white-space:nowrap;line-height:1.02;}}
h1.kn .l{{line-height:1.32;}} h1.kn .l2{{margin-top:6px;}}
h1 .l1{{font-size:140px;}} h1 .l2{{font-size:112px;}}
h1 em{{font-style:italic;color:var(--deep);}}
.rule{{margin-top:24px;width:300px;height:6px;border-radius:3px;background:var(--copper);flex:none;}}
.strips{{margin-top:32px;width:900px;display:flex;flex-direction:column;gap:20px;}}
.st{{display:flex;align-items:center;gap:26px;padding:22px 32px;border-radius:28px;font-weight:700;font-size:42px;line-height:1.1;}}
.st .ic{{width:64px;height:64px;border-radius:22px;flex:none;display:flex;align-items:center;justify-content:center;}}
.st svg{{width:40px;height:40px;fill:none;stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round;}}
.st.copper{{background:var(--copper);color:#fff;box-shadow:0 22px 50px rgba(179,87,63,.30);}}
.st.copper .ic{{background:rgba(255,255,255,.18);}} .st.copper svg{{stroke:#fff;}}
.st.paper{{background:var(--paper);border:2px solid var(--rule);box-shadow:0 22px 50px rgba(60,40,25,.10);}}
.st.paper .ic{{background:var(--wash);}} .st.paper svg{{stroke:var(--deep);}}
.st.ink{{background:#1f1e1d;color:#f7f1e8;box-shadow:0 22px 50px rgba(30,20,15,.28);}}
.st.ink .ic{{background:rgba(255,255,255,.08);box-shadow:inset 0 0 0 2px rgba(255,255,255,.10);}} .st.ink svg{{stroke:#e9a283;}}
.bench{{margin-top:50px;display:flex;justify-content:center;gap:70px;position:relative;z-index:2;}}
.court{{position:absolute;left:0;width:1080px;z-index:1;background-size:cover;background-position:center 32%;opacity:.92;filter:sepia(.62) saturate(.78) brightness(1.06) contrast(.94);-webkit-mask-image:linear-gradient(to bottom,transparent 0,#000 26%,#000 70%,transparent 100%);mask-image:linear-gradient(to bottom,transparent 0,#000 26%,#000 70%,transparent 100%);}}
.strips{{position:relative;z-index:3;}}
.nm{{background:rgba(245,240,232,.94);padding:8px 24px 10px;border-radius:30px;box-shadow:0 8px 20px rgba(60,40,25,.12);}}
.jd{{display:flex;flex-direction:column;align-items:center;gap:22px;}}
.fr{{width:290px;height:366px;padding:13px;background:#fff;border-radius:6px;box-shadow:0 30px 64px rgba(60,40,25,.22),0 3px 8px rgba(60,40,25,.10);}}
.fr img{{width:100%;height:100%;object-fit:cover;object-position:50% 18%;display:block;border-radius:2px;}}
.nm{{font-family:"Instrument Serif","Noto Serif Kannada",serif;font-size:44px;line-height:1;color:var(--ink);}}
.badge{{margin-top:40px;text-align:center;position:relative;z-index:3;}}
.badge span{{display:inline-block;background:#1f1e1d;color:#e9a283;font-weight:800;font-size:34px;letter-spacing:4px;padding:20px 42px;border-radius:44px;box-shadow:0 18px 40px rgba(30,20,15,.25);}}
</style></head><body>
<div class="top"><img class="mk" src="{BRAND}/site_logo_mark.png"><img class="wm" src="{BRAND}/wordmark_ink.png"></div>
<div class="kick"><span>{e(cfg.get("kicker", "JUDGMENT EXPLAINED"))}</span></div>
<h1 class="{KN}"><span class="l l1">{e(cfg["head1"])}</span><span class="l l2">{head2()}</span></h1>
<div class="rule"></div>
<div class="strips">{strips}</div>
{court}<div class="bench">{judges}</div>
<script>window.__layout = () => {{ const c = document.querySelector(".court"), b = document.querySelector(".bench"); if (!c) return;
  const r = b.getBoundingClientRect(); c.style.top = (r.top - 150) + "px"; c.style.height = (r.height + 230) + "px"; }};</script>
<div class="badge"><span>{e(cfg["badge"])}</span></div>
</body></html>"""

tmp = os.path.join(ROOT, "overlays", "_thumb_brand.html")
os.makedirs(os.path.dirname(tmp), exist_ok=True)
open(tmp, "w").write(page)
out = os.path.abspath(cfg["out"])
js = """
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ headless: true, channel: 'chrome' });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  await p.goto('file://' + process.argv[1]);
  await p.evaluate(async () => { await document.fonts.ready; if (window.__layout) window.__layout();
    for (const l of document.querySelectorAll('h1 .l')) { let fs = parseFloat(getComputedStyle(l).fontSize);
      while (l.scrollWidth > 940 && fs > 60) { fs -= 2; l.style.fontSize = fs + 'px'; } }
    await Promise.all([...document.images].map(i => i.decode().catch(() => {}))); });
  const fams = await p.evaluate(() => [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family + ' ' + f.style));
  await p.screenshot({ path: process.argv[2] });
  console.log('fonts loaded:', fams.join(', ')); await b.close();
})().catch(e => { console.error(e); process.exit(1); });
"""
r = subprocess.run(["node", "-e", js, tmp, out], cwd=ROOT, capture_output=True, text=True)
print(r.stdout.strip(), r.stderr.strip()[-400:]); r.check_returncode()
print("saved", out)
