/* split_cues_coa6.js (scenes 4-7: pin, slots; cite cases + endcard line live in split_panel.html): cue types for the full Cause of Action video, see split/COA_CUES.md. Loaded after split_panel.html's main script;
   uses its globals (BUILD, LAYOUT, SEEK, mk, $, $$, P, clamp, easing helpers, geometry constants). Deterministic: pure function of t.

   pin   {type:"pin", t0, t1, text:"Arose: 1 Apr 2025", land_at, fly_at, slot:5 [, park_at]}
         At land_at the red date stamp (the scene-1 stamp's ink, fall, wobble and panel shake) hits the middle of the content band.
         At park_at (default: just before the next content cue, 1.4..4 s after the hit) it shrinks into the column's top corner AWAY
         from the seam - below the header rule, centred on the kicker row - and a copper tack pins it there. At fly_at it is
         unpinned and flies into the dashed dock of slot `slot` of the slots cue on screen (beside the clock of a clock slot, else
         the card's top-right corner; never before that card has settled), where it stays stamped and leaves with that card.
         No fly_at / no slots cue: it stays parked until t1.
         Exported: window.coaPinZone(c) = the corner box {left, right, top, bottom, cy, gap, side} the parked pin keeps while cue c
         is on screen (null otherwise): split_panel.html's areaFor() starts content below it, the kicker sits beside it.
   slots {type:"slots", t0, t1, head, head_at, slots:[{n, title, at, rule, text [, sub, sub_at]
           [, visual:"map", pins:[{label, at}]] [, visual:"bar", claimed, lost, split_at] [, visual:"clock", clock_at]}]}
         The heading builds as the scene opens (title_at, default t0 + 0.15: no empty panel during the opening question) beside the
         parked pin; at head_at the five numbered slots land EMPTY (dashed) in one compact row; slot k fills at its `at`, turns into
         the active (copper) slot with a pointer, and its detail card (rule chip, text, optional sub-line and visual) rises in under
         the row, large. Earlier slots stay filled (paper) in the row. A card ends above every citation bar on screen while it is
         the active one (a bar that only fades out as the card rises in does not count). The clock starts at clock_at (never
         before the pin has landed in its dock).
         Guests: another content cue on screen while the slot row stands (head_at .. the exit fade, > 0.25 s; e.g. the scene-6
         Arivandandam quote) takes the card area - split_panel.html's areaFor() starts it below the heading + slot row
         (window.coaSlotsRow(c)) and the active card lifts away while it is on screen (and comes back if its slot is still the
         active one when the guest leaves).
   Everything lives in the content column (CL..CL+CW): nothing enters from, crosses or is clipped at the seam. */
