/* split_cues_course.js: generic cue types for the LawWorld course series (owner 19-10-2026: BNSS / CPC storyboards, one long video each,
   16:9 + 9:16). Loaded after split_panel.html's main script and split_cues_coa*.js; uses the page globals (BUILD, LAYOUT, SEEK, mk, $, $$,
   P, clamp, lerp, easing helpers, ico, esc, areaFor, fitFont, fitLines, cueRoot, rise, wipeIn, CL, CW, CX, AWAY, away). Deterministic: every
   pose is a pure function of t. Everything lives in one IIFE; styles are injected once, namespaced .cr-*.
   Fields (+ = optional):
     section   t0 t1 at act num title +points[{text, at, +tone:"no"}] +icon +note{text, at}
               a statute card: act tag + big "§ num" + title; points tick in one by one (tone "no" = a red cross: what the provision
               does NOT do); note = a dashed footnote line under the points.
     compare   t0 t1 +head +head_at cols[{title, +icon, +at}, {title, +icon, +at}] rows[{cells:[left, right], at | cells_at:[tl, tr]}] +verdict{text, at}
               two columns side by side (left ink, right copper); row k fills both cells at its at (right cell 0.15 s later); the
               verdict line lands under the columns.
     flow      t0 t1 +head +head_at steps[{label, +sub, +icon, at, +tone:"stop"|"ok"|"muted"}] +dir:"h"|"v" +note{text, at}
               a chain of step cards joined by arrows that draw towards each new step; tone stop = red outline + cross badge (a route
               that is closed), ok = copper card (the right route), muted = greyed. dir "h" (default for <= 4 steps) or "v".
     counters  t0 t1 +head +head_at items[{value, unit, label, +sub, at, +tone:"red"}] +note{text, at}
               up to 3 big day / hour counters side by side; the ring fills while the number counts up from 0 at its at.
   Every cue also takes the optional fade_out and y (top, panel px) like the page's own cues. */
