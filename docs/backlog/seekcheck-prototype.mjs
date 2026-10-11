// PROTOTYPE for ops/tasks.md task 27 (seek-order gate). Not a gate and run by nothing.
// Copied as it ran in the El Reno worktree, where it sat in episodes/ep4-el-reno/.qc-tmp/replot-stage/:
// its import path, EP and COMPS assume that place and that episode. A gate built from it takes the episode as an argument.
// replot-stage scratch (read-only checker, never committed): does a comp draw the same picture at second t
// whatever was seeked before? Order A = fresh page, forward only. Order B = fresh page, seek 0, seek past t, seek back to t.
// Usage: node seekcheck.mjs state            -> DOM-state diff, every 0.5 s, all 11 replot comps
//        node seekcheck.mjs shot comp:t ...  -> two PNGs per pair (A and B), byte-compared, saved to seek-frames/
import { chromium, chromiumExecutable } from '../../../../scripts/playwright_env.mjs';
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = dirname(fileURLToPath(import.meta.url));
const EP = join(HERE, '..', '..');
const COMPS = ['g-i1s8-replot', 'g-a2s6-replot', 'g-a2s7-replot', 'g-a2s8-replot', 'g-a2s11-replot', 'g-a3s2-replot',
  'g-a3s8-replot', 'g-a3s9-replot', 'g-a3s11-replot', 'g-a3s13-split', 'g-a5s2-rating'];
