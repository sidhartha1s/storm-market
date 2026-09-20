import { chromium, chromiumExecutable } from './playwright_env.mjs';
import { readFileSync, writeFileSync } from 'fs';

const E = 'C:/Users/Sidhartha/Automation Projects/storm-market/.worktrees/ep-1974-super-outbreak/episodes/ep-1974-super-outbreak';
const raw = readFileSync(E + '/compositions/g-map-a4.html', 'utf-8');
const body = raw.match(/<template>([\s\S]*?)<\/template>/)[1];
const html = `<!doctype html><html><head><meta charset="UTF-8"><script src="../gsap.min.js"></script></head><body style="margin:0;background:#000">${body}</body></html>`;
writeFileSync(E + '/compositions/_debug_a4labels.html', html);

const browser = await chromium.launch({ executablePath: chromiumExecutable() });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
await page.goto('file:///' + (E + '/compositions/_debug_a4labels.html').split('\\').join('/'), { waitUntil: 'load' });
const times = [0.02, 0.5, 1, 1.5, 2, 2.5, 65.0, 65.5, 66.0, 66.3, 66.6, 66.9, 67.2, 67.5, 67.9];
const out = await page.evaluate((times) => {
  const tl = window.__timelines['g-map-a4'];
  const root = document.querySelector('#root').getBoundingClientRect();
  const rail = { left: 1270, top: 100, right: 1850, bottom: 300 }; // eyebrow+hl box, generous
  const frame = { left: 0, top: 0, right: 1920, bottom: 1080 };
  const result = {};
  for (const t of times) {
    tl.seek(t, false);
    const labs = [...document.querySelectorAll('.stlab')].map(el => {
      const r = el.getBoundingClientRect();
      const rr = { left: r.left - root.left, top: r.top - root.top, right: r.right - root.left, bottom: r.bottom - root.top };
      const inRail = !(rr.right < rail.left || rr.left > rail.right || rr.bottom < rail.top || rr.top > rail.bottom);
      const outOfFrame = rr.right < frame.left || rr.left > frame.right || rr.bottom < frame.top || rr.top > frame.bottom;
      return { text: el.textContent, ...rr, inRail, outOfFrame };
    });
    result[t] = labs.filter(l => l.inRail || l.outOfFrame);
  }
  return result;
}, times);
console.log(JSON.stringify(out, null, 2));
await browser.close();
