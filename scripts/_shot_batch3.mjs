// One-off: screenshot changed comps at chosen beat times (verify-the-artifact gate).
import { chromium, chromiumExecutable } from './playwright_env.mjs';
import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'fs';
import { join, resolve } from 'path';
const ep = resolve(process.argv[2]);
const OUT = join(ep, '_compshots');
if (!existsSync(OUT)) mkdirSync(OUT, { recursive: true });
const plan = {
  'g-person-pearson-hook': [0.1, 0.5, 1.5, 2.8],
  'g-person-pearson': [0.1, 1, 20, 45.5],
  'g-person-haley': [0.1, 1, 25, 50.2],
  'g-person-allen': [0.1, 1, 12, 24.2],
  'g-person-heath': [0.1, 1, 10, 20.6],
  'g-person-gilligan': [0.1, 1, 25, 49.3],
  'g-person-gilbert': [0.1, 1, 20, 39.3],
  'g-person-poole': [0.1, 1, 19, 38.0],
  'g-person-lindley': [0.1, 1, 7, 13.6],
  'g-person-todd': [0.1, 1, 6, 11.6],
  'g-person-mcguire': [0.1, 1, 14, 27.5],
  'g-person-pennington': [0.1, 1, 18, 35.7],
  'g-cite-warning': [0.1, 1, 4, 7.6],
  'g-cite-cvg': [0.1, 1, 4.5, 8.6],
  'g-cite-paper': [0.1, 1, 4, 7.6],
  'g-cite-tape': [0.1, 1, 6.5, 12.6],
  'g-outro': [0.3, 2, 4.8, 20.9],
};
const browser = await chromium.launch({ executablePath: chromiumExecutable() });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
for (const [comp, times] of Object.entries(plan)) {
  const raw = readFileSync(join(ep, 'compositions', comp + '.html'), 'utf-8');
  let body = raw.match(/<template>([\s\S]*?)<\/template>/)[1];
  // tmp file stays inside compositions/ (scope rule) — rewrite this batch's episode-root-relative
  // media="media/..." references (person photos, tape waveform) to ../media/... so they resolve.
  body = body.replace(/src="media\//g, 'src="../media/');
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
