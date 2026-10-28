/* split_cues_judgment.js: cue types for judgment reels in the course (concept) format, owner 26-10-2026. Loaded after split_panel.html's
   main script; registers into BUILD / LAYOUT / SEEK like split_cues_course.js.
     bench  t0 t1 tag? judges[{name, photo, at}]
            The bench as official portraits (never AI, owner 26-10: a photo on every judge card): white frames tilted like the reel
            thumbnails, the name under each; every portrait pops in at its own `at` (the spoken "Honourable" before that judge). */
document.head.insertAdjacentHTML('beforeend', `<style>
  .bnc{left:var(--cl);width:var(--cw);display:flex;flex-direction:column;align-items:center;gap:34px;}
  .bnc .btag{font-weight:800;font-size:26px;letter-spacing:3.2px;color:var(--accent-deep);text-transform:uppercase;line-height:1;opacity:0;}
  .bnc .brow{display:flex;justify-content:center;gap:56px;}
  .bnc .bj{display:flex;flex-direction:column;align-items:center;gap:22px;opacity:0;}
  .bnc .bf{width:330px;height:420px;padding:14px;background:#fff;border-radius:6px;box-shadow:0 26px 60px rgba(60,40,25,.20),0 3px 8px rgba(60,40,25,.10);}
  .bnc .bf img{width:100%;height:100%;object-fit:cover;object-position:50% 18%;display:block;border-radius:2px;}
  .bnc .bn{font-size:44px;line-height:1.08;color:var(--ink);text-align:center;max-width:380px;text-wrap:balance;}
  /* three-judge benches (rcc, 28-10-2026): 3 x 358 px + gaps overflowed the 1068 px column in the 9:16 crop */
  .bnc .brow:has(> .bj:nth-child(3)){gap:28px;} .bnc .brow:has(> .bj:nth-child(3)) .bf{width:272px;height:346px;} .bnc .brow:has(> .bj:nth-child(3)) .bn{font-size:38px;max-width:328px;}
</style>`);

BUILD.bench = (c) => {
  const fig = (j) => `<div class="bj"><div class="bf"><img src="${esc(j.photo)}" decoding="sync" alt=""></div><div class="bn serif">${esc(j.name)}</div></div>`;
  const el = mk(pcontent, 'cue bnc', (c.tag ? `<div class="btag">${esc(c.tag)}</div>` : '') + `<div class="brow">${c.judges.map(fig).join('')}</div>`);
  return { el, q: { tag: $(el, '.btag'), figs: $$(el, '.bj') } };
};
LAYOUT.bench = (x) => { const A = areaFor(x.c); x.top = x.c.y ?? centerTop(A, x.el.offsetHeight, -10); x.el.style.top = x.top + 'px'; };
SEEK.bench = (x, t) => {
  const c = x.c, q = x.q;
  if (q.tag) rise(q.tag, P(t, c.t0 + 0.05, 0.5), 30);
  q.figs.forEach((f, i) => {
    const p = P(t, c.judges[i].at ?? c.t0, 0.62);
    f.style.opacity = f4(clamp(p * 2.5));
    f.style.transform = `translateY(${f2((1 - outExpo(p)) * 70)}px) rotate(${f2((i % 2 ? -1 : 1) * 2.5)}deg) scale(${f4(0.86 + 0.14 * outBack(p))})`;
  });
  cueRoot(x, t, { from: c.t0 });
};
