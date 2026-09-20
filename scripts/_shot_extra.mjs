import { chromium, chromiumExecutable } from './playwright_env.mjs';
import { readFileSync, writeFileSync } from 'fs';
import { join, resolve } from 'path';
const ep = resolve('episodes/ep-1974-super-outbreak');
const raw = readFileSync(join(ep, 'compositions', 'g-radar-a3.html'), 'utf-8');
const body = raw.match(/<template>([\s\S]*?)<\/template>/)[1];
const html = `<!doctype html><html><head><meta charset="UTF-8"><script src="../gsap.min.js"></script></head><body style="margin:0;background:#000">${body}</body></html>`;
const tmp = join(ep, 'compositions', '_shot_extra.html');
writeFileSync(tmp, html);
const browser = await chromium.launch({ executablePath: chromiumExecutable() });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
await page.goto('file:///' + tmp.split('\\').join('/'), { waitUntil: 'load' });
for (const t of [9.4, 21.06, 33.5, 37.5]) {
  await page.evaluate((tt) => { const k = Object.keys(window.__timelines)[0]; window.__timelines[k].seek(tt, false); }, t);
  await page.screenshot({ path: join(ep, '_compshots', 'g-radar-a3-extra@' + t + '.png') });
}
await browser.close();
console.log('extra shots done');
