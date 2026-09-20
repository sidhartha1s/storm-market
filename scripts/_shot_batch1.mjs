// One-off: screenshot batch-1 comps at chosen beat times (verify-the-artifact gate).
// Scratch script per mg_briefs.md contract — lives in scripts/ only so the relative
// `../gsap.min.js` import in the staged page resolves the same way _shot_comps.mjs does.
import { chromium, chromiumExecutable } from './playwright_env.mjs';
import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'fs';
import { join, resolve } from 'path';
const ep = resolve(process.argv[2]);
const OUT = join(ep, '_compshots');
if (!existsSync(OUT)) mkdirSync(OUT, { recursive: true });
const plan = {
  'g-scale-hook': [0, 0.5, 1.0, 2.3, 2.9, 3.9],
  'g-scale-a1':   [0, 0.3, 0.5, 2, 4, 5.9],
  'g-scale-a2':   [0, 0.3, 0.5, 2, 4, 5.9],
  'g-scale-a4':   [0, 0.4, 1, 4.3, 5, 7.9],
  'g-radar-hook': [0, 0.3, 0.6, 1.5, 3, 4.9],
  'g-radar-a3':   [0, 4.68, 8.94, 15.06, 32.56, 38.5],
  'g-f6':         [0, 3, 6.84, 11.48, 12.5, 14.3],
  'g-campus':     [0, 5, 12.2, 14.88, 17.26, 27.3],
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
