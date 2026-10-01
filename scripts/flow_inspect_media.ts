/** Zero-credit: open a Flow project, click the newest clip tile, log every media-like network response and <video> src. */
import fs from 'fs';
import path from 'path';
import { BrowserManager } from '/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/services/reel-service/pipeline/browser';

const OUT = '/Users/admin/Downloads/New short/product-explainer/logs/inspect_media';
fs.mkdirSync(OUT, { recursive: true });
const PROJECT = process.argv[2] || 'https://flow.google.com/project/a8ade941-d76f-4dd7-bd4f-ea8d214bd0b2';
const shot = async (page: any, name: string) => { await page.screenshot({ path: path.join(OUT, name + '.png') }); console.log('[shot]', name); };
const TILES_JS = `(() => { const out = []; document.querySelectorAll('img, video').forEach(el => { const r = el.getBoundingClientRect(); if (r.width < 80 || r.height < 120 || r.y < 50) return; out.push({ tag: el.tagName, x: r.x, y: r.y, w: r.width, h: r.height, src: (el.currentSrc || el.src || '').slice(0, 140) }); }); return out.sort((a, b) => a.y - b.y || a.x - b.x); })()`;
const VIDEOS_JS = `(() => Array.from(document.querySelectorAll('video')).map(v => ({ src: (v.src || '').slice(0, 160), cur: (v.currentSrc || '').slice(0, 160), rs: v.readyState, dur: v.duration, w: v.videoWidth, h: v.videoHeight, srcs: Array.from(v.querySelectorAll('source')).map(s => (s.src || '').slice(0, 160)) })))()`;
const BTNS_JS = `(() => Array.from(document.querySelectorAll('button,[role="menuitem"],[role="option"],a')).filter(e => { const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0; }).map(e => { const r = e.getBoundingClientRect(); return (e.tagName + ' @' + Math.round(r.x) + ',' + Math.round(r.y) + ' ' + (e.getAttribute('aria-label') || '') + ' | ' + (e.textContent || '').replace(/\\s+/g, ' ').trim().slice(0, 50) + ' | ' + (e.getAttribute('href') || '').slice(0, 80)); }))()`;

