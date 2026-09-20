// One-off: screenshot changed comps at chosen beat times (verify-the-artifact gate).
import { chromium, chromiumExecutable } from './playwright_env.mjs';
import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'fs';
import { join, resolve } from 'path';
const ep = resolve(process.argv[2]);
const OUT = join(ep, '_compshots');
if (!existsSync(OUT)) mkdirSync(OUT, { recursive: true });
const plan = {
  'g-map-i': [1, 11.5, 14, 47.5, 50, 75.2],
  'g-map-a1': [1, 4, 37.5, 44.6, 62, 85],
  'g-map-a2': [1, 3, 16.5, 19.9, 25],
  'g-map-a3': [1, 2.2, 31.5, 34, 35.9, 79, 115.2],
  'g-map-a4': [1, 9.5, 18, 22.6, 30, 67.5, 71, 78.2],
  'g-map-a6': [1, 4.5, 20, 44.2, 45.2],
  'g-plane': [1, 4, 11, 15.5, 21.5, 26.2],
};
const browser = await chromium.launch({ executablePath: chromiumExecutable() });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
for (const [comp, times] of Object.entries(plan)) {
  const raw = readFileSync(join(ep, 'compositions', comp + '.html'), 'utf-8');
  const body = raw.match(/<template>([\s\S]*?)<\/template>/)[1];
  const html = `<!doctype html><html><head><meta charset="UTF-8">
<script src="../gsap.min.js"></script></head><body style="margin:0;background:#000">${body}</body></html>`;
  const tmp = join(ep, 'compositions', '_shot_' + comp + '.html');
  writeFileSync(tmp, html);
  await page.goto('file:///' + tmp.split('\\').join('/'), { waitUntil: 'load' });
  for (const t of times) {
    await page.evaluate((tt) => { const k = Object.keys(window.__timelines)[0]; window.__timelines[k].seek(tt, false); }, t);
    await page.screenshot({ path: join(OUT, `${comp}@${t}.png`) });
  }
}
await browser.close();
console.log('shots done');
