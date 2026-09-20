import { chromium, chromiumExecutable } from './playwright_env.mjs';
import { readFileSync, writeFileSync } from 'fs';

const E = 'C:/Users/Sidhartha/Automation Projects/storm-market/.worktrees/ep-1974-super-outbreak/episodes/ep-1974-super-outbreak';
const raw = readFileSync(E + '/compositions/g-map-a6.html', 'utf-8');
const body = raw.match(/<template>([\s\S]*?)<\/template>/)[1];
const html = `<!doctype html><html><head><meta charset="UTF-8"><script src="../gsap.min.js"></script></head><body style="margin:0;background:#000">${body}</body></html>`;
writeFileSync(E + '/compositions/_debug_mat.html', html);

const browser = await chromium.launch({ executablePath: chromiumExecutable() });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
await page.goto('file:///' + (E + '/compositions/_debug_mat.html').split('\\').join('/'), { waitUntil: 'load' });
const r = await page.evaluate(() => {
  const tl = window.__timelines['g-map-a6'];
  tl.seek(0.02, false);
  const mg = document.getElementById('g-map-a6-mapgroup');
  const cs = getComputedStyle(mg);
  const wv = [...document.querySelectorAll('.stlab')].find(e => e.textContent === 'WV');
  const root = document.querySelector('#root').getBoundingClientRect();
  const wr = wv.getBoundingClientRect();
  return { transform: cs.transform, attrTransform: mg.getAttribute('transform'), wv_left: wr.left - root.left, wv_top: wr.top - root.top };
});
console.log(JSON.stringify(r, null, 2));
await browser.close();
