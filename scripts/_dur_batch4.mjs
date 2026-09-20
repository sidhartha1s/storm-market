// One-off: report tl.duration() for each batch-4 composition (scratch, per-instance use only).
import { chromium, chromiumExecutable } from './playwright_env.mjs';
import { readFileSync, writeFileSync } from 'fs';
import { join, resolve } from 'path';
const ep = resolve(process.argv[2]);
const comps = ['g-f4f5','g-engine','g-combed','g-legacy','g-thennow-16-4','g-thennow-cols','g-thennow-rooms'];
const browser = await chromium.launch({ executablePath: chromiumExecutable() });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
const results = {};
for (const comp of comps) {
  const raw = readFileSync(join(ep, 'compositions', comp + '.html'), 'utf-8');
  const body = raw.match(/<template>([\s\S]*?)<\/template>/)[1];
  const html = `<!doctype html><html><head><meta charset="UTF-8">
<script src="../gsap.min.js"></script></head><body style="margin:0;background:#000">${body}</body></html>`;
  const tmp = join(ep, 'compositions', '_dur_' + comp + '.html');
  writeFileSync(tmp, html);
  await page.goto('file:///' + tmp.split('\\').join('/'), { waitUntil: 'load' });
  const dur = await page.evaluate(() => {
    const k = Object.keys(window.__timelines)[0];
    return window.__timelines[k].duration();
  });
  results[comp] = dur;
}
await browser.close();
console.log(JSON.stringify(results, null, 2));
