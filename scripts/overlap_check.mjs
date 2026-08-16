// overlap_check.mjs — graphics-layering QC (owner order 2026-08-16, ep6 RCA).
// Catches the two defect classes the ep6 draft shipped with:
//   A) two track-3 cards on screen at the same time whose screen zones intersect
//   B) a track-3 card window overlapping a track-2 composition host while the comp
//      draws visible text inside the card's screen zone (the "sandwich" bug)
// READ-ONLY checker: loads HTML, never writes it. Usage: node scripts/overlap_check.mjs <episode-dir>
import { chromium } from 'file:///C:/Users/Sidhartha/AppData/Roaming/npm/node_modules/@playwright/cli/node_modules/playwright/index.mjs';
import fs from 'fs';
import path from 'path';

const EXE = 'C:/Users/Sidhartha/AppData/Local/ms-playwright/chromium-1228/chrome-win64/chrome.exe';
const epDir = path.resolve(process.argv[2] || '.');
const indexPath = path.join(epDir, 'index.html');
const html = fs.readFileSync(indexPath, 'utf8');

// -- parse timed elements from index.html attributes --
const els = [];
const re = /<(section|div)\b[^>]*\bid="([^"]+)"[^>]*>/g;
let m;
while ((m = re.exec(html))) {
  const tag = m[0];
  const attr = (n) => { const r = new RegExp(`${n}="([^"]*)"`).exec(tag); return r ? r[1] : null; };
  const start = parseFloat(attr('data-start')); const dur = parseFloat(attr('data-duration'));
  if (isNaN(start) || isNaN(dur)) continue;
  els.push({ id: m[2], start, dur, track: attr('data-track-index'), comp: attr('data-composition-id'), compSrc: attr('data-composition-src') });
}
const cards = els.filter(e => e.track === '3');
const hosts = els.filter(e => e.compSrc);

const overlapT = (a, b) => Math.min(a.start + a.dur, b.start + b.dur) - Math.max(a.start, b.start);

const browser = await chromium.launch({ headless: true, executablePath: EXE });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
await page.goto('file:///' + indexPath.replace(/\\/g, '/'));
await page.waitForTimeout(600);

// measure each card's screen rect in the bare page (all elements render; gsap initial states may hide
// some — force visible for measurement only)
const cardRects = await page.evaluate((ids) => {
  const out = {};
  for (const id of ids) {
    const el = document.getElementById(id);
    if (!el) continue;
    el.style.visibility = 'visible'; el.style.opacity = '1'; el.style.display = 'block';
    for (const c of el.querySelectorAll('*')) { c.style.visibility = 'visible'; c.style.opacity = '1'; }
    const r = el.getBoundingClientRect();
    // shrink to the union of text-bearing children (the section itself is often inset:0)
    let u = null;
    for (const c of el.querySelectorAll('div,span,text')) {
      if (!c.textContent.trim()) continue;
      const cr = c.getBoundingClientRect();
      if (cr.width < 2 || cr.height < 2) continue;
      u = u ? { left: Math.min(u.left, cr.left), top: Math.min(u.top, cr.top), right: Math.max(u.right, cr.right), bottom: Math.max(u.bottom, cr.bottom) } : { left: cr.left, top: cr.top, right: cr.right, bottom: cr.bottom };
    }
    out[id] = u || { left: r.left, top: r.top, right: r.right, bottom: r.bottom };
  }
  return out;
}, cards.map(c => c.id));

const rectHit = (a, b, pad = 8) => a && b && a.left < b.right + pad && b.left < a.right + pad && a.top < b.bottom + pad && b.top < a.bottom + pad;

const findings = [];
// Class A: card vs card
for (let i = 0; i < cards.length; i++) for (let j = i + 1; j < cards.length; j++) {
  const t = overlapT(cards[i], cards[j]);
  if (t > 0.05 && rectHit(cardRects[cards[i].id], cardRects[cards[j].id]))
    findings.push(`A card-vs-card: #${cards[i].id} and #${cards[j].id} co-occur ${t.toFixed(2)}s with intersecting zones`);
}
// Class B: card vs comp text — load each comp, seek its own timeline to the card window, measure text
for (const h of hosts) {
  const over = cards.filter(c => overlapT(c, h) > 0.05 && cardRects[c.id]);
  if (!over.length) continue;
  const compPath = path.join(epDir, h.compSrc);
  if (!fs.existsSync(compPath)) { findings.push(`B missing comp file: ${h.compSrc}`); continue; }
  const p2 = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  await p2.goto('file:///' + compPath.replace(/\\/g, '/'));
  await p2.waitForTimeout(500);
  for (const c of over) {
    const relT = Math.max(c.start, h.start) - h.start + 0.5; // sample mid-entry of the card window
    const hit = await p2.evaluate(({ compId, relT, zone }) => {
      const tl = (window.__timelines || {})[compId];
      if (tl && tl.seek) { tl.pause && tl.pause(); tl.seek(relT); }
      const hits = [];
      const walk = (root) => {
        for (const el of root.querySelectorAll('div,span,text,tspan')) {
          if (!el.textContent || !el.textContent.trim()) continue;
          if (el.children.length > 0 && el.tagName !== 'text') continue; // leaf-ish only
          const st = getComputedStyle(el);
          if (st.visibility === 'hidden' || parseFloat(st.opacity) < 0.15) continue;
          let vis = true, n = el;
          while (n && n !== document.body) { const s = getComputedStyle(n); if (s.visibility === 'hidden' || parseFloat(s.opacity) < 0.15 || s.display === 'none') { vis = false; break; } n = n.parentElement; }
          if (!vis) continue;
          const r = el.getBoundingClientRect();
          if (r.width < 4 || r.height < 4) continue;
          if (r.left < zone.right && zone.left < r.right && r.top < zone.bottom && zone.top < r.bottom)
            hits.push(el.textContent.trim().slice(0, 40));
        }
      };
      walk(document);
      return hits;
    }, { compId: h.comp, relT, zone: cardRects[c.id] });
    if (hit.length) findings.push(`B sandwich: #${c.id} (t=${c.start}) over comp ${h.comp} text: ${hit.slice(0, 3).join(' | ')}`);
  }
  await p2.close();
}
await browser.close();

if (findings.length) {
  console.log(`OVERLAP CHECK: ${findings.length} finding(s)`);
  findings.forEach(f => console.log('  FAIL ' + f));
  process.exit(1);
}
console.log(`OVERLAP CHECK: PASS (${cards.length} cards, ${hosts.length} comp hosts checked)`);
