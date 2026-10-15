/**
 * Render the overlay page to a transparent PNG sequence, one frame per video frame.
 *   tsx render_overlays.ts --timeline <timeline.json> --out <dir> [--html page.html] [--fps 24] [--preview <t,t,t>]
 *                          [--from N] [--to M]
 * Deterministic: every frame is produced by seeking the page to its exact time (no CSS animations).
 * --from N --to M: render only frames N..M (inclusive, frame numbers of the whole timeline; files keep their names
 * f%05d.png), so several renderers can share one timeline (split/render_parallel.sh). Either may be left out (default: from
 * frame 0 / to the last frame). The older --from-frame A --to-frame B (B exclusive) still work. Without a range the output
 * and the log are as before. A range first replays (screenshots, not written) the builds of the cues on screen at its start
 * and the second before it (see "Warm-up" below), so its frames match a sequential render's within 6/255 (not byte for byte).
 */
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';

const args = process.argv.slice(2);
const arg = (k: string, d?: string) => { const i = args.indexOf(k); return i >= 0 ? args[i + 1] : d; };
const tlPath = path.resolve(arg('--timeline')!);
const out = path.resolve(arg('--out')!);
const fps = Number(arg('--fps', '24'));
const preview = arg('--preview');
const tl = JSON.parse(fs.readFileSync(tlPath, 'utf8'));
const html = path.resolve(arg('--html', path.resolve(__dirname, '..', 'overlays', 'overlay.html'))!);
fs.mkdirSync(out, { recursive: true });

(async () => {
  const cached = '/Users/admin/Library/Caches/ms-playwright/chromium-1223/chrome-mac/Chromium.app/Contents/MacOS/Chromium';
  // Playwright 1.62 wants a browser build that is not on this Mac; use installed Chrome headless, else the cached Chromium.
  const browser = await chromium.launch({ headless: true, channel: 'chrome' }).catch(async (e) => {
    console.warn('[overlay] Chrome channel failed, falling back to cached Chromium:', String(e).split('\n')[0]);
    return chromium.launch({ headless: true, executablePath: cached });
  });
  const page = await browser.newPage({ viewport: { width: tl.width ?? 1080, height: tl.height ?? 1920 }, deviceScaleFactor: 1 });
  await page.goto('file://' + html);
  await page.evaluate(() => document.fonts.ready);
  const n = await page.evaluate((t) => (window as any).__init(t), tl);
  console.log(`[overlay] ${n} elements, duration ${tl.duration}s @ ${fps}fps`);
  if (preview) {
    for (const ts of preview.split(',')) {
      const t = Number(ts);
      await page.evaluate((t) => (window as any).__seek(t), t);
      const f = path.join(out, `preview_${t.toFixed(2)}.png`);
      await page.screenshot({ path: f, omitBackground: true, type: 'png' });
      console.log('[overlay] preview', f);
    }
    await browser.close(); return;
  }
  const total = Math.ceil(tl.duration * fps);
  const fromA = arg('--from'), toA = arg('--to'); const ranged = fromA !== undefined || toA !== undefined;
  const fromF = Number(fromA ?? arg('--from-frame', '0'));
  const toF = toA !== undefined ? Number(toA) + 1 : Number(arg('--to-frame', String(total)));   // exclusive end
  if (ranged && (!Number.isInteger(fromF) || !Number.isInteger(toF) || fromF < 0 || toF <= fromF)) {
    console.error(`[overlay] bad frame range: --from ${fromA ?? '(0)'} --to ${toA ?? '(last)'} (inclusive frame numbers, from <= to)`);
    await browser.close(); process.exit(2);
  }
  if (ranged && fromF >= total) console.warn(`[overlay] range starts at frame ${fromF}, past the last frame ${total - 1}: nothing to render`);
  if (ranged && fromF < total) {
    // Warm-up (screenshots taken, nothing written): the first 48 frames (the build) of every cue on screen at the range start
    // and the 24 frames before it, in time order; at frame 0 one screenshot of frame 0. Chrome keeps the raster scale a
    // will-change:transform layer reached while it animated, so a renderer that starts in the middle of a cue drew it
    // differently from a sequential render (measured on the coa page: up to 65/255 on the sting wordmark for ~18 frames, up
    // to 122/255 on a few stamp pixels for 70 frames; 3 concurrent renderers also differed from frame 0 on). With this
    // warm-up ranges matched the sequential frames within 6/255 (mostly <= 2, like two sequential runs); not byte for byte.
    const tf = fromF / fps;
    const firsts = (tl.cues || []).filter((c: any) => c.t0 <= tf && tf <= c.t1 + 1).map((c: any) => Math.max(0, Math.ceil(c.t0 * fps - 1e-9)));
    const warm = [...new Set([...firsts.flatMap((s: number) => Array.from({ length: Math.max(0, Math.min(48, fromF - s)) }, (_, k) => s + k)),
      ...Array.from({ length: Math.min(24, fromF) }, (_, k) => fromF - Math.min(24, fromF) + k)])].sort((a, b) => a - b);
    if (!warm.length) warm.push(fromF);
    for (const f of warm) { await page.evaluate((t) => (window as any).__seek(t), f / fps); await page.screenshot({ omitBackground: true, type: 'png' }); }
    console.log(`[overlay] warm-up: ${warm.length} frames before frame ${fromF} (builds of the cues on screen + the last second)`);
  }
  let blank: Buffer | null = null; let drawn = 0;
  const t0 = Date.now();
  for (let i = fromF; i < Math.min(total, toF); i++) {
    const t = i / fps;
    const f = path.join(out, `f${String(i).padStart(5, '0')}.png`);
    const active = await page.evaluate((t) => (window as any).__seek(t), t);
    if (active) { await page.screenshot({ path: f, omitBackground: true, type: 'png' }); drawn++; }
    else {
      if (!blank) { await page.evaluate(() => (window as any).__seek(-1)); blank = await page.screenshot({ omitBackground: true, type: 'png' }); }
      fs.writeFileSync(f, blank);
    }
    if (i % 120 === 0) console.log(`[overlay] ${i}/${total} (${((Date.now() - t0) / 1000).toFixed(0)}s)`);
  }
  const end = Math.min(total, toF);
  if (ranged) console.log(`[overlay] done: range ${fromF}-${end - 1} of ${total}: ${Math.max(0, end - fromF)} frames, ${drawn} drawn, ${((Date.now() - t0) / 1000).toFixed(0)}s`);
  else console.log(`[overlay] done: ${total} frames, ${drawn} drawn, ${((Date.now() - t0) / 1000).toFixed(0)}s`);
  await browser.close();
})();
