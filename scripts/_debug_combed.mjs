import { chromium, chromiumExecutable } from './playwright_env.mjs';
import { readFileSync, writeFileSync } from 'fs';
import { join, resolve } from 'path';
const ep = resolve(process.argv[2]);
const raw = readFileSync(join(ep, 'compositions', 'g-combed.html'), 'utf-8');
const body = raw.match(/<template>([\s\S]*?)<\/template>/)[1];
const html = `<!doctype html><html><head><meta charset="UTF-8">
<script src="../gsap.min.js"></script></head><body style="margin:0;background:#000">${body}</body></html>`;
const tmp = join(ep, 'compositions', '_debug_combed.html');
writeFileSync(tmp, html);
const browser = await chromium.launch({ executablePath: chromiumExecutable() });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
await page.goto('file:///' + tmp.split('\\').join('/'), { waitUntil: 'load' });
const info = await page.evaluate(() => {
  const panelL = document.getElementById('g-combed-panel-l');
  const trees = Array.from(panelL.querySelectorAll('.treemark'));
  const k = Object.keys(window.__timelines)[0];
  window.__timelines[k].seek(10, false);
  return trees.slice(0, 8).map(t => ({
    inlineTransform: t.style.transform,
    computed: getComputedStyle(t).transform
  }));
});
console.log(JSON.stringify(info, null, 2));
await browser.close();