const css = [...readFileSync(join(EP, 'index.html'), 'utf8').matchAll(/<style[^>]*>([\s\S]*?)<\/style>/g)].map(x => x[1]).join('\n');
const STAGED = join(HERE, 'seek-staged'); mkdirSync(STAGED, { recursive: true });
const stage = (comp) => {
  const raw = readFileSync(join(EP, 'compositions', comp + '.html'), 'utf8');
  const body = raw.match(/<template>([\s\S]*?)<\/template>/)[1];
  const out = join(STAGED, comp + '.html');
  writeFileSync(out, `<!doctype html><html><head><meta charset="utf-8"><base href="../../../"><style>${css}</style>
<style>html,body{margin:0;width:1920px;height:1080px;background:#111;overflow:hidden}</style><script src="gsap.min.js"></script></head><body>${body}</body></html>`, 'utf8');
  return 'file:///' + out.replace(/\\/g, '/');
};
const browser = await chromium.launch({ executablePath: chromiumExecutable(), args: ['--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
const fresh = async (comp) => { await page.goto(stage(comp), { waitUntil: 'load' }); await page.evaluate(() => document.fonts.ready); await page.waitForTimeout(150); };
const seek = (comp, t) => page.evaluate(([c, x]) => { window.__timelines[c].seek(x, false); }, [comp, t]);
const dur = (comp) => page.evaluate((c) => window.__timelines[c].duration(), comp);
const settle = () => page.evaluate(() => new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r))));
const state = () => page.evaluate(() => {
  const o = {};
  for (const el of document.querySelectorAll('[id]')) {
    const r = el.getBoundingClientRect(), cs = getComputedStyle(el);
    let op = 1, vis = cs.visibility; for (let n = el; n && n.nodeType === 1; n = n.parentElement) op *= parseFloat(getComputedStyle(n).opacity);
    o[el.id] = [Math.round(r.x * 2) / 2, Math.round(r.y * 2) / 2, Math.round(r.width * 2) / 2, Math.round(r.height * 2) / 2, Math.round(op * 50) / 50, vis, el.children.length ? '' : el.textContent];
  }
  return o;
});
const mode = process.argv[2];
if (mode === 'measure') {
  /* the numbers the fix-round rows ask for, read from the staged page instead of estimated */
  const op = (id) => page.evaluate((i) => { let o = 1; for (let n = document.getElementById(i); n && n.nodeType === 1; n = n.parentElement) { const c = getComputedStyle(n); if (c.visibility === 'hidden') return 0; o *= parseFloat(c.opacity); } return +o.toFixed(2); }, id);
  const right = (id) => page.evaluate((i) => +document.getElementById(i).getBoundingClientRect().right.toFixed(1), id);
  await fresh('g-a2s7-replot');
  for (const t of [10.8, 11.7, 11.8, 12.2]) { await seek('g-a2s7-replot', t); console.log(`a2s7 "about 260 feet every second" opacity at ${t} s:`, await op('rp27-t-fps')); }
  await fresh('g-i1s8-replot');
  for (const t of [7.5, 8.3, 10.4, 11.0]) { await seek('g-i1s8-replot', t); console.log(`i1s8 at ${t} s: square opacity`, await op('rp18-suv'), '| diamond opacity', await op('rp18-car')); }
  await fresh('g-a3s9-replot'); await seek('g-a3s9-replot', 17.72);
  const r20 = await right('rp39-t-20'); console.log(`a3s9 "In about 20 seconds" right edge x ${r20}; Radio Road line left edge x 1332.5; gap ${(1332.5 - r20).toFixed(1)} px`);
  await fresh('g-a3s2-replot'); await seek('g-a3s2-replot', 6.98);
  console.log('a3s2 bottom captions right edge x:', await right('rp32-t-own'), 'and', await right('rp32-t-ring'), '; US-81 line left edge x 996.5');
  await fresh('g-a5s2-rating'); await seek('g-a5s2-rating', 10.94);
  const dots = await page.evaluate(() => [...document.querySelectorAll('#rp52-dots rect')].map((r) => { const x = +r.getAttribute('x') + 6, y = +r.getAttribute('y') + 6; return [x, y, +(Math.hypot(x - 1040, y - 548) - 390).toFixed(0)]; }));
  const near = dots.slice().sort((a, b) => Math.abs(a[2]) - Math.abs(b[2]))[0];
  console.log(`a5s2 ${dots.length} structure squares; closest to the ring line: (${near[0]}, ${near[1]}), ${Math.abs(near[2])} px ${near[2] < 0 ? 'inside' : 'outside'} it (ring band reaches 15 px each side)`);
  const marks = await page.evaluate(() => ['rp52-s1', 'rp52-s2', 'rp52-s3'].map((i) => { const c = document.querySelector('#' + i + ' circle'); return [document.querySelectorAll('#' + i + ' circle').length, c.getAttribute('fill'), c.getAttribute('stroke'), c.getAttribute('stroke-dasharray')].join(' / '); }));
  console.log('a5s2 sub-vortex marks (circles / fill / stroke / dash):', marks.join(' ; '));
} else if (mode === 'state') {
  let bad = 0;
  for (const comp of COMPS) {
    const STEP = parseFloat(process.argv[3] || '0.5');   // 0.1 catches the 0.3 s pulses a 0.5 s step walks past
    await fresh(comp); const D = await dur(comp); const times = []; for (let t = STEP / 2; t < D; t += STEP) times.push(+t.toFixed(2));
    const A = {}; for (const t of times) { await seek(comp, t); A[t] = await state(); }
    await fresh(comp); const diffs = {};
    for (const t of times) {
      await seek(comp, 0); await seek(comp, Math.min(D, t + 3)); await seek(comp, t); const B = await state();
      for (const id of Object.keys(A[t])) if (JSON.stringify(A[t][id]) !== JSON.stringify(B[id])) (diffs[id] = diffs[id] || []).push(t);
    }
    const ids = Object.keys(diffs); bad += ids.length;
    console.log(comp, ids.length ? 'DIFF' : 'same', `(${times.length} times)`);
    for (const id of ids) console.log('   ', id, 'at', diffs[id].length, 'times, first', diffs[id][0], 'last', diffs[id][diffs[id].length - 1]);
  }
  console.log(bad ? `SEEK-ORDER FAIL: ${bad} element(s) differ` : 'SEEK-ORDER PASS: all 11 comps, same state in both orders');
} else {
  const OUT = join(HERE, 'seek-frames'); mkdirSync(OUT, { recursive: true });
  for (const pair of process.argv.slice(3)) {
    const [comp, ts] = pair.split(':'); const t = parseFloat(ts);
    await fresh(comp); const D = await dur(comp); await seek(comp, t); await settle();
    const a = await page.screenshot({ path: join(OUT, `${comp}_${ts}_A-forward.png`), type: 'png' });
    await fresh(comp); await seek(comp, 0); await seek(comp, Math.min(D, t + 3)); await seek(comp, t); await settle();
    const b = await page.screenshot({ path: join(OUT, `${comp}_${ts}_B-rewound.png`), type: 'png' });
    if (a.equals(b)) { console.log(comp, 't=' + ts, 'MATCH (PNG bytes identical)'); continue; }
    /* bytes differ: count the pixels that differ, the largest channel difference, and where they sit */
    await page.goto('about:blank');
    const d = await page.evaluate(async ([ua, ub]) => {
      const load = (u) => new Promise((r) => { const i = new Image(); i.onload = () => r(i); i.src = u; });
      const [ia, ib] = await Promise.all([load(ua), load(ub)]);
      const px = (i) => { const c = document.createElement('canvas'); c.width = 1920; c.height = 1080; const x = c.getContext('2d'); x.drawImage(i, 0, 0); return x.getImageData(0, 0, 1920, 1080).data; };
      const A = px(ia), B = px(ib); let n = 0, n8 = 0, mx = 0, x0 = 1e9, y0 = 1e9, x1 = -1, y1 = -1;
      for (let p = 0; p < A.length; p += 4) {
        const dd = Math.max(Math.abs(A[p] - B[p]), Math.abs(A[p + 1] - B[p + 1]), Math.abs(A[p + 2] - B[p + 2]));
        if (dd) { n++; if (dd > 8) n8++; if (dd > mx) mx = dd; const i = p / 4, x = i % 1920, y = (i - x) / 1920; if (x < x0) x0 = x; if (x > x1) x1 = x; if (y < y0) y0 = y; if (y > y1) y1 = y; }
      }
      return { n, n8, mx, box: [x0, y0, x1, y1] };
    }, ['data:image/png;base64,' + a.toString('base64'), 'data:image/png;base64,' + b.toString('base64')]);
    console.log(comp, 't=' + ts, `BYTES DIFFER: ${d.n} of 2073600 px differ, ${d.n8} by more than 8/255, largest ${d.mx}/255, inside box x ${d.box[0]}-${d.box[2]} y ${d.box[1]}-${d.box[3]}`);
  }
}
await browser.close();
