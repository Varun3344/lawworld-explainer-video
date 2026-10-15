/* split_cues_coa.js (scenes 3-5: blocks, verdicts, timeline, checklist, notequal, splitcard): cue types for the full Cause of Action video, see split/COA_CUES.md. Loaded after split_panel.html's main script;
   uses its globals (BUILD, LAYOUT, SEEK, mk, $, $$, P, clamp, easing helpers, geometry constants). Deterministic: pure function of t.
   Everything lives in one IIFE: nothing but the BUILD / LAYOUT / SEEK entries reaches the shared global scope (a top-level const
   here that split_cues_coa6.js also declared would stop the second file from loading). Styles are injected once, namespaced .ca-*.
   The side-aware geometry globals (CL CW CX PW AWAY away ...) are read inside BUILD / LAYOUT / SEEK only: __init changes them.
   Fields (split/COA_CUES.md; + = optional extra, not required by the contract):
     blocks    t0 t1 open_at items[{label, sub, at}] merge{label, at}
               A scene-2 bundle cue still fully on screen at t0 (settled, tied) is taken over in place - same tiles, cord, bow and
               label, its own element hidden from our first frame - so "open the bundle" opens that very bundle; with none before it
               a small bundle of our own ties itself first. At open_at the bow unties, the cord slips off and the facts drop into two
               dashed numbered slots; item k fills slot k at its at (badge, lead words of the label in caps, last word large, sub);
               at merge.at the cards slide together and the accent block (merge.label, the key words "RIGHT + BREACH" above it)
               bursts out of them.
     verdicts  t0 t1 rows[{text, ok, at, +strike_at}]
               ok:false rows build with a "?" disc and are struck (red bar, grey, the disc flips to a red cross) at strike_at -
               default: halfway to the next row's at (0.9..2.2 s); the ok row lands in the accent with a check, the struck rows step back.
     timeline  t0 t1 nodes[{label, value, sub?, tone?, at}]
               the line draws left to right at t0; the copper fill reaches node k as it pops at its at; cards alternate above / below
               the line and hug their words; tone "red" = red value (it shakes once), red dot and label.
     checklist t0 t1 head head_at items[{n, text, at}] fold{label, at}
               the sheet of empty numbered lines shows after head_at; item k ticks in at its at; at fold.at the badges become tiles
               that fly into a 2x2 cluster, which the cord ties into a bundle labelled fold.label.
     notequal  t0 t1 left right at sub? sub_at? +left_at +icon
               left (from left_at, default at), then the ≠ (bars, then the slash), then right; sub ("A, not B": B muted and struck)
               under a dashed rule at sub_at. Kept on screen > 0.5 s together with a splitcard, it moves up into a heading above it.
     splitcard t0 t1 left{title, text, at, +icon} right{title, text, at, +icon}
               the card arrives with its left half (default icon gavel); the right half waits dashed and floods with the accent from
               the split line at right.at (default icon key-round).
   every cue also takes the optional fade_out (cueRoot) and y (top of the composition, panel px) like the page's own cues; every
   composition sits in areaFor()'s free band (below a kicker / a parked date pin, above a citation bar).
   Motion: each build lands at its `at`; entries come from the side away from the seam (away()), from below, or pop in place; the
   content stays inside the column (CL .. CL + CW) - transient rays / glow rings stay >= 96 px clear of the seam. A transform is
   cleared once its element has landed (tf()): renders then match whatever frames were rendered before (chunked renders). */
