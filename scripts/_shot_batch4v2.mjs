// One-off: screenshot changed comps at chosen beat times (verify-the-artifact gate).
import { chromium, chromiumExecutable } from './playwright_env.mjs';
import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'fs';
import { join, resolve } from 'path';
const ep = resolve(process.argv[2]);
const OUT = join(ep, '_compshots');
if (!existsSync(OUT)) mkdirSync(OUT, { recursive: true });
const plan = {
  'g-f4f5': [0.5, 4.5, 7.5, 9.8, 12.5, 19],
  'g-engine': [1.5, 8, 13, 17.9, 18.5, 19.2, 22.7, 29.7, 33],
  'g-combed': [0.8, 3, 6.2, 9, 17.9, 21],
  'g-legacy': [0.8, 4.5, 6.1, 10.3, 13],
  'g-thennow-16-4': [0.3, 1, 4.1, 8.2, 13.9],
  'g-thennow-cols': [0.5, 9.5, 11.3, 16.8, 21, 34.7, 49.2],
  'g-thennow-rooms': [0.4, 0.9, 5.9, 6.3, 7.8, 13.5],
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
