import { chromium, chromiumExecutable } from './playwright_env.mjs';
import { readFileSync, writeFileSync } from 'fs';

const E = 'C:/Users/Sidhartha/Automation Projects/storm-market/.worktrees/ep-1974-super-outbreak/episodes/ep-1974-super-outbreak';
const raw = readFileSync(E + '/compositions/g-map-a4.html', 'utf-8');
const body = raw.match(/<template>([\s\S]*?)<\/template>/)[1];
const html = `<!doctype html><html><head><meta charset="UTF-8"><script src="../gsap.min.js"></script></head><body style="margin:0;background:#000">${body}</body></html>`;
writeFileSync(E + '/compositions/_debug_a4.html', html);

const browser = await chromium.launch({ executablePath: chromiumExecutable() });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
await page.goto('file:///' + (E + '/compositions/_debug_a4.html').split('\\').join('/'), { waitUntil: 'load' });
const info = await page.evaluate(() => {
  const k = Object.keys(window.__timelines)[0];
  const tl = window.__timelines[k];
  const children = tl.getChildren(true, true, false).map(t => ({ start: t.startTime(), dur: t.duration(), targets: (t.targets ? t.targets().map(x => x.id || x.tagName) : []) }));
  tl.seek(78.2, false);
  const hl2 = document.getElementById('g-map-a4-hl2');
  const cs = getComputedStyle(hl2);
  const last5 = children.slice(-5);
  return { key: k, dur: tl.duration(), hl2_transform: cs.transform, hl2_opacity: cs.opacity, last5 };
});
console.log(JSON.stringify(info, null, 2));
await browser.close();