(() => {
'use strict';

const CSS = `
/* ---------- split_cues_coa.js (namespaced .ca-*) ---------- */
.ca-full{left:0;top:0;width:var(--pw);height:1080px;}
.ca-acc{background:linear-gradient(120deg,#c9714f 0%,var(--accent) 46%,var(--accent-deep) 100%);}
.ca-sheen{position:absolute;left:0;top:-30%;width:220px;height:160%;background:linear-gradient(100deg,rgba(255,255,255,0) 0%,rgba(255,255,255,.32) 50%,rgba(255,255,255,0) 100%);opacity:0;}
.ca-sbar{position:absolute;height:7px;border-radius:4px;background:var(--red);transform-origin:0 50%;transform:scaleX(0);}

/* blocks: the bundle opens into two numbered blocks that slide together into one accent block */
.ca-blk .ca-bd{position:absolute;left:0;top:0;width:var(--pw);height:1080px;}
.ca-blk .ca-slot{position:absolute;left:0;top:0;border-radius:30px;border:3px dashed rgba(179,87,63,.4);box-sizing:border-box;background:rgba(255,252,246,.35);}
.ca-blk .ca-gn{position:absolute;left:35px;top:35px;width:56px;height:56px;border-radius:50%;box-sizing:border-box;border:2.5px dashed rgba(179,87,63,.5);display:flex;align-items:center;justify-content:center;font-weight:800;font-size:26px;line-height:1;color:rgba(179,87,63,.72);}
.ca-blk .ca-bk{position:absolute;left:0;top:0;padding:35px 38px 40px;box-sizing:border-box;transform-origin:50% 50%;}
.ca-blk .ca-bh{display:flex;align-items:center;gap:18px;min-height:56px;}
.ca-blk .ca-nb{width:56px;height:56px;border-radius:50%;background:var(--copper);color:#fff;font-weight:800;font-size:26px;line-height:1;display:flex;align-items:center;justify-content:center;flex:none;box-shadow:0 10px 22px rgba(179,87,63,.3);}
.ca-blk .ca-pre{font-weight:800;font-size:24px;letter-spacing:4px;color:var(--accent-deep);text-transform:uppercase;line-height:1.2;white-space:nowrap;}
.ca-blk .ca-key{font-weight:800;font-size:80px;letter-spacing:2px;line-height:1.04;color:var(--ink);text-transform:uppercase;white-space:nowrap;margin-top:26px;}
.ca-blk .ca-sub{font-size:40px;line-height:1.16;color:var(--muted);margin-top:16px;text-wrap:balance;}
.ca-blk .ca-op{position:absolute;left:0;top:0;width:74px;height:74px;margin:-37px 0 0 -37px;border-radius:50%;background:var(--wash);color:var(--accent-deep);font-weight:800;font-size:48px;line-height:1;display:flex;align-items:center;justify-content:center;box-shadow:inset 0 0 0 1.5px rgba(179,87,63,.18);}
.ca-blk .ca-mg{position:absolute;left:0;top:0;}
.ca-blk .ca-mgb{position:relative;border-radius:34px;padding:42px 50px 46px;display:flex;flex-direction:column;align-items:center;color:#fffaf3;box-sizing:border-box;}
.ca-blk .ca-mgs{font-weight:800;font-size:25px;letter-spacing:7px;color:rgba(255,250,243,.82);text-transform:uppercase;line-height:1.2;white-space:nowrap;margin-right:-7px;}
.ca-blk .ca-mgl{font-weight:800;font-size:72px;letter-spacing:4px;line-height:1.04;text-transform:uppercase;white-space:nowrap;margin-top:14px;margin-right:-4px;}
.ca-blk .ca-glow{position:absolute;left:0;top:0;right:0;bottom:0;border-radius:34px;}
.ca-blk .ca-ray{position:absolute;left:50%;top:50%;width:44px;height:7px;margin:-3.5px 0 0 -22px;border-radius:4px;background:var(--accent);opacity:0;}

/* verdicts: wrong combinations struck through and greyed, the right one highlighted */
.ca-vd{left:var(--cl);width:var(--cw);}
.ca-vd .ca-vr{position:relative;}
.ca-vd .ca-vr + .ca-vr{margin-top:26px;}
.ca-vd .ca-vc{position:relative;display:flex;align-items:center;gap:32px;padding:28px 44px 28px 30px;overflow:hidden;}
.ca-vd .ca-vs{position:relative;width:78px;height:78px;flex:none;}
.ca-vd .ca-vs > div{position:absolute;left:0;top:0;width:78px;height:78px;border-radius:50%;display:flex;align-items:center;justify-content:center;}
.ca-vd .ca-vq{background:var(--wash);color:var(--accent-deep);box-shadow:inset 0 0 0 1.5px rgba(179,87,63,.14);font-weight:800;font-size:40px;line-height:1;}
.ca-vd .ca-vx{background:var(--red);color:#fff;box-shadow:0 10px 22px rgba(192,57,43,.26);opacity:0;}
.ca-vd .ca-vk{background:rgba(255,250,243,.2);color:#fffaf3;box-shadow:inset 0 0 0 2px rgba(255,250,243,.42);}
.ca-vd .ca-vs svg{width:42px;height:42px;stroke-width:2.8;}
.ca-vd .ca-vt{position:relative;flex:1;min-width:0;font-size:66px;line-height:1.1;color:var(--ink);}
.ca-vd .ca-vt b{font-weight:400;color:var(--accent-deep);}
.ca-vd .ok .ca-vc{background:linear-gradient(120deg,#c9714f 0%,var(--accent) 46%,var(--accent-deep) 100%);border-color:transparent;box-shadow:0 28px 64px rgba(179,87,63,.34),0 4px 10px rgba(120,50,30,.12);}
.ca-vd .ok .ca-vt,.ca-vd .ok .ca-vt b{color:#fffaf3;}
.ca-vd .ca-vglow{position:absolute;left:0;top:0;right:0;bottom:0;border-radius:30px;}

/* timeline: a line drawing left to right, nodes popping in above / below it */
.ca-tl .ca-trk{position:absolute;left:0;top:0;height:6px;border-radius:3px;background:var(--rule);transform-origin:0 50%;}
.ca-tl .ca-tf{position:absolute;left:0;top:0;height:6px;border-radius:3px;background:linear-gradient(90deg,var(--brand),var(--accent-deep));width:0;}
.ca-tl svg.ca-arw{position:absolute;left:0;top:0;width:36px;height:36px;overflow:visible;fill:none;stroke-width:6;stroke-linecap:round;stroke-linejoin:round;}
.ca-tl svg.ca-arw.a0{stroke:var(--rule);}
.ca-tl svg.ca-arw.a1{stroke:var(--accent-deep);}
.ca-tl .ca-dot{position:absolute;left:0;top:0;width:32px;height:32px;margin:-16px 0 0 -16px;border-radius:50%;background:var(--paper);box-shadow:inset 0 0 0 8px var(--accent),0 6px 14px rgba(179,87,63,.25);}
.ca-tl .ca-dot.red{box-shadow:inset 0 0 0 8px var(--red),0 6px 14px rgba(192,57,43,.28);}
.ca-tl .ca-ring{position:absolute;left:0;top:0;width:32px;height:32px;margin:-16px 0 0 -16px;border-radius:50%;border:3px solid var(--accent);box-sizing:border-box;opacity:0;}
.ca-tl .ca-ring.red{border-color:var(--red);}
.ca-tl .ca-stem{position:absolute;left:0;top:0;width:3px;margin-left:-1.5px;border-radius:2px;background:var(--accent-soft);}
.ca-tl .ca-stem.red{background:rgba(192,57,43,.45);}
.ca-tl .ca-tc{position:absolute;left:0;top:0;padding:26px 34px 30px;box-sizing:border-box;}
.ca-tl .ca-tc.red{border-color:rgba(192,57,43,.30);}
.ca-tl .ca-tlab{font-weight:800;font-size:24px;letter-spacing:5px;color:var(--accent-deep);text-transform:uppercase;line-height:1.2;white-space:nowrap;}
.ca-tl .ca-tc.red .ca-tlab{color:var(--red);}
.ca-tl .ca-tval{font-size:96px;line-height:1.02;color:var(--ink);white-space:nowrap;margin-top:8px;}
.ca-tl .ca-tc.red .ca-tval{color:var(--red);}
.ca-tl .ca-tval .rs{font-family:var(--sans);font-weight:600;font-size:.8em;margin-right:.04em;}   /* the rupee in Manrope (its latin-ext face is loaded for it) */
.ca-tl .ca-tsub{font-size:40px;line-height:1.15;color:var(--muted);margin-top:6px;white-space:nowrap;}
.ca-tl .ca-tsub b{font-weight:400;color:var(--accent-deep);}

/* checklist: a sheet of numbered lines that tick in one by one, then fold into a tied bundle */
.ca-ck .ca-ckl{position:absolute;left:var(--cl);top:0;width:var(--cw);}
.ca-ck .ca-ckh{font-size:92px;line-height:1.02;color:var(--ink);white-space:nowrap;}
.ca-ck .ca-cku{width:116px;height:6px;border-radius:3px;background:var(--copper);margin-top:26px;transform-origin:0 50%;}
.ca-ck .ca-ckc{position:relative;margin-top:44px;padding:8px 36px;}
.ca-ck .ca-ckbg{position:absolute;left:0;top:0;right:0;bottom:0;}
.ca-ck .ca-cki{position:relative;height:112px;display:flex;align-items:center;gap:30px;}
.ca-ck .ca-ckdv{position:absolute;left:0;right:0;top:-1px;height:0;border-top:2px dashed var(--rule);}
.ca-ck .ca-ckg{position:absolute;left:0;top:50%;width:64px;height:64px;margin-top:-32px;border-radius:50%;box-sizing:border-box;border:2.5px dashed rgba(179,87,63,.4);display:flex;align-items:center;justify-content:center;font-weight:800;font-size:28px;line-height:1;color:rgba(179,87,63,.55);}
.ca-ck .ca-ckn{position:relative;width:64px;height:64px;border-radius:50%;background:var(--copper);color:#fff;font-weight:800;font-size:30px;line-height:1;display:flex;align-items:center;justify-content:center;flex:none;box-shadow:0 10px 22px rgba(179,87,63,.28);}
.ca-ck .ca-ckt{flex:1;min-width:0;font-size:62px;line-height:1.1;color:var(--ink);white-space:nowrap;transform-origin:0 50%;}
.ca-ck .ca-ckb{position:relative;width:62px;height:62px;border-radius:18px;flex:none;box-shadow:inset 0 0 0 3px rgba(179,87,63,.32);}
.ca-ck .ca-ckb .fill{position:absolute;left:0;top:0;width:62px;height:62px;border-radius:18px;background:var(--copper);box-shadow:0 8px 18px rgba(179,87,63,.3);}
.ca-ck .ca-ckb svg{position:absolute;left:11px;top:11px;width:40px;height:40px;fill:none;stroke:#fff;stroke-width:3.4;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:1 1;}
.ca-ck .ca-ckf{position:absolute;left:0;top:0;width:var(--pw);height:1080px;}
.ca-ck .ca-ckf .fct{overflow:visible;}
.ca-ck .ca-ckd{font-weight:800;font-size:56px;line-height:1;}
.ca-ck .ca-cks{position:absolute;right:-14px;top:-14px;width:44px;height:44px;border-radius:50%;background:var(--copper);color:#fff;display:flex;align-items:center;justify-content:center;box-shadow:0 6px 14px rgba(179,87,63,.3);}
.ca-ck .ca-ckf .ca-cks svg{width:26px;height:26px;stroke-width:3.2;}

/* notequal: "left ≠ right", the ≠ drawn in the accent, an optional note under a dashed rule */
.ca-ne{left:var(--cl);width:var(--cw);}
.ca-ne .ca-nl,.ca-ne .ca-nr{font-size:128px;line-height:1.06;color:var(--ink);white-space:nowrap;}
.ca-ne .ca-nr{display:flex;align-items:center;gap:.2em;}
.ca-ne .ca-neq{position:relative;width:.74em;height:.74em;flex:none;transform-origin:50% 50%;}
.ca-ne .ca-neq svg{position:absolute;left:0;top:0;width:100%;height:100%;overflow:visible;}
.ca-ne .ca-neq .b{fill:var(--accent);transform-box:fill-box;transform-origin:0 50%;}
.ca-ne .ca-neq .sl{fill:none;stroke:var(--accent-deep);stroke-width:10;stroke-linecap:round;stroke-dasharray:1 1;}
.ca-ne .ca-ns{position:relative;display:flex;align-items:center;gap:26px;margin-top:54px;padding-top:36px;}
.ca-ne .ca-nsr{position:absolute;left:0;top:0;width:100%;height:0;border-top:2px dashed var(--rule);transform-origin:0 50%;}
.ca-ne .ca-ns .tile{width:78px;height:78px;border-radius:22px;}
.ca-ne .ca-ns .tile svg{width:40px;height:40px;}
.ca-ne .ca-nst{position:relative;flex:1;min-width:0;font-size:58px;line-height:1.12;color:var(--ink);text-wrap:balance;}
.ca-ne .ca-nsn{color:var(--muted);}
.ca-ne .ca-sbar{height:5px;background:rgba(165,159,151,.95);}

/* splitcard: one card, two halves; the right half floods with the accent */
.ca-sp{left:var(--cl);width:var(--cw);}
.ca-sp .ca-spc{position:relative;display:flex;}
.ca-sp .ca-sph{position:relative;flex:1 1 0;min-width:0;box-sizing:border-box;}
.ca-sp .ca-spl{padding:44px 44px 50px 46px;background:var(--paper);border:1.5px solid var(--rule);border-right:none;border-radius:30px 0 0 30px;box-shadow:0 24px 58px rgba(60,40,25,.12),0 3px 8px rgba(60,40,25,.06);}
.ca-sp .ca-spr{border-radius:0 30px 30px 0;}
.ca-sp .ca-spph{position:absolute;left:0;top:0;right:0;bottom:0;border:3px dashed rgba(179,87,63,.28);border-left:none;border-radius:0 30px 30px 0;box-sizing:border-box;}
.ca-sp .ca-spbg{position:absolute;left:0;top:0;right:0;bottom:0;border-radius:0 30px 30px 0;overflow:hidden;box-shadow:0 28px 64px rgba(179,87,63,.32),0 4px 10px rgba(120,50,30,.12);}
.ca-sp .ca-spin{position:relative;padding:44px 46px 50px 48px;}
.ca-sp .tile{width:84px;height:84px;border-radius:24px;}
.ca-sp .tile svg{width:42px;height:42px;}
.ca-sp .ca-spt{font-weight:800;font-size:28px;letter-spacing:5px;color:var(--accent-deep);text-transform:uppercase;line-height:1.2;white-space:nowrap;margin-top:30px;}
.ca-sp .ca-spx{font-size:64px;line-height:1.1;color:var(--ink);margin-top:14px;text-wrap:balance;}
.ca-sp .ca-spr .ca-spt{color:rgba(255,250,243,.84);}
.ca-sp .ca-spr .ca-spx{color:#fffaf3;}
.ca-sp .ca-spr .tile{background:rgba(255,250,243,.17);color:#fffaf3;box-shadow:inset 0 0 0 1.5px rgba(255,250,243,.32);}
`;
const styleEl = document.createElement('style'); styleEl.setAttribute('data-cues', 'coa'); styleEl.textContent = CSS; document.head.appendChild(styleEl);

/* ---------------- shared helpers ---------------- */
// the scene-2 bundle's cord and bow (same paths / classes as LAYOUT.bundle, so the same look inside a .bdl container)
const BOWD = { l1: 'M0 0 C -26 -40 -86 -40 -82 -2 C -78 30 -30 22 0 0 Z', l2: 'M0 0 C 26 -40 86 -40 82 -2 C 78 30 30 22 0 0 Z',
  t1: 'M0 0 C -10 24 -22 44 -40 64', t2: 'M0 0 C 10 24 24 44 36 66' };
const cordHTML = () => `<svg class="cord"><path class="rope"/><path class="rope2"/><g class="bow" style="opacity:0"><path class="lp l1" d="${BOWD.l1}"/><path class="lp l2" d="${BOWD.l2}"/><path class="tl t1" d="${BOWD.t1}"/><path class="tl t2" d="${BOWD.t2}"/><circle r="10"/></g></svg>`;
const cordQ = (el) => ({ rope: $(el, '.rope'), rope2: $(el, '.rope2'), bow: $(el, '.bow'), l1: $(el, '.l1'), l2: $(el, '.l2'), t1: $(el, '.t1'), t2: $(el, '.t2') });
function cordPath(q, cx, cy, R) {   // closed loop from the knot (bottom) round and back, drawing from the seam side first like the scene-2 cord
  const sw = AWAY > 0 ? 1 : 0, d = `M ${f2(cx)} ${f2(cy + R)} A ${f2(R)} ${f2(R)} 0 1 ${sw} ${f2(cx)} ${f2(cy - R)} A ${f2(R)} ${f2(R)} 0 1 ${sw} ${f2(cx)} ${f2(cy + R)}`;
  for (const p of [q.rope, q.rope2]) { p.setAttribute('d', d); p.setAttribute('pathLength', '1'); }
}
// the cord shows from s = a to s = min(draw, 1 - a) of its length (s = 0 at the knot): draw ties it round, a (0 .. 0.5) slips it open at the knot
function cordPose(q, draw, a) {
  // a cord slipping off fades over its last stretch (no stray arc); one being tied fades in over its first (no lone dot at the knot)
  const L = Math.min(draw, 1 - a) - a, o = f4(clamp((0.5 - a) / 0.3) ** 2 * clamp(draw / 0.06));
  for (const p of [q.rope, q.rope2]) {
    if (L <= 0.001) { p.style.opacity = '0'; continue; }
    p.style.opacity = o; p.style.strokeDasharray = `${f4(L)} 2`; p.style.strokeDashoffset = f4(-a);
  }
}
// typographic apostrophes for display ("Ravi's" -> "Ravi’s", "PLAINTIFF'S" -> "PLAINTIFF’S")
const typo = (s) => String(s ?? '').replace(/(\w)'(\w)/g, '$1’$2');
// bow at the knot; untie (0..1) swings the loops apart and drops the tails (SVG transforms about the knot, the group's origin)
function bowPose(q, x, y, rot, sc, op, untie) {
  q.bow.style.opacity = f4(op);
  q.bow.style.transform = `translate(${f2(x)}px,${f2(y)}px) rotate(${f2(rot)}deg) scale(${f4(sc)})`;
  const u = untie;
  q.l1.style.transform = u > 0 ? `rotate(${f2(-34 * u)}deg) translate(${f2(-18 * u)}px,${f2(12 * u)}px)` : '';
  q.l2.style.transform = u > 0 ? `rotate(${f2(34 * u)}deg) translate(${f2(18 * u)}px,${f2(12 * u)}px)` : '';
  q.t1.style.transform = u > 0 ? `translate(${f2(-12 * u)}px,${f2(34 * u)}px) rotate(${f2(18 * u)}deg)` : '';
  q.t2.style.transform = u > 0 ? `translate(${f2(12 * u)}px,${f2(34 * u)}px) rotate(${f2(-18 * u)}deg)` : '';
}
// LAYOUT.bundle's tight cluster: centre + ring of 6 (+ outer ring), mirrored with AWAY
function homeRing(n, cx, cy) {
  return Array.from({ length: n }, (_, k) => { if (k === 0) return [cx, cy];
    const ring = k <= 6 ? 1 : 2, idx = ring === 1 ? k - 1 : k - 7, cnt = ring === 1 ? Math.min(6, n - 1) : n - 7;
    const a = -Math.PI / 2 + (idx / cnt) * TAU + (ring === 2 ? Math.PI / cnt : 0), r = BDL_RING[ring - 1];
    return [cx + AWAY * Math.cos(a) * r, cy + Math.sin(a) * r]; });
}
const bundleGat = (c) => { const one = c.one_at ?? c.t0 + 0.5, many = c.many_at ?? one + 1.2; return c.gather_at ?? many + 1.3; };   // = SEEK.bundle
const breatheAt = (gat, t) => t > gat + 0.9 ? 1 + 0.008 * Math.sin(TAU * (t - gat) / 2.2) : 1;                                          // = SEEK.bundle
// strike bars over the rendered lines of `src` (an element or a span inside host), positioned in host (position: relative)
function strikeBars(src, host, cls = 'ca-sbar') {
  const r = document.createRange(); r.selectNodeContents(src); const box = host.getBoundingClientRect(); const lines = [];
  for (const rc of r.getClientRects()) { if (rc.width < 2) continue; const L = lines.find(l => Math.abs(l.top - rc.top) < 6);
    if (L) { L.left = Math.min(L.left, rc.left); L.right = Math.max(L.right, rc.right); L.bottom = Math.max(L.bottom, rc.bottom); }
    else lines.push({ top: rc.top, bottom: rc.bottom, left: rc.left, right: rc.right }); }
  return lines.map(L => { const b = mk(host, cls); b.style.left = f2(L.left - box.left - 7) + 'px'; b.style.width = f2(L.right - L.left + 14) + 'px';
    b.style.top = f2((L.top + L.bottom) / 2 - box.top + 7) + 'px'; return b; });
}
// position of el's box relative to an ancestor (offset chain; every element on the way is positioned)
function offIn(el, anc) { let X = 0, Y = 0, e = el; while (e && e !== anc) { X += e.offsetLeft; Y += e.offsetTop; e = e.offsetParent; } return [X, Y]; }
const fsOf = (el) => parseFloat(getComputedStyle(el).fontSize);
// set a transform, or none once the element has landed: an element that keeps an identity rotate()/scale() after animating is
// rasterised differently depending on which frames were rendered before (frames rendered out of order differed by up to 85 levels)
const tf = (el, rest, s) => { el.style.transform = rest ? '' : s; };
// word-mask reveal (the house title move), p = 0..1
function maskIn(w, p, rot = 6) {
  if (p >= 1) { w.style.transform = ''; w.style.opacity = ''; return; }
  const e = outExpo(p); w.style.transform = `translateY(${f2((1 - e) * 108)}%) rotate(${f2((1 - e) * rot)}deg)`; w.style.opacity = f4(clamp(p * 4)); }
// a burst of rays round an ellipse (the equation result's landing), ex / ey = ellipse radii at rest
function raysPose(rays, p, rx, ry) {
  const n = rays.length;
  rays.forEach((r, j) => { const ang = (j / n) * TAU + 0.2, ex = rx + 40 * outCubic(p), ey = ry + 46 * outCubic(p);
    r.style.opacity = p > 0 && p < 1 ? f4(1 - p) : '0';
    r.style.transform = `translate(${f2(Math.cos(ang) * ex)}px,${f2(Math.sin(ang) * ey)}px) rotate(${f2(Math.atan2(Math.sin(ang) * ey, Math.cos(ang) * ex) * 180 / Math.PI)}deg) scaleX(${f4(1 - 0.7 * p)})`; });
}
const ringPulse = (el, p, spread, rgb, a0) => { el.style.boxShadow = p > 0 && p < 1 ? `0 0 0 ${f2(outCubic(p) * spread)}px rgba(${rgb},${f4(a0 * (1 - p))})` : 'none'; };
const sheenPose = (el, p, w) => { el.style.transform = `translateX(${f2(lerp(-260, w + 80, inOutCubic(p)))}px) skewX(-18deg)`; el.style.opacity = p > 0 && p < 1 ? '1' : '0'; };

/* ======================= blocks (scene 3a): the bundle opens into RIGHT and BREACH, which slide together ======================= */
const OWN_ICONS = ['file-text', 'calendar', 'indian-rupee', 'handshake', 'pen-line'];
// the scene-2 bundle this cue opens: a bundle cue that is settled (tied, tiles home) and still fully on screen when this cue starts -
// its composition is taken over in place (same tiles, cord, bow and label), so "open the bundle" opens that very bundle
function prevBundle(c) {
  return EL.find(y => y.c.type === 'bundle' && y.c.t0 < c.t0 && y.c.t1 >= c.t0 + (y.c.fade_out ?? 0.3) - 0.01 && y.c.t1 <= c.t0 + 3
    && c.t0 >= bundleGat(y.c) + 1.2) || null;
}
BUILD.blocks = (c) => {
  const items = c.items || [], m = c.merge && c.merge.label != null ? c.merge : null, pb = prevBundle(c);
  const icons = pb ? (pb.c.icons && pb.c.icons.length ? pb.c.icons : ['file-text']) : OWN_ICONS;
  const parts = items.map(it => { const ws = typo(it.label).trim().split(/\s+/).filter(Boolean); const key = ws.length ? ws.pop() : ''; return { pre: ws.join(' '), key }; });
  const keys = parts.map(p => p.key).filter(Boolean);
  const el = mk(pcontent, 'cue ca-full ca-blk',
    `<div class="ca-bd bdl">${cordHTML()}${icons.map(n => `<div class="fct" style="opacity:0">${ico(n)}</div>`).join('')}${pb ? `<div class="lab serif">${connHTML(pb.c.label)}</div>` : ''}</div>` +
    items.map((_, k) => `<div class="ca-slot" style="opacity:0"><div class="ca-gn">${k + 1}</div></div>`).join('') +
    items.map((it, k) => `<div class="ca-bk card" style="opacity:0"><div class="ca-bh"><div class="ca-nb">${k + 1}</div>${parts[k].pre ? `<div class="ca-pre">${esc(parts[k].pre)}</div>` : ''}</div>` +
      `<div class="ca-key"><span class="wm"><span class="wi">${esc(parts[k].key)}</span></span></div>${it.sub ? `<div class="ca-sub serif">${esc(typo(it.sub))}</div>` : ''}</div>`).join('') +
    items.slice(1).map(() => '<div class="ca-op" style="opacity:0">+</div>').join('') +
    (m ? `<div class="ca-mg"><div class="ca-glow"></div><div class="ca-mgb ca-acc" style="opacity:0">${keys.length > 1 ? `<div class="ca-mgs">${keys.map(esc).join(' + ')}</div>` : ''}<div class="ca-mgl">${esc(typo(m.label))}</div></div>` +
      Array.from({ length: 16 }, () => '<div class="ca-ray"></div>').join('') + '</div>' : ''));
  const bd = $(el, '.ca-bd');
  return { el, pb, q: { bd, cord: cordQ(bd), ics: $$(bd, '.fct'), lab: $(bd, '.lab'), slots: $$(el, '.ca-slot'), ops: $$(el, '.ca-op'),
    b: $$(el, '.ca-bk').map(b => ({ el: b, nb: $(b, '.ca-nb'), pre: $(b, '.ca-pre'), key: $(b, '.ca-key'), ki: $(b, '.ca-key .wi'), sub: $(b, '.ca-sub') })),
    mg: $(el, '.ca-mg'), mgb: $(el, '.ca-mgb'), mgl: $(el, '.ca-mgl'), glow: $(el, '.ca-glow'), rays: $$(el, '.ca-ray') } };
};
LAYOUT.blocks = (x) => {
  const c = x.c, q = x.q, n = q.b.length, A = areaFor(c);
  const G = 120, w = n ? Math.floor((CW - G * (n - 1)) / n) : CW, inner = w - 76;
  q.b.forEach(B => { B.el.style.width = w + 'px'; });
  // the key word on one line (one size for every block), the lead words in letter-spaced caps beside the badge, the sub on <= 2 lines
  const ks = q.b.map(B => fitFont(B.key, () => B.ki.offsetWidth <= inner, 40, 2));
  if (ks.length) { const mn = Math.min(...ks); q.b.forEach(B => { B.key.style.fontSize = mn + 'px'; }); }
  // (lead words that do not fit on one line at 18 px wrap beside the badge instead of shrinking further; the sub takes <= 3 lines)
  q.b.forEach(B => { if (B.pre) { fitFont(B.pre, () => B.pre.scrollWidth <= inner - 74, 18, 1); if (B.pre.scrollWidth > inner - 74) B.pre.style.whiteSpace = 'normal'; }
    if (B.sub) fitLines(B.sub, 34, 3, 30); });
  const h = n ? Math.max(...q.b.map(B => B.el.offsetHeight)) : 0; q.b.forEach(B => { B.el.style.height = h + 'px'; });
  const top = c.y ?? centerTop(A, h, -10), cy = top + h / 2;
  x.bx = q.b.map((_, k) => CL + k * (w + G)); x.w = w; x.h = h; x.rowCy = cy;
  q.b.forEach((B, k) => { B.el.style.left = x.bx[k] + 'px'; B.el.style.top = top + 'px'; });
  q.slots.forEach((s, k) => { Object.assign(s.style, { left: x.bx[k] + 'px', top: top + 'px', width: w + 'px', height: h + 'px' }); });
  q.ops.forEach((o, k) => { o.style.left = (x.bx[k] + w + G / 2) + 'px'; o.style.top = cy + 'px'; });
  // the fused block, centred on the row; <= 820 px wide so its ray burst stays >= 96 px clear of the seam
  if (q.mg) {
    q.mgb.style.width = Math.min(820, CW - 120) + 'px';
    const mx = q.mgb.clientWidth - 100;   // one line down to 52 px, else <= 2 balanced lines
    fitFont(q.mgl, () => q.mgl.scrollWidth <= mx, 52, 2);
    if (q.mgl.scrollWidth > mx) { Object.assign(q.mgl.style, { whiteSpace: 'normal', textAlign: 'center', textWrap: 'balance', maxWidth: mx + 'px', fontSize: '72px' }); fitLines(q.mgl, 52, 2, 36); }
    const ms = $(q.mgb, '.ca-mgs'); if (ms) fitFont(ms, () => ms.scrollWidth <= mx, 16, 1);
    const mw = q.mgb.offsetWidth, mh = q.mgb.offsetHeight;
    Object.assign(q.mg.style, { left: f2(CX - mw / 2) + 'px', top: f2(cy - mh / 2) + 'px', width: mw + 'px', height: mh + 'px' });
    x.rayR = [mw / 2 + 66, mh / 2 + 21];
  }
  // the tied bundle: the scene-2 bundle taken over in place, or a small one of our own on the row (LAYOUT runs in cue order, so the
  // bundle is normally laid out already; if not, lay it out now - LAYOUT.bundle only sets positions, running it twice is harmless)
  if (x.pb && !x.pb.home) LAYOUT.bundle(x.pb);
  const pb = x.pb && x.pb.home ? x.pb : null;
  x.B = pb ? { cx: pb.cx, cy: pb.cy, R: pb.R, fs: pb.fs, home: pb.home.map(p => p.slice()), inh: true, gat: bundleGat(pb.c) }
           : { cx: CX, cy, R: BDL_R[0], fs: 0.62, home: homeRing(q.ics.length, CX, cy), inh: false };
  const B = x.B;
  q.bd.style.transformOrigin = `${f2(B.cx)}px ${f2(B.cy)}px`;
  cordPath(q.cord, B.cx, B.cy, B.R);
  if (q.lab) q.lab.style.top = (B.cy + B.R + BDL_LAB) + 'px';
  // as it opens, every fact tile drops into the slot on its side ("two things"): a loose heap, in container coordinates
  const sc = x.bx.map(bx => [bx + w / 2, cy]);
  x.to = B.home.map(([hx], k) => { const side = n < 2 ? 0 : hx < B.cx - 1 ? 0 : hx > B.cx + 1 ? n - 1 : (k % 2 ? n - 1 : 0);
    const jx = ((k * 37) % 5) / 4 - 0.5, jy = ((k * 53) % 3) / 2 - 0.5, S = sc[side] || [CX, cy];
    return [B.cx + (S[0] + jx * 140 - B.cx) / B.fs, B.cy + (S[1] + jy * 90 - B.cy) / B.fs]; });
  // our first frame hides the taken-over cue (its SEEK runs before ours in the same frame)
  x.handoff = !!pb && EL.indexOf(pb) < EL.indexOf(x);
  x.el.style.transformOrigin = `${f2(CX)}px ${f2(cy)}px`;
};
SEEK.blocks = (x, t) => {
  const c = x.c, q = x.q, B = x.B, items = c.items || [], m = c.merge && c.merge.label != null ? c.merge : null;
  // a taken-over bundle opens from our first frame at the earliest (open_at can fall a hair before t0: the bow must not jump at the
  // hand-over); our own bundle is built over the first 0.75 s, so it never opens before it is tied
  const op = Math.max(c.open_at ?? c.t0 + 0.3, B.inh ? c.t0 : c.t0 + 0.8);
  if (x.handoff && t >= c.t0 && t <= (x.pb.end ?? x.pb.c.t1)) x.pb.el.style.opacity = '0';
  // ---- 1. the tied bundle, then it opens: the bow unties, the cord slips off, the facts drop into two slots
  const bre = B.inh ? 1 + (breatheAt(B.gat, t) - 1) * (1 - P(t, op, 0.4)) : 1;
  q.bd.style.transform = `scale(${f4(B.fs * bre)})`;
  const tie = B.inh ? 1 : inOutCubic(P(t, c.t0 + 0.15, 0.35));
  cordPose(q.cord, tie, 0.5 * inOutCubic(P(t, op + 0.1, 0.65)));
  const pbw = B.inh ? 1 : P(t, c.t0 + 0.35, 0.45), pu = P(t, op, 0.5);
  bowPose(q.cord, B.cx, B.cy + B.R, (1 - outCubic(pbw)) * -40, BDL_BOW * spring(pbw) * (1 + 0.12 * outCubic(pu)), clamp(pbw * 4) * (1 - inCubic(clamp(pu * 1.3))), outCubic(pu));
  if (q.lab) { const pl = outCubic(P(t, op, 0.45)); q.lab.style.opacity = f4(1 - pl); q.lab.style.transform = `translateY(${f2(-24 * pl)}px)`; }
  q.ics.forEach((el, k) => {
    const pi = B.inh ? 1 : P(t, c.t0 + k * 0.05, 0.4), pk = P(t, op + 0.35 + k * 0.05, 0.75), e = inOutCubic(pk);
    const [hx, hy] = B.home[k], [tx, ty] = x.to[k];
    const X = lerp(hx, tx, e), Y = lerp(hy, ty, e) - 60 * Math.sin(Math.PI * e), rot = (k % 2 ? 1 : -1) * 24 * Math.sin(Math.PI * e);
    el.style.opacity = f4(clamp(pi * 3) * (1 - clamp((pk - 0.55) / 0.45)));
    el.style.transform = `translate(${f2(X)}px,${f2(Y)}px) rotate(${f2(rot)}deg) scale(${f4((B.inh ? 1 : spring(pi)) * lerp(1, 0.4, outCubic(pk)))})`;
  });
  // ---- 2. two empty numbered slots as the facts land in them; each gives way to its block
  const sa = op + 0.75, ats = q.b.map((_, k) => items[k].at ?? (sa + 1.2 * (k + 1)));
  q.slots.forEach((s, k) => { const p = P(t, sa + k * 0.08, 0.45);
    s.style.opacity = f4(outCubic(p) * (1 - P(t, ats[k] + 0.08, 0.25))); tf(s, p >= 1, `scale(${f4(0.94 + 0.06 * outBack(p))})`); });
  // ---- 3. each block builds at its at (badge, lead words, key word, sub); 4. at merge.at they slide together and fuse
  // the merge: the words clear first, the blank cards slide together and fold into one, the accent block bursts out of them
  // (the sub-lines go first; RIGHT and BREACH stay readable until the cards start to cover each other)
  const pm = m ? P(t, m.at, 0.5) : 0, em = inOutCubic(pm), clr = 1 - clamp((pm - 0.32) / 0.22), clrS = 1 - clamp((pm - 0.08) / 0.25), land = m ? m.at + 0.4 : Infinity;
  const fo = 1 - clamp((t - land - 0.06) / 0.14);
  q.b.forEach((Bk, k) => {
    const at = ats[k], p = P(t, at, 0.6), s0 = 0.86 + 0.14 * outBack(p);
    const dx = (CX - (x.bx[k] + x.w / 2)) * em;
    Bk.el.style.opacity = f4(clamp(p * 3) * fo);
    tf(Bk.el, p >= 1 && em === 0, `translate(${f2(dx)}px,${f2((1 - outExpo(p)) * 46)}px) scale(${f4(s0 * (1 - 0.1 * em))},${f4(s0 * (1 - 0.34 * em))})`);
    const pn = P(t, at + 0.1, 0.6); Bk.nb.style.opacity = f4(clamp(pn * 4) * clr); tf(Bk.nb, pn >= 1, `scale(${f4(spring(pn))}) rotate(${f2((1 - outCubic(pn)) * -110)}deg)`);
    if (Bk.pre) { wipeIn(Bk.pre, outCubic(P(t, at + 0.16, 0.45))); Bk.pre.style.opacity = f4(clr); }
    maskIn(Bk.ki, P(t, at + 0.2, 0.62), 5); if (clr < 1) Bk.ki.style.opacity = f4(clr);
    if (Bk.sub) { rise(Bk.sub, P(t, at + 0.36, 0.55), 24); if (clrS < 1) Bk.sub.style.opacity = f4(clrS); }
  });
  q.ops.forEach((o, k) => { const po = P(t, ats[k + 1] - 0.06, 0.5), g = clamp(pm * 4);
    o.style.opacity = f4(clamp(po * 3) * (1 - g)); tf(o, po >= 1 && g === 0, `scale(${f4(spring(po) * (1 - 0.6 * g))}) rotate(${f2((1 - outCubic(po)) * -120)}deg)`); });
  if (q.mg) {
    const pr = P(t, land, 0.55);
    q.mgb.style.opacity = f4(clamp(pr * 5)); tf(q.mgb, pr >= 1, `scale(${f4(0.6 + 0.4 * spring(pr, 7, 12))})`);
    ringPulse(q.glow, P(t, land + 0.12, 0.75), 34, '204,120,92', 0.38);
    raysPose(q.rays, P(t, land + 0.12, 0.62), x.rayR[0], x.rayR[1]);
    const lv = t > land + 0.9 ? 0.5 + 0.5 * Math.sin(TAU * (t - land) / 2.4) : 0;   // gentle living pulse once it has landed
    q.mgb.style.boxShadow = `0 ${f2(30 + 6 * lv)}px ${f2(66 + 14 * lv)}px rgba(179,87,63,${f4(0.36 + 0.1 * lv)}),0 4px 10px rgba(120,50,30,.14)`;
  }
  cueRoot(x, t, { from: op });
};

/* ======================= verdicts (scene 3b): two wrong combinations crossed out, the right one highlighted ======================= */
BUILD.verdicts = (c) => {
  const rows = c.rows || [];
  const el = mk(pcontent, 'cue ca-vd', rows.map(r => `<div class="ca-vr${r.ok ? ' ok' : ''}"><div class="ca-vglow"></div><div class="ca-vc card" style="opacity:0"><div class="ca-vs">` +
    (r.ok ? `<div class="ca-vk">${ico('check')}</div>` : `<div class="ca-vq">?</div><div class="ca-vx">${ico('x')}</div>`) +
    `</div><div class="ca-vt serif">${opsHTML(typo(r.text))}</div>${r.ok ? '<div class="ca-sheen"></div>' : ''}</div></div>`).join(''));
  return { el, q: { rows: $$(el, '.ca-vr').map(r => ({ g: $(r, '.ca-vglow'), c: $(r, '.ca-vc'), s: $(r, '.ca-vs'), qm: $(r, '.ca-vq'), x: $(r, '.ca-vx'), t: $(r, '.ca-vt'), bs: $$(r, '.ca-vt b'), sh: $(r, '.ca-sheen') })) } };
};
LAYOUT.verdicts = (x) => {
  const c = x.c, q = x.q, A = areaFor(c), rows = c.rows || [];
  // one type size for every row: one line each down to 52 px, else <= 2 lines
  q.rows.forEach(R => fitLines(R.t, 52, 2, 46));
  if (q.rows.length) { const mn = Math.min(...q.rows.map(R => fsOf(R.t))); q.rows.forEach(R => { R.t.style.fontSize = mn + 'px'; }); }
  q.rows.forEach((R, k) => { R.bars = rows[k].ok ? [] : strikeBars(R.t, R.t); });
  x.ats = rows.map((r, k) => r.at ?? (c.t0 + 0.3 + 2 * k));
  // a wrong row is struck about halfway to the next row ("... gives you nothing"), unless strike_at says when
  x.sas = rows.map((r, k) => r.ok ? null : r.strike_at ?? (k + 1 < rows.length ? x.ats[k] + clamp(0.5 * (x.ats[k + 1] - x.ats[k]), 0.9, 2.2) : Math.min(x.ats[k] + 1.4, c.t1 - 0.8)));
  const ko = rows.findIndex(r => r.ok); x.okAt = ko >= 0 ? x.ats[ko] : null;
  x.rw = q.rows.length ? q.rows[0].c.offsetWidth : CW;
  x.el.style.top = (c.y ?? centerTop(A, x.el.offsetHeight, -10)) + 'px';
};
SEEK.verdicts = (x, t) => {
  const c = x.c, q = x.q, rows = c.rows || [];
  const okP = x.okAt != null ? outCubic(P(t, x.okAt, 0.5)) : 0;   // the right answer lands: the struck rows step back
  q.rows.forEach((R, k) => {
    const at = x.ats[k], p = P(t, at, 0.6);
    let sc = 0.94 + 0.06 * outBack(p), op = clamp(p * 2.5);
    if (!rows[k].ok) {
      const sa = x.sas[k], g = outCubic(P(t, sa + 0.18, 0.45));
      R.bars.forEach((b, j) => { b.style.transform = `scaleX(${f4(outCubic(P(t, sa + j * 0.16, 0.38)))}) rotate(-1.2deg)`; });
      R.t.style.color = mixC('#1f1e1d', '#a59f97', g); R.bs.forEach(b => { b.style.color = mixC('#b3573f', '#a59f97', g); });
      R.c.style.background = g > 0 ? mixC('#fffcf6', '#f2ede5', g) : '';
      const pf = P(t, sa + 0.1, 0.5);   // the "?" flips to the red cross
      R.qm.style.opacity = f4(1 - clamp(pf * 3)); tf(R.qm, pf <= 0, `scale(${f4(1 - 0.4 * clamp(pf * 2))})`);
      R.x.style.opacity = f4(clamp(pf * 3)); tf(R.x, pf >= 1, `scale(${f4(spring(pf))}) rotate(${f2((1 - outCubic(pf)) * -90)}deg)`);
      sc *= 1 - 0.03 * okP * g; op *= 1 - 0.22 * okP * g;
    } else {
      ringPulse(R.g, P(t, at + 0.35, 0.8), 22, '204,120,92', 0.32);   // a full-width row: the halo stays >= 96 px clear of the seam
      if (R.sh) sheenPose(R.sh, P(t, at + 0.45, 0.75), x.rw);
    }
    R.c.style.opacity = f4(op);
    tf(R.c, p >= 1 && Math.abs(sc - 1) < 1e-6, `translateY(${f2((1 - outExpo(p)) * 52)}px) scale(${f4(sc)})`);
    const pd = P(t, at + 0.08, 0.6); tf(R.s, pd >= 1, `scale(${f4(spring(pd))}) rotate(${f2((1 - outCubic(pd)) * -40)}deg)`);
    wipeIn(R.t, outCubic(P(t, at + 0.1, 0.5)));
  });
  cueRoot(x, t, { from: x.ats.length ? x.ats[0] : c.t0 });
};

/* ======================= timeline (scene 4a): the loan story ======================= */
const valHTML = (v) => String(v ?? '').trim().split(/\s+/).map(w => `<span class="wm"><span class="wi">${esc(w).replace(/₹/g, '<span class="rs">₹</span>')}</span></span>`).join(' ');
BUILD.timeline = (c) => {
  const nodes = c.nodes || [];
  const el = mk(pcontent, 'cue ca-full ca-tl', `<div class="ca-trk"><div class="ca-tf"></div></div><svg class="ca-arw a0" viewBox="0 0 36 36"><path d="M10 6 L28 18 L10 30"/></svg><svg class="ca-arw a1" viewBox="0 0 36 36" style="opacity:0"><path d="M10 6 L28 18 L10 30"/></svg>` +
    nodes.map(nd => { const red = nd.tone === 'red' ? ' red' : '';
      return `<div class="ca-stem${red}"></div><div class="ca-ring${red}"></div><div class="ca-dot${red}" style="opacity:0"></div><div class="ca-tc card${red}" style="opacity:0"><div class="ca-tlab">${esc(typo(nd.label))}</div><div class="ca-tval serif">${valHTML(nd.value)}</div>${nd.sub ? `<div class="ca-tsub serif">${opsHTML(typo(nd.sub))}</div>` : ''}</div>`; }).join(''));
  const st = $$(el, '.ca-stem'), rg = $$(el, '.ca-ring'), dt = $$(el, '.ca-dot'), cd = $$(el, '.ca-tc');
  return { el, q: { trk: $(el, '.ca-trk'), tf: $(el, '.ca-tf'), a0: $(el, '.ca-arw.a0'), a1: $(el, '.ca-arw.a1'),
    n: nodes.map((nd, k) => ({ red: nd.tone === 'red', stem: st[k], ring: rg[k], dot: dt[k], card: cd[k], lab: $(cd[k], '.ca-tlab'), val: $(cd[k], '.ca-tval'), ws: $$(cd[k], '.ca-tval .wi'), sub: $(cd[k], '.ca-tsub') })) } };
};
LAYOUT.timeline = (x) => {
  const c = x.c, q = x.q, n = q.n.length, A = areaFor(c); if (!n) return;
  // nodes alternate above / below the line (the zig-zag gives each card room for a big value); same-side cards never overlap
  const gap = 40, w = n === 1 ? 640 : Math.min(560, Math.floor((2 * CW - gap * (n - 1)) / (n + 1))), inner = w - 68;
  q.n.forEach(N => { N.card.style.width = w + 'px'; });
  const vs = q.n.map(N => fitFont(N.val, () => N.val.scrollWidth <= inner + 1, 52, 2)), vm = Math.min(...vs);
  q.n.forEach(N => { N.val.style.fontSize = vm + 'px'; fitFont(N.lab, () => N.lab.scrollWidth <= inner + 1, 16, 1); if (N.sub) fitFont(N.sub, () => N.sub.scrollWidth <= inner + 1, 26, 1); });
  // each card hugs its words (300 px at least); node k sits under / over its card's centre, the first card starting at the column's
  // left edge and the last ending at its right edge, the nodes evenly spaced between - unless same-side cards would then collide, in
  // which case every card takes the common width w
  let ws = q.n.map(N => { N.card.style.width = 'max-content'; const v = Math.ceil(N.card.offsetWidth); return Math.max(300, Math.min(w, v)); });
  const place = () => { const a = CL + ws[0] / 2, b = CL + CW - ws[n - 1] / 2; return q.n.map((_, k) => n === 1 ? CX : a + (b - a) * k / (n - 1)); };
  x.nx = place();
  if (q.n.some((_, k) => k + 2 < n && x.nx[k + 2] - x.nx[k] < (ws[k] + ws[k + 2]) / 2 + gap)) { ws = ws.map(() => w); x.nx = place(); }
  q.n.forEach((N, k) => { N.card.style.width = ws[k] + 'px'; });
  const hs = q.n.map(N => N.card.offsetHeight), hA = Math.max(...hs.filter((_, k) => k % 2 === 0)), hB = n > 1 ? Math.max(...hs.filter((_, k) => k % 2 === 1)) : 0;
  const L = 54, H = hA + L + (n > 1 ? L + hB : 30), top = c.y ?? centerTop(A, H, -6), Ly = top + hA + L;
  x.Ly = Ly;
  q.n.forEach((N, k) => {
    const up = k % 2 === 0, cx = x.nx[k];
    N.up = up;
    N.card.style.left = f2(cx - ws[k] / 2) + 'px'; N.card.style.top = f2(up ? Ly - L - hs[k] : Ly + L) + 'px';
    N.card.style.transformOrigin = up ? '50% 100%' : '50% 0%';
    Object.assign(N.stem.style, { left: f2(cx) + 'px', top: f2(up ? Ly - L : Ly) + 'px', height: L + 'px', transformOrigin: up ? '50% 100%' : '50% 0%' });
    for (const e of [N.dot, N.ring]) { e.style.left = f2(cx) + 'px'; e.style.top = f2(Ly) + 'px'; }
  });
  Object.assign(q.trk.style, { left: CL + 'px', top: f2(Ly - 3) + 'px', width: (CW - 12) + 'px' });
  for (const a of [q.a0, q.a1]) { a.style.left = f2(CL + CW - 31) + 'px'; a.style.top = f2(Ly - 18) + 'px'; }
  x.ats = (c.nodes || []).map((nd, k) => nd.at ?? (c.t0 + 0.8 + 1.5 * k));
  x.el.style.transformOrigin = `${f2(CX)}px ${f2(Ly)}px`;
};
SEEK.timeline = (x, t) => {
  const c = x.c, q = x.q, n = q.n.length; if (!n) return;
  const ats = x.ats, x0 = CL, x1 = CL + CW - 14;
  const pt = P(t, c.t0, 0.8); q.trk.style.transform = `scaleX(${f4(outExpo(pt))})`; q.trk.style.opacity = f4(clamp(pt * 3));
  q.a0.style.opacity = f4(clamp(P(t, c.t0 + 0.45, 0.3) * 3));
  // the copper fill reaches each node as it builds, then runs on to the arrow
  let fx = x0;
  for (let k = 0; k < n; k++) { const a = Math.max(c.t0 + 0.2, ats[k] - 0.5); if (t < a) break; fx = lerp(k ? x.nx[k - 1] : x0, x.nx[k], inOutCubic(P(t, a, ats[k] - a))); }
  const ae = ats[n - 1] + 0.3; if (t >= ae) fx = lerp(x.nx[n - 1], x1, outCubic(P(t, ae, 0.8)));
  q.tf.style.width = f2(Math.max(0, fx - x0)) + 'px';
  const pa = P(t, ae + 0.5, 0.35); q.a1.style.opacity = f4(clamp(pa * 3)); tf(q.a1, pa >= 1, `translateX(${f2((1 - outBack(pa)) * -10)}px)`);
  q.n.forEach((N, k) => {
    const at = ats[k];
    const pd = P(t, at, 0.5); N.dot.style.opacity = f4(clamp(pd * 4)); tf(N.dot, pd >= 1, `scale(${f4(spring(pd))})`);
    const pr = P(t, at, 0.75); N.ring.style.opacity = pr > 0 && pr < 1 ? f4(0.6 * (1 - pr)) : '0'; N.ring.style.transform = `scale(${f4(1 + 1.8 * outCubic(pr))})`;
    const pst = P(t, at + 0.05, 0.35); tf(N.stem, pst >= 1, `scaleY(${f4(outCubic(pst))})`);
    const pc = P(t, at + 0.12, 0.6), dir = N.up ? 1 : -1;
    N.card.style.opacity = f4(clamp(pc * 3));
    tf(N.card, pc >= 1, `translateY(${f2(dir * (1 - outExpo(pc)) * 36)}px) scale(${f4(0.9 + 0.1 * outBack(pc))})`);
    wipeIn(N.lab, outCubic(P(t, at + 0.2, 0.45)));
    N.ws.forEach((w, j) => maskIn(w, P(t, at + 0.24 + j * 0.08, 0.6), 0));
    // the "nothing" shake: a red value shakes its head once it has landed (the words move inside the card, the card stays put)
    if (N.red) { const tau = t - at - 0.8; N.val.style.transform = tau > 0 && tau < 0.7 ? `translateX(${f2(9 * Math.exp(-6 * tau) * Math.sin(TAU * 6 * tau))}px)` : ''; }
    if (N.sub) rise(N.sub, P(t, at + 0.42, 0.55), 18);
  });
  cueRoot(x, t, { from: ats[0] });
};

/* ======================= checklist (scene 4b): what Ravi must prove, folding into a bundle ======================= */
BUILD.checklist = (c) => {
  const items = c.items || [], f = c.fold && c.fold.label != null ? c.fold : null, num = (it, k) => esc(it.n ?? k + 1);
  const el = mk(pcontent, 'cue ca-full ca-ck', `<div class="ca-ckl">${c.head ? `<div class="ca-ckhd"><div class="ca-ckh serif">${maskWords(typo(c.head))}</div><div class="ca-cku"></div></div>` : ''}<div class="ca-ckc"><div class="ca-ckbg card" style="opacity:0"></div>` +
    items.map((it, k) => `<div class="ca-cki">${k ? '<div class="ca-ckdv" style="opacity:0"></div>' : ''}<div class="ca-ckg" style="opacity:0">${num(it, k)}</div><div class="ca-ckn" style="opacity:0">${num(it, k)}</div><div class="ca-ckt serif" style="opacity:0">${esc(typo(it.text))}</div>` +
      `<div class="ca-ckb" style="opacity:0"><div class="fill"></div><svg viewBox="0 0 24 24"><path d="M20 6 9 17l-5-5" pathLength="1"/></svg></div></div>`).join('') + '</div></div>' +
    (f ? `<div class="ca-ckf bdl">${cordHTML()}${items.map((it, k) => `<div class="fct ca-ckm" style="opacity:0"><span class="ca-ckd">${num(it, k)}</span><div class="ca-cks">${ico('check')}</div></div>`).join('')}<div class="lab serif" style="opacity:0">${connHTML(typo(f.label))}</div></div>` : ''));
  const fl = $(el, '.ca-ckf');
  return { el, q: { l: $(el, '.ca-ckl'), hd: $(el, '.ca-ckhd'), h: $(el, '.ca-ckh'), hw: $$(el, '.ca-ckh .wi'), u: $(el, '.ca-cku'), c: $(el, '.ca-ckc'), bg: $(el, '.ca-ckbg'),
    r: $$(el, '.ca-cki').map(r => ({ row: r, dv: $(r, '.ca-ckdv'), g: $(r, '.ca-ckg'), n: $(r, '.ca-ckn'), t: $(r, '.ca-ckt'), b: $(r, '.ca-ckb'), fill: $(r, '.ca-ckb .fill'), chk: $(r, '.ca-ckb path') })),
    f: fl, cord: fl ? cordQ(fl) : null, m: fl ? $$(fl, '.ca-ckm').map(m => ({ el: m, d: $(m, '.ca-ckd'), s: $(m, '.ca-cks') })) : [], fl: fl ? $(fl, '.lab') : null } };
};
const FOLD_STAG = 0.11;   // the fold: one line after another (their flight paths cross, so they are kept apart in time)
function clusterPos(n, cx, cy) {   // the folded items, in reading order
  const S = 156, h = S / 2;
  if (n === 1) return [[cx, cy]];
  if (n === 2) return [[cx - h, cy], [cx + h, cy]];
  if (n === 3) return [[cx - h, cy - S * 0.43], [cx + h, cy - S * 0.43], [cx, cy + S * 0.43]];
  if (n === 4) return [[cx - h, cy - h], [cx + h, cy - h], [cx - h, cy + h], [cx + h, cy + h]];
  return homeRing(n, cx, cy);
}
LAYOUT.checklist = (x) => {
  const c = x.c, q = x.q, A = areaFor(c), items = c.items || [];
  if (q.h) fitFont(q.h, () => q.h.scrollWidth <= CW + 1, 56, 2);
  // one type size for every line, each text clear of its tick box
  // (each on one line down to 52 px; a line too long even then wraps onto two lines - its row grows - at the largest size that takes,
  // rather than running under the tick box or shrinking every line)
  const fitsOne = (R) => R.t.scrollWidth <= R.t.clientWidth + 1;
  const fs = q.r.map(R => { fitFont(R.t, () => fitsOne(R), 52, 2); if (fitsOne(R)) return fsOf(R.t);
    R.t.style.fontSize = ''; Object.assign(R.t.style, { whiteSpace: 'normal', textWrap: 'balance', lineHeight: '1.06' });
    Object.assign(R.row.style, { height: 'auto', minHeight: '112px', paddingTop: '14px', paddingBottom: '14px', boxSizing: 'border-box' });
    fitLines(R.t, 1000, 2, 40); return fsOf(R.t); });
  if (fs.length) { const mn = Math.min(...fs); q.r.forEach(R => { R.t.style.fontSize = mn + 'px'; }); }
  const lh = q.l.offsetHeight, top = c.y ?? centerTop(A, lh, -14);
  q.l.style.top = top + 'px';
  x.ats = items.map((it, k) => it.at ?? ((c.head_at ?? c.t0) + 1 + 1.2 * k));
  x.el.style.transformOrigin = `${f2(CX)}px ${f2(top + lh / 2)}px`;
  if (!q.f) return;
  // the bundle the items fold into: same language as the scene-2 bundle (cord ring, bow at the bottom, serif label under it)
  const n = q.m.length, half = 64, lab = q.fl.offsetHeight;
  const rel = clusterPos(n, 0, 0), R = Math.ceil(Math.max(...rel.map(([a, b]) => Math.hypot(a, b))) + half * 1.3 + 24);
  const up = R + 8, down = R + BDL_LAB + lab, avail = A.bottom - A.top, fsc = Math.min(1, avail / (up + down));
  const cx = CX, cy = Math.round(A.top + (avail - (up + down) * fsc) / 2 + up * fsc);
  x.F = { cx, cy, R, fs: fsc, home: rel.map(([a, b]) => [cx + a, cy + b]) };
  q.f.style.transformOrigin = `${cx}px ${cy}px`;
  cordPath(q.cord, cx, cy, R);
  q.fl.style.top = (cy + R + BDL_LAB) + 'px';
  // each tile starts as its line's number badge (same place, same size), in the fold layer's coordinates (scaled by fs about the centre)
  x.F.from = q.r.map(Rw => { const [bx, by] = offIn(Rw.n, x.el); const sx = bx + Rw.n.offsetWidth / 2, sy = by + Rw.n.offsetHeight / 2; return [cx + (sx - cx) / fsc, cy + (sy - cy) / fsc]; });
  x.F.s0 = (q.r.length ? q.r[0].n.offsetWidth : 64) / (2 * half * fsc);
  // a tile that has landed stays on top: the next one (coming from the left, across its spot) slides in from behind it
  q.m.forEach((M, k) => { M.el.style.zIndex = String(n - k); });
};
SEEK.checklist = (x, t) => {
  const c = x.c, q = x.q, ha = c.head_at ?? c.t0, fd = q.f && c.fold.at != null ? c.fold.at : null;
  const ef = fd != null ? outCubic(P(t, fd, 0.4)) : 0;   // the sheet gives way to the bundle
  if (q.hd) { q.hw.forEach((w, k) => maskIn(w, P(t, ha + k * 0.09, 0.62), 5));
    const pu = P(t, ha + 0.35, 0.6); tf(q.u, pu >= 1, `scaleX(${f4(outExpo(pu))})`);
    q.hd.style.opacity = f4(1 - ef); tf(q.hd, ef <= 0, `translateY(${f2(-22 * ef)}px)`); }
  // the sheet with its empty numbered lines (paper, dashed dividers, ghost numbers); each line's own parts build and fold on their own
  const pc = P(t, ha + 0.25, 0.6), sheet = clamp(pc * 2.5) * (1 - (fd != null ? outCubic(P(t, fd + 0.12, 0.4)) : 0));
  q.bg.style.opacity = f4(sheet); tf(q.c, pc >= 1, `translateY(${f2((1 - outExpo(pc)) * 40)}px)`);
  q.r.forEach((R, k) => {
    const at = x.ats[k], sk = fd != null ? fd + FOLD_STAG * k : Infinity, pg = P(t, sk, 0.3);
    if (R.dv) R.dv.style.opacity = f4(sheet);
    R.g.style.opacity = f4(sheet * (1 - P(t, at, 0.2)));
    const pn = P(t, at, 0.6); R.n.style.opacity = t >= sk ? '0' : f4(clamp(pn * 4)); tf(R.n, pn >= 1, `scale(${f4(spring(pn))}) rotate(${f2((1 - outCubic(pn)) * -110)}deg)`);
    const pt = P(t, at + 0.07, 0.55), eg = inCubic(pg);
    R.t.style.opacity = f4(clamp(pt * 2.2) * (1 - outCubic(pg)));
    tf(R.t, pt >= 1 && pg <= 0, `translateX(${f2(away((1 - outExpo(pt)) * 70) - 60 * eg)}px) scaleX(${f4(1 - 0.5 * eg)})`);
    const pb = P(t, at + 0.12, 0.5); R.b.style.opacity = f4(clamp(pb * 3) * (1 - outCubic(pg))); tf(R.b, pb >= 1 && pg <= 0, `scale(${f4(spring(pb) * (1 - 0.5 * outCubic(pg)))})`);
    const pk = P(t, at + 0.34, 0.3); R.fill.style.opacity = f4(outCubic(pk)); tf(R.fill, pk >= 1, `scale(${f4(0.6 + 0.4 * outBack(pk))})`);
    const pck = P(t, at + 0.42, 0.32); R.chk.style.opacity = pck > 0 ? '1' : '0'; R.chk.style.strokeDashoffset = f4(1 - outCubic(pck));
  });
  // the fold: each number badge becomes a fact tile and flies into the bundle, the cord ties round, the bow, the label
  if (fd != null) {
    const F = x.F, n = q.m.length, bre = t > fd + 1.6 ? 1 + 0.008 * Math.sin(TAU * (t - fd) / 2.2) : 1;
    q.f.style.transform = `scale(${f4(F.fs * bre)})`;
    q.m.forEach((M, k) => {
      const sk = fd + FOLD_STAG * k, p = P(t, sk, 0.62), e = inOutCubic(p), mc = outCubic(clamp(p * 1.6));
      const [ax, ay] = F.from[k], [hx, hy] = F.home[k];
      const X = lerp(ax, hx, e), Y = lerp(ay, hy, e) - 50 * Math.sin(Math.PI * e), s = lerp(F.s0, 1, outCubic(p)), rot = (k % 2 ? 1 : -1) * 16 * Math.sin(Math.PI * e);
      M.el.style.opacity = t >= sk ? '1' : '0';
      M.el.style.transform = `translate(${f2(X)}px,${f2(Y)}px) rotate(${f2(rot)}deg) scale(${f4(s)})`;
      M.el.style.background = mc >= 1 ? '' : `linear-gradient(135deg,${mixC('#de8a6a', '#fffcf6', mc)} 0%,${mixC('#d97757', '#fffcf6', mc)} 38%,${mixC('#b3573f', '#fffcf6', mc)} 100%)`;
      M.el.style.borderRadius = f2(lerp(64, 34, mc)) + 'px';
      M.el.style.borderColor = mc >= 1 ? '' : `rgba(224,215,198,${f4(mc)})`;
      M.d.style.color = mixC('#ffffff', '#b3573f', mc);
      const ps = P(t, sk + 0.55, 0.45); M.s.style.opacity = f4(clamp(ps * 4)); tf(M.s, ps >= 1, `scale(${f4(spring(ps))})`);
    });
    const tie = fd + 0.62 + FOLD_STAG * (n - 1);
    cordPose(q.cord, inOutCubic(P(t, tie, 0.5)), 0);
    const pb = P(t, tie + 0.32, 0.6);
    bowPose(q.cord, F.cx, F.cy + F.R, (1 - outCubic(pb)) * -40, BDL_BOW * spring(pb), clamp(pb * 4), 0);
    rise(q.fl, P(t, tie + 0.2, 0.6), 34);
  }
  cueRoot(x, t, { from: ha });
};

/* ======================= notequal (scene 5): "Cause of action ≠ the defence" ======================= */
const NEQ_SVG = '<span class="ca-neq"><svg viewBox="0 0 100 100"><rect class="b" x="8" y="31" width="84" height="12" rx="6"/><rect class="b" x="8" y="57" width="84" height="12" rx="6"/><path class="sl" d="M68 8 L32 92" pathLength="1"/></svg></span>';
BUILD.notequal = (c) => {
  let sub = '';
  if (c.sub) { const s = typo(c.sub), m = s.match(/^(.*?,)\s*(not)\s+(.+)$/i);   // "A, not B": B is the thing to ignore - muted, struck through
    sub = `<div class="ca-ns"><div class="ca-nsr"></div><div class="tile" style="opacity:0">${ico(c.icon || 'file-text')}</div><div class="ca-nst serif" style="opacity:0">${m ? `${esc(m[1])} <span class="ca-nsn">${esc(m[2])} <span class="ca-nsb">${esc(m[3])}</span></span>` : esc(s)}</div></div>`; }
  const el = mk(pcontent, 'cue ca-ne', `<div class="ca-nl serif">${maskWords(typo(c.left))}</div><div class="ca-nr serif">${NEQ_SVG}<span class="ca-nrw">${maskWords(typo(c.right))}</span></div>${sub}`);
  return { el, q: { l: $(el, '.ca-nl'), r: $(el, '.ca-nr'), lw: $$(el, '.ca-nl .wi'), rw: $$(el, '.ca-nrw .wi'), eq: $(el, '.ca-neq'), bars: $$(el, '.ca-neq .b'), sl: $(el, '.ca-neq .sl'),
    ns: $(el, '.ca-ns'), nsr: $(el, '.ca-nsr'), tile: $(el, '.ca-ns .tile'), st: $(el, '.ca-nst'), nsb: $(el, '.ca-nsb') } };
};
LAYOUT.notequal = (x) => {
  const c = x.c, q = x.q, A = areaFor(c);
  if (q.st) fitLines(q.st, 48, 2, 40);
  // both lines one size, each on one line in the column, the whole block inside the free band
  let fs = 128; const set = (v) => { q.l.style.fontSize = v + 'px'; q.r.style.fontSize = v + 'px'; };
  const fits = () => q.l.scrollWidth <= CW + 1 && q.r.scrollWidth <= CW + 1 && x.el.offsetHeight <= A.bottom - A.top - 16;
  set(fs); while (!fits() && fs > 64) { fs -= 4; set(fs); }
  x.sb = q.nsb ? strikeBars(q.nsb, q.st) : [];
  x.top = c.y ?? centerTop(A, x.el.offsetHeight, -10); x.el.style.top = x.top + 'px';
  x.el.style.transformOrigin = '0 0';   // left-aligned text: the push-in (and a pairing's shrink) keep the column's left edge
};
SEEK.notequal = (x, t) => {
  const c = x.c, q = x.q, at = c.at ?? c.t0, la = c.left_at ?? at;
  q.lw.forEach((w, k) => maskIn(w, P(t, la + k * 0.12, 0.62)));
  const ea = Math.max(at, la + 0.12 * q.lw.length) + 0.12;   // the ≠ once the left side stands: two bars, then the slash through them
  q.bars.forEach((b, j) => { const pbj = P(t, ea + j * 0.07, 0.32); tf(b, pbj >= 1, `scaleX(${f4(outExpo(pbj))})`); });
  const psl = P(t, ea + 0.2, 0.3); q.sl.style.opacity = f4(clamp(psl * 6)); q.sl.style.strokeDashoffset = f4(1 - inOutCubic(psl));
  q.eq.style.opacity = f4(clamp(P(t, ea, 0.15) * 4));
  const pkk = P(t, ea + 0.3, 0.36); tf(q.eq, pkk <= 0 || pkk >= 1, `scale(${f4(1 + 0.16 * Math.sin(Math.PI * pkk))})`);   // a small kick as the slash lands
  q.rw.forEach((w, k) => maskIn(w, P(t, ea + 0.3 + k * 0.12, 0.62)));
  if (q.ns) { const sa = c.sub_at ?? (ea + 1.2);
    const pr = P(t, sa, 0.6); tf(q.nsr, pr >= 1, `scaleX(${f4(outExpo(pr))})`);
    const pt = P(t, sa + 0.08, 0.6); q.tile.style.opacity = f4(clamp(pt * 3)); tf(q.tile, pt >= 1, `scale(${f4(spring(pt))}) rotate(${f2((1 - outCubic(pt)) * -30)}deg)`);
    rise(q.st, P(t, sa + 0.16, 0.6), 26);
    x.sb.forEach((b, j) => { b.style.transform = `scaleX(${f4(outCubic(P(t, sa + 0.8 + j * 0.16, 0.4)))})`; });
    if (q.nsb) q.nsb.style.color = mixC('#6b6660', '#a59f97', outCubic(P(t, sa + 0.95, 0.4)));
  }
  // paired with a split card that shares the screen with it (> 0.5 s): it moves up and shrinks into a heading above the card
  const pe = x.pair ? outExpo(P(t, x.pair.at, 0.6)) : 0;
  cueRoot(x, t, { from: la, dy: x.pair ? x.pair.dy * pe : 0 });
  if (pe > 0) x.el.style.transform += ` scale(${f4(1 - (1 - x.pair.s) * pe)})`;
};

/* ======================= splitcard (scene 5b): relief vs cause of action ======================= */
BUILD.splitcard = (c) => {
  const L = c.left || {}, R = c.right || {};
  const half = (h, def) => `<div class="tile">${ico(h.icon || def)}</div><div class="ca-spt">${esc(typo(h.title))}</div><div class="ca-spx serif">${esc(typo(h.text))}</div>`;
  const el = mk(pcontent, 'cue ca-sp', `<div class="ca-spc" style="opacity:0"><div class="ca-sph ca-spl">${half(L, 'gavel')}</div><div class="ca-sph ca-spr"><div class="ca-spph"></div><div class="ca-spbg ca-acc" style="opacity:0"><div class="ca-sheen"></div></div><div class="ca-spin">${half(R, 'key-round')}</div></div></div>`);
  const l = $(el, '.ca-spl'), r = $(el, '.ca-spr');
  return { el, q: { card: $(el, '.ca-spc'), l: { tile: $(l, '.tile'), tt: $(l, '.ca-spt'), tx: $(l, '.ca-spx') },
    r: { el: r, ph: $(r, '.ca-spph'), bg: $(r, '.ca-spbg'), sh: $(r, '.ca-sheen'), tile: $(r, '.tile'), tt: $(r, '.ca-spt'), tx: $(r, '.ca-spx') } } };
};
LAYOUT.splitcard = (x) => {
  const A = areaFor(x.c), q = x.q, H2 = [q.l, q.r];
  H2.forEach(H => { fitLines(H.tx, 56, 3, 44); fitFont(H.tt, () => H.tt.scrollWidth <= H.tt.clientWidth + 1, 18, 1); });
  const mn = Math.min(...H2.map(H => fsOf(H.tx))); H2.forEach(H => { H.tx.style.fontSize = mn + 'px'; });
  x.rw = q.r.el.offsetWidth;
  const hS = x.el.offsetHeight;
  // a "left ≠ right" line still on screen with the card (the plan keeps it > 0.5 s): it becomes the heading, the card sits under it
  const ne = x.c.y == null ? EL.find(y => y.c.type === 'notequal' && y.top != null && overlaps(y.c, x.c, 0.5)) : null;
  if (ne) {
    const B = areaFor(ne.c), top = Math.max(A.top, B.top), bottom = Math.min(A.bottom, B.bottom), hN = ne.el.offsetHeight, gap = 44;
    const s = clamp((bottom - top - hS - gap) / hN, 0.5, 0.72), top0 = centerTop({ top, bottom }, hN * s + gap + hS, -10);
    ne.pair = { at: ((x.c.left || {}).at ?? x.c.t0) - 0.12, dy: top0 - ne.top, s };
    x.el.style.top = (top0 + hN * s + gap) + 'px';
  } else x.el.style.top = (x.c.y ?? centerTop(A, hS, -10)) + 'px';
};
SEEK.splitcard = (x, t) => {
  const c = x.c, q = x.q, la = (c.left || {}).at ?? c.t0, ra = (c.right || {}).at ?? la + 1.5;
  // the card arrives with its left half; the right half waits as a dashed outline
  const p = P(t, la, 0.6);
  q.card.style.opacity = f4(clamp(p * 2.5));
  tf(q.card, p >= 1, `translate(${f2(away((1 - outExpo(p)) * 60))}px,${f2((1 - outExpo(p)) * 30)}px) scale(${f4(0.95 + 0.05 * outBack(p))})`);
  const L = q.l, pl = P(t, la + 0.1, 0.6);
  tf(L.tile, pl >= 1, `scale(${f4(spring(pl))}) rotate(${f2((1 - outCubic(pl)) * -30)}deg)`);
  wipeIn(L.tt, outCubic(P(t, la + 0.16, 0.5)));
  rise(L.tx, P(t, la + 0.24, 0.6), 30);
  // at right.at the accent floods the right half outwards from the split line, then its words land
  const R = q.r, pr = P(t, ra, 0.6), er = outExpo(pr);
  R.bg.style.opacity = pr > 0 ? '1' : '0'; R.bg.style.clipPath = pr >= 1 ? 'none' : `inset(0 ${f2((1 - er) * 100)}% 0 0)`;
  R.ph.style.opacity = f4(1 - clamp(pr * 2.5));
  const pt = P(t, ra + 0.12, 0.6); R.tile.style.opacity = f4(clamp(pt * 3)); tf(R.tile, pt >= 1, `scale(${f4(spring(pt))}) rotate(${f2((1 - outCubic(pt)) * -30)}deg)`);
  R.tt.style.opacity = pr > 0 ? '1' : '0'; wipeIn(R.tt, outCubic(P(t, ra + 0.18, 0.5)));
  rise(R.tx, P(t, ra + 0.26, 0.6), 30);
  sheenPose(R.sh, P(t, ra + 0.55, 0.8), x.rw);
  cueRoot(x, t, { from: la });
};
})();
