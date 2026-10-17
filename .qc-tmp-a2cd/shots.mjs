// Read-only frame + section-4 check rig for g-a2-countdown (scratch, never committed).
// freeze_scan cannot stage the episode while other comps (g-intro-161) are unbuilt, so this stages the comp alone.
import { readFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';
import { createHash } from 'node:crypto';
import { pathToFileURL } from 'node:url';
const R = 'C:/Users/Sidhartha/Automation Projects/storm-market/.worktrees/ep-joplin-2011';
const { chromium, chromiumExecutable } = await import(pathToFileURL(R + '/scripts/playwright_env.mjs'));
const { hostCss, stageComp } = await import(pathToFileURL(R + '/scripts/stage_comp.mjs'));
const ep = join(R, 'episodes/ep-joplin-2011');
const ID = 'g-a2-countdown';
const out = join(ep, 'sheets-pre', ID + '-frames');
mkdirSync(join(out, 'tiles'), { recursive: true });
const page0 = stageComp(ep, join(ep, 'compositions', ID + '.html'), hostCss(readFileSync(join(ep, 'index.html'), 'utf8')), '_a2cd_');
const browser = await chromium.launch({ executablePath: chromiumExecutable(), args: ['--allow-file-access-from-files', '--disable-gpu'] });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
const errs = [];
page.on('pageerror', e => errs.push(String(e)));
const open = async () => { await page.goto(pathToFileURL(page0).href); await page.waitForFunction((id) => !!(window.__timelines && window.__timelines[id]), ID); };
const seek = (t) => page.evaluate(([id, t]) => { window.__timelines[id].seek(t, false); }, [ID, t]);
const shot = async (t, name) => { await seek(t); return page.screenshot({ path: name ? join(out, name) : undefined }); };
const md5 = b => createHash('md5').update(b).digest('hex');
await open();
const D = await page.evaluate((id) => window.__timelines[id].duration(), ID);
console.log('duration', D);
const S1 = -3.02, S2 = 18.76, S3 = 28.34, S5 = 55.22, S6 = 62.60;
// settled frames, one per state
const keys = { '00-frame0': 0, '01-130': S1 + 6, '02-433': S1 + 15, '03-509-ne': S2 + 6, '04-511-ring': S3 + 4.4, '05-kansas': S3 + 8, '06-s4-hold': 50,
  '07-517-whole': S5 + 4.5, '08-dark-nosiren': S5 + 7, '09-flash-on': S6 + 2.6, '10-6min': S6 + 3.8, '11-cite1': S6 + 6, '12-cite3-north': S6 + 10.5,
  '13-carl-lab': S6 + 14, '14-exit': D - 0.3 };
for (const [n, t] of Object.entries(keys)) await shot(t, n + `_${t.toFixed(2)}s.png`);
if (!process.env.NO_TILES) for (let t = 0, i = 0; t <= D; t += 3, i++) await page.screenshot({ path: join(out, 'tiles', `t${String(i).padStart(3, '0')}.png`), scale: 'css' }, await seek(t));

const truth = await page.evaluate(([id, D, S5, S6]) => {
  const tl = window.__timelines[id];
  const q = (s) => document.querySelector(s);
  const vis = (e) => e.checkVisibility({ opacityProperty: true, visibilityProperty: true }) && +getComputedStyle(e).opacity > 0.02;
  const res = {};
  // map-space geometry (all inside #a2cd-cam, so map coords compare directly)
  const city = q('#a2cd-mm-city'); const L = city.getTotalLength(); const pts = [];
  for (let i = 0; i <= 2000; i++) { const p = city.getPointAtLength(L * i / 2000); pts.push([p.x, p.y]); }
  const CX = 874.1, CY = 505.7, RR = 419.9;
  res.t3_cityMaxDistFromCentroid = Math.max(...pts.map(([x, y]) => Math.hypot(x - CX, y - CY))).toFixed(1) + ' vs ring r ' + RR;
  res.t4_westTipX = 180; res.t4_stateLineX = 579.5;
  const nearY = (x0) => Math.min(...pts.filter(([x]) => Math.abs(x - x0) < 15).map(([, y]) => y));
  res.t5_carlPinY_vs_outlineTopNearX = [230.6, nearY(772.3).toFixed(1)];
  res.t5_webbPinY_vs_outlineTopNearX = [303.5, nearY(961.6).toFixed(1)];
  res.t5_outlineMinY = Math.min(...pts.map(p => p[1])).toFixed(1);
  // truth 6: clock sequence, one at a time
  const tg = ['t130', 't433', 't509', 't511', 't517']; const seq = []; const multi = [];
  for (let t = 0; t <= D; t += 0.05) { tl.seek(t, false); const v = tg.filter(g => vis(q('#a2cd-' + g)) && +getComputedStyle(q('#a2cd-' + g)).opacity > 0.5);
    if (v.length > 1) multi.push(t.toFixed(2)); if (v.length === 1 && seq[seq.length - 1] !== v[0]) seq.push(v[0]); }
  res.t6_clockSeq = seq.join(' > '); res.t6_twoAtOnce = multi.length; res.t6_has300 = document.body.innerHTML.includes('3:00');
  // truth 7: dark ring from S5 sirens 5.76 (settled +0.5) to S6 six 2.42; flashback states
  const ringA = q('#a2cd-mm-ring-a'), dark = q('#a2cd-ringdark'), stamp = q('#a2cd-stamp');
  const bad7 = [];
  for (let t = S5 + 6.3; t < S6 + 2.42; t += 0.05) { tl.seek(t, false); if (!vis(dark) || +getComputedStyle(ringA).opacity > 0.01) bad7.push(t.toFixed(2)); }
  res.t7_notDarkInSpan = bad7.length;
  const fl = []; for (const t of [S6 + 2.6, S6 + 2.9, S6 + 3.2, S6 + 3.5, S6 + 4.2]) { tl.seek(t, false); fl.push([t.toFixed(2), +(+getComputedStyle(ringA).opacity).toFixed(2), vis(stamp), vis(dark)]); }
  res.t7_flash_t_ringA_stamp_dark = fl;
  res.t7_maxRingAinFlash = 0; for (let t = S6 + 2.4; t < S6 + 4; t += 0.02) { tl.seek(t, false); res.t7_maxRingAinFlash = Math.max(res.t7_maxRingAinFlash, +getComputedStyle(ringA).opacity); }
  // truth 8: polygon numbers in any text
  res.t8_polyNumbers = (document.querySelector('#a2cd-root').textContent.match(/polygon\s*#?\d+/gi) || []);
  // truth 9 + label clearances: sample every 0.1 s
  const T = [...document.querySelectorAll('#a2cd-root text, #a2cd-root .a2cd-glass, #a2cd-cite, #a2cd-root .a2cd-pin, #a2cd-root .a2cd-arw')];
  const corner = new Set(), edge = new Set();
  for (let t = 0; t <= D; t += 0.1) { tl.seek(t, false);
    for (const e of T) { if (!vis(e)) continue; const b = e.getBoundingClientRect(); if (!b.width) continue;
      if (b.right > 1600 && b.bottom > 680) corner.add(e.id || e.className);
      if (e.textContent.trim() && (b.left < 96 || b.right > 1824 || b.top < 54 || b.bottom > 1026)) edge.add(e.id); } }
  res.t9_inCorner = [...corner]; res.safeEdge = [...edge];
  // labels vs ring A circle / outline at their settled time
  const ringDist = (el) => { const b = el.getBBox(); const xs = [b.x, b.x + b.width], ys = [b.y, b.y + b.height];
    const nx = Math.max(b.x, Math.min(CX, b.x + b.width)), ny = Math.max(b.y, Math.min(CY, b.y + b.height));
    const dIn = Math.hypot(nx - CX, ny - CY); const dOut = Math.max(...xs.flatMap(x => ys.map(y => Math.hypot(x - CX, y - CY))));
    return [+(RR - dOut).toFixed(1), +(dIn - RR).toFixed(1)]; };  // >0 first = wholly inside, >0 second = wholly outside
  const crossOutline = (el) => { const b = el.getBBox(); return pts.filter(([x, y]) => x > b.x - 4 && x < b.x + b.width + 4 && y > b.y - 4 && y < b.y + b.height + 4).length; };
  res.westLab_ring_in_out = ringDist(q('#a2cd-west-lab')); res.westLab_outlinePts = crossOutline(q('#a2cd-west-lab'));
  res.northLab_ring_in_out = ringDist(q('#a2cd-north-lab')); res.northLab_outlinePts = crossOutline(q('#a2cd-north-lab'));
  res.stamp_ring_in_out = ringDist(stamp);
  tl.seek(0, false);
  res.frame0 = [...document.querySelectorAll('#a2cd-root *')].filter(e => vis(e) && e.getBoundingClientRect().width && e.closest('.a2cd-svg') === null).map(e => e.id).filter(Boolean);
  return res;
}, [ID, D, S5, S6]);
console.log(JSON.stringify(truth, null, 1));

// seek order: each cue second forward on a fresh page vs seek 0 -> past -> back
const cues = [S1 + 3.02, S1 + 5.14, S1 + 10.8, S1 + 14.12, S2 + 1.28, S2 + 5.04, S3 + 0.92, S3 + 2.98, S3 + 3.86, S3 + 5.66, S3 + 6.96, S3 + 10.92,
  S5 + 0.76, S5 + 3.6, S5 + 5.76, S5 + 6.26, S6 + 2.42, S6 + 4.5, S6 + 8.22, S6 + 8.78, S6 + 12.68].map(t => +(t + 0.6).toFixed(2));
const fwd = {};
await open();
for (const t of cues) fwd[t] = md5(await shot(t));
await open();
const bad = [];
for (const t of cues) { await shot(0); await shot(D - 0.01); const h = md5(await shot(t)); if (h !== fwd[t]) bad.push(t); }
console.log('seek-order mismatches', bad, 'of', cues.length, 'page errors', errs);
await browser.close();
