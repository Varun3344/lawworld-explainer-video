"""Reel thumbnail v4, POSTER (owner 02-11-2026, after v3: "this is looking like two different image and that 3 points design is not
looking good, even the colours also, make a different design"). One picture top to bottom: the court building fills the whole
frame, toned with gradients so the text stays readable, the foot near-black for the apps' view count / play bar. The three points
are ONE numbered list (copper number discs), not three coloured bars. The bench as round portraits. Never the presenter.
Two looks (cfg "look" or the 2nd argument):
  dark   the photo under a deep ink tint at the top: white headline, the second line in copper
  light  the photo under a cream wash at the top: ink serif headline as the classic thumbnails, the list on a white card
Same config as split/thumb_brand.py: {"head1", "head2", "accent", "strips": [[text, ...] x3], "judges": [[photo, name], ...],
"court", "badge", "kicker", "out"}; writes cfg["out_poster"] (with {look} filled in) when set, else cfg["out"].
Usage: python3 split/thumb_poster.py <config.json> [dark|light]"""
import html, json, os, subprocess, sys

cfg = json.load(open(sys.argv[1]))
LOOK = (sys.argv[2] if len(sys.argv) > 2 else cfg.get("look", "dark"))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BRAND = "../brand"
e = html.escape


def head2():
    h, a = cfg["head2"], cfg.get("accent", "")
    if a and a in h:
        i = h.index(a)
        return e(h[:i]) + f'<em>{e(a)}</em>' + e(h[i + len(a):])
    return e(h)


points = "".join(f'<div class="pt"><div class="n">{k}</div><div class="tx">{e(s[0])}</div></div>' for k, s in enumerate(cfg["strips"], 1))
judges = "".join(f'<div class="jd"><div class="ring"><img src="file://{e(p)}"></div><div class="nm">{e(n)}</div></div>' for p, n in cfg["judges"])
DARK = LOOK == "dark"
shade = ("linear-gradient(to bottom, #100c0a 0%, #100c0a 20%, rgba(16,12,10,.86) 27%, rgba(16,12,10,.42) 45%, rgba(16,12,10,.22) 60%,"
         " rgba(11,9,8,.80) 79%, #0b0908 88%)" if DARK else
         "linear-gradient(to bottom, #f5f0e8 0%, #f5f0e8 20%, rgba(245,240,232,.9) 27%, rgba(245,240,232,.45) 43%, rgba(245,240,232,0) 55%,"
         " rgba(11,9,8,.15) 68%, rgba(11,9,8,.82) 80%, #0b0908 88%)")
page = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:"Instrument Serif";font-style:normal;src:url({BRAND}/fonts/Instrument_Serif_jizBRFtNs2ka5fXjeivQ4LroWlx-6zUTjnTLgNs.woff2) format("woff2");}}
@font-face{{font-family:"Instrument Serif";font-style:italic;src:url({BRAND}/fonts/Instrument_Serif_jizHRFtNs2ka5fXjeivQ4LroWlx-6zAjjH7Motmp5g.woff2) format("woff2");}}
@font-face{{font-family:"Manrope";font-weight:200 800;src:url({BRAND}/fonts/Manrope_xn7gYHE41ni1AdIRggexSvfedN4.woff2) format("woff2");}}
:root{{--ink:#1f1e1d;--cream:#f5f0e8;--accent:#e08a66;--deep:#b3573f;--copper:linear-gradient(135deg,#e8946f 0%,#d97757 40%,#b3573f 100%);}}
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:1080px;height:1920px;overflow:hidden;background:#0b0908;font-family:Manrope,sans-serif;-webkit-font-smoothing:antialiased;}}
.bg{{position:absolute;inset:0;background:url(file://{e(cfg["court"])}) no-repeat;background-size:auto 1300px;background-position:50% 380px;
     filter:contrast(1.18) saturate(1.08) brightness({".92" if DARK else ".98"});}}
.shade{{position:absolute;inset:0;background:{shade};}}
.wrap{{position:absolute;left:0;right:0;top:0;display:flex;flex-direction:column;align-items:center;padding:96px 64px 0;}}
.top{{display:flex;align-items:center;gap:20px;}} .top img.mk{{width:74px;height:74px;}} .top img.wm{{height:60px;}}
.kick{{margin-top:28px;}}
.kick span{{display:inline-block;font-weight:800;font-size:28px;letter-spacing:5px;padding:14px 30px;border-radius:40px;
  {"background:var(--copper);color:#fff;box-shadow:0 14px 30px rgba(179,87,63,.35);" if DARK else "background:#f5dfd0;color:var(--deep);box-shadow:inset 0 0 0 2px rgba(179,87,63,.18);"}}}
h1{{margin-top:26px;width:960px;text-align:center;}}
h1 .l{{display:block;text-wrap:balance;}}
{"h1 .l1{font-weight:800;font-size:112px;line-height:1.02;letter-spacing:-2px;color:#fff;text-shadow:0 6px 28px rgba(0,0,0,.5);} h1 .l2{margin-top:12px;font-weight:800;font-size:92px;line-height:1.04;letter-spacing:-2px;color:#f0a07c;} h1 em{font-family:'Instrument Serif',serif;font-style:italic;font-weight:400;font-size:1.22em;letter-spacing:0;color:#f6b08f;}"
 if DARK else
 "h1{font-family:'Instrument Serif',serif;font-weight:400;letter-spacing:-1px;color:var(--ink);} h1 .l{white-space:nowrap;line-height:1.02;} h1 .l1{font-size:140px;} h1 .l2{font-size:112px;} h1 em{font-style:italic;color:var(--deep);}"}
.list{{margin-top:40px;width:930px;border-radius:30px;padding:10px 34px;
  {"background:rgba(14,11,9,.55);box-shadow:inset 0 0 0 2px rgba(255,255,255,.12),0 30px 60px rgba(0,0,0,.35);backdrop-filter:blur(8px);" if DARK else "background:rgba(255,252,246,.96);box-shadow:0 26px 60px rgba(60,40,25,.18),inset 0 0 0 2px rgba(224,215,198,.9);"}}}
.pt{{display:flex;align-items:center;gap:26px;padding:22px 0;}}
.pt + .pt{{border-top:2px solid {"rgba(255,255,255,.12)" if DARK else "#eee4d4"};}}
.pt .n{{width:62px;height:62px;flex:none;border-radius:50%;background:var(--copper);color:#fff;font-weight:800;font-size:32px;display:flex;align-items:center;justify-content:center;box-shadow:0 8px 18px rgba(179,87,63,.35);}}
.pt .tx{{font-weight:700;font-size:42px;line-height:1.12;color:{"#fff" if DARK else "var(--ink)"};}}
.bench{{position:absolute;left:0;right:0;display:flex;justify-content:center;gap:150px;}}
.jd{{display:flex;flex-direction:column;align-items:center;gap:18px;}}
.ring{{width:270px;height:270px;border-radius:50%;padding:8px;background:var(--copper);box-shadow:0 24px 60px rgba(0,0,0,.55);}}
.ring img{{width:100%;height:100%;border-radius:50%;object-fit:cover;object-position:50% 16%;display:block;border:6px solid #fff;background:#fff;}}
.nm{{font-family:"Instrument Serif",serif;font-size:44px;line-height:1;color:#fff;text-shadow:0 3px 14px rgba(0,0,0,.8);}}
.badge{{position:absolute;left:0;right:0;text-align:center;}}
.badge span{{display:inline-block;color:#f3a37f;font-weight:800;font-size:31px;letter-spacing:5px;padding:14px 34px;border-radius:40px;box-shadow:inset 0 0 0 3px rgba(224,138,102,.8);}}
</style></head><body>
<div class="bg"></div><div class="shade"></div>
<div class="wrap">
<div class="top"><img class="mk" src="{BRAND}/site_logo_mark.png"><img class="wm" src="{BRAND}/{"wordmark_white.png" if DARK else "wordmark_ink.png"}"></div>
<div class="kick"><span>{e(cfg.get("kicker", "JUDGMENT EXPLAINED"))}</span></div>
<h1><span class="l l1">{e(cfg["head1"])}</span><span class="l l2">{head2()}</span></h1>
<div class="list">{points}</div>
</div>
<div class="bench">{judges}</div>
<div class="badge"><span>{e(cfg["badge"])}</span></div>
<script>window.__layout = () => {{ const L = document.querySelector('.list').getBoundingClientRect(), b = document.querySelector('.bench'),
  bd = document.querySelector('.badge');
  // the bench in the photo's open middle, under the list; the badge under the bench, everything above y 1700 (the apps' bar)
  const bt = Math.max(L.bottom + 120, 1190); b.style.top = bt + 'px'; const br = b.getBoundingClientRect();
  bd.style.top = Math.round(br.bottom + 26) + 'px'; }};</script>
</body></html>"""

tmp = os.path.join(ROOT, "overlays", f"_thumb_poster_{LOOK}.html")
open(tmp, "w").write(page)
out = os.path.abspath((cfg.get("out_poster") or cfg["out"]).replace("{look}", LOOK))
js = """
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ headless: true, channel: 'chrome' });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  await p.goto('file://' + process.argv[1]);
  const end = await p.evaluate(async () => { await document.fonts.ready;
    for (const l of document.querySelectorAll('h1 .l')) { let fs = parseFloat(getComputedStyle(l).fontSize);
      while (l.scrollWidth > 960 && fs > 56) { fs -= 2; l.style.fontSize = fs + 'px'; } }
    if (window.__layout) window.__layout();
    for (let k = 0; k < 8 && document.querySelector('.badge').getBoundingClientRect().bottom > 1700; k++) {
      for (const r of document.querySelectorAll('.ring')) { r.style.width = r.style.height = (r.offsetWidth * 0.92) + 'px'; } window.__layout(); }
    await Promise.all([...document.images].map(i => i.decode().catch(() => {})));
    return Math.round(document.querySelector('.badge').getBoundingClientRect().bottom); });
  await p.screenshot({ path: process.argv[2] });
  console.log('stack ends at y', end); await b.close();
})().catch(e => { console.error(e); process.exit(1); });
"""
r = subprocess.run(["node", "-e", js, tmp, out], cwd=ROOT, capture_output=True, text=True)
print(r.stdout.strip(), r.stderr.strip()[-400:]); r.check_returncode()
print("saved", out)
