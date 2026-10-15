/**
 * Render the overlay page to a transparent PNG sequence, one frame per video frame.
 *   tsx render_overlays.ts --timeline <timeline.json> --out <dir> [--fps 24] [--preview <t,t,t>]
 * Deterministic: every frame is produced by seeking the page to its exact time (no CSS animations).
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
  const fromF = Number(arg('--from-frame', '0')); const toF = Number(arg('--to-frame', String(total)));
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
  console.log(`[overlay] done: ${total} frames, ${drawn} drawn, ${((Date.now() - t0) / 1000).toFixed(0)}s`);
  await browser.close();
})();