(() => {
'use strict';

const CSS = `
/* ---------- split_cues_course.js (namespaced .cr-*) ---------- */
.cr-hd{display:flex;align-items:flex-end;gap:18px;}
/* digits in serif text are set in Manrope: Instrument Serif's 1 reads as an l ("2(l)(g)", "Art. ll5") */
.cr-d{font-family:var(--sans);font-weight:600;font-size:.84em;letter-spacing:0;font-style:normal;}
.cr-sec .cr-num .cr-d{font-weight:700;font-size:.8em;letter-spacing:-1px;}
.cr-h{font-size:84px;line-height:1.02;color:var(--ink);text-wrap:balance;}
.cr-hu{width:116px;height:6px;border-radius:3px;background:var(--copper);margin-top:24px;transform-origin:0 50%;}
.cr-sec{left:var(--cl);width:var(--cw);}
.cr-sec .cr-card{position:relative;padding:46px 54px 50px;overflow:hidden;}
.cr-sec .cr-top{display:flex;align-items:center;gap:26px;}
.cr-sec .cr-act{font-weight:800;font-size:30px;letter-spacing:6px;color:#fffaf3;background:var(--copper);border-radius:16px;padding:12px 18px 12px 24px;line-height:1;white-space:nowrap;box-shadow:0 10px 22px rgba(179,87,63,.28);}
.cr-sec .cr-num{font-size:118px;line-height:.95;color:var(--ink);white-space:nowrap;}
.cr-sec .cr-num i{font-style:normal;color:var(--accent-deep);margin-right:.12em;}
.cr-sec .cr-ttl{font-size:60px;line-height:1.1;color:var(--ink-soft);margin-top:26px;text-wrap:balance;}
.cr-sec .cr-pts{margin-top:30px;border-top:2px solid var(--rule);padding-top:12px;}
.cr-sec .cr-pt{display:flex;align-items:center;gap:24px;padding:14px 0;}
.cr-sec .cr-pk{width:58px;height:58px;border-radius:50%;flex:none;display:flex;align-items:center;justify-content:center;background:var(--copper);color:#fff;box-shadow:0 8px 18px rgba(179,87,63,.26);}
.cr-sec .cr-pk.no{background:var(--red);box-shadow:0 8px 18px rgba(192,57,43,.26);}
.cr-sec .cr-pk svg{width:32px;height:32px;stroke-width:3;}
.cr-sec .cr-ptx{flex:1;min-width:0;font-size:48px;line-height:1.14;color:var(--ink);}
.cr-note{display:flex;align-items:center;gap:18px;margin-top:22px;padding-top:20px;border-top:2px dashed var(--rule);font-size:40px;line-height:1.15;color:var(--muted);}
.cr-note .tile{width:62px;height:62px;border-radius:18px;}
.cr-note .tile svg{width:32px;height:32px;}
.cr-cmp{left:var(--cl);width:var(--cw);}
.cr-cmp .cr-cols{display:flex;gap:30px;margin-top:40px;}
.cr-cmp .cr-col{position:relative;flex:1 1 0;min-width:0;padding:0 0 18px;overflow:hidden;}
.cr-cmp .cr-ch{display:flex;align-items:center;gap:18px;padding:28px 32px 26px;color:#fffaf3;}
.cr-cmp .cr-col.l .cr-ch{background:linear-gradient(135deg,#3a3532 0%,#1f1e1d 100%);}
.cr-cmp .cr-col.r .cr-ch{background:linear-gradient(120deg,#c9714f 0%,var(--accent) 46%,var(--accent-deep) 100%);}
.cr-cmp .cr-ch svg{width:44px;height:44px;flex:none;}
.cr-cmp .cr-cht{font-weight:800;font-size:34px;letter-spacing:4px;line-height:1.15;text-transform:uppercase;}
.cr-cmp .cr-cell{position:relative;padding:22px 32px 6px 32px;font-size:46px;line-height:1.14;color:var(--ink);}
.cr-cmp .cr-cell + .cr-cell{border-top:2px dashed var(--rule);margin-top:12px;padding-top:24px;}
.cr-cmp .cr-vd{margin-top:30px;display:flex;align-items:center;gap:22px;padding:26px 36px;border-radius:26px;background:var(--wash);box-shadow:inset 0 0 0 1.5px rgba(179,87,63,.16);font-size:50px;line-height:1.12;color:var(--ink);}
.cr-cmp .cr-vd svg{width:46px;height:46px;flex:none;color:var(--accent-deep);}
.cr-flw{left:var(--cl);width:var(--cw);}
.cr-flw .cr-steps{position:relative;margin-top:44px;}
.cr-flw .cr-st{position:absolute;left:0;top:0;box-sizing:border-box;padding:30px 28px 32px;display:flex;flex-direction:column;align-items:flex-start;}
.cr-flw.v .cr-st{flex-direction:row;align-items:center;gap:26px;padding:22px 32px;}
.cr-flw .cr-st .tile{width:76px;height:76px;border-radius:22px;}
.cr-flw .cr-st .tile svg{width:40px;height:40px;}
.cr-flw .cr-sl{font-size:50px;line-height:1.08;color:var(--ink);margin-top:20px;text-wrap:balance;}
.cr-flw.v .cr-sl{margin-top:0;}
.cr-flw .cr-ss{font-size:32px;line-height:1.2;color:var(--muted);margin-top:10px;text-wrap:balance;}
.cr-flw.v .cr-ss{margin-top:4px;}
.cr-flw .cr-stx{min-width:0;flex:1;}
.cr-flw .cr-st.ok{background:linear-gradient(120deg,#c9714f 0%,var(--accent) 46%,var(--accent-deep) 100%);border-color:transparent;box-shadow:0 26px 60px rgba(179,87,63,.32),0 4px 10px rgba(120,50,30,.12);}
.cr-flw .cr-st.ok .cr-sl,.cr-flw .cr-st.ok .cr-ss{color:#fffaf3;}
.cr-flw .cr-st.ok .tile{background:rgba(255,250,243,.17);color:#fffaf3;box-shadow:inset 0 0 0 1.5px rgba(255,250,243,.32);}
.cr-flw .cr-st.stop{border-color:rgba(192,57,43,.45);box-shadow:0 18px 40px rgba(192,57,43,.12);}
.cr-flw .cr-st.stop .cr-sl{color:var(--red);}
.cr-flw .cr-st.stop .tile{background:rgba(192,57,43,.1);color:var(--red);box-shadow:inset 0 0 0 1.5px rgba(192,57,43,.25);}
.cr-flw .cr-st.muted{background:#f2ede5;box-shadow:none;}
.cr-flw .cr-st.muted .cr-sl{color:#a59f97;}
.cr-flw .cr-x{position:absolute;right:-16px;top:-16px;width:52px;height:52px;border-radius:50%;background:var(--red);color:#fff;display:flex;align-items:center;justify-content:center;box-shadow:0 8px 18px rgba(192,57,43,.3);}
.cr-flw .cr-x svg{width:30px;height:30px;stroke-width:3.2;}
.cr-flw svg.cr-ar{position:absolute;left:0;top:0;overflow:visible;fill:none;stroke:var(--accent);stroke-width:6;stroke-linecap:round;stroke-linejoin:round;}
.cr-cnt{left:var(--cl);width:var(--cw);}
.cr-cnt .cr-its{display:flex;gap:30px;margin-top:44px;justify-content:center;}
.cr-cnt .cr-it{position:relative;flex:1 1 0;min-width:0;max-width:560px;padding:34px 26px 34px;display:flex;flex-direction:column;align-items:center;text-align:center;box-sizing:border-box;}
.cr-cnt .cr-il{font-weight:800;font-size:28px;letter-spacing:4px;color:var(--accent-deep);text-transform:uppercase;line-height:1.2;text-wrap:balance;}
.cr-cnt .cr-ring{position:relative;width:250px;height:250px;margin-top:22px;}
.cr-cnt .cr-ring svg{position:absolute;left:0;top:0;width:250px;height:250px;transform:rotate(-90deg);}
.cr-cnt .cr-ring .bg{fill:none;stroke:var(--rule);stroke-width:14;}
.cr-cnt .cr-ring .fg{fill:none;stroke:url(#crg);stroke-width:14;stroke-linecap:round;}
.cr-cnt .cr-it.red .cr-ring .fg{stroke:var(--red);}
.cr-cnt .cr-iv{position:absolute;left:0;top:0;width:250px;height:250px;display:flex;flex-direction:column;align-items:center;justify-content:center;}
.cr-cnt .cr-ivn{font-family:var(--sans);font-weight:700;font-size:104px;line-height:.9;letter-spacing:-2px;color:var(--ink);font-variant-numeric:tabular-nums;}
.cr-cnt .cr-it.red .cr-ivn{color:var(--red);}
.cr-cnt .cr-ivu{font-weight:800;font-size:24px;letter-spacing:5px;color:var(--muted);margin-top:10px;text-transform:uppercase;}
.cr-cnt .cr-is{font-size:36px;line-height:1.16;color:var(--muted);margin-top:22px;text-wrap:balance;}
`;
const styleEl = document.createElement('style'); styleEl.setAttribute('data-cues', 'course'); styleEl.textContent = CSS; document.head.appendChild(styleEl);
document.body.insertAdjacentHTML('beforeend', '<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs><linearGradient id="crg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e29776"/><stop offset=".55" stop-color="#cc785c"/><stop offset="1" stop-color="#a24c35"/></linearGradient></defs></svg>');

/* ---------------- shared helpers ---------------- */
const tf = (el, rest, s) => { el.style.transform = rest ? '' : s; };   // a landed element drops its transform (chunked renders match)
const typo = (s) => String(s ?? '').replace(/'/g, '’');
const rsHTML = (s) => esc(typo(s)).replace(/₹/g, '<span style="font-family:var(--sans);font-weight:600;font-size:.82em">₹</span>');
function headHTML(c) { return c.head ? `<div class="cr-hdw"><div class="cr-h serif">${rsHTML(c.head)}</div><div class="cr-hu"></div></div>` : ''; }
function headLayout(q) { if (q.h) fitFont(q.h, () => q.h.scrollWidth <= CW + 1 && q.h.offsetHeight < 2.3 * parseFloat(getComputedStyle(q.h).fontSize), 56, 2); }
function headSeek(q, c, t) { if (!q.h) return; const ha = c.head_at ?? c.t0; rise(q.h, P(t, ha, 0.6), 38); q.hu.style.transform = `scaleX(${f4(outExpo(P(t, ha + 0.3, 0.6)))})`; }
function noteHTML(n) { return n && n.text ? `<div class="cr-note" style="opacity:0"><div class="tile">${ico(n.icon || 'info')}</div><div>${rsHTML(n.text)}</div></div>` : ''; }
function noteSeek(el, n, t) { if (!el) return; const p = P(t, n.at, 0.55); el.style.opacity = f4(clamp(p * 2.5)); tf(el, p >= 1, `translateY(${f2((1 - outExpo(p)) * 22)}px)`); }
function place(x, extra = 0) { const A = areaFor(x.c); x.el.style.top = (x.c.y ?? centerTop(A, x.el.offsetHeight + extra, -12)) + 'px'; }
const fsOf = (el) => parseFloat(getComputedStyle(el).fontSize);

/* ======================= section: a statute card ======================= */
BUILD.section = (c) => {
  const pts = c.points || [];
  const num = String(c.num ?? '').trim();
  const el = mk(pcontent, 'cue cr-sec', `<div class="cr-card card"><div class="cr-top">${c.act ? `<div class="cr-act">${esc(c.act)}</div>` : ''}<div class="cr-num serif">${num ? `<i>${/^(Art|Order|O\.|Sch|Rule|Article)/i.test(num) ? '' : '§'}</i>` : ''}${esc(num)}</div></div>` +
    (c.title ? `<div class="cr-ttl serif">${rsHTML(c.title)}</div>` : '') +
    (pts.length ? `<div class="cr-pts">${pts.map(p => `<div class="cr-pt" style="opacity:0"><div class="cr-pk${p.tone === 'no' ? ' no' : ''}">${ico(p.tone === 'no' ? 'x' : 'check')}</div><div class="cr-ptx serif">${rsHTML(p.text)}</div></div>`).join('')}</div>` : '') +
    noteHTML(c.note) + '</div>');
  return { el, q: { card: $(el, '.cr-card'), act: $(el, '.cr-act'), num: $(el, '.cr-num'), ttl: $(el, '.cr-ttl'), pts: $$(el, '.cr-pt'), ptx: $$(el, '.cr-ptx'), note: $(el, '.cr-note') } };
};
LAYOUT.section = (x) => {
  const q = x.q, A = areaFor(x.c), room = A.bottom - A.top;
  fitFont(q.num, () => q.num.scrollWidth <= CW - 108 - (q.act ? q.act.offsetWidth + 26 : 0), 64, 2);
  if (q.ttl) fitLines(q.ttl, 52, 2, 44);
  if (q.ptx.length) { q.ptx.forEach(tx => fitLines(tx, 42, 2, 38)); const m = Math.min(...q.ptx.map(fsOf)); q.ptx.forEach(tx => { tx.style.fontSize = m + 'px'; }); }
  for (let s = 0; x.el.offsetHeight > room && s < 8; s++) {   // too tall for the free band: shrink everything a step
    for (const e of [q.num, q.ttl, ...q.ptx]) if (e) e.style.fontSize = (fsOf(e) * 0.93) + 'px'; }
  place(x);
};
SEEK.section = (x, t) => {
  const c = x.c, q = x.q, at = c.at ?? c.t0, p = P(t, at, 0.6);
  q.card.style.opacity = f4(clamp(p * 2.5)); tf(q.card, p >= 1, `translateY(${f2((1 - outExpo(p)) * 60)}px) scale(${f4(0.93 + 0.07 * outBack(p))})`);
  if (q.act) { const pa = P(t, at + 0.12, 0.5); q.act.style.opacity = f4(clamp(pa * 3)); tf(q.act, pa >= 1, `scale(${f4(spring(pa))}) rotate(${f2((1 - outCubic(pa)) * -12)}deg)`); }
  wipeIn(q.num, outCubic(P(t, at + 0.18, 0.55)));
  if (q.ttl) rise(q.ttl, P(t, at + 0.4, 0.55), 24);
  (c.points || []).forEach((pt, k) => { const pp = P(t, pt.at ?? at + 1 + k * 0.8, 0.5), el = q.pts[k];
    el.style.opacity = f4(clamp(pp * 2.5)); tf(el, pp >= 1, `translateX(${f2(away((1 - outExpo(pp)) * 60))}px)`);
    const pk = el.firstElementChild; tf(pk, pp >= 1, `scale(${f4(spring(pp))}) rotate(${f2((1 - outCubic(pp)) * -90)}deg)`); });
  noteSeek(q.note, c.note, t);
  cueRoot(x, t, { from: at });
};

/* ======================= compare: two columns side by side ======================= */
BUILD.compare = (c) => {
  const cols = (c.cols || []).slice(0, 2), rows = c.rows || [];
  const colHTML = (col, j) => `<div class="cr-col card ${j ? 'r' : 'l'}" style="opacity:0"><div class="cr-ch">${col.icon ? ico(col.icon) : ''}<div class="cr-cht">${esc(typo(col.title))}</div></div>` +
    rows.map(r => `<div class="cr-cell serif" style="opacity:0">${rsHTML((r.cells || [])[j] ?? '')}</div>`).join('') + '</div>';
  const el = mk(pcontent, 'cue cr-cmp', headHTML(c) + `<div class="cr-cols">${cols.map(colHTML).join('')}</div>` +
    (c.verdict ? `<div class="cr-vd" style="opacity:0">${ico(c.verdict.icon || 'scale')}<div>${rsHTML(c.verdict.text)}</div></div>` : ''));
  const colEls = $$(el, '.cr-col');
  return { el, q: { h: $(el, '.cr-h'), hu: $(el, '.cr-hu'), cols: colEls, cells: colEls.map(ce => $$(ce, '.cr-cell')), vd: $(el, '.cr-vd') } };
};
LAYOUT.compare = (x) => {
  const q = x.q, A = areaFor(x.c), room = A.bottom - A.top; headLayout(q);
  const all = q.cells.flat(); all.forEach(e => fitLines(e, 40, 3, 34));
  if (all.length) { const m = Math.min(...all.map(fsOf)); all.forEach(e => { e.style.fontSize = m + 'px'; }); }
  // the two cells of a row share one height, so row k lines up across the columns
  const n = (x.c.rows || []).length;
  for (let k = 0; k < n; k++) { const cs = q.cells.map(cc => cc[k]).filter(Boolean); cs.forEach(e => { e.style.minHeight = ''; });
    const h = Math.max(...cs.map(e => e.offsetHeight)); cs.forEach(e => { e.style.minHeight = (h - 28) + 'px'; }); }
  for (let s = 0; x.el.offsetHeight > room && s < 8; s++) all.forEach(e => { e.style.fontSize = (fsOf(e) * 0.93) + 'px'; });
  if (q.vd) fitLines(q.vd.lastElementChild, 44, 2, 36);
  place(x);
};
SEEK.compare = (x, t) => {
  const c = x.c, q = x.q, cols = c.cols || [], rows = c.rows || [];
  headSeek(q, c, t);
  q.cols.forEach((ce, j) => { const a = cols[j].at ?? (c.head_at ?? c.t0) + 0.3 + 0.2 * j, p = P(t, a, 0.6);
    ce.style.opacity = f4(clamp(p * 2.5)); tf(ce, p >= 1, `translateY(${f2((1 - outExpo(p)) * 70)}px) scale(${f4(0.94 + 0.06 * outBack(p))})`); });
  rows.forEach((r, k) => q.cells.forEach((cc, j) => { const e = cc[k]; if (!e) return; const p = P(t, r.cells_at ? r.cells_at[j] : (r.at ?? c.t0 + 1 + k) + 0.15 * j, 0.5);
    e.style.opacity = f4(clamp(p * 2.2)); tf(e, p >= 1, `translateY(${f2((1 - outExpo(p)) * 26)}px)`); }));
  if (q.vd) { const p = P(t, c.verdict.at, 0.6); q.vd.style.opacity = f4(clamp(p * 2.5)); tf(q.vd, p >= 1, `translateY(${f2((1 - outExpo(p)) * 40)}px) scale(${f4(0.92 + 0.08 * outBack(p))})`); }
  cueRoot(x, t, { from: c.head_at ?? c.t0 });
};

/* ======================= flow: steps joined by arrows ======================= */
BUILD.flow = (c) => {
  const steps = c.steps || [], v = (c.dir ?? (steps.length > 4 ? 'v' : 'h')) === 'v';
  const el = mk(pcontent, 'cue cr-flw' + (v ? ' v' : ''), headHTML(c) + `<div class="cr-steps">` +
    steps.map(s => `<div class="cr-st card ${s.tone || ''}" style="opacity:0"><div class="tile">${ico(s.icon || 'arrow-right')}</div><div class="cr-stx"><div class="cr-sl serif">${rsHTML(s.label)}</div>${s.sub ? `<div class="cr-ss">${rsHTML(s.sub)}</div>` : ''}</div>${s.tone === 'stop' ? `<div class="cr-x" style="opacity:0">${ico('x')}</div>` : ''}</div>`).join('') +
    steps.slice(1).map(() => `<svg class="cr-ar"><path pathLength="1" stroke-dasharray="1 1"/></svg>`).join('') + `</div>` + noteHTML(c.note));
  return { el, v, q: { h: $(el, '.cr-h'), hu: $(el, '.cr-hu'), box: $(el, '.cr-steps'), st: $$(el, '.cr-st'), sl: $$(el, '.cr-sl'), ss: $$(el, '.cr-ss'), xs: $$(el, '.cr-st').map(s => $(s, '.cr-x')), ar: $$(el, '.cr-ar'), note: $(el, '.cr-note') } };
};
LAYOUT.flow = (x) => {
  const q = x.q, n = q.st.length, A = areaFor(x.c), room = A.bottom - A.top; headLayout(q); if (!n) return;
  const AG = x.v ? 46 : 64;   // room for an arrow between two cards
  if (!x.v) {
    const w = Math.floor((CW - AG * (n - 1)) / n);
    q.st.forEach(s => { s.style.width = w + 'px'; });
    q.sl.forEach(e => fitLines(e, 40, 3, 34)); const m = Math.min(...q.sl.map(fsOf)); q.sl.forEach(e => { e.style.fontSize = m + 'px'; });
    q.ss.forEach(e => fitLines(e, 28, 3, 24));
    const h = Math.max(...q.st.map(s => s.offsetHeight)); q.st.forEach((s, k) => { s.style.height = h + 'px'; s.style.left = (k * (w + AG)) + 'px'; s.style.top = '0px'; });
    q.box.style.height = h + 'px';
    q.ar.forEach((a, k) => { const x0 = (k + 1) * w + k * AG + 10, x1 = x0 + AG - 20, y = h / 2;
      Object.assign(a.style, { width: AG + 'px', height: '40px' }); a.setAttribute('viewBox', `${x0 - 4} ${y - 20} ${AG} 40`);
      a.style.left = (x0 - 4) + 'px'; a.style.top = (y - 20) + 'px'; a.firstElementChild.setAttribute('d', `M${x0} ${y} L${x1} ${y} M${x1 - 12} ${y - 12} L${x1} ${y} L${x1 - 12} ${y + 12}`); });
  } else {
    q.st.forEach(s => { s.style.width = CW + 'px'; });
    q.sl.forEach(e => fitLines(e, 44, 2, 36)); const m = Math.min(...q.sl.map(fsOf)); q.sl.forEach(e => { e.style.fontSize = m + 'px'; });
    let y = 0; const hs = q.st.map(s => s.offsetHeight);
    const fitH = () => hs.reduce((a, b) => a + b, 0) + AG * (n - 1) + (q.h ? q.h.parentNode.offsetHeight + 44 : 0) + (q.note ? q.note.offsetHeight + 22 : 0);
    for (let s = 0; fitH() > room && s < 8; s++) { q.sl.forEach(e => { e.style.fontSize = (fsOf(e) * 0.93) + 'px'; }); q.st.forEach((st, k) => { hs[k] = st.offsetHeight; }); }
    q.st.forEach((s, k) => { s.style.left = '0px'; s.style.top = y + 'px'; y += hs[k] + AG; });
    q.box.style.height = (y - AG) + 'px';
    q.ar.forEach((a, k) => { const y0 = parseFloat(q.st[k].style.top) + hs[k] + 6, y1 = y0 + AG - 12, xx = 70;
      Object.assign(a.style, { width: '40px', height: AG + 'px', left: (xx - 20) + 'px', top: y0 + 'px' }); a.setAttribute('viewBox', `${xx - 20} ${y0} 40 ${AG}`);
      a.firstElementChild.setAttribute('d', `M${xx} ${y0} L${xx} ${y1} M${xx - 12} ${y1 - 12} L${xx} ${y1} L${xx + 12} ${y1 - 12}`); });
  }
  place(x);
};
SEEK.flow = (x, t) => {
  const c = x.c, q = x.q, steps = c.steps || [];
  headSeek(q, c, t);
  const ats = steps.map((s, k) => s.at ?? (c.head_at ?? c.t0) + 0.5 + 1.2 * k);
  q.st.forEach((s, k) => { const p = P(t, ats[k], 0.55);
    s.style.opacity = f4(clamp(p * 2.5));
    tf(s, p >= 1, x.v ? `translateX(${f2(away((1 - outExpo(p)) * 70))}px)` : `translateY(${f2((1 - outExpo(p)) * 60)}px) scale(${f4(0.9 + 0.1 * outBack(p))})`);
    const ti = s.firstElementChild, pi = P(t, ats[k] + 0.08, 0.55); tf(ti, pi >= 1, `scale(${f4(spring(pi))}) rotate(${f2((1 - outCubic(pi)) * -30)}deg)`);
    const xe = q.xs[k]; if (xe) { const px = P(t, ats[k] + 0.45, 0.45); xe.style.opacity = f4(clamp(px * 3)); tf(xe, px >= 1, `scale(${f4(spring(px))}) rotate(${f2((1 - outCubic(px)) * -90)}deg)`); } });
  q.ar.forEach((a, k) => { const p = P(t, ats[k + 1] - 0.3, 0.32); a.style.opacity = p > 0 ? '1' : '0'; a.firstElementChild.style.strokeDashoffset = f4(1 - outCubic(p)); });
  noteSeek(q.note, c.note, t);
  cueRoot(x, t, { from: c.head_at ?? ats[0] ?? c.t0 });
};

/* ======================= counters: day / hour counts with filling rings ======================= */
const RING_C = 2 * Math.PI * 110;
BUILD.counters = (c) => {
  const items = (c.items || []).slice(0, 3);
  const el = mk(pcontent, 'cue cr-cnt', headHTML(c) + `<div class="cr-its">` + items.map(it => `<div class="cr-it card${it.tone === 'red' ? ' red' : ''}" style="opacity:0"><div class="cr-il">${esc(typo(it.label))}</div>` +
    `<div class="cr-ring"><svg viewBox="0 0 250 250"><circle class="bg" cx="125" cy="125" r="110"/><circle class="fg" cx="125" cy="125" r="110" stroke-dasharray="${f2(RING_C)} ${f2(RING_C)}" stroke-dashoffset="${f2(RING_C)}"/></svg>` +
    `<div class="cr-iv"><div class="cr-ivn serif">0</div><div class="cr-ivu">${esc(it.unit ?? '')}</div></div></div>${it.sub ? `<div class="cr-is serif">${rsHTML(it.sub)}</div>` : ''}</div>`).join('') + `</div>` + noteHTML(c.note));
  const its = $$(el, '.cr-it');
  return { el, q: { h: $(el, '.cr-h'), hu: $(el, '.cr-hu'), its, fg: its.map(i => $(i, '.fg')), n: its.map(i => $(i, '.cr-ivn')), il: its.map(i => $(i, '.cr-il')), is: its.map(i => $(i, '.cr-is')), note: $(el, '.cr-note') } };
};
LAYOUT.counters = (x) => {
  const q = x.q; headLayout(q);
  q.il.forEach(e => fitLines(e, 24, 2, 20)); q.is.forEach(e => e && fitLines(e, 30, 3, 26));
  const h = Math.max(0, ...q.its.map(i => i.offsetHeight)); q.its.forEach(i => { i.style.height = h + 'px'; });
  place(x);
};
SEEK.counters = (x, t) => {
  const c = x.c, q = x.q, items = (c.items || []).slice(0, 3);
  headSeek(q, c, t);
  items.forEach((it, k) => { const at = it.at ?? (c.head_at ?? c.t0) + 0.5 + 1.0 * k, p = P(t, at, 0.55), e = q.its[k];
    e.style.opacity = f4(clamp(p * 2.5)); tf(e, p >= 1, `translateY(${f2((1 - outExpo(p)) * 60)}px) scale(${f4(0.9 + 0.1 * outBack(p))})`);
    const pc = outCubic(P(t, at + 0.15, 1.0)), v = Number(it.value) || 0;
    q.n[k].textContent = String(Math.round(v * pc));
    q.fg[k].setAttribute('stroke-dashoffset', f2(RING_C * (1 - pc)));
    if (q.is[k]) rise(q.is[k], P(t, at + 0.9, 0.5), 18); });
  noteSeek(q.note, c.note, t);
  cueRoot(x, t, { from: c.head_at ?? c.t0 });
};
/* ---------------- digits: every cue's serif text gets its digit runs in Manrope (all cue types, the page's own included) ---------------- */
function digitsIn(root) {
  if (!root) return;
  const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT), nodes = [];
  for (let n = walker.nextNode(); n; n = walker.nextNode()) {
    if (!/\d/.test(n.nodeValue)) continue;
    const host = n.parentElement; if (!host || host.closest('.cr-d, .cr-ivn, svg')) continue;
    const ff = getComputedStyle(host).fontFamily || ''; if (!/Instrument Serif/i.test(ff)) continue;
    nodes.push(n);
  }
  for (const n of nodes) {
    const frag = document.createDocumentFragment(), parts = n.nodeValue.split(/(\d[\d,]*(?:\.\d+)?)/);
    parts.forEach((p, i) => { if (!p) return; if (i % 2) { const sp = document.createElement('span'); sp.className = 'cr-d'; sp.textContent = p; frag.appendChild(sp); } else frag.appendChild(document.createTextNode(p)); });
    n.parentNode.replaceChild(frag, n);
  }
}
for (const k of Object.keys(BUILD)) { const f = BUILD[k]; BUILD[k] = (c) => { const x = f(c); if (x && x.el) digitsIn(x.el); return x; }; }
})();