(async () => {
  const bm = new BrowserManager({ userDataDir: '/Users/admin/Downloads/New short/Google Flow AI Video/user_data', headless: false });
  const { page } = await bm.init();
  const seen: string[] = [];
  page.on('response', (r: any) => {
    const url = r.url(); const ct = (r.headers()['content-type'] || '');
    if (/video|octet|mpegurl|dash|\.mp4|\.m3u8|\.mpd|\.webm|blob:|media|download/i.test(url + ' ' + ct) && !/\.js|\.css|image\/|font/i.test(ct + url)) {
      const line = `${r.status()} ${ct.slice(0, 40)} ${url.slice(0, 200)}`; seen.push(line); console.log('[net]', line);
    }
  });
  page.on('request', (q: any) => { const u = q.url(); if (/\.mp4|\.m3u8|\.mpd|videoplayback|flow-content|media/i.test(u)) console.log('[req]', q.method(), u.slice(0, 200)); });
  await page.goto(PROJECT, { waitUntil: 'domcontentloaded' });
  await page.waitForSelector('text=Loading...', { state: 'hidden', timeout: 90000 }).catch(() => {});
  await page.waitForTimeout(6000);
  await shot(page, '01_project');
  let tiles = await page.evaluate(TILES_JS);
  console.log('tiles:', JSON.stringify(tiles, null, 0));
  console.log('videos initial:', JSON.stringify(await page.evaluate(VIDEOS_JS)));
  if (!tiles.length) { console.log('no tiles'); await bm.close(); return; }
  const t = tiles[0];
  // hover
  await page.mouse.move(t.x + t.w / 2, t.y + t.h / 2); await page.waitForTimeout(3000);
  console.log('videos after hover:', JSON.stringify(await page.evaluate(VIDEOS_JS)));
  await shot(page, '02_hover');
  const hoverBtns: string[] = await page.evaluate(BTNS_JS);
  console.log('--- hover buttons inside tile ---'); hoverBtns.filter(b => { const m = b.match(/@(\d+),(\d+)/); return m && +m[1] >= t.x - 5 && +m[1] <= t.x + t.w + 5 && +m[2] >= t.y - 5 && +m[2] <= t.y + t.h + 5; }).forEach(b => console.log(b));
  // click tile -> detail view
  await page.mouse.click(t.x + t.w / 2, t.y + t.h / 2); await page.waitForTimeout(4000);
  await shot(page, '03_detail');
  console.log('videos after click:', JSON.stringify(await page.evaluate(VIDEOS_JS)));
  await page.evaluate(`Array.from(document.querySelectorAll('video')).forEach(v => { v.muted = true; v.play().catch(() => {}); })`);
  await page.waitForTimeout(4000);
  console.log('videos after play:', JSON.stringify(await page.evaluate(VIDEOS_JS)));
  console.log('--- detail view buttons ---'); ((await page.evaluate(BTNS_JS)) as string[]).forEach(b => console.log(b));
  await shot(page, '04_detail_played');
  // performance entries for media
  const perf: string[] = await page.evaluate(`performance.getEntriesByType('resource').map(e => e.initiatorType + ' ' + e.name.slice(0, 180)).filter(s => /video|media|mp4|m3u8|flow-content|googleusercontent|blob/i.test(s)).slice(-40)`);
  console.log('--- perf media entries ---'); perf.forEach(p => console.log(p));
  await page.keyboard.press('Escape'); await page.waitForTimeout(1000);
  // tile menu
  await page.mouse.move(t.x + t.w / 2, t.y + t.h / 2); await page.waitForTimeout(1500);
  const menuPt = await page.evaluate(`(() => { const r = ${JSON.stringify({ x: t.x, y: t.y, w: t.w, h: t.h })}; const btns = Array.from(document.querySelectorAll('button')).filter(b => /more_vert|more options/i.test((b.textContent || '') + ' ' + (b.getAttribute('aria-label') || ''))); for (const b of btns) { const rr = b.getBoundingClientRect(); if (rr.width > 0 && rr.x >= r.x - 5 && rr.x <= r.x + r.w + 5 && rr.y >= r.y - 5 && rr.y <= r.y + r.h + 5) return { x: rr.x + rr.width / 2, y: rr.y + rr.height / 2 }; } return null; })()`);
  console.log('menuPt', JSON.stringify(menuPt));
  if (menuPt) {
    await page.mouse.click(menuPt.x, menuPt.y); await page.waitForTimeout(1500); await shot(page, '05_menu');
    console.log('--- menu items ---'); ((await page.evaluate(BTNS_JS)) as string[]).filter(b => /download|save|export|copy/i.test(b)).forEach(b => console.log(b));
    const dl = await page.evaluate(`(() => { const els = Array.from(document.querySelectorAll('button,[role="menuitem"],[role="option"],li')); const el = els.find(e => /download/i.test((e.textContent || '').trim()) && e.getBoundingClientRect().width > 0); if (!el) return null; const r = el.getBoundingClientRect(); return { x: r.x + r.width / 2, y: r.y + r.height / 2 }; })()`);
    console.log('download item', JSON.stringify(dl));
    if (dl) {
      await page.mouse.move(dl.x, dl.y); await page.waitForTimeout(1200); await shot(page, '06_download_hover');
      console.log('--- submenu ---'); ((await page.evaluate(BTNS_JS)) as string[]).filter(b => /720|1080|original|gif|mp4|upscale|download/i.test(b)).forEach(b => console.log(b));
      const dlp = page.waitForEvent('download', { timeout: 20000 }).catch(() => null);
      await page.mouse.click(dl.x, dl.y); await page.waitForTimeout(1500); await shot(page, '07_download_clicked');
      const sub = await page.evaluate(`(() => { const els = Array.from(document.querySelectorAll('button,[role="menuitem"],[role="option"],li')); const el = els.find(e => /720p|original|1080|mp4/i.test((e.textContent || '').trim()) && e.getBoundingClientRect().width > 0); if (!el) return null; const r = el.getBoundingClientRect(); return { x: r.x + r.width / 2, y: r.y + r.height / 2, t: el.textContent.trim().slice(0, 40) }; })()`);
      console.log('submenu pick', JSON.stringify(sub));
      if (sub) { await page.mouse.click(sub.x, sub.y); }
      const d = await dlp;
      if (d) { const p = path.join(OUT, 'menu_download.mp4'); await d.saveAs(p); console.log('DOWNLOAD EVENT saved', p, fs.statSync(p).size); } else console.log('no download event');
      await page.waitForTimeout(3000); await shot(page, '08_after_download');
    }
  }
  console.log('--- all media-like responses ---'); seen.forEach(s => console.log(s));
  await bm.close();
})().catch(async e => { console.error('inspect failed:', e); try { const { execSync } = require('child_process'); execSync(`pkill -f "user-data-dir=/Users/admin/Downloads/New short/Google Flow AI Video/user_data"`); } catch {} process.exit(1); });
