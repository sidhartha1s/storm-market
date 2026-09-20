import { chromium, chromiumExecutable } from './playwright_env.mjs';
import { readFileSync, writeFileSync } from 'fs';

const E = 'C:/Users/Sidhartha/Automation Projects/storm-market/.worktrees/ep-1974-super-outbreak/episodes/ep-1974-super-outbreak';

function rectsOverlap(a, b) {
  return !(a.right <= b.left || a.left >= b.right || a.bottom <= b.top || a.top >= b.bottom);
}

async function check(browser, name, checks) {
  const raw = readFileSync(`${E}/compositions/${name}.html`, 'utf-8');
  const body = raw.match(/<template>([\s\S]*?)<\/template>/)[1];
  const html = `<!doctype html><html><head><meta charset="UTF-8"><script src="../gsap.min.js"></script></head><body style="margin:0;background:#000">${body}</body></html>`;
  const tmpFile = `${E}/compositions/_debug_ov_${name}.html`;
  writeFileSync(tmpFile, html);
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  await page.goto('file:///' + tmpFile.split('\\').join('/'), { waitUntil: 'load' });
  const res = await page.evaluate(([name, checks]) => {
    const tl = window.__timelines[name];
    const root = document.querySelector('#root').getBoundingClientRect();
    const out = [];
    for (const { t, a, b, label } of checks) {
      tl.seek(t, false);
      const ea = document.querySelector(a), eb = document.querySelector(b);
      if (!ea || !eb) { out.push({ label, t, missing: true }); continue; }
      const ra = ea.getBoundingClientRect(), rb = eb.getBoundingClientRect();
      const rectA = { left: ra.left - root.left, top: ra.top - root.top, right: ra.right - root.left, bottom: ra.bottom - root.top };
      const rectB = { left: rb.left - root.left, top: rb.top - root.top, right: rb.right - root.left, bottom: rb.bottom - root.top };
      const overlap = !(rectA.right <= rectB.left || rectA.left >= rectB.right || rectA.bottom <= rectB.top || rectA.top >= rectB.bottom);
      out.push({ label, t, overlap, aVis: getComputedStyle(ea).opacity, bVis: getComputedStyle(eb).opacity, rectA, rectB });
    }
    return out;
  }, [name, checks]);
  await page.close();
  return res;
}

const browser = await chromium.launch({ executablePath: chromiumExecutable() });
const results = {};

results['g-map-i'] = await check(browser, 'g-map-i', [
  { label: 'eb1 x hl1 @1', t: 1, a: '#g-map-i-eb1', b: '#g-map-i-hl1' },
  { label: 'eb1 x hl1 @20', t: 20, a: '#g-map-i-eb1', b: '#g-map-i-hl1' },
]);
results['g-map-a1'] = await check(browser, 'g-map-a1', [
  { label: 'eb x hl1 @5', t: 5, a: '#g-map-a1-eb', b: '#g-map-a1-hl1' },
  { label: 'eb x hl2 @40', t: 40, a: '#g-map-a1-eb', b: '#g-map-a1-hl2' },
  { label: 'eb x hl3 @65', t: 65, a: '#g-map-a1-eb', b: '#g-map-a1-hl3' },
]);
results['g-map-a3'] = await check(browser, 'g-map-a3', [
  { label: 'eb x hl1 @5', t: 5, a: '#g-map-a3-eb', b: '#g-map-a3-hl1' },
  { label: 'eb x hl2 @50', t: 50, a: '#g-map-a3-eb', b: '#g-map-a3-hl2' },
  { label: 'eb x hl3 @90', t: 90, a: '#g-map-a3-eb', b: '#g-map-a3-hl3' },
]);
results['g-map-a6'] = await check(browser, 'g-map-a6', [
  { label: 'eb x hl @2', t: 2, a: '#g-map-a6-eb', b: '#g-map-a6-hl' },
  { label: 'eb x hl @20', t: 20, a: '#g-map-a6-eb', b: '#g-map-a6-hl' },
]);
results['g-plane'] = await check(browser, 'g-plane', [
  { label: 'eb x hl @2', t: 2, a: '#g-plane-eb', b: '#g-plane-hl' },
  { label: 'r2 x ft @26', t: 26, a: '#g-plane-r2', b: '#g-plane-ft' },
]);
results['g-map-a4-labels-during-zoom'] = await check(browser, 'g-map-a4', [
  { label: 'stlabels opacity @2', t: 2, a: '#g-map-a4-stlabels', b: '#g-map-a4-stlabels' },
  { label: 'stlabels opacity @68', t: 68, a: '#g-map-a4-stlabels', b: '#g-map-a4-stlabels' },
]);
results['g-map-a6-labels'] = await check(browser, 'g-map-a6', [
  { label: 'stlabels opacity @2', t: 2, a: '#g-map-a6-stlabels', b: '#g-map-a6-stlabels' },
]);

await browser.close();
console.log(JSON.stringify(results, null, 2));
