"""Writes overlays/overlay_brand.html with the site's Lucide icons inlined (file:// pages cannot fetch JSON)."""
import json, os
P = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
icons = json.load(open(os.path.join(P, "brand", "lucide_icons.json")))
html = r'''<!doctype html>
<html><head><meta charset="utf-8"><title>LawWorld overlay</title>
<style>
  @font-face{font-family:"Instrument Serif";font-style:normal;font-weight:400;src:url(../brand/fonts/Instrument_Serif_jizBRFtNs2ka5fXjeivQ4LroWlx-6zUTjnTLgNs.woff2) format("woff2");}
  @font-face{font-family:"Instrument Serif";font-style:italic;font-weight:400;src:url(../brand/fonts/Instrument_Serif_jizHRFtNs2ka5fXjeivQ4LroWlx-6zAjjH7Motmp5g.woff2) format("woff2");}
  @font-face{font-family:"Manrope";font-style:normal;font-weight:200 800;src:url(../brand/fonts/Manrope_xn7gYHE41ni1AdIRggexSvfedN4.woff2) format("woff2");}
  @font-face{font-family:"Noto Sans Kannada";font-style:normal;font-weight:400 700;src:url(../brand/fonts/Noto_Sans_Kannada_400.woff2) format("woff2");}
  @font-face{font-family:"Noto Serif Kannada";font-style:normal;font-weight:400 700;src:url(../brand/fonts/Noto_Serif_Kannada_400.woff2) format("woff2");}
  :root{--cream:#f5f0e8;--cream-soft:#faf7f2;--cream-deep:#ede6d9;--paper:#fffcf6;--ink:#1f1e1d;--ink-soft:#2a2624;--muted:#6b6660;--rule:#e0d7c6;--accent:#cc785c;--accent-deep:#b3573f;--accent-soft:#e8bfa9;--wash:#f5dfd0;--brand:#d97757;}
  html,body{margin:0;padding:0;width:1080px;height:1920px;overflow:hidden;background:transparent;}
  body{font-family:"Manrope","Noto Sans Kannada",-apple-system,"Helvetica Neue",Arial,sans-serif;color:var(--ink);-webkit-font-smoothing:antialiased;}
  .serif{font-family:"Instrument Serif","Noto Serif Kannada",Georgia,serif;font-weight:400;}
  /* Kannada: taller glyphs, no tracking tricks */
  body.kn .caps{font-size:50px;line-height:1.5;letter-spacing:0;}
  body.kn .chapter{letter-spacing:1px;text-transform:none;font-size:30px;}
  body.kn .bignum .l{letter-spacing:1px;text-transform:none;font-size:46px;}
  body.kn .title .h{font-size:64px;line-height:1.3;}
  body.kn .title .s{line-height:1.5;}
  body.kn .lt .name{font-size:48px;line-height:1.2;top:22px;}
  body.kn .lt .role{top:84px;}
  body.kn .chip .t{font-size:34px;line-height:1.4;}
  body.kn .cta .url{letter-spacing:0;text-transform:none;font-size:34px;}
  body.kn #sting .tag{font-size:46px;line-height:1.4;}
  /* swap rows: old law -> new law */
  .swap{left:0;top:1060px;width:1080px;display:flex;flex-direction:column;align-items:center;gap:14px;}
  .swap .row{width:960px;height:104px;display:flex;align-items:center;gap:18px;padding:0 26px;box-sizing:border-box;}
  .swap .old{font-size:28px;font-weight:600;color:var(--muted);text-decoration:line-through;text-decoration-color:var(--accent);white-space:nowrap;flex:none;}
  .swap .arr{width:34px;height:34px;flex:none;}
  .swap .arr svg{width:34px;height:34px;stroke:var(--accent-deep);fill:none;stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round;}
  .swap .new{font-size:34px;line-height:1.35;color:var(--ink);white-space:nowrap;flex:1;overflow:hidden;text-overflow:ellipsis;}
  .swap .tag{font-size:24px;font-weight:700;letter-spacing:1px;color:var(--accent-deep);background:var(--wash);border-radius:12px;padding:6px 12px;flex:none;}
  .abs{position:absolute;left:0;top:0;}
  #scrim-bot{top:1400px;width:1080px;height:520px;background:linear-gradient(0deg,rgba(245,240,232,.94) 0%,rgba(245,240,232,.6) 42%,rgba(245,240,232,0) 100%);}
  .card{background:var(--paper);border:1.5px solid var(--rule);border-radius:24px;box-shadow:0 18px 50px rgba(31,30,29,.10),0 2px 6px rgba(31,30,29,.05);}
  .tile{width:60px;height:60px;border-radius:16px;background:var(--wash);display:flex;align-items:center;justify-content:center;flex:none;}
  .tile svg{width:32px;height:32px;stroke:var(--accent-deep);fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;}
  /* sting */
  #sting{width:1080px;height:1920px;background:var(--cream);}
  #sting .wash{position:absolute;left:0;top:0;width:1080px;height:1920px;background:radial-gradient(circle at 82% 10%,rgba(245,223,208,.95) 0%,rgba(245,223,208,.5) 18%,rgba(245,240,232,0) 42%),radial-gradient(circle at 50% 46%,rgba(255,252,246,.9) 0%,rgba(245,240,232,0) 40%);}
  #sting .ring{position:absolute;left:390px;top:640px;width:300px;height:300px;border-radius:50%;border:1.5px solid rgba(179,87,63,.35);}
  #sting .mark{position:absolute;left:380px;top:630px;width:320px;height:320px;background:url(../brand/site_logo_mark.png) center/contain no-repeat;filter:drop-shadow(0 28px 50px rgba(120,60,30,.28));}
  #sting .word{position:absolute;left:200px;top:1010px;width:680px;height:182px;background:url(../brand/wordmark_ink.png) center/contain no-repeat;}
  #sting .tag{position:absolute;left:0;top:1230px;width:1080px;text-align:center;font-size:48px;color:var(--ink);}
  #sting .tag i{color:var(--accent);}
  /* lower third */
  .lt{left:64px;top:1225px;width:640px;height:144px;overflow:hidden;}
  .lt .bar{position:absolute;left:0;top:0;width:7px;height:144px;background:linear-gradient(180deg,var(--brand),var(--accent-deep));}
  .lt .mk{position:absolute;left:34px;top:36px;width:72px;height:72px;background:url(../brand/site_logo_mark.png) center/contain no-repeat;}
  .lt .name{position:absolute;left:134px;top:26px;font-size:54px;line-height:1;}
  .lt .role{position:absolute;left:136px;top:90px;font-size:28px;font-weight:500;color:var(--muted);}
  /* pills */
  .pills{left:0;top:130px;width:1080px;height:100px;display:flex;justify-content:center;gap:18px;}
  .pill{height:88px;padding:0 36px;border-radius:44px;background:var(--paper);border:1.5px solid var(--rule);display:flex;align-items:center;gap:14px;font-size:40px;font-weight:600;box-shadow:0 12px 34px rgba(31,30,29,.10);}
  .pill .dot{width:14px;height:14px;border-radius:50%;background:linear-gradient(135deg,var(--brand),var(--accent-deep));}
  /* lockup */
  .lockup{left:0;top:96px;width:1080px;height:150px;}
  .lockup .in{position:relative;margin:0 auto;width:620px;height:150px;}
  .lockup .mk{position:absolute;left:0;top:6px;width:138px;height:138px;background:url(../brand/site_logo_mark.png) center/contain no-repeat;filter:drop-shadow(0 10px 24px rgba(120,60,30,.25));}
  .lockup .wd{position:absolute;left:160px;top:12px;width:460px;height:124px;background:url(../brand/wordmark_ink.png) center/contain no-repeat;}
  /* big number */
  .bignum{left:0;top:940px;width:1080px;height:560px;text-align:center;background:radial-gradient(ellipse 62% 58% at 50% 45%,rgba(245,240,232,.92) 0%,rgba(245,240,232,.6) 45%,rgba(245,240,232,0) 75%);}
  .bignum .n{font-size:340px;letter-spacing:-8px;line-height:1;color:var(--ink);display:inline-block;}
  .bignum .rule{width:180px;height:3px;margin:20px auto 26px;background:linear-gradient(90deg,rgba(204,120,92,0),var(--accent),rgba(204,120,92,0));}
  .bignum .l{font-size:46px;font-weight:500;letter-spacing:10px;text-transform:uppercase;color:var(--accent-deep);}
  /* chapter */
  .chapter{left:0;top:118px;width:1080px;text-align:center;font-size:28px;font-weight:600;letter-spacing:7px;text-transform:uppercase;color:var(--accent-deep);display:flex;justify-content:center;align-items:center;gap:26px;}
  .chapter i{display:block;width:56px;height:1.5px;background:var(--accent-soft);}
  /* chips */
  .chips{left:0;top:0;width:1080px;height:1920px;}
  .chip{position:absolute;height:98px;border-radius:22px;display:flex;align-items:center;gap:18px;padding:0 24px 0 18px;box-sizing:border-box;white-space:nowrap;}
  .chip .t{font-size:38px;color:var(--ink);}
  .chips.right .chip{left:690px;width:350px;}
  .chips.left .chip{left:40px;width:350px;}
  .chips.row{top:1160px;height:auto;display:flex;flex-wrap:wrap;justify-content:center;gap:16px 16px;padding:0 60px;box-sizing:border-box;}
  .chips.row .chip{position:relative;left:auto;width:auto;}
  .chips.lowrow{top:1140px;height:auto;display:flex;flex-wrap:wrap;justify-content:center;gap:16px 16px;padding:0 60px;box-sizing:border-box;}
  .chips.lowrow .chip{position:relative;left:auto;width:auto;}
  /* title card over 3D */
  .title{left:0;top:140px;width:1080px;display:flex;justify-content:center;}
  .title .in{padding:26px 46px 28px;max-width:920px;text-align:center;}
  .title .h{font-size:76px;line-height:1.05;color:var(--ink);}
  .title .s{font-size:30px;font-weight:500;color:var(--muted);margin-top:10px;}
  /* captions */
  .caps{left:60px;top:1500px;width:960px;text-align:center;font-size:54px;font-weight:600;letter-spacing:-.4px;line-height:1.25;}
  .caps .box{display:inline-block;background:rgba(255,252,246,.92);border:1.5px solid var(--rule);border-radius:22px;padding:12px 26px;box-shadow:0 10px 30px rgba(31,30,29,.08);}
  .caps span{display:inline-block;margin:0 8px;color:rgba(107,102,96,.75);}
  .caps span.on{color:var(--accent-deep);}
  .caps span.done{color:var(--ink);}
  /* pricing canvas */
  .pricing{width:1080px;height:1920px;background:var(--cream);}
  .pricing .wash{position:absolute;left:0;top:0;width:1080px;height:1920px;background:radial-gradient(circle at 85% 8%,rgba(245,223,208,.9) 0%,rgba(245,240,232,0) 38%);}
  .pricing .h{position:absolute;left:0;top:190px;width:1080px;text-align:center;font-size:74px;color:var(--ink);}
  .pricing .h i{color:var(--accent);}
  .pcard{position:absolute;left:90px;width:900px;padding:34px 40px;box-sizing:border-box;}
  .pcard .head{display:flex;align-items:center;gap:20px;}
  .pcard .name{font-size:62px;line-height:1;color:var(--ink);}
  .pcard .price{display:flex;align-items:baseline;gap:16px;margin-top:22px;}
  .pcard .big{font-size:112px;line-height:1;color:var(--ink);letter-spacing:-2px;}
  .pcard .per{font-size:34px;font-weight:500;color:var(--muted);}
  .pcard .line{display:flex;align-items:center;gap:16px;font-size:36px;font-weight:500;color:var(--ink);margin-top:16px;}
  .pcard .line svg{width:30px;height:30px;stroke:var(--accent-deep);fill:none;stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round;flex:none;}
  .pcard .line.sub{font-size:30px;color:var(--muted);}
  /* cta canvas */
  .cta{width:1080px;height:1920px;background:var(--cream);}
  .cta .wash{position:absolute;left:0;top:0;width:1080px;height:1920px;background:radial-gradient(circle at 80% 10%,rgba(245,223,208,.95) 0%,rgba(245,240,232,0) 40%),radial-gradient(circle at 20% 90%,rgba(245,223,208,.7) 0%,rgba(245,240,232,0) 35%);}
  .cta .card{position:absolute;left:90px;top:380px;width:900px;padding:46px 40px 44px;box-sizing:border-box;text-align:center;}
  .cta .amt{font-size:170px;line-height:1;color:var(--ink);letter-spacing:-4px;}
  .cta .what{font-size:64px;line-height:1.1;color:var(--accent-deep);margin-top:8px;}
  .cta .who{font-size:34px;font-weight:500;color:var(--muted);margin-top:14px;}
  .cta .link{position:absolute;left:0;top:1000px;width:1080px;text-align:center;font-size:46px;font-weight:600;color:var(--ink);}
  .cta .arrow{position:absolute;left:510px;top:1070px;width:60px;height:60px;}
  .cta .arrow svg{width:60px;height:60px;stroke:var(--accent-deep);fill:none;stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round;}
  .cta .lk{position:absolute;left:0;top:1190px;width:1080px;height:160px;}
  .cta .lk .in{position:relative;margin:0 auto;width:640px;height:160px;}
  .cta .lk .mk{position:absolute;left:0;top:6px;width:148px;height:148px;background:url(../brand/site_logo_mark.png) center/contain no-repeat;}
  .cta .lk .wd{position:absolute;left:170px;top:16px;width:470px;height:126px;background:url(../brand/wordmark_ink.png) center/contain no-repeat;}
  .cta .url{position:absolute;left:0;top:1380px;width:1080px;text-align:center;font-size:34px;font-weight:600;letter-spacing:8px;text-transform:uppercase;color:var(--accent-deep);}

  /* ---------- creator edit (fast-cut) components ---------- */
  .hook{width:1080px;height:1920px;background:var(--ink);overflow:hidden;}
  .hook .bg{position:absolute;left:-200px;top:-200px;width:1480px;height:2320px;background:radial-gradient(circle at 30% 20%,rgba(217,119,87,.55) 0%,rgba(31,30,29,0) 45%),radial-gradient(circle at 80% 85%,rgba(179,87,63,.5) 0%,rgba(31,30,29,0) 40%);}
  .hook .l1,.hook .l2,.hook .l3{position:absolute;left:70px;width:940px;font-weight:800;line-height:1.02;letter-spacing:-2px;color:#fff;}
  .hook .l1{top:600px;font-size:108px;white-space:nowrap;}
  .hook .l2{top:730px;font-size:128px;color:#F5C542;white-space:nowrap;}
  .hook .l3{top:930px;font-size:56px;font-weight:600;letter-spacing:-.5px;color:rgba(255,255,255,.8);}
  .hook .bar{position:absolute;left:70px;top:1040px;height:14px;width:520px;background:var(--brand);border-radius:7px;transform-origin:left;}
  .kcap{left:60px;top:1100px;width:960px;text-align:center;font-weight:800;font-size:82px;line-height:1.08;letter-spacing:-1.5px;color:var(--ink);text-shadow:0 2px 0 rgba(255,252,246,.9),0 0 18px rgba(255,252,246,.9);}
  .kcap.up{top:70px;font-size:70px;}
  .kcap span{display:inline-block;margin:0 10px;position:relative;}
  .kcap span.on{color:#fff;}
  .kcap span.on::before{content:"";position:absolute;left:-10px;right:-10px;top:4px;bottom:0;background:var(--brand);border-radius:14px;z-index:-1;transform:rotate(-1.2deg);}
  .kcap span.done{color:var(--ink);}
  body.kn .kcap{font-size:70px;line-height:1.4;letter-spacing:0;}
  .emo{left:0;top:0;width:1080px;height:1920px;}
  .emo .e{position:absolute;font-size:150px;line-height:1;filter:drop-shadow(0 16px 30px rgba(31,30,29,.35));transform-origin:center;}
  .stat{left:0;top:1020px;width:1080px;height:420px;display:flex;flex-direction:column;align-items:center;justify-content:center;}
  .stat .card{background:var(--ink);color:#fff;border-radius:30px;padding:34px 60px;text-align:center;box-shadow:0 30px 90px rgba(31,30,29,.45);}
  .stat .n{font-size:150px;font-weight:800;line-height:1;letter-spacing:-6px;color:#F5C542;}
  .stat .l{font-size:52px;font-weight:700;margin-top:10px;letter-spacing:-.5px;}
  .stat .s{font-size:32px;font-weight:500;margin-top:14px;color:rgba(255,255,255,.7);}
  .flash{width:1080px;height:1920px;background:#fff;}
  .grain{width:1080px;height:1920px;opacity:.06;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 0.9 0'/></filter><rect width='300' height='300' filter='url(%23n)'/></svg>");}
  .endc{width:1080px;height:1920px;background:var(--ink);}
  .endc .wash{position:absolute;left:0;top:0;width:1080px;height:1920px;background:radial-gradient(circle at 50% 40%,rgba(217,119,87,.45) 0%,rgba(31,30,29,0) 50%);}
  .endc .amt{position:absolute;left:0;top:560px;width:1080px;text-align:center;font-size:200px;font-weight:800;color:#F5C542;letter-spacing:-6px;line-height:1;}
  .endc .what{position:absolute;left:0;top:790px;width:1080px;text-align:center;font-size:66px;font-weight:700;color:#fff;letter-spacing:-1px;}
  .endc .who{position:absolute;left:0;top:880px;width:1080px;text-align:center;font-size:36px;font-weight:500;color:rgba(255,255,255,.7);}
  .endc .link{position:absolute;left:0;top:1030px;width:1080px;text-align:center;font-size:54px;font-weight:800;color:#fff;}
  .endc .arrow{position:absolute;left:510px;top:1110px;width:60px;height:60px;}
  .endc .arrow svg{width:60px;height:60px;stroke:#F5C542;fill:none;stroke-width:3;stroke-linecap:round;stroke-linejoin:round;}
  .endc .lk{position:absolute;left:0;top:1260px;width:1080px;height:150px;}
  .endc .lk .in{position:relative;margin:0 auto;width:620px;height:150px;}
  .endc .lk .mk{position:absolute;left:0;top:6px;width:138px;height:138px;background:url(../brand/site_logo_mark.png) center/contain no-repeat;}
  .endc .lk .wd{position:absolute;left:160px;top:12px;width:460px;height:124px;background:url(../brand/wordmark_white_serif.png) center/contain no-repeat;}
  .endc .url{position:absolute;left:0;top:1440px;width:1080px;text-align:center;font-size:34px;font-weight:700;letter-spacing:6px;color:#F5C542;}

  /* ===== office layout zones (2026-09-29): TOP zone y 80-460 = cards; BOTTOM zone y 1560+ = captions only ===== */
  body.zones .kcap{top:1590px !important;font-size:66px;}
  body.zones .kcap.up{top:1590px !important;}
  body.zones .stat{top:90px;height:380px;}
  body.zones .chips.lowrow{top:130px;}
  body.zones .lt{top:110px;left:60px;}
  body.zones .title{top:96px;}
  body.zones .pills{top:120px;}
  .slam{left:0;top:110px;width:1080px;height:360px;display:flex;flex-direction:column;align-items:center;justify-content:center;}
  .slam .w{font-size:112px;font-weight:800;letter-spacing:-3px;line-height:1;color:#fff;text-shadow:0 8px 30px rgba(31,30,29,.45);position:absolute;white-space:nowrap;}
  .slam .w.hl{color:#F5C542;}
  .orbit{left:0;top:40px;width:1080px;height:520px;perspective:1100px;}
  .orbit .ring{position:absolute;left:540px;top:230px;}
  .orbit .it{position:absolute;left:-60px;top:-60px;width:120px;height:120px;border-radius:28px;background:rgba(255,252,246,.94);border:1.5px solid var(--rule);display:flex;align-items:center;justify-content:center;box-shadow:0 14px 34px rgba(31,30,29,.25);backface-visibility:hidden;}
  .orbit .it svg{width:58px;height:58px;stroke:var(--accent-deep);fill:none;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round;}
  .orbit .core{position:absolute;left:390px;top:130px;width:300px;height:200px;text-align:center;z-index:300;background:rgba(31,30,29,.86);border-radius:36px;padding-top:14px;box-sizing:border-box;box-shadow:0 20px 50px rgba(31,30,29,.4);}
  .orbit .core .n{font-size:130px;font-weight:800;color:#F5C542;letter-spacing:-5px;line-height:1;text-shadow:0 10px 40px rgba(31,30,29,.5);}
  .orbit .core .l{font-size:40px;font-weight:700;color:#fff;margin-top:6px;text-shadow:0 4px 20px rgba(31,30,29,.6);}
  .phone{left:0;top:60px;width:1080px;height:460px;display:flex;justify-content:center;}
  .phone .dev{width:300px;height:430px;border-radius:44px;background:var(--ink);padding:16px;box-sizing:border-box;box-shadow:0 30px 70px rgba(31,30,29,.45);}
  .phone .scr{width:100%;height:100%;border-radius:30px;background:var(--paper);padding:26px 18px;box-sizing:border-box;overflow:hidden;}
  .phone .hd{font-size:26px;font-weight:800;color:var(--ink);margin-bottom:14px;}
  .phone .row{display:flex;align-items:center;gap:12px;background:#fff;border:1.5px solid var(--rule);border-radius:16px;padding:12px;margin-bottom:12px;}
  .phone .row .d{width:48px;height:48px;border-radius:12px;background:var(--wash);color:var(--accent-deep);font-weight:800;font-size:20px;display:flex;align-items:center;justify-content:center;flex:none;}
  .phone .row .t{font-size:20px;font-weight:700;color:var(--ink);}
  .phone .row .s{font-size:16px;color:var(--muted);}
  .sweep{width:1080px;height:1920px;background:linear-gradient(100deg,rgba(255,255,255,0) 40%,rgba(255,236,200,.28) 50%,rgba(255,255,255,0) 60%);background-size:300% 100%;mix-blend-mode:screen;}

  /* ===== low zones: presenter's face fills the top half -> cards over the lower body, captions at the bottom ===== */
  body.zlow .kcap{top:1640px !important;font-size:62px;}
  body.zlow .kcap.up{top:1640px !important;}
  body.zlow .stat{top:1100px;height:420px;}
  body.zlow .chips.lowrow{top:1260px;}
  body.zlow .lt{top:1230px;left:60px;}
  body.zlow .title{top:1150px;}
  body.zlow .slam{top:1120px;}
  body.zlow .title .h{font-size:64px;}

  /* Kannada in the zones layout: taller glyphs, keep captions on one or two tidy lines */
  body.kn.zones .kcap{font-size:58px;line-height:1.4;letter-spacing:0;font-weight:700;}
  body.kn .kcap span{margin:0 9px;}
  body.kn .hook .l1{font-size:96px;letter-spacing:0;line-height:1.25;top:570px;}
  body.kn .hook .l2{font-size:104px;letter-spacing:0;line-height:1.25;top:720px;}
  body.kn .hook .l3{font-size:50px;letter-spacing:0;top:910px;}
  body.kn .hook .bar{top:1010px;}
  body.kn .slam .w{font-size:100px;letter-spacing:0;line-height:1.3;}
  body.kn .stat .l{font-size:46px;letter-spacing:0;line-height:1.35;}
  body.kn .stat .s{font-size:30px;line-height:1.4;}
  body.kn .orbit .core .l{font-size:34px;line-height:1.3;}
  body.kn .phone .hd{font-size:24px;} body.kn .phone .row .t{font-size:19px;line-height:1.3;} body.kn .phone .row .s{font-size:15px;line-height:1.3;}
  body.kn .pricing .h{font-size:62px;line-height:1.3;}
  body.kn .pcard .name{font-size:52px;line-height:1.25;} body.kn .pcard .line{font-size:32px;line-height:1.4;} body.kn .pcard .per{font-size:30px;}
  body.kn .endc .what{font-size:52px;letter-spacing:0;line-height:1.3;} body.kn .endc .who{font-size:32px;line-height:1.4;}
  body.kn .title .s{font-size:28px;}
  body.kn .chip{height:auto;padding:14px 24px 14px 18px;}

  /* slam words and the orbit badge must read on a light wall */
  body.zones .slam .w{background:rgba(31,30,29,.9);padding:6px 36px 12px;border-radius:28px;box-shadow:0 18px 44px rgba(31,30,29,.35);text-shadow:none;}
  body.kn .orbit .core{height:236px;top:112px;left:360px;width:360px;}
  body.kn .orbit .core .l{font-size:32px;line-height:1.35;margin-top:2px;}

  /* zones layout: captions sit on the dark desk -> white words with a soft dark shadow */
  body.zones .kcap{color:#fff;text-shadow:0 3px 0 rgba(31,30,29,.55),0 0 10px rgba(31,30,29,.7),0 0 28px rgba(31,30,29,.85);}
  body.zones .kcap span.done{color:#fff;}
</style></head>
<body><div id="stage"></div>
<script>
const ICONS = __ICONS__;
const svg=(n)=>'<svg viewBox="0 0 24 24">'+(ICONS[n]||ICONS['sparkles']||'')+'</svg>';
const clamp=(x,a=0,b=1)=>Math.max(a,Math.min(b,x));
const outExpo=x=>x>=1?1:1-Math.pow(2,-10*x);
const outBack=x=>{const c1=1.70158,c3=c1+1;return 1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2);};
const outCubic=x=>1-Math.pow(1-x,3);
const P=(t,t0,d)=>clamp((t-t0)/d);
let EL=[]; const stage=document.getElementById('stage');
function div(cls,html){const d=document.createElement('div');d.className='abs '+(cls||'');if(html!==undefined)d.innerHTML=html;stage.appendChild(d);return d;}
function chipHTML(i){return '<div class="chip card"><div class="tile">'+svg(i.icon)+'</div><div class="t serif">'+i.text+'</div></div>';}
function init(tl){
  stage.innerHTML='';EL=[];document.body.classList.toggle('kn',tl.lang==='kn');document.body.classList.toggle('zones',!!tl.zones);document.body.classList.toggle('zlow',!!tl.zlow);
  const sb=div(''); sb.id='scrim-bot'; EL.push({type:'_scrim',el:sb,t0:tl.scrim_from??0,t1:tl.duration});
  for(const c of tl.cues){
    switch(c.type){
      case 'sting':{const e=div('');e.id='sting';e.innerHTML='<div class="wash"></div><div class="ring"></div><div class="mark"></div><div class="word"></div><div class="tag serif">'+(c.tag||'The all-in-one AI platform for advocates').replace('AI platform','<i>AI platform</i>')+'</div>';EL.push({c,el:e,q:{ring:e.querySelector('.ring'),mark:e.querySelector('.mark'),word:e.querySelector('.word'),tag:e.querySelector('.tag')}});break;}
      case 'lower_third':{const e=div('lt card','<div class="bar"></div><div class="mk"></div><div class="name serif">'+c.name+'</div><div class="role">'+c.role+'</div>');EL.push({c,el:e});break;}
      case 'pills':{const e=div('pills',c.items.map(i=>'<div class="pill"><div class="dot"></div>'+i.text+'</div>').join(''));EL.push({c,el:e,items:[...e.querySelectorAll('.pill')]});break;}
      case 'lockup':{const e=div('lockup','<div class="in"><div class="mk"></div><div class="wd"></div></div>');EL.push({c,el:e});break;}
      case 'bignum':{const e=div('bignum','<div class="n serif">'+c.num+'</div><div class="rule"></div><div class="l">'+c.label+'</div>');EL.push({c,el:e,q:{n:e.querySelector('.n'),r:e.querySelector('.rule'),l:e.querySelector('.l')}});break;}
      case 'chapter':{const e=div('chapter','<i></i><span>'+c.text+'</span><i></i>');EL.push({c,el:e});break;}
      case 'chips':{const side=c.side||'right';const e=div('chips '+side,c.items.map(chipHTML).join(''));const items=[...e.querySelectorAll('.chip')];if(c.top!=null&&side==='lowrow')e.style.top=c.top+'px';if(side!=='row'&&side!=='lowrow')items.forEach((p,k)=>p.style.top=((c.top??400)+k*116)+'px');EL.push({c,el:e,items});break;}
      case 'swaprows':{const e=div('swap',c.rows.map(r=>'<div class="row card"><div class="old">'+r.old+'</div><div class="arr">'+svg('arrow-right')+'</div><div class="new serif">'+r.new+'</div>'+(r.tag?'<div class="tag">'+r.tag+'</div>':'')+'</div>').join(''));e.style.top=(c.top??1040)+'px';EL.push({c,el:e,items:[...e.querySelectorAll('.row')]});break;}

      case 'hook':{const e=div('hook','<div class="bg"></div><div class="l1">'+c.l1+'</div><div class="l2">'+c.l2+'</div><div class="l3">'+(c.l3||'')+'</div><div class="bar"></div>');EL.push({c,el:e,q:{l1:e.querySelector('.l1'),l2:e.querySelector('.l2'),l3:e.querySelector('.l3'),bar:e.querySelector('.bar'),bg:e.querySelector('.bg')}});break;}
      case 'kcap':{const e=div('kcap','');EL.push({c,el:e,phrases:groupWords(c.words,c),cur:-1});break;}
      case 'emoji':{const e=div('emo',c.items.map(i=>'<div class="e" style="left:'+i.x+'px;top:'+i.y+'px">'+i.emoji+'</div>').join(''));EL.push({c,el:e,items:[...e.querySelectorAll('.e')]});break;}
      case 'stat':{const e=div('stat','<div class="card"><div class="n">'+c.num+'</div><div class="l">'+c.label+'</div>'+(c.sub?'<div class="s">'+c.sub+'</div>':'')+'</div>');EL.push({c,el:e,q:{card:e.querySelector('.card'),n:e.querySelector('.n')}});break;}
      case 'flash':{const e=div('flash','');EL.push({c,el:e});break;}
      case 'grain':{const e=div('grain','');EL.push({c,el:e});break;}
      case 'endc':{const e=div('endc','<div class="wash"></div><div class="amt">'+c.amt+'</div><div class="what">'+c.what+'</div><div class="who">'+(c.who||'')+'</div><div class="link">'+c.link+'</div><div class="arrow">'+svg('arrow-down')+'</div><div class="lk"><div class="in"><div class="mk"></div><div class="wd"></div></div></div><div class="url">'+(c.url||'lawworld.ai')+'</div>');EL.push({c,el:e,q:{amt:e.querySelector('.amt'),what:e.querySelector('.what'),who:e.querySelector('.who'),link:e.querySelector('.link'),arrow:e.querySelector('.arrow'),lk:e.querySelector('.lk'),url:e.querySelector('.url')}});break;}
      case 'slam':{const e=div('slam',c.words.map(w=>'<div class="w'+(w.hl?' hl':'')+'">'+w.text+'</div>').join(''));EL.push({c,el:e,items:[...e.querySelectorAll('.w')]});break;}
      case 'orbit':{const e=div('orbit','<div class="ring">'+c.icons.map(n=>'<div class="it">'+svg(n)+'</div>').join('')+'</div><div class="core"><div class="n">'+c.num+'</div><div class="l">'+c.label+'</div></div>');EL.push({c,el:e,items:[...e.querySelectorAll('.it')],q:{core:e.querySelector('.core'),n:e.querySelector('.n')}});break;}
      case 'phone':{const e=div('phone','<div class="dev"><div class="scr"><div class="hd">'+c.head+'</div>'+c.rows.map(r=>'<div class="row"><div class="d">'+r.d+'</div><div><div class="t">'+r.t+'</div><div class="s">'+r.s+'</div></div></div>').join('')+'</div></div>');EL.push({c,el:e,q:{dev:e.querySelector('.dev')},items:[...e.querySelectorAll('.row')]});break;}
      case 'sweep':{const e=div('sweep','');EL.push({c,el:e});break;}
      case 'title':{const e=div('title','<div class="in card"><div class="h serif">'+c.title+'</div>'+(c.sub?'<div class="s">'+c.sub+'</div>':'')+'</div>');EL.push({c,el:e,q:{s:e.querySelector('.s')}});break;}
      case 'captions':{const e=div('caps','');EL.push({c,el:e,phrases:groupWords(c.words,c),cur:-1});break;}
      case 'pricing':{const e=div('pricing','<div class="wash"></div><div class="h serif">'+(c.heading||'Two simple ways to <i>pay</i>')+'</div>'
        +'<div class="pcard card" id="payg" style="top:330px"><div class="head"><div class="tile">'+svg('badge-indian-rupee')+'</div><div class="name serif">'+(c.payg_name||'Pay-as-you-go')+'</div></div>'+c.payg_lines.map(l=>'<div class="line">'+svg('check')+'<span>'+l.text+'</span></div>').join('')+'</div>'
        +'<div class="pcard card" id="pro" style="top:790px"><div class="head"><div class="tile">'+svg('star')+'</div><div class="name serif">'+(c.pro_name||'Pro')+'</div></div><div class="price"><div class="big serif" id="p1">₹1,500</div><div class="per">'+(c.per_month||'/ month')+'</div></div><div class="price" style="margin-top:6px"><div class="big serif" id="p2" style="font-size:72px">₹12,000</div><div class="per">'+(c.per_year||'/ year')+'</div><div class="per" id="p3" style="color:var(--accent-deep)">+ GST</div></div>'+c.pro_lines.slice(3).map(l=>'<div class="line">'+svg('check')+'<span>'+l.text+'</span></div>').join('')+'</div>');
        EL.push({c,el:e,q:{h:e.querySelector('.h'),payg:e.querySelector('#payg'),pro:e.querySelector('#pro'),paygLines:[...e.querySelectorAll('#payg .line')],p1:e.querySelector('#p1'),p2:e.querySelector('#p2'),p3:e.querySelector('#p3'),proLines:[...e.querySelectorAll('#pro .line')]}});break;}
      case 'cta':{const e=div('cta','<div class="wash"></div><div class="card"><div class="tile" style="margin:0 auto 14px;width:76px;height:76px;border-radius:20px">'+svg('gift').replace('<svg','<svg style="width:40px;height:40px"')+'</div><div class="amt serif">₹200</div><div class="what serif">free AI credits</div><div class="who">for every new user</div></div><div class="link">Click the link below to start</div><div class="arrow">'+svg('arrow-down')+'</div><div class="lk"><div class="in"><div class="mk"></div><div class="wd"></div></div></div><div class="url">'+(c.url||'lawworld.ai')+'</div>');
        EL.push({c,el:e,q:{card:e.querySelector('.card'),link:e.querySelector('.link'),arrow:e.querySelector('.arrow'),lk:e.querySelector('.lk'),url:e.querySelector('.url')}});break;}
    }
  }
  return EL.length;
}
function groupWords(words,c){
  const maxW=c.max_words||4, maxD=c.max_dur||1.7; const out=[]; let cur=null;
  for(const w of words){const txt=(w.word||'').trim(); if(!txt) continue; const endsSent=/[.!?]$/.test(txt);
    if(!cur||cur.words.length>=maxW||(w.end-cur.start)>maxD){cur={start:w.start,end:w.end,words:[]};out.push(cur);}
    cur.words.push({t:txt,s:w.start,e:w.end}); cur.end=w.end; if(endsSent) cur=null;}
  for(let i=0;i<out.length-1;i++){const gap=out[i+1].start-out[i].end; out[i].hold=gap<0.6?out[i+1].start:out[i].end+0.35;}
  if(out.length) out[out.length-1].hold=out[out.length-1].end+0.6; return out;
}
const show=(el,on)=>{el.style.visibility=on?'visible':'hidden';};
const rise=(el,a,px=40)=>{el.style.opacity=String(clamp(a*1.6));el.style.transform=`translateY(${(1-outExpo(a))*px}px)`;};
function seek(t){
  let active=false;
  for(const x of EL){
    if(x.type==='_scrim'){const on=t>=x.t0&&t<=x.t1;show(x.el,on);x.el.style.opacity=on?String(P(t,x.t0,0.4)):'0';if(on)active=true;continue;}
    const c=x.c,el=x.el; const on=t>=c.t0&&t<=c.t1; show(el,on); if(!on) continue; active=true;
    const fo=c.fade_out??0.35; const outA=clamp((c.t1-t)/fo);
    switch(c.type){
      case 'sting':{const a=P(t,c.t0,0.7),b=P(t,c.t0+0.45,0.7),g=P(t,c.t0+1.05,0.6);
        x.q.mark.style.transform=`scale(${0.6+0.4*outBack(a)}) rotate(${-8*(1-outCubic(a))}deg)`;x.q.mark.style.opacity=String(clamp(a*2));
        x.q.ring.style.transform=`scale(${0.7+1.9*outExpo(P(t,c.t0+0.25,1.3))})`;x.q.ring.style.opacity=String(0.7*(1-P(t,c.t0+0.25,1.3)));
        x.q.word.style.opacity=String(outCubic(b));x.q.word.style.transform=`translateY(${26*(1-outExpo(b))}px)`;x.q.word.style.filter=`blur(${10*(1-outExpo(b))}px)`;
        x.q.tag.style.opacity=String(outCubic(g));x.q.tag.style.transform=`translateY(${16*(1-outExpo(g))}px)`;el.style.opacity=String(outA);break;}
      case 'lower_third':{const a=outExpo(P(t,c.t0,0.55));el.style.opacity=String(Math.min(a,outA));el.style.transform=`translateY(${(1-a)*46+(1-outA)*30}px)`;break;}
      case 'pills':{el.style.opacity=String(outA);x.items.forEach((p,k)=>{const a=P(t,c.items[k].at??c.t0,0.45);p.style.opacity=String(clamp(a*2));p.style.transform=`scale(${0.7+0.3*outBack(a)}) translateY(${(1-outExpo(a))*14}px)`;});break;}
      case 'lockup':{const a=outExpo(P(t,c.t0,0.6));el.style.opacity=String(Math.min(clamp(a*1.5),outA));el.style.transform=`translateY(${(1-a)*-34}px)`;break;}
      case 'bignum':{const a=P(t,c.t0,0.9);const n=parseInt(c.num)||0;const plus=c.num.replace(/^\d+/,'');x.q.n.textContent=(a<1?Math.round(n*outCubic(a)):n)+(a>=0.85?plus:'');
        x.q.n.style.transform=`translateY(${(1-outExpo(P(t,c.t0,0.8)))*40-(t-c.t0)*1.2}px) scale(${0.92+0.08*outExpo(P(t,c.t0,0.8))})`;x.q.n.style.opacity=String(clamp(a*3));
        const r=P(t,c.t0+0.5,0.5);x.q.r.style.transform=`scaleX(${outExpo(r)})`;x.q.r.style.opacity=String(r);const l=P(t,c.t0+0.7,0.6);x.q.l.style.opacity=String(outCubic(l));x.q.l.style.transform=`translateY(${(1-outExpo(l))*18}px)`;el.style.opacity=String(outA);break;}
      case 'chapter':{const a=outExpo(P(t,c.t0,0.5));el.style.opacity=String(Math.min(a,outA));el.style.transform=`translateY(${(1-a)*-14}px)`;break;}
      case 'chips':{el.style.opacity=String(outA);const row=['row','lowrow'].includes(c.side||'right');x.items.forEach((p,k)=>{const a=P(t,c.items[k].at??c.t0,0.5);p.style.opacity=String(clamp(a*2));p.style.transform=row?`translateY(${(1-outExpo(a))*40}px) scale(${0.94+0.06*outBack(a)})`:`translateX(${(1-outExpo(a))*70}px) scale(${0.94+0.06*outBack(a)})`;});break;}
      case 'swaprows':{el.style.opacity=String(outA);x.items.forEach((r,k)=>{const a=P(t,c.rows[k].at??c.t0,0.5);r.style.opacity=String(clamp(a*2));r.style.transform=`translateY(${(1-outExpo(a))*44}px) scale(${0.96+0.04*outBack(a)})`;});break;}

      case 'hook':{const I=c.instant?1:0;const a=I||P(t,c.t0,0.35),b=I||P(t,c.t0+0.18,0.35),d=I||P(t,c.t0+0.45,0.4),k=I||P(t,c.t0+0.55,0.5);
        x.q.bg.style.transform=`scale(${1+0.06*(t-c.t0)})`;
        x.q.l1.style.transform=`translateY(${(1-outExpo(a))*90}px) scale(${1.25-0.25*outExpo(a)})`;x.q.l1.style.opacity=String(clamp(a*3));
        x.q.l2.style.transform=`translateY(${(1-outExpo(b))*90}px) scale(${1.25-0.25*outExpo(b)})`;x.q.l2.style.opacity=String(clamp(b*3));
        x.q.l3.style.opacity=String(outCubic(d));x.q.l3.style.transform=`translateY(${(1-outExpo(d))*30}px)`;x.q.bar.style.transform=`scaleX(${outExpo(k)})`;if(I){const z=1.05-0.05*outExpo(P(t,c.t0,0.6));x.q.l1.style.transform=`scale(${z})`;x.q.l2.style.transform=`scale(${z})`;x.q.l1.style.transformOrigin='left center';x.q.l2.style.transformOrigin='left center';}el.style.opacity=String(outA);break;}
      case 'kcap':{if(EL.some(y=>y.c&&(y.c.type==='endc'||y.c.type==='hook'||y.c.type==='pricing')&&t>=y.c.t0&&t<=y.c.t1)){el.style.opacity='0';break;}const busyLow=EL.some(y=>y.c&&(y.c.type==='stat'||y.c.type==='chips'||y.c.type==='swaprows')&&t>=y.c.t0-0.1&&t<=y.c.t1);el.classList.toggle('up',busyLow&&!document.body.classList.contains('zones')&&!document.body.classList.contains('zlow'));const ph=x.phrases.find(p=>t>=p.start-0.08&&t<=p.hold);if(!ph){el.style.opacity='0';break;}const idx=x.phrases.indexOf(ph);
        if(x.cur!==idx){el.innerHTML=ph.words.map(w=>'<span>'+w.t+'</span>').join('');x.cur=idx;x.spans=[...el.querySelectorAll('span')];}
        const a=P(t,ph.start-0.08,0.14);el.style.opacity='1';el.style.transform=`scale(${0.86+0.14*outBack(a)}) rotate(${(1-a)*-1.5}deg)`;
        x.spans.forEach((s,k)=>{const w=ph.words[k];const on=t>=w.s-0.02&&t<w.e+0.06;const done=t>=w.e+0.06;s.className=on?'on':(done?'done':'');s.style.transform=on?`scale(${1.06+0.04*Math.sin(Math.PI*clamp((t-w.s)/Math.max(0.18,w.e-w.s)))})`:'scale(1)';});break;}
      case 'emoji':{el.style.opacity=String(outA);x.items.forEach((p,k)=>{const i=c.items[k];const a=P(t,i.at,0.42);const life=t-i.at;p.style.opacity=String(clamp(a*3)*(life>(i.dur||1.6)-0.25?clamp(((i.dur||1.6)-life)/0.25):1));p.style.transform=`scale(${0.2+0.8*outBack(a)}) rotate(${(i.rot||-8)*(1-outExpo(a))+Math.sin(life*5)*3}deg) translateY(${-Math.min(life,1.6)*22}px)`;});break;}
      case 'stat':{const a=P(t,c.t0,0.38);el.style.opacity=String(Math.min(clamp(a*3),outA));x.q.card.style.transform=`scale(${0.6+0.4*outBack(a)}) rotate(${(1-outExpo(a))*-4}deg)`;const n=parseFloat(String(c.num).replace(/[^0-9.]/g,''))||0;if(c.count){const v=Math.round(n*outCubic(P(t,c.t0,0.7)));x.q.n.textContent=String(c.num).replace(/[0-9][0-9,]*/,v.toLocaleString('en-IN'));}break;}
      case 'flash':{const d=c.t1-c.t0;el.style.opacity=String(Math.max(0,1-(t-c.t0)/d));break;}
      case 'grain':{el.style.backgroundPosition=`${(Math.floor(t*24)%7)*41}px ${(Math.floor(t*24)%5)*67}px`;break;}
      case 'endc':{el.style.opacity=String(Math.min(P(t,c.t0,0.2),outA));const a=P(t,c.t0+0.05,0.5);x.q.amt.style.transform=`scale(${0.5+0.5*outBack(a)})`;x.q.amt.style.opacity=String(clamp(a*3));rise(x.q.what,P(t,c.t0+0.35,0.4),30);rise(x.q.who,P(t,c.t0+0.55,0.4),20);rise(x.q.link,P(t,c.link_at??(c.t0+1.0),0.4),30);const la=P(t,(c.link_at??(c.t0+1.0))+0.15,0.4);x.q.arrow.style.opacity=String(la);x.q.arrow.style.transform=`translateY(${10*Math.sin((t-c.t0)*5)}px)`;rise(x.q.lk,P(t,c.logo_at??(c.t0+1.6),0.6),30);rise(x.q.url,P(t,(c.logo_at??(c.t0+1.6))+0.3,0.5),14);break;}
      case 'slam':{el.style.opacity=String(outA);x.items.forEach((w,k)=>{const at=c.words[k].at,nx=(c.words[k+1]||{}).at??c.t1;const on=t>=at&&t<nx+0.05;const a=P(t,at,0.22);w.style.opacity=on?String(clamp(a*4)):'0';w.style.transform=`scale(${1.6-0.6*outExpo(a)}) translateY(${Math.sin(Math.min(1,a)*Math.PI*3)*(1-a)*10}px)`;});break;}
      case 'orbit':{const a=P(t,c.t0,0.6);el.style.opacity=String(Math.min(clamp(a*2),outA));const n=x.items.length;const rot=(t-c.t0)*40;x.items.forEach((it,k)=>{const ang=((k/n)*360+rot)*Math.PI/180;const R=400*outExpo(a),ry=120*outExpo(a);const X=Math.cos(ang)*R,Y=Math.sin(ang)*ry;const depth=(Math.sin(ang)+1)/2;const sc=(0.62+0.5*depth)*(0.6+0.4*outBack(P(t,c.t0+k*0.05,0.5)));it.style.transform=`translate(${X}px,${Y}px) scale(${sc})`;it.style.opacity=String(0.5+0.5*depth);it.style.zIndex=String(Math.round(depth*200));it.style.filter=`blur(${(1-depth)*1.6}px)`;});
        const b=P(t,c.t0+0.35,0.6);x.q.core.style.opacity=String(clamp(b*2));x.q.core.style.transform=`scale(${0.6+0.4*outBack(b)})`;x.q.core.style.zIndex='300';const num=parseInt(c.num)||0;x.q.n.textContent=(b<1?Math.round(num*outCubic(b)):num)+(b>=0.9?String(c.num).replace(/^\d+/,''):'');break;}
      case 'phone':{const a=P(t,c.t0,0.6);el.style.opacity=String(Math.min(clamp(a*2),outA));x.q.dev.style.transform=`perspective(1200px) rotateY(${(1-outExpo(a))*-35}deg) translateY(${(1-outExpo(a))*60}px)`;x.items.forEach((r,k)=>{const b=P(t,(c.rows[k].at??(c.t0+0.5+k*0.35)),0.4);r.style.opacity=String(clamp(b*2));r.style.transform=`translateX(${(1-outExpo(b))*40}px)`;});break;}
      case 'sweep':{const a=P(t,c.t0,c.t1-c.t0);el.style.backgroundPosition=`${120-240*a}% 0`;el.style.opacity='1';break;}
      case 'title':{const a=outExpo(P(t,c.t0,0.55));el.style.opacity=String(Math.min(clamp(a*1.4),outA));el.style.transform=`translateY(${(1-a)*-24}px)`;if(x.q.s){const s=P(t,c.sub_at??(c.t0+0.8),0.5);x.q.s.style.opacity=String(outCubic(s));x.q.s.style.transform=`translateY(${(1-outExpo(s))*10}px)`;}break;}
      case 'captions':{const ph=x.phrases.find(p=>t>=p.start-0.12&&t<=p.hold);if(!ph){el.style.opacity='0';break;}const idx=x.phrases.indexOf(ph);
        if(x.cur!==idx){el.innerHTML='<div class="box">'+ph.words.map(w=>'<span>'+w.t+'</span>').join('')+'</div>';x.cur=idx;x.spans=[...el.querySelectorAll('span')];}
        const a=outExpo(P(t,ph.start-0.12,0.22));el.style.opacity=String(a);el.style.transform=`translateY(${(1-a)*14}px)`;
        x.spans.forEach((s,k)=>{const w=ph.words[k];const on=t>=w.s-0.02&&t<w.e+0.05;const done=t>=w.e+0.05;s.className=on?'on':(done?'done':'');const pop=on?1+0.05*Math.sin(Math.PI*clamp((t-w.s)/Math.max(0.18,w.e-w.s))):1;s.style.transform=`scale(${pop})`;});break;}
      case 'pricing':{el.style.opacity=String(Math.min(P(t,c.t0,0.35),outA));rise(x.q.h,P(t,c.heading_at??c.t0,0.6),30);rise(x.q.payg,P(t,c.payg_at,0.6),50);
        x.q.paygLines.forEach((l,k)=>rise(l,P(t,c.payg_lines[k].at,0.45),18));rise(x.q.pro,P(t,c.pro_at,0.6),50);
        rise(x.q.p1,P(t,c.pro_lines[0].at,0.5),20);rise(x.q.p2,P(t,c.pro_lines[1].at,0.5),20);rise(x.q.p3,P(t,c.pro_lines[2].at,0.4),10);
        x.q.proLines.forEach((l,k)=>rise(l,P(t,(c.pro_lines[k+3]||{}).at??c.t1,0.45),18));break;}
      case 'cta':{el.style.opacity=String(Math.min(P(t,c.t0,0.4),outA));rise(x.q.card,P(t,c.credit_at,0.7),60);rise(x.q.link,P(t,c.link_at,0.5),24);
        const la=P(t,c.link_at+0.2,0.5);x.q.arrow.style.opacity=String(la);x.q.arrow.style.transform=`translateY(${10*Math.sin((t-c.link_at)*4)}px)`;
        rise(x.q.lk,P(t,c.logo_at,0.7),30);rise(x.q.url,P(t,c.logo_at+0.4,0.6),14);break;}
    }
  }
  return active;
}
window.__init=init;window.__seek=seek;
</script></body></html>
'''
out = os.path.join(P, "overlays", "overlay_brand.html")
open(out, "w").write(html.replace("__ICONS__", json.dumps(icons)))
print("wrote", out, os.path.getsize(out), "bytes")
