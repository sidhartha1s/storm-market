/* Comp-over-comp occlusion: a card mounted on a higher track can cover the text of the composition below it.
   overlap_check v2 only tests index elements over comp text ("sandwich") and comp-internal collisions, so a
   g-cite-* card sitting on a g-map-* headline passes every gate and only shows up in the render (ep-1974,
   21 Sep 26: "Alabama" sliced at 15:02, radar rail rows cut at 7:06).
   For each pair of overlapping host windows it loads both comps, walks the shared window, and reports any
   OPAQUE box in the upper comp whose rect intersects a visible TEXT rect in the lower comp. */
import { chromium, chromiumExecutable } from './playwright_env.mjs';
import { readFileSync, writeFileSync, unlinkSync } from 'fs';
import { join, resolve } from 'path';

const ep = resolve(process.argv[2] || '.');   // usage: node scripts/occlusion_check.mjs <episode dir>
const idx = readFileSync(join(ep, 'index.html'), 'utf-8');

const hosts = [];
for (const m of idx.matchAll(/<div[^>]*id="(host-[^"]+)"[^>]*data-composition-src="compositions\/([^"]+)"[^>]*>/g)) {
  const tag = m[0];
  const num = (re) => { const x = tag.match(re); return x ? parseFloat(x[1]) : null; };
  hosts.push({ id: m[1], file: m[2], start: num(/data-start="([\d.]+)"/), dur: num(/data-duration="([\d.]+)"/), track: num(/data-track-index="(\d+)"/) });
}
const pairs = [];
for (const a of hosts) for (const b of hosts) {
  if (a === b || a.track <= b.track) continue;                      // a is above b
  const s = Math.max(a.start, b.start), e = Math.min(a.start + a.dur, b.start + b.dur);
  if (e - s > 0.5) pairs.push({ up: a, lo: b, s, e });
}
console.log(`${hosts.length} hosts, ${pairs.length} overlapping pair(s)`);

const browser = await chromium.launch({ executablePath: chromiumExecutable(), args: ['--allow-file-access-from-files'] });
const HOST_CSS = hostCss(idx);
const stage = async (page, file) => {
  const tmp = stageComp(ep, join(ep, 'compositions', file), HOST_CSS, 'occ-');
  await page.goto('file:///' + tmp.split('\\').join('/'), { waitUntil: 'load' });
  return tmp;
};
const RECTS = `(() => {
  const k = Object.keys(window.__timelines || {})[0]; const tl = window.__timelines[k];
  const vis = el => { const s = getComputedStyle(el); if (s.visibility === 'hidden' || s.display === 'none' || parseFloat(s.opacity) < 0.15) return false;
    let p = el.parentElement; while (p && p !== document.body) { const ps = getComputedStyle(p); if (ps.visibility === 'hidden' || ps.display === 'none' || parseFloat(ps.opacity) < 0.15) return false; p = p.parentElement; } return true; };
  return (t) => { tl.seek(t, false);
    const text = [], box = [];
    for (const el of document.querySelectorAll('div,span,text,tspan,p,li')) {
      if (!vis(el)) continue; const r = el.getBoundingClientRect(); if (r.width < 4 || r.height < 4) continue;
      if (el.textContent.trim() && !el.children.length) text.push({ t: el.textContent.trim().slice(0, 44), x: r.left, y: r.top, X: r.right, Y: r.bottom });
      const s = getComputedStyle(el); const bg = s.backgroundColor;
      const a = bg.startsWith('rgba') ? parseFloat(bg.split(',')[3]) : (bg === 'transparent' ? 0 : 1);
      if (a >= 0.5 && r.width > 300 && r.height > 120) box.push({ x: r.left, y: r.top, X: r.right, Y: r.bottom, a: +a.toFixed(2) });
    }
    return { text, box }; };
})()`;
const pageUp = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
const pageLo = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
const findings = [];
const seenPair = new Set();
for (const p of pairs) {
  const key = p.up.file + '|' + p.lo.file;
  if (seenPair.has(key)) continue; seenPair.add(key);
  const t1 = await stage(pageUp, p.up.file), t2 = await stage(pageLo, p.lo.file);
  const fUp = await pageUp.evaluateHandle(RECTS), fLo = await pageLo.evaluateHandle(RECTS);
  const hits = {};
  for (let i = 0; i <= 6; i++) {
    const t = p.s + (p.e - p.s) * i / 6;
    const U = await pageUp.evaluate(({ f, tt }) => f(tt), { f: fUp, tt: t - p.up.start });
    const L = await pageLo.evaluate(({ f, tt }) => f(tt), { f: fLo, tt: t - p.lo.start });
    for (const b of U.box) for (const tx of L.text) {
      if (b.X > tx.x && b.x < tx.X && b.Y > tx.y && b.y < tx.Y) {
        const ov = (Math.min(b.X, tx.X) - Math.max(b.x, tx.x)) * (Math.min(b.Y, tx.Y) - Math.max(b.y, tx.y));
        const frac = ov / ((tx.X - tx.x) * (tx.Y - tx.y));
        /* two-letter map labels (AL, GA, MS...) are decoration on the map plate: a card over them is the
           authored design, not a defect. Anything longer is content the viewer is meant to read. */
        if (/^[A-Z]{2}$/.test(tx.t)) continue;
        if (frac > 0.08 && !hits[tx.t]) hits[tx.t] = { at: +t.toFixed(1), cover: Math.round(frac * 100) };
      }
    }
  }
  for (const [txt, h] of Object.entries(hits)) findings.push(`${p.up.file.replace('.html','')} covers ${p.lo.file.replace('.html','')} text ${JSON.stringify(txt)} ${h.cover}% at ${h.at}s`);
  unlinkSync(t1); unlinkSync(t2);
}
await browser.close();
if (!findings.length) console.log('OCCLUSION PASS - no mounted card covers another composition\'s text');
else { console.log(`OCCLUSION FAIL - ${findings.length} finding(s)`); for (const f of findings) console.log('   ', f); process.exitCode = 1; }