(() => {
'use strict';

/* ---------------- styles (scoped to .dpin / .slts) ---------------- */
const STYLE = `
/* pin: the scene-4 date stamp, same red ink as the scene-1 stamp, above the other content cues */
.dpin{left:0;top:0;width:var(--pw);height:1px;mix-blend-mode:multiply;z-index:6;}
.dpin .dps{position:absolute;left:0;top:0;color:var(--red);border:13px double var(--red);border-radius:22px;padding:10px 40px 14px;text-align:center;white-space:nowrap;filter:url(#ink);transform-origin:50% 50%;font-size:86px;text-transform:uppercase;}
.dpin .d1{font-weight:800;font-size:.4em;letter-spacing:.36em;line-height:1.2;margin-right:-.36em;}
.dpin .d2{font-weight:800;font-size:1em;letter-spacing:.04em;line-height:1.02;}
.dpin .dtk{position:absolute;left:0;top:0;width:30px;height:30px;margin:-15px 0 0 -15px;border-radius:50%;
  background:radial-gradient(circle at 35% 30%,#fbd9c6 0%,#e59c7a 22%,#c96a4b 52%,#8f4330 100%);box-shadow:0 6px 10px rgba(70,35,20,.30),inset 0 -2px 3px rgba(80,30,15,.28);}

/* slots: heading, a compact row of numbered slots, the active slot's detail card */
.slts{left:0;top:0;width:var(--pw);height:1080px;}
.slts .sh{position:absolute;left:0;top:0;font-size:80px;line-height:1.04;color:var(--ink);white-space:nowrap;}
.slts .tl{position:absolute;left:0;top:0;}
.slts .tl > div{position:absolute;left:0;top:0;width:100%;height:100%;border-radius:26px;box-sizing:border-box;}
.slts .tl .dsh{border:2.5px dashed rgba(179,87,63,.36);}
.slts .tl .pap{background:var(--paper);border:1.5px solid var(--rule);box-shadow:0 14px 30px rgba(60,40,25,.10),0 2px 6px rgba(60,40,25,.05);}
.slts .tl .act{background:linear-gradient(120deg,#c9714f 0%,var(--accent) 46%,var(--accent-deep) 100%);box-shadow:0 20px 42px rgba(179,87,63,.34),0 4px 10px rgba(120,50,30,.14);}
.slts .tl .in{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:11px;}
.slts .nb{position:relative;width:46px;height:46px;flex:none;}
.slts .nb > div{position:absolute;left:0;top:0;width:46px;height:46px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:23px;line-height:1;}
.slts .nb .n0{box-shadow:inset 0 0 0 2.5px rgba(179,87,63,.36);color:rgba(179,87,63,.62);}
.slts .nb .n1{background:var(--copper);color:#fff;box-shadow:0 8px 16px rgba(179,87,63,.30);}
.slts .nb .n2{background:#fffaf3;color:var(--accent-deep);box-shadow:0 6px 14px rgba(90,35,20,.24);}
.slts .tt{font-weight:800;font-size:21px;letter-spacing:1.6px;text-transform:uppercase;line-height:1.15;white-space:nowrap;color:var(--ink);}
.slts .tl .ph{position:absolute;left:27%;top:0;width:46%;height:10px;border-radius:5px;background:rgba(179,87,63,.13);}
.slts .ptr{position:absolute;left:0;top:0;width:0;height:0;margin-left:-17px;border-left:17px solid transparent;border-right:17px solid transparent;border-top:15px solid #bf6649;}
.slts .sc{position:absolute;left:0;top:0;padding:34px 48px 40px;box-sizing:border-box;transform-origin:50% 0;}
.slts .rl{display:inline-flex;align-items:center;gap:12px;height:54px;padding:0 24px 0 16px;border-radius:27px;background:var(--wash);box-shadow:inset 0 0 0 1.5px rgba(179,87,63,.16);
  color:var(--accent-deep);font-weight:800;font-size:28px;letter-spacing:1px;line-height:1;white-space:nowrap;}
.slts .rl svg{width:30px;height:30px;stroke-width:2.1;}
.slts .stx{font-size:72px;line-height:1.1;color:var(--ink);margin-top:20px;}
.slts .stx .w{position:relative;}
.slts .stx b{font-weight:400;color:var(--accent-deep);}
.slts .ssb{display:flex;align-items:center;gap:20px;margin-top:22px;padding-top:20px;border-top:2px dashed var(--rule);}
.slts .ssb .tile{width:64px;height:64px;border-radius:20px;}
.slts .ssb .tile svg{width:34px;height:34px;}
.slts .ssb .st{font-family:var(--serif);font-size:44px;line-height:1.12;color:var(--ink-soft);}
.slts .vis{position:relative;margin-top:26px;}
.slts .vis svg{position:absolute;left:0;top:0;overflow:visible;}
.slts .mlab{position:absolute;left:0;top:0;display:flex;align-items:center;gap:11px;height:52px;padding:0 22px 0 16px;border-radius:26px;background:var(--paper);border:1.5px solid var(--rule);
  box-shadow:0 12px 26px rgba(60,40,25,.14),0 2px 5px rgba(60,40,25,.06);font-weight:700;font-size:26px;color:var(--ink);white-space:nowrap;box-sizing:border-box;}
.slts .mlab i{display:block;width:13px;height:13px;border-radius:50%;background:var(--accent);flex:none;}
.slts .bw{position:absolute;left:0;top:0;height:84px;transform-origin:0 50%;}
.slts .bp{position:absolute;top:0;height:84px;overflow:hidden;}
.slts .bp > div{position:absolute;left:0;top:0;width:100%;height:100%;}
.slts .bl{left:0;border-radius:42px 0 0 42px;box-shadow:0 18px 38px rgba(179,87,63,.28);}
.slts .br{border-radius:0 42px 42px 0;}
.slts .bp .bg{background:linear-gradient(90deg,#c9714f 0%,var(--accent) 50%,var(--accent-deep) 100%);}
.slts .bp .gy{background:#d8d1c6;}
.slts .bp .hz{background:repeating-linear-gradient(135deg,rgba(255,255,255,0) 0 13px,rgba(255,255,255,.5) 13px 21px);}
.slts .crk{position:absolute;top:-8px;width:5px;height:100px;margin-left:-2.5px;border-radius:3px;background:#fffaf3;}
.slts .blab{position:absolute;left:0;top:0;display:flex;align-items:baseline;gap:12px;white-space:nowrap;}
.slts .blab .am{font-weight:800;font-size:46px;letter-spacing:.3px;line-height:1.1;}
.slts .blab .wd{font-weight:800;font-size:22px;letter-spacing:3px;text-transform:uppercase;line-height:1.1;}
.slts .blab.lc .am,.slts .blab.lc .wd{color:var(--accent-deep);}
.slts .blab.ll .am,.slts .blab.ll .wd{color:#9a938a;}
.slts .blab .sk{position:absolute;left:-6px;top:50%;height:5px;margin-top:-1px;border-radius:3px;background:#9a938a;transform-origin:0 50%;}
.slts .dock{position:absolute;left:0;top:0;border-radius:24px;border:3px dashed rgba(192,57,43,.40);box-sizing:border-box;}
.slts svg.clk{filter:drop-shadow(0 16px 26px rgba(60,40,25,.14));}
`;
document.head.appendChild(Object.assign(document.createElement('style'), { textContent: STYLE }));

/* ---------------- shared ---------------- */
const NOT_CONTENT = new Set(['panel', 'sting', 'endcard', 'lower_third', 'cite', 'pin']);
const PARK_S = 0.45, PARK_R = -4, PARK_D = 0.85, PARK_AIR = 16;   // parked stamp: scale, tilt, travel time, air under the header rule
const FLY_D = 0.6, DOCK_R = -3;                                   // flight into the slot, tilt in the dock
const TILE_H = 108, TILE_GAP = 14, ROW_GAP = 30, CARD_GAP = 36;   // slot row / detail card
const OPS = new Set(['+', '=', '→', '≠', '&', '·']);
let UID = 0;
const opWords = (text) => String(text ?? '').trim().split(/\s+/).filter(Boolean)
  .map(w => `<span class="w">${OPS.has(w) ? `<b>${esc(w)}</b>` : esc(w)}</span>`).join(' ');
const num = (s) => { const m = String(s ?? '').replace(/[,\s]/g, '').match(/\d+(?:\.\d+)?/); return m ? +m[0] : NaN; };
const splitFirst = (s) => { const m = String(s ?? '').trim().match(/^(\S+)\s+(.+)$/); return m ? [m[1], m[2]] : [String(s ?? ''), '']; };
const spanOver = (a0, a1, b0, b1, thr = 0.1) => Math.min(a1, b1) - Math.max(a0, b0) > thr;
const rotPt = (lx, ly, deg) => { const a = deg * Math.PI / 180; return [lx * Math.cos(a) - ly * Math.sin(a), lx * Math.sin(a) + ly * Math.cos(a)]; };

/* ---------------- pin ---------------- */
BUILD.pin = (c) => {
  const s = String(c.text ?? ''), m = s.match(/^\s*([^:]{1,24}):\s*(.+)$/);
  const el = mk(pcontent, 'cue dpin', `<div class="dps">${m ? `<div class="d1">${esc(m[1])}</div><div class="d2">${esc(m[2])}</div>` : `<div class="d2">${esc(s)}</div>`}</div><div class="dtk"></div>`);
  return { el, q: { st: $(el, '.dps'), tk: $(el, '.dtk') } };
};
// geometry + schedule, computed once on first use (the kicker / areaFor() may ask before LAYOUT.pin runs)
function pinGeo(x) {
  if (x.geo) return x.geo;
  const c = x.c, st = x.q.st;
  fitFont(st, () => st.offsetWidth <= CW - 260, 40, 2);
  const w = st.offsetWidth, h = st.offsetHeight, land = c.land_at ?? c.t0 + 0.1;
  let park = c.park_at;
  if (park == null) {   // leaves the middle just before the next content cue arrives, never before the hit has read
    let nx = Infinity;
    for (const y of EL) if (y !== x && !NOT_CONTENT.has(y.c.type) && y.c.t0 > land + 0.3 && y.c.t0 < c.t1) nx = Math.min(nx, y.c.t0);
    park = nx < Infinity ? clamp(nx - PARK_D - 0.15, land + 1.4, land + 4) : land + 2.5;
  }
  // the hit: the middle of the content band, a hair off the column centre (as the scene-1 stamp) so the tilt reads centred; the
  // fall's start scale is capped so the tilted stamp stays STAMP_AIR clear of the seam and below the header rule (uncapped, this
  // wider stamp's first frames covered the scene chip and the logo lockup)
  const bx = CX + 12, by = Math.round((AREA_TOP + AREA_BOTTOM) / 2) - 20;
  const r22 = 22 * Math.PI / 180, half = 1.08 * (w / 2) * Math.cos(r22) + 1.2 * (h / 2) * Math.sin(r22);
  const halfV = 1.08 * (w / 2) * Math.sin(r22) + 1.2 * (h / 2) * Math.cos(r22);
  const s0 = clamp(Math.min((seamDist(bx + away(STAMP_FROM[0])) - STAMP_AIR) / half, (by + STAMP_FROM[1] - RULE_Y - 8) / halfV), 1, STAMP_S0);
  // parked: the column's top corner away from the seam, centred on the kicker row, PARK_AIR below the header rule
  const rr = Math.abs(PARK_R) * Math.PI / 180, ps = PARK_S;
  const hx = ps * (w / 2 * Math.cos(rr) + h / 2 * Math.sin(rr)), hy = ps * (w / 2 * Math.sin(rr) + h / 2 * Math.cos(rr));
  const kx = EL.find(y => y.c.type === 'kicker'), kh = kx ? kx.el.offsetHeight : 38;
  const lft = SIDE === 'right';
  const px = lft ? CL + hx + 2 : CL + CW - hx - 2, py = Math.max(KICK_Y + kh / 2, RULE_Y + 2 + PARK_AIR + hy);
  // the slot it flies into (the slots cue on screen at fly_at): never before that slot's card has settled
  let sx = null, si = -1, flyStart = null;
  if (c.fly_at != null) {
    sx = EL.find(y => y.c.type === 'slots' && y.c.t0 <= c.fly_at && y.c.t1 > c.fly_at) || null;
    const ss = sx ? (sx.c.slots || []) : [];
    if (ss.length) { si = ss.findIndex(s => s.n === c.slot); if (si < 0) si = clamp(Math.round(Number(c.slot) || ss.length) - 1, 0, ss.length - 1);
      flyStart = Math.max(c.fly_at, (ss[si].at ?? sx.c.t0) + 0.7); }
    else sx = null;
  }
  x.geo = { w, h, land, park, bx, by, s0, ps, px, py, hx, hy, sx, si, flyStart,
    zone: { left: px - hx, right: px + hx, top: py - hy, bottom: py + hy, cy: py, gap: 36, side: lft ? 'left' : 'right', t0: park, t1: flyStart ?? c.t1 } };
  return x.geo;
}
// the corner the parked pin keeps while cue c is on screen (split_panel.html: areaFor() / LAYOUT.kicker); the slots cue lays
// itself out round the pin
window.coaPinZone = (c) => {
  if (!c || c.type === 'pin' || c.type === 'slots') return null;
  for (const y of EL) { if (y.c.type !== 'pin') continue; const z = pinGeo(y).zone; if (spanOver(z.t0, z.t1, c.t0, c.t1)) return z; }
  return null;
};
LAYOUT.pin = (x) => { pinGeo(x); x.hitAt = x.geo.land; };   // x.hitAt: shakeAt() shakes the panel on the hit, like the stamp's
SEEK.pin = (x, t) => {
  const g = pinGeo(x), c = x.c, q = x.q;
  let cx, cy, s, r;
  // 1 the hit (the scene-1 stamp's fall and wobble)
  const p = P(t, g.land, STAMP_FALL), tau = t - g.land - STAMP_FALL;
  if (tau < 0) { const e = p * p; s = g.s0 - (g.s0 - 1) * e; r = -22 + 13 * e; cx = g.bx + away(STAMP_FROM[0]) * (1 - e); cy = g.by + STAMP_FROM[1] * (1 - e); }
  else { const d = Math.exp(-9 * tau); s = 1 - 0.05 * d * Math.sin(30 * tau); r = -9 + 1.3 * d * Math.sin(24 * tau); cx = g.bx; cy = g.by; }
  // 2 into the corner: lifts a touch while it travels (away from the seam), then is pressed in
  const pk = P(t, g.park, PARK_D);
  if (pk > 0) {
    const e = inOutCubic(pk);
    cx = lerp(g.bx, g.px, e); cy = lerp(g.by, g.py, inOutCubic(clamp(pk * 1.12)));
    s = lerp(1, g.ps, e) * (1 + 0.1 * Math.sin(Math.PI * pk)); r = lerp(-9, PARK_R, e);
    if (pk >= 1) { const u = t - g.park - PARK_D, d = Math.exp(-10 * u); s = g.ps * (1 - 0.07 * d * Math.sin(24 * u)); r = PARK_R; }
  }
  // 3 unpinned, it drops out of the corner (bowing towards the frame edge, clear of the heading beside it), swings into the
  // slot's dock and is stamped in
  let docked = false;
  const D = g.sx && g.sx.dock;
  if (D && t >= g.flyStart) {
    const f = P(t, g.flyStart, FLY_D), e = inOutCubic(f), ex = inOutCubic(clamp((f - 0.2) / 0.8)), ey = inOutCubic(clamp(f / 0.85));
    cx = lerp(g.px, D.cx, ex) + away(60 * Math.sin(Math.PI * f)); cy = lerp(g.py, D.cy, ey);
    s = lerp(g.ps, D.s, e) * (1 + 0.1 * Math.sin(Math.PI * f)); r = lerp(PARK_R, D.r, e) - away(7 * Math.sin(Math.PI * f));
    if (f >= 1) { docked = true; const u = t - g.flyStart - FLY_D, d = Math.exp(-11 * u); s = D.s * (1 - 0.08 * d * Math.sin(26 * u)); r = D.r + 1.4 * d * Math.sin(22 * u); }
  }
  q.st.style.opacity = f4(clamp(p * 3.5));
  q.st.style.transform = `translate(${f2(cx - g.w / 2)}px,${f2(cy - g.h / 2)}px) rotate(${f2(r)}deg) scale(${f4(s)})`;
  // the tack (through the stamp's top-left corner, clear of the text): drops in as the stamp arrives, pops off as it is unpinned
  const ta = P(t, g.park + PARK_D - 0.12, 0.45), tf = g.flyStart != null && D ? P(t, g.flyStart - 0.06, 0.16) : 0;
  if (ta <= 0 || tf >= 1) q.tk.style.opacity = '0';
  else { const [ox, oy] = rotPt((-g.w / 2 + 16) * s, (-g.h / 2 + 14) * s, r), e = outCubic(ta);
    q.tk.style.opacity = f4(clamp(ta * 4) * (1 - tf));
    q.tk.style.transform = `translate(${f2(cx + ox)}px,${f2(cy + oy - 26 * (1 - e) - 14 * tf)}px) scale(${f4((1 + 0.45 * (1 - e)) * (1 - 0.6 * tf))})`; }
  // exit: its own t1, or with the slot card it was stamped into
  let k = clamp((c.t1 - t) / (c.fade_out ?? 0.3));
  if (docked) { const sc = g.sx.c, ss = sc.slots || [];
    k = Math.min(k, clamp((sc.t1 - t) / (sc.fade_out ?? 0.3)));
    if (g.si + 1 < ss.length && ss[g.si + 1].at != null) k = Math.min(k, 1 - P(t, ss[g.si + 1].at - 0.02, 0.32)); }
  x.el.style.opacity = f4(k); x.el.style.transform = `translateY(${f2(-18 * (1 - k) * (1 - k))}px)`;
};

/* ---------------- slots ---------------- */
function visHTML(s) {
  if (s.visual === 'map') return `<div class="vis vmap"><svg class="mp"></svg>${(s.pins || []).map(p => `<div class="mlab"><i></i><span>${esc(p.label)}</span></div>`).join('')}</div>`;
  if (s.visual === 'bar') {
    const [a1, w1] = splitFirst(s.claimed), [a2, w2] = splitFirst(s.lost);
    return `<div class="vis vbar"><div class="bw"><div class="bp bl"><div class="bg"></div></div><div class="bp br"><div class="bg"></div><div class="gy"></div><div class="hz"></div></div><div class="crk"></div></div>
      <div class="blab lc"><span class="am">${esc(a1)}</span><span class="wd">${esc(w1)}</span></div><div class="blab ll"><span class="am">${esc(a2)}</span><span class="wd">${esc(w2)}</span><div class="sk"></div></div></div>`;
  }
  if (s.visual === 'clock') return `<div class="vis vclk"><div class="dock"></div><svg class="arr"></svg><svg class="clk"></svg></div>`;
  return '';
}
BUILD.slots = (c) => {
  const S = c.slots || [];
  const tiles = S.map((s, k) => { const n = esc(s.n ?? k + 1);
    return `<div class="tl"><div class="dsh"></div><div class="pap"></div><div class="act"></div><div class="in"><div class="nb"><div class="n0">${n}</div><div class="n1">${n}</div><div class="n2">${n}</div></div><div class="tt">${esc(s.title)}</div><div class="ph"></div></div></div>`; }).join('');
  const cards = S.map(s => `<div class="sc card">${s.rule ? `<div class="rl">${ico('book-marked')}<span>${esc(s.rule)}</span></div>` : ''}<div class="stx serif">${opWords(s.text)}</div>${s.sub ? `<div class="ssb"><div class="tile">${ico('file-text')}</div><div class="st">${esc(s.sub)}</div></div>` : ''}${visHTML(s)}</div>`).join('');
  const el = mk(pcontent, 'cue slts', `${c.head ? `<div class="sh serif">${maskWords(c.head)}</div>` : ''}${tiles}<div class="ptr"></div>${cards}`);
  const T = $$(el, '.tl').map(tl => ({ el: tl, dsh: $(tl, '.dsh'), pap: $(tl, '.pap'), act: $(tl, '.act'), n0: $(tl, '.n0'), n1: $(tl, '.n1'), n2: $(tl, '.n2'), tt: $(tl, '.tt'), ph: $(tl, '.ph') }));
  const C = $$(el, '.sc').map(cd => ({ el: cd, rl: $(cd, '.rl'), tx: $(cd, '.stx'), words: $$(cd, '.stx .w'), sb: $(cd, '.ssb'), sbt: $(cd, '.ssb .tile'), vis: $(cd, '.vis') }));
  return { el, q: { sh: $(el, '.sh'), hw: $$(el, '.sh .wi'), T, ptr: $(el, '.ptr'), C } };
};
// a content cue that shares the screen with slots cue s while its slot row stands (head_at .. the exit fade, > 0.25 s): it takes the
// card area under the row. The scene-5 cue leaving as the scene opens and the scene-7 cue arriving as it closes are not guests.
const isGuest = (c, s) => !!c && !NOT_CONTENT.has(c.type) && c.type !== 'slots' && c.type !== 'kicker'
  && spanOver(c.t0, c.t1, s.head_at ?? s.t0, s.t1 - (s.fade_out ?? 0.3), 0.25);
// the bottom of the heading + slot row of the slots cue that content cue c is a guest of, null otherwise: split_panel.html's
// areaFor() starts such a guest below it
window.coaSlotsRow = (c) => {
  if (!c) return null;
  for (const y of EL) { if (y.c.type !== 'slots' || !isGuest(c, y.c)) continue;
    if (y.rowBottom == null) LAYOUT.slots(y);
    return y.rowBottom ?? null; }
  return null;
};
// the pin that is parked while this slots cue is on screen, and the one that flies into it
const pinFor = (x) => EL.find(y => y.c.type === 'pin' && (() => { const z = pinGeo(y).zone; return spanOver(z.t0, z.t1, x.c.t0, x.c.t1); })());
const pinInto = (x, k) => EL.find(y => y.c.type === 'pin' && pinGeo(y).sx === x && pinGeo(y).si === k);

function layMap(V, s, W, H) {
  const id = 'c6m' + (++UID), svg = $(V.el, 'svg.mp'), pins = s.pins || [];
  V.el.style.height = H + 'px';
  svg.setAttribute('width', W); svg.setAttribute('height', H); svg.setAttribute('viewBox', `0 0 ${W} ${H}`);
  const PP = [[0.19, 0.72], [0.81, 0.44], [0.52, 0.86]];   // first pin lower left, second upper right (labels face inwards)
  V.pts = pins.map((p, i) => [Math.round(PP[i % 3][0] * W), Math.round(PP[i % 3][1] * H)]);
  const X = (f) => f2(f * W), Y = (f) => f2(f * H);
  const blocks = [[.04, .07, .2, .16], [.44, .05, .16, .17], [.66, .07, .12, .14], [.05, .42, .14, .18], [.6, .66, .16, .16], [.84, .7, .13, .18], [.41, .5, .11, .14]]
    .map(([a, b, cw, ch]) => `<rect x="${X(a)}" y="${Y(b)}" width="${X(cw)}" height="${Y(ch)}" rx="12" fill="#e9dfcd" opacity=".75"/>`).join('');
  const roads = [`M -20 ${Y(.33)} C ${X(.3)} ${Y(.24)} ${X(.55)} ${Y(.48)} ${W + 20} ${Y(.36)}`,
                 `M ${X(.33)} -20 C ${X(.39)} ${Y(.42)} ${X(.29)} ${Y(.72)} ${X(.36)} ${H + 20}`,
                 `M ${X(.57)} ${H + 20} C ${X(.65)} ${Y(.62)} ${X(.71)} ${Y(.3)} ${X(.9)} -20`];
  const river = `M -30 ${Y(.9)} C ${X(.26)} ${Y(.74)} ${X(.55)} ${Y(1.04)} ${W + 30} ${Y(.82)}`;
  let route = '';
  if (V.pts.length >= 2) { const [a, b] = V.pts; route = `M ${a[0]} ${a[1]} C ${f2(a[0] + 0.3 * W)} ${f2(a[1] + 0.05 * H)} ${f2(b[0] - 0.32 * W)} ${f2(b[1] + 0.32 * H)} ${b[0]} ${b[1]}`; }
  const tear = 'M0 0 C -4 -10 -22 -22 -22 -38 A 22 22 0 1 1 22 -38 C 22 -22 4 -10 0 0 Z';
  svg.innerHTML = `<defs><clipPath id="${id}c"><rect width="${W}" height="${H}" rx="26"/></clipPath><clipPath id="${id}r"><rect class="rtr" x="0" y="-60" width="0" height="${H + 120}"/></clipPath>
      <linearGradient id="${id}g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e29776"/><stop offset=".5" stop-color="#cc785c"/><stop offset="1" stop-color="#a24c35"/></linearGradient></defs>
    <g clip-path="url(#${id}c)"><rect width="${W}" height="${H}" fill="#f2e9da"/>${blocks}
      <path d="${river}" fill="none" stroke="#cbd6d2" stroke-width="30" stroke-linecap="round" opacity=".9"/>
      ${roads.map(d => `<path class="rd0" d="${d}" pathLength="1" fill="none" stroke="#e3d6c2" stroke-width="20" stroke-linecap="round"/><path class="rd1" d="${d}" pathLength="1" fill="none" stroke="#fffaf3" stroke-width="14" stroke-linecap="round"/>`).join('')}
      ${route ? `<path class="rt" d="${route}" fill="none" stroke="#c4694c" stroke-width="5" stroke-dasharray="2 13" stroke-linecap="round" clip-path="url(#${id}r)"/>` : ''}</g>
    <rect width="${W}" height="${H}" rx="26" fill="none" stroke="#e0d7c6" stroke-width="1.5"/>
    ${V.pts.map(([px, py]) => `<g class="mpin" transform="translate(${px} ${py})"><ellipse class="msh" rx="16" ry="6" fill="rgba(60,40,25,.28)"/><ellipse class="mrp" rx="16" ry="6" fill="none" stroke="#cc785c" stroke-width="3"/>
      <g class="mdr"><path d="${tear}" fill="url(#${id}g)"/><circle cy="-38" r="9" fill="#fffaf3"/></g></g>`).join('')}`;
  V.roads = $$(svg, '.rd0').map((r0, j) => [r0, $$(svg, '.rd1')[j]]);
  V.route = $(svg, '.rt'); V.rtr = $(svg, '.rtr');
  V.pins = $$(svg, '.mpin').map((g, i) => ({ g, sh: $(g, '.msh'), rp: $(g, '.mrp'), dr: $(g, '.mdr'), at: pins[i].at }));
  // labels beside the pin heads, facing inwards (left pins: label to the right; right pins: to the left)
  V.labs = $$(V.el, '.mlab');
  V.labs.forEach((lb, i) => { const [px, py] = V.pts[i], hy = py - 38 * 1.3, w = lb.offsetWidth, lh = lb.offsetHeight;
    lb.style.left = f2(px <= W / 2 ? px + 44 : px - 44 - w) + 'px'; lb.style.top = f2(hy - lh / 2) + 'px'; });
  if (V.pts.length >= 2) { V.rx0 = Math.min(V.pts[0][0], V.pts[1][0]) - 10; V.rx1 = Math.max(V.pts[0][0], V.pts[1][0]) + 10; }
}
function layBar(V, s, W) {
  const a = num(s.claimed), b = num(s.lost); let fc = a > 0 && b > 0 ? a / (a + b) : 0.6; fc = clamp(fc, 0.25, 0.8);
  const bw = W - 46, wl = Math.round(bw * fc);
  V.bw = $(V.el, '.bw'); V.bl = $(V.el, '.bl'); V.br = $(V.el, '.br'); V.crk = $(V.el, '.crk');
  V.bw.style.width = bw + 'px'; V.bw.style.top = '6px';
  V.bl.style.width = wl + 'px'; V.br.style.left = wl + 'px'; V.br.style.width = (bw - wl) + 'px'; V.crk.style.left = wl + 'px';
  // one continuous gradient across both parts while the bar is whole
  for (const [el, off] of [[$(V.bl, '.bg'), 0], [$(V.br, '.bg'), wl]]) { el.style.width = bw + 'px'; el.style.left = -off + 'px'; }
  V.gy = $(V.br, '.gy'); V.hz = $(V.br, '.hz');
  V.lc = $(V.el, '.blab.lc'); V.ll = $(V.el, '.blab.ll'); V.sk = $(V.ll, '.sk');
  V.lc.style.top = V.ll.style.top = (6 + 84 + 26) + 'px'; V.ll.style.left = (wl + 26) + 'px';
  V.sk.style.width = ($(V.ll, '.am').offsetWidth + 12) + 'px';
  V.el.style.height = (6 + 84 + 26 + V.lc.offsetHeight + 4) + 'px';
}
function layClock(V, s, W, H, dk) {
  V.el.style.height = H + 'px';
  // dock -> arrow -> clock, centred in the card
  const R = Math.round(H / 2) - 14, lead = dk ? dk.w + 30 + 150 + 22 : 0, ox = Math.round(Math.max(0, (W - lead - 2 * R - 24) / 2));
  const cx = ox + lead + R + 12, cy = H / 2;
  V.dock = $(V.el, '.dock');
  if (dk) { Object.assign(V.dock.style, { left: ox + 'px', top: f2((H - dk.h) / 2) + 'px', width: dk.w + 'px', height: dk.h + 'px' }); V.dc = [ox + dk.w / 2, H / 2]; }
  else V.dock.style.display = 'none';
  const arr = $(V.el, 'svg.arr'), clk = $(V.el, 'svg.clk');
  if (dk) { const x0 = ox + dk.w + 24, x1 = cx - R - 20;
    arr.setAttribute('width', W); arr.setAttribute('height', H);
    arr.innerHTML = `<path class="al" d="M ${x0} ${cy} L ${x1 - 6} ${cy}" pathLength="1" fill="none" stroke="#cc785c" stroke-width="5" stroke-linecap="round"/>
      <path class="ah" d="M ${x1 - 20} ${cy - 15} L ${x1} ${cy} L ${x1 - 20} ${cy + 15}" fill="none" stroke="#cc785c" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>`;
    V.al = $(arr, '.al'); V.ah = $(arr, '.ah'); V.ahx = x1; }
  else arr.style.display = 'none';
  clk.setAttribute('width', W); clk.setAttribute('height', H);
  let ticks = '';
  for (let i = 0; i < 12; i++) { const a = i * Math.PI / 6, big = i % 3 === 0, r1 = R - 18, r2 = R - (big ? 38 : 29);
    ticks += `<line x1="${f2(cx + Math.sin(a) * r1)}" y1="${f2(cy - Math.cos(a) * r1)}" x2="${f2(cx + Math.sin(a) * r2)}" y2="${f2(cy - Math.cos(a) * r2)}" stroke="${big ? '#b3573f' : '#dcc9b5'}" stroke-width="${big ? 5.5 : 3.5}" stroke-linecap="round"/>`; }
  clk.innerHTML = `<g class="face"><circle cx="${cx}" cy="${cy}" r="${R}" fill="#fffcf6" stroke="#cc785c" stroke-width="9"/><circle cx="${cx}" cy="${cy}" r="${R - 9}" fill="none" stroke="#f0e2d3" stroke-width="2"/>
      <path class="arc" fill="rgba(204,120,92,.22)" d=""/>${ticks}
      <line class="hh" x1="${cx}" y1="${cy + 10}" x2="${cx}" y2="${f2(cy - R * 0.46)}" stroke="#b3573f" stroke-width="10" stroke-linecap="round"/>
      <line class="mh" x1="${cx}" y1="${cy + 14}" x2="${cx}" y2="${f2(cy - R + 34)}" stroke="#2a2624" stroke-width="6.5" stroke-linecap="round"/>
      <circle cx="${cx}" cy="${cy}" r="11" fill="#b3573f"/><circle cx="${cx}" cy="${cy}" r="4.5" fill="#fffaf3"/></g>`;
  Object.assign(V, { cx, cy, R, face: $(clk, '.face'), arc: $(clk, '.arc'), hh: $(clk, '.hh'), mh: $(clk, '.mh') });
}
LAYOUT.slots = (x) => {
  if (x.laid) return; x.laid = true;   // once: coaSlotsRow() may lay it out before init's own pass reaches it
  const c = x.c, q = x.q, S = c.slots || [], n = S.length, A = areaFor(c);
  const pz = pinFor(x), z = pz ? pinGeo(pz).zone : null;
  x.ats = S.map((s, k) => s.at ?? (c.head_at ?? c.t0) + 1 + 2 * k);
  x.headT = c.title_at ?? Math.min(c.head_at ?? c.t0, c.t0 + 0.15);
  // heading: on the parked pin's row, beside it; else at the top of the band
  let rowB = z ? z.bottom : A.top - ROW_GAP;
  if (q.sh) {
    let hx = CL, hw = CW;
    if (z) { if (z.side === 'left') { hx = Math.round(z.right + z.gap); hw = CL + CW - hx; } else hw = Math.round(z.left - z.gap - CL); }
    fitFont(q.sh, () => q.sh.offsetWidth <= hw, 52, 2);
    const h = q.sh.offsetHeight, top = z ? Math.round(z.cy - h / 2 + 3) : A.top;
    q.sh.style.left = hx + 'px'; q.sh.style.top = top + 'px'; rowB = Math.max(rowB, top + h);
    // once the pin has flown out of the corner (and landed), the heading glides into the corner
    const pg = pz ? pinGeo(pz) : null;
    x.glide = pg && z.side === 'left' && pg.flyStart != null && pg.sx && pg.flyStart < c.t1 - 1 ? { at: pg.flyStart + FLY_D + 0.35, dx: CL - hx } : null;
  }
  // the row of numbered slots (one title size for the row)
  const tw = n ? (CW - (n - 1) * TILE_GAP) / n : 0, ty = Math.round(rowB + ROW_GAP);
  x.tileX = q.T.map((T, k) => { const lx = CL + k * (tw + TILE_GAP);
    Object.assign(T.el.style, { left: f2(lx) + 'px', top: ty + 'px', width: f2(tw) + 'px', height: TILE_H + 'px' }); return lx + tw / 2; });
  if (n) { const fs = q.T.map(T => fitFont(T.tt, () => T.tt.offsetWidth <= tw - 24, 15, 1)), m = Math.min(...fs); q.T.forEach(T => { T.tt.style.fontSize = m + 'px'; }); }
  q.T.forEach(T => { T.ph.style.top = f2(T.tt.offsetTop + T.tt.offsetHeight / 2 - 5) + 'px'; });
  x.ptrY = ty + TILE_H - 2; x.rowBottom = ty + TILE_H;
  // guests: other content cues on screen with this one take the card area (they start below the row, see coaSlotsRow)
  x.guests = EL.filter(y => isGuest(y.c, c));
  // the detail cards: one per slot, under the row, each ending above the citation bars on screen while it is the active one
  const top = Math.round(ty + TILE_H + CARD_GAP), W = CW - 96;
  x.cardTop = top; x.V = [];
  q.C.forEach((C, k) => {
    const s = S[k], from = x.ats[k], to = k + 1 < n ? x.ats[k + 1] : c.t1;
    let bottom = AREA_BOTTOM;
    // a bar on screen while the card is (its fade-out against the card's rise-in does not count: an outgoing bar 0.13 s into
    // the next slot squeezed that whole 16 s card - map and text - to the minimum sizes)
    for (const y of EL) if (y.c.type === 'cite' && y.top != null && spanOver(y.c.at ?? y.c.t0, y.c.t1 - (y.c.fade_out ?? 0.3), from + 0.06, to, 0.25)) bottom = Math.min(bottom, y.top - GAP);
    const avail = bottom - top, cd = C.el;
    Object.assign(cd.style, { left: CL + 'px', top: top + 'px', width: CW + 'px' });
    const V = { el: C.vis, type: s.visual }; x.V.push(V);
    const pinIn = pinInto(x, k), pg = pinIn ? pinGeo(pinIn) : null;
    const dk = pg ? { w: Math.round(pg.w * pg.ps) + 34, h: Math.round(pg.h * pg.ps) + 28 } : null;
    const lay = (vh) => { if (!C.vis) return;
      if (s.visual === 'map') layMap(V, s, W, vh); else if (s.visual === 'bar') layBar(V, s, W); else if (s.visual === 'clock') layClock(V, s, W, vh, dk); };
    // text: big; a card with a visual keeps it to one line when it can, a text-only card may take two lines at a larger size
    C.tx.style.fontSize = (C.vis ? 72 : 90) + 'px';
    if (C.vis) fitLines(C.tx, 62, 2, 50); else fitLines(C.tx, 84, 2, 54);
    let vh = s.visual === 'map' ? 300 : s.visual === 'clock' ? 264 : 0; const vmin = s.visual === 'map' ? 220 : 210;
    lay(vh);
    while (cd.offsetHeight > avail && vh > vmin) { vh -= 8; lay(vh); }
    fitFont(C.tx, () => cd.offsetHeight <= avail, 44, 2);
    if (C.sb) fitFont($(C.sb, '.st'), () => C.sb.scrollWidth <= C.sb.clientWidth + 1 && cd.offsetHeight <= avail, 30, 2);
    if (cd.offsetHeight > avail) console.warn('[split_cues_coa6] slots card', k + 1, 'is', cd.offsetHeight - avail, 'px taller than its band');
    if (C.sb && !C.vis) { V.h1 = cd.offsetHeight; C.sb.style.display = 'none'; V.h0 = cd.offsetHeight; C.sb.style.display = ''; cd.style.overflow = 'hidden'; }
    // where the pin is stamped in (panel coordinates, the card at rest): the clock's dock, else the card's top-right corner
    if (pinIn && !V.dc) { V.dock = mk(cd, 'dock'); V.dcCard = true; V.dc = [CW - 40 - dk.w / 2, 24 + dk.h / 2];
      Object.assign(V.dock.style, { left: (CW - 40 - dk.w) + 'px', top: '24px', width: dk.w + 'px', height: dk.h + 'px' }); }
    if (pinIn) x.dock = { cx: CL + cd.clientLeft + (V.dcCard ? 0 : C.vis.offsetLeft) + V.dc[0], cy: top + cd.clientTop + (V.dcCard ? 0 : C.vis.offsetTop) + V.dc[1], s: pg.ps, r: DOCK_R, k };
    V.subAt = s.sub_at ?? from + 1.2;
    V.splitAt = s.split_at ?? from + 2.5;
    V.land = pg && pg.flyStart != null ? pg.flyStart + FLY_D : null;
    V.clockAt = Math.max(s.clock_at ?? from + 1.5, V.land != null ? V.land + 0.02 : -Infinity);
  });
};

// tile k's state: shown (empty) from head_at, filled at its `at`, active until the next slot fills
function seekTile(x, T, k, t) {
  const c = x.c, n = x.ats.length, ha = c.head_at ?? c.t0, at = x.ats[k];
  const pa = P(t, ha + k * 0.08, 0.5), pf = P(t, at, 0.55), ef = outCubic(pf);
  const on = clamp(P(t, at, 0.45) - (k + 1 < n ? P(t, x.ats[k + 1], 0.45) : 0)), eo = outCubic(on);
  T.el.style.opacity = f4(clamp(pa * 2.5));
  T.el.style.transform = `translateY(${f2((1 - outExpo(pa)) * 28 - 5 * eo)}px) scale(${f4((0.86 + 0.14 * outBack(pa)) * (1 + 0.035 * eo))})`;
  T.dsh.style.opacity = f4(1 - ef); T.pap.style.opacity = f4(ef * (1 - eo)); T.act.style.opacity = f4(ef * eo);
  T.n0.style.opacity = f4(1 - clamp(pf * 3));
  T.n1.style.opacity = f4(clamp(pf * 3) * (1 - eo)); T.n2.style.opacity = f4(clamp(pf * 3) * eo);
  const nb = T.n1.parentNode;
  nb.style.transform = pf > 0 && pf < 1 ? `scale(${f4(0.6 + 0.4 * spring(pf))}) rotate(${f2((1 - outCubic(pf)) * -110)}deg)` : '';
  wipeIn(T.tt, outCubic(P(t, at + 0.1, 0.45)));
  T.tt.style.color = mixC('#1f1e1d', '#fffaf3', eo);
  T.ph.style.opacity = f4(1 - clamp(pf * 2.5));
  return eo;
}
function seekMap(V, t, a) {
  const pm = P(t, a + 0.28, 0.6);
  V.el.style.opacity = f4(clamp(pm * 2)); V.el.style.transform = `scale(${f4(0.97 + 0.03 * outCubic(pm))})`;
  V.roads.forEach((pair, j) => { const p = P(t, a + 0.38 + j * 0.14, 0.9), d = f4(1 - inOutCubic(p));   // drawn: no dash pattern left at rest
    pair.forEach(r => { r.style.strokeDasharray = p >= 1 ? 'none' : '1 1'; r.style.strokeDashoffset = p >= 1 ? '0' : d; }); });
  V.pins.forEach((p, i) => {
    const pp = P(t, p.at ?? a + 1 + i, 0.7);
    p.g.style.opacity = pp > 0 ? '1' : '0';
    p.dr.setAttribute('transform', `translate(0 ${f2(-96 * (1 - spring(pp, 6, 12)))}) scale(1.3)`);
    p.dr.setAttribute('opacity', f4(clamp(pp * 5)));
    p.sh.setAttribute('transform', `scale(${f4(0.3 + 0.7 * clamp(pp * 1.6))})`); p.sh.setAttribute('opacity', f4(clamp(pp * 2)));
    const pr = P(t, (p.at ?? a + 1 + i) + 0.2, 0.7);
    p.rp.setAttribute('opacity', pr > 0 && pr < 1 ? f4(0.75 * (1 - pr)) : '0');
    p.rp.setAttribute('transform', `scale(${f4(1 + 2.6 * outCubic(pr))})`);
    if (V.labs[i]) { const pl = P(t, (p.at ?? a + 1 + i) + 0.16, 0.5); V.labs[i].style.opacity = f4(clamp(pl * 2.5));
      V.labs[i].style.transform = `translateY(${f2((1 - outExpo(pl)) * 14)}px) scale(${f4(0.9 + 0.1 * outBack(pl))})`; }
  });
  if (V.route) { const last = Math.max(...V.pins.map((p, i) => p.at ?? a + 1 + i)), pr = P(t, last + 0.35, 0.8);
    V.rtr.setAttribute('x', f2(V.rx0)); V.rtr.setAttribute('width', f2((V.rx1 - V.rx0) * outCubic(pr)));
    V.route.style.strokeDashoffset = f2(-t * 26); }
}
function seekBar(V, t, a) {
  const pf = P(t, a + 0.32, 0.85);
  V.bw.style.opacity = f4(clamp(pf * 4)); V.bw.style.transform = `scaleX(${f4(outExpo(pf))})`;
  const sa = V.splitAt, ps = P(t, sa, 0.6), e = outCubic(ps);
  const ck = P(t, sa - 0.1, 0.3); V.crk.style.opacity = f4(Math.sin(Math.PI * ck) * (ps < 0.6 ? 1 : 0));
  V.br.style.transform = `translate(${f2(26 * e)}px,${f2(14 * e)}px) rotate(${f2(2.5 * e)}deg)`;
  V.br.style.boxShadow = e > 0 ? `0 ${f2(12 * (1 - e))}px ${f2(30 * (1 - e))}px rgba(179,87,63,${f4(0.28 * (1 - e))})` : '';
  V.gy.style.opacity = f4(e); V.hz.style.opacity = f4(outCubic(P(t, sa + 0.2, 0.5)));
  V.bl.style.transform = `scale(${f4(1 + 0.03 * Math.sin(Math.PI * P(t, sa + 0.05, 0.45)))})`;
  rise(V.lc, P(t, sa + 0.15, 0.55), 18); rise(V.ll, P(t, sa + 0.32, 0.55), 18);
  V.sk.style.transform = `scaleX(${f4(outCubic(P(t, sa + 0.65, 0.4)))})`;
}
function seekDock(V, t, a) {   // the empty dock breathes slowly until the stamp lands in it
  const pd = P(t, a + 0.42, 0.45), gone = V.land != null ? P(t, V.land - 0.04, 0.16) : 0;
  V.dock.style.opacity = f4(clamp(pd * 2) * (0.7 + 0.3 * Math.cos(TAU * Math.max(0, t - a - 0.42) / 1.3)) * (1 - gone));
}
function seekClock(V, t, a) {
  const pc = P(t, a + 0.3, 0.6);
  V.face.style.opacity = f4(clamp(pc * 2.5));
  V.face.style.transformOrigin = `${V.cx}px ${V.cy}px`;
  const u = t - V.clockAt, TK = 0.42;
  let ang = 0, pulse = 0;
  if (u > 0) { const n = Math.floor(u / TK), fr = (u - n * TK) / 0.16; ang = 30 * (n + outBack(clamp(fr), 2.2)); pulse = Math.exp(-14 * (u - n * TK)); }
  V.face.style.transform = `scale(${f4((0.8 + 0.2 * spring(pc)) * (1 + 0.012 * pulse * (u > 0 ? 1 : 0)))})`;
  V.mh.setAttribute('transform', `rotate(${f2(ang)} ${V.cx} ${V.cy})`); V.hh.setAttribute('transform', `rotate(${f2(ang / 12)} ${V.cx} ${V.cy})`);
  const A = Math.min(ang, 359.9) * Math.PI / 180, r = V.R - 10;
  V.arc.setAttribute('d', ang <= 0.01 ? '' : `M ${V.cx} ${V.cy} L ${V.cx} ${f2(V.cy - r)} A ${r} ${r} 0 ${A > Math.PI ? 1 : 0} 1 ${f2(V.cx + Math.sin(A) * r)} ${f2(V.cy - Math.cos(A) * r)} Z`);
  if (V.dc) {   // the empty dock waits until the stamp is in, then the arrow runs to the clock
    seekDock(V, t, a);
    const pa = P(t, V.clockAt - 0.18, 0.4);
    V.al.style.strokeDasharray = pa >= 1 ? 'none' : '1 1'; V.al.style.strokeDashoffset = pa >= 1 ? '0' : f4(1 - outCubic(pa)); V.al.style.opacity = pa > 0 ? '1' : '0';
    const ph = P(t, V.clockAt + 0.1, 0.3); V.ah.style.opacity = f4(clamp(ph * 3));
    V.ah.style.transformOrigin = `${V.ahx}px ${V.cy}px`; V.ah.style.transform = `scale(${f4(spring(ph))})`;
  }
}
SEEK.slots = (x, t) => {
  const c = x.c, q = x.q, n = x.ats.length;
  if (q.sh) q.sh.style.transform = x.glide ? `translateX(${f2(x.glide.dx * inOutCubic(P(t, x.glide.at, 0.8)))}px)` : '';
  q.hw.forEach((w, k) => { const p = P(t, x.headT + k * 0.13, 0.62), e = outExpo(p);
    w.style.transform = `translateY(${f2((1 - e) * 108)}%) rotate(${f2((1 - e) * 6)}deg)`; w.style.opacity = f4(clamp(p * 4)); });
  const on = q.T.map((T, k) => seekTile(x, T, k, t));
  // the pointer under the active slot glides along the row
  let act = -1; for (let k = 0; k < n; k++) if (t >= x.ats[k]) act = k;
  if (act < 0) q.ptr.style.opacity = '0';
  else { const p = outExpo(P(t, x.ats[act], 0.5)), px = act > 0 ? lerp(x.tileX[act - 1], x.tileX[act], p) : x.tileX[0];
    q.ptr.style.opacity = f4(act > 0 ? 1 : clamp(P(t, x.ats[0] + 0.1, 0.3) * 2));
    q.ptr.style.transform = `translate(${f2(px)}px,${f2(x.ptrY - 5 * on[act] + 2)}px)`; }
  // a guest on screen (e.g. the scene-6 quote) takes the card area: the active card lifts away as it arrives, back when it leaves
  const gy = (x.guests || []).reduce((m, y) => Math.max(m, outCubic(P(t, (y.c.at ?? y.c.t0) - 0.12, 0.32)) * (1 - P(t, y.c.t1 - 0.15, 0.35))), 0);
  // detail cards: the active one rises in under the row as the previous one lifts away
  q.C.forEach((C, k) => {
    const a = x.ats[k], pe = P(t, a + 0.06, 0.65), px = Math.max(k + 1 < n ? P(t, x.ats[k + 1] - 0.02, 0.32) : 0, gy), show = t >= a + 0.06 && px < 1;
    // '' (inherit), never 'visible': a child set visible stays drawn after seek() hides the cue's root - the last card stayed on
    // screen at the root's last exit opacity (~7 %) through all of scene 7 in a sequential render
    const vv = show ? '' : 'hidden'; if (C.el.style.visibility !== vv) C.el.style.visibility = vv; if (!show) return;
    C.el.style.opacity = f4(clamp(pe * 2.5) * (1 - outCubic(px)));
    C.el.style.transform = `translateY(${f2((1 - outExpo(pe)) * 56 - 18 * outCubic(px))}px) scale(${f4((0.96 + 0.04 * outBack(pe)) * (1 - 0.02 * px))})`;
    if (C.rl) rise(C.rl, P(t, a + 0.1, 0.5), 16);
    C.words.forEach((w, j) => { const p = P(t, a + 0.18 + j * 0.045, 0.4); w.style.opacity = f4(outCubic(p)); w.style.top = f2((1 - outCubic(p)) * 22) + 'px'; });
    const V = x.V[k];
    if (C.sb) { rise(C.sb, P(t, V.subAt, 0.55), 20); C.sbt.style.transform = `scale(${f4(spring(P(t, V.subAt + 0.08, 0.6)))})`;
      if (V.h1 != null) C.el.style.height = f2(lerp(V.h0, V.h1, outExpo(P(t, V.subAt - 0.1, 0.55)))) + 'px'; }
    if (V.type === 'map') seekMap(V, t, a); else if (V.type === 'bar') seekBar(V, t, a); else if (V.type === 'clock') seekClock(V, t, a);
    if (V.dcCard) seekDock(V, t, a);
  });
  cueRoot(x, t, { noLife: true });
};
})();
