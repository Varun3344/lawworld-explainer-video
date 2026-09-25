/** Zero-credit inspection of Flow's new composer: open the project, open the settings popup, dump controls. */
import fs from 'fs';
import path from 'path';
import { BrowserManager } from '/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/services/reel-service/pipeline/browser';

const OUT = '/Users/admin/Downloads/New short/product-explainer/logs/inspect';
fs.mkdirSync(OUT, { recursive: true });
const PROJECT = process.argv[2] || 'https://flow.google.com/project/3c52f891-7d38-425c-a11d-067d3f580b0f';
const shot = async (page: any, name: string) => { await page.screenshot({ path: path.join(OUT, name + '.png') }); console.log('[shot]', name); };
const DUMP_JS = `(() => {
  const vis = (e) => { const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0; };
  const out = [];
  for (const e of Array.from(document.querySelectorAll('button,[role="option"],[role="radio"],[role="menuitem"],[role="tab"],[role="switch"],[role="menuitemradio"],li,input,textarea,[contenteditable="true"]'))) {
    if (!vis(e)) continue;
    const r = e.getBoundingClientRect();
    const t = (e.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 70);
    const al = e.getAttribute('aria-label') || ''; const ac = e.getAttribute('aria-checked') || e.getAttribute('aria-selected') || e.getAttribute('aria-pressed') || '';
    const role = e.getAttribute('role') || e.tagName.toLowerCase();
    const ph = e.getAttribute('placeholder') || e.getAttribute('data-placeholder') || ''; if (!t && !al && !ph) continue;
    out.push(role.padEnd(14) + ' @' + Math.round(r.x) + ',' + Math.round(r.y) + ' ' + Math.round(r.width) + 'x' + Math.round(r.height) + ' ' + (ac ? '[' + ac + '] ' : '') + (al ? 'aria="' + al + '" ' : '') + (ph ? 'ph="' + ph + '" ' : '') + '"' + t + '"');
  }
  return out;
})()`;
const dump = async (page: any, label: string) => {
  const rows: string[] = await page.evaluate(DUMP_JS);
  console.log(`\n===== ${label} (${rows.length}) =====`); rows.forEach((r) => console.log(r));
};
(async () => {
  const bm = new BrowserManager({ userDataDir: '/Users/admin/Downloads/New short/Google Flow AI Video/user_data', headless: false });
  const { page } = await bm.init();
  await page.goto(PROJECT, { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(7000);
  await shot(page, '01_project');
  await dump(page, 'initial controls');
  // settings trigger
  const trig = page.locator('button[aria-label="Settings"]').last();
  console.log('\nSettings trigger count:', await trig.count());
  if (await trig.count()) { await trig.click({ timeout: 5000 }).catch(e => console.log('click failed', e.message)); await page.waitForTimeout(1500); await shot(page, '02_settings_open'); await dump(page, 'after settings click'); }
  const modelBtn = page.locator('button', { hasText: /veo|omni|nano|model/i }).last();
  console.log('\nmodel-like buttons:', await page.locator('button', { hasText: /veo|omni|nano|model/i }).count());
  if (await modelBtn.count()) { await modelBtn.click({ timeout: 5000 }).catch(e => console.log('model click failed', e.message)); await page.waitForTimeout(1200); await shot(page, '03_model_menu'); await dump(page, 'model menu'); await page.keyboard.press('Escape').catch(() => {}); await page.waitForTimeout(600); }
  // model family button?
  const mf = page.locator('button[aria-label="Select model family"]').first();
  console.log('\nModel family button count:', await mf.count());
  if (await mf.count()) { await mf.click({ timeout: 5000 }).catch(() => {}); await page.waitForTimeout(1200); await shot(page, '03_model_menu'); await dump(page, 'model menu'); await page.keyboard.press('Escape').catch(() => {}); await page.waitForTimeout(500); }
  await page.keyboard.press('Escape').catch(() => {});
  await page.waitForTimeout(500);
  await shot(page, '04_end');
  await bm.close();
})().catch(async e => { console.error('inspect failed:', e); try { const { execSync } = require('child_process'); execSync(`pkill -f "user-data-dir=/Users/admin/Downloads/New short/Google Flow AI Video/user_data"`); } catch {} process.exit(1); });
