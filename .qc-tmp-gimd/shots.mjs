// Read-only frame + section-4 check rig for g-intro-map-dots (scratch, never committed).
import { readFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';
import { createHash } from 'node:crypto';
import { pathToFileURL } from 'node:url';
const R = 'C:/Users/Sidhartha/Automation Projects/storm-market/.worktrees/ep-joplin-2011';
const { chromium, chromiumExecutable } = await import(pathToFileURL(R + '/scripts/playwright_env.mjs'));
const { hostCss, stageComp } = await import(pathToFileURL(R + '/scripts/stage_comp.mjs'));
const ep = join(R, 'episodes/ep-joplin-2011');
const out = join(R, '.qc-tmp-gimd/png');
mkdirSync(out, { recursive: true });
const page0 = stageComp(ep, join(ep, 'compositions/g-intro-map-dots.html'), hostCss(readFileSync(join(ep, 'index.html'), 'utf8')), '_gimd_');
const browser = await chromium.launch({ executablePath: chromiumExecutable(), args: ['--allow-file-access-from-files', '--disable-gpu'] });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
const errs = [];
page.on('pageerror', e => errs.push(String(e)));
page.on('console', m => console.log('console:', m.text()));
const open = async () => { await page.goto(pathToFileURL(page0).href); console.log('errs', errs, await page.evaluate(() => typeof gsap + ' ' + Object.keys(window.__timelines || {}))); await page.waitForFunction(() => !!(window.__timelines && window.__timelines['g-intro-map-dots'])); };
const seek = (t) => page.evaluate(t => { window.__timelines['g-intro-map-dots'].seek(t, false); }, t);
const shot = async (t, name) => { await seek(t); return page.screenshot({ path: name ? join(out, name) : undefined }); };
const md5 = b => createHash('md5').update(b).digest('hex');
await open();
console.log('duration', await page.evaluate(() => window.__timelines['g-intro-map-dots'].duration()));
for (const t of [0, 0.042, 1.3, 2.3, 9.2, 11.6, 13.9, 15.7, 16.2]) await shot(t, `t${t.toFixed(2)}.png`);

if (process.env.ONLY_FRAMES) { await browser.close(); process.exit(0); }
// section 4 checks
const truth = await page.evaluate(() => {
  const tl = window.__timelines['g-intro-map-dots'];
  const res = {};
  const P = '#g-intro-map-dots-';
  const groups = [...document.querySelectorAll(P + 'dots > g[id]')];
  res.counts = Object.fromEntries(groups.map(g => [g.id.replace('g-intro-map-dots-', ''), g.querySelectorAll('.gimd-dot').length]));
  res.total = document.querySelectorAll(P + 'dots .gimd-dot').length;
  res.rings = document.querySelectorAll(P + 'outside .gimd-ring').length;
  const path = document.querySelector(P + 'path');
  const line = document.querySelector(P + 'below');
  const toLocal = (el, x, y) => { const p = new DOMPoint(x, y).matrixTransform(el.getScreenCTM().inverse()); return p; };
  const inPath = (x, y) => { const p = toLocal(path, x, y); return path.isPointInFill(new DOMPoint(p.x, p.y)); };
  tl.seek(16.2, false);
  const lineY = line.getBoundingClientRect().top + 1;
  res.dotsOutsidePath = 0; res.dotsOnOrUnderLine = 0;
  for (const c of document.querySelectorAll(P + 'dots .gimd-dot')) {
    const b = c.getBoundingClientRect(); const cx = b.x + b.width / 2, cy = b.y + b.height / 2;
    if (!inPath(cx, cy)) res.dotsOutsidePath++;
    if (b.bottom >= lineY - 1) res.dotsOnOrUnderLine++;
  }
  // labels: at their visible time, distance to every dot edge and whether any box corner/edge sample lies in the path
  const labelAt = { 'lab-homes': 1.3, 'lab-apts': 2.3, 'lab-out': 9.2, placed: 16.2, 'nosign-t1': 16.2, 'nosign-t2': 16.2, nosign: 16.2, 'below-lab': 16.2 };
  res.labels = {};
  for (const [id, t] of Object.entries(labelAt)) {
    tl.seek(t, false);
    const el = document.querySelector(P + id); const b = el.getBoundingClientRect();
    let minDot = 1e9;
    for (const c of document.querySelectorAll(P + 'dots .gimd-dot')) {
      if (+getComputedStyle(c).opacity < 0.05) continue;
      const d = c.getBoundingClientRect(); const cx = d.x + d.width / 2, cy = d.y + d.height / 2, r = d.width / 2;
      minDot = Math.min(minDot, Math.hypot(Math.max(b.left - cx, 0, cx - b.right), Math.max(b.top - cy, 0, cy - b.bottom)) - r);
    }
    let inP = 0;
    for (let i = 0; i <= 20; i++) for (let j = 0; j <= 4; j++) if (inPath(b.left + b.width * i / 20, b.top + b.height * j / 4)) inP++;
    res.labels[id] = { x: Math.round(b.left), y: Math.round(b.top), r: Math.round(b.right), b: Math.round(b.bottom), minDotEdge: Math.round(minDot), samplesInPath: inP, opacity: getComputedStyle(el).opacity };
  }
  // spoken labels never together
  res.labelsTogether = [];
  for (let t = 0; t < 16.28; t += 0.05) {
    tl.seek(t, false);
    const vis = ['lab-homes', 'lab-apts', 'lab-out'].filter(id => +getComputedStyle(document.querySelector(P + id)).opacity > 0.01 && getComputedStyle(document.querySelector(P + id)).visibility !== 'hidden');
    if (vis.length > 1) res.labelsTogether.push([t.toFixed(2), vis]);
  }
  // frame 0: no dot visible
  tl.seek(0, false);
  res.frame0VisibleDots = [...document.querySelectorAll(P + 'dots circle')].filter(c => +getComputedStyle(c).opacity > 0).length;
  tl.seek(16.2, false);
  res.rail = [...document.querySelectorAll('#g-intro-map-dots-rail > div')].map(d => d.textContent);
  // presenter corner: any visible text/box at x >= 1600 and y >= 680
  res.corner = [...document.querySelectorAll('#g-intro-map-dots-root text, #g-intro-map-dots-root div, #g-intro-map-dots-root circle')].filter(e => {
    const b = e.getBoundingClientRect(); return b.width && b.right > 1600 && b.bottom > 680 && +getComputedStyle(e).opacity > 0.01;
  }).map(e => e.id || e.className.baseVal || e.className);
  return res;
});
console.log(JSON.stringify(truth, null, 1));

// seek order: each cue second forward on a fresh page vs seek 0 -> past -> back
const cues = [0.9, 1.68, 8.48, 9.86, 11.98, 12.86, 15.06];
const fwd = {};
await open();
for (const t of cues) fwd[t] = md5(await shot(t + 0.2));
await open();
const bad = [];
for (const t of cues) { await shot(0); await shot(16.2); const h = md5(await shot(t + 0.2)); if (h !== fwd[t]) bad.push(t); }
console.log('seek-order mismatches', bad, 'page errors', errs);
await browser.close();
