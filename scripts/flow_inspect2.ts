/** Zero-credit: close the session panel and see what composer remains; open the ingredients menu; dump controls. */
import fs from 'fs'; import path from 'path';
import { BrowserManager } from '/Users/admin/Desktop/lawworld project/lw-plateform-node-backend/services/reel-service/pipeline/browser';
const OUT = '/Users/admin/Downloads/New short/product-explainer/logs/inspect'; fs.mkdirSync(OUT, { recursive: true });
const PROJECT = 'https://flow.google.com/project/3c52f891-7d38-425c-a11d-067d3f580b0f';
const DUMP_JS = `(() => { const vis=(e)=>{const r=e.getBoundingClientRect();return r.width>0&&r.height>0;}; const out=[];
 for (const e of Array.from(document.querySelectorAll('button,[role="option"],[role="radio"],[role="menuitem"],[role="tab"],[role="switch"],[role="menuitemradio"],li,input,textarea,[contenteditable="true"]'))) {
  if(!vis(e)) continue; const r=e.getBoundingClientRect(); const t=(e.textContent||'').replace(/\\s+/g,' ').trim().slice(0,70);
  const al=e.getAttribute('aria-label')||''; const ac=e.getAttribute('aria-checked')||e.getAttribute('aria-selected')||e.getAttribute('aria-pressed')||'';
  const ph=e.getAttribute('placeholder')||e.getAttribute('data-placeholder')||''; const role=e.getAttribute('role')||e.tagName.toLowerCase();
  if(!t&&!al&&!ph) continue; out.push(role.padEnd(14)+' @'+Math.round(r.x)+','+Math.round(r.y)+' '+Math.round(r.width)+'x'+Math.round(r.height)+' '+(ac?'['+ac+'] ':'')+(al?'aria="'+al+'" ':'')+(ph?'ph="'+ph+'" ':'')+'"'+t+'"'); }
 return out; })()`;
const shot = async (p: any, n: string) => { await p.screenshot({ path: path.join(OUT, n + '.png') }); console.log('[shot]', n); };
const dump = async (p: any, l: string) => { const rows: string[] = await p.evaluate(DUMP_JS); console.log(`\n===== ${l} (${rows.length}) =====`); rows.forEach(r => console.log(r)); };
(async () => {
  const bm = new BrowserManager({ userDataDir: '/Users/admin/Downloads/New short/Google Flow AI Video/user_data', headless: false });
  const { page } = await bm.init();
  await page.goto(PROJECT, { waitUntil: 'domcontentloaded' }); await page.waitForTimeout(6000);
  const close = page.locator('button[aria-label="Close"]').first();
  console.log('Close buttons:', await page.locator('button[aria-label="Close"]').count());
  if (await close.count()) { await close.click({ timeout: 5000 }).catch(e => console.log('close failed', e.message)); await page.waitForTimeout(2500); }
  await shot(page, '11_panel_closed');
  // turn the Agent toggle OFF (direct generation mode)
  const agent = page.locator('button', { hasText: /^Agent$/ }).first();
  console.log('Agent chip count:', await agent.count(), 'pressed:', await agent.getAttribute('aria-pressed').catch(()=>null));
  if (await agent.count()) { await agent.click({ timeout: 5000 }).catch(e => console.log('agent click failed', e.message)); await page.waitForTimeout(2000); }
  await shot(page, '13_agent_off'); await dump(page, 'agent off');
  const tune = page.locator('button[aria-label="Settings"]').last();
  if (await tune.count()) { await tune.click({ timeout: 5000 }).catch(e => console.log('tune click failed', e.message)); await page.waitForTimeout(1500); }
  await shot(page, '14_settings_direct'); await dump(page, 'direct settings popup');
  const mfam = page.locator('button[aria-label="Select model family"]').first();
  console.log('Select model family count:', await mfam.count());
  if (await mfam.count()) { await mfam.click({ timeout: 4000 }).catch(()=>{}); await page.waitForTimeout(1200); await shot(page, '15_model_menu'); await dump(page, 'model menu (direct)'); await page.keyboard.press('Escape'); await page.waitForTimeout(500); }
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  // any prompt/textarea anywhere, including hidden ones
  const tas: string[] = await page.evaluate(`Array.from(document.querySelectorAll('textarea,[contenteditable="true"],[role="textbox"]')).map(e=>{const r=e.getBoundingClientRect();return e.tagName+' @'+Math.round(r.x)+','+Math.round(r.y)+' '+Math.round(r.width)+'x'+Math.round(r.height)+' ph="'+(e.getAttribute('placeholder')||e.getAttribute('data-placeholder')||'')+'" aria="'+(e.getAttribute('aria-label')||'')+'"';})`);
  console.log('\n--- textboxes (incl. hidden) ---'); tas.forEach(t => console.log(t));
  const trig: string[] = await page.evaluate(`Array.from(document.querySelectorAll('button')).filter(b=>/settings|trigger|tune|model|Video|720p|1080p|\\ds\\b/i.test((b.getAttribute('aria-label')||'')+' '+b.textContent)).map(b=>{const r=b.getBoundingClientRect();return (r.width>0?'VIS ':'hid ')+'aria="'+(b.getAttribute('aria-label')||'')+'" text="'+(b.textContent||'').replace(/\\s+/g,' ').trim().slice(0,60)+'" @'+Math.round(r.x)+','+Math.round(r.y);})`);
  console.log('\n--- settings-like buttons ---'); trig.forEach(t => console.log(t));
  await page.waitForTimeout(500); await shot(page, '12_end'); await bm.close();
})().catch(async e => { console.error('inspect failed:', e); try { require('child_process').execSync(`pkill -f "user-data-dir=/Users/admin/Downloads/New short/Google Flow AI Video/user_data"`); } catch {} process.exit(1); });
