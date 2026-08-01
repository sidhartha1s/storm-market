import { readFileSync, mkdirSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, chromiumExecutable } from '../../../scripts/playwright_env.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const gsapSrc = readFileSync(join(__dirname, '..', 'gsap.min.js'), 'utf8');
const id = 'g-efscale-v1';
const html = readFileSync(join(__dirname, id + '.html'), 'utf8');
const m = html.match(/<template>([\s\S]*)<\/template>/);
const scriptMatches = [...m[1].matchAll(/<script>([\s\S]*?)<\/script>/g)].map(s => s[1]);
const templateInner = m[1].replace(/<script>[\s\S]*?<\/script>/g, '');

const browser = await chromium.launch({ executablePath: chromiumExecutable() });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
page.on('pageerror', e => console.error('pageerror:', e.message));
await page.setContent('<!doctype html><html><head><meta charset="UTF-8"></head><body></body></html>');
await page.addScriptTag({ content: gsapSrc });
await page.evaluate((inner) => { document.body.innerHTML = inner; }, templateInner);
for (const s of scriptMatches) await page.addScriptTag({ content: s });

const dir = join(__dirname, 'media', '_snap', id + '_recheck');
mkdirSync(dir, { recursive: true });
for (const t of [65.12, 70, 75, 78, 81.3]) {
  await page.evaluate(({ id, t }) => { window.__timelines[id].seek(t, false); }, { id, t });
  await page.waitForTimeout(400);
  await page.screenshot({ path: join(dir, `${t}.png`) });
  console.log(`${t}s done`);
}
await browser.close();
