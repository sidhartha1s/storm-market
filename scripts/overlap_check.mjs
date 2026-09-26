// overlap_check.mjs v2 — text-collision + duplicate-fact QC (owner orders 2026-08-16 + 2026-08-22).
// v1 sampled one instant per card/comp pair and ignored comp-internal text pairs — the ep6 v2
// draft shipped mid-animation collisions (AUG 23 over DEPRESSION chip) and duplicate facts
// (AUG 30 twice, 80% twice) straight through it. v2 fixes both false-negative classes:
//   1) For every comp host window, step the comp's OWN timeline densely (0.5s) and collect the
//      bboxes of ALL visible leaf text nodes — post-transform, so camera pans/tweens count.
//   2) Flag any text pair whose intersection exceeds AREA_FRAC of the smaller box (25% — the
//      initial 8% draft flagged line-box touches of stacked title/subtitle pairs; comp-internal AND
//      comp-vs-active-card), unless either element carries data-overlap-ok="reason".
//   3) Duplicate-fact: two visible nodes rendering the same normalized fact string (dates,
//      percentages, numbers) at the same instant = FAIL — one fact, one on-screen instance.
// READ-ONLY checker. Usage: node scripts/overlap_check.mjs <episode-dir>
import { chromium, chromiumExecutable } from './playwright_env.mjs';
import fs from 'fs';
import path from 'path';

const EXE = chromiumExecutable();
const STEP = 0.5;
const AREA_FRAC = 0.25;   // heavy overlap = garble; line-box touches of stacked title/subtitle are fine
const epDir = path.resolve(process.argv[2] || '.');
const indexPath = path.join(epDir, 'index.html');
const html = fs.readFileSync(indexPath, 'utf8');

const els = [];
const findings = new Set();
const re = /<(section|div)\b[^>]*\bid="([^"]+)"[^>]*>/g;
let m;
while ((m = re.exec(html))) {
  const tag = m[0];
  const attr = (n) => { const r = new RegExp(`${n}="([^"]*)"`).exec(tag); return r ? r[1] : null; };
  const start = parseFloat(attr('data-start')); const dur = parseFloat(attr('data-duration'));
  if (isNaN(start) || isNaN(dur)) continue;
  els.push({ id: m[2], start, dur, track: attr('data-track-index'), comp: attr('data-composition-id'),
             compSrc: attr('data-composition-src'), ok: attr('data-overlap-ok') });
}
const cards = els.filter(e => e.track === '3');
const hosts = els.filter(e => e.compSrc);
const overlays = els.filter(e => !e.compSrc && e.track !== '3' && !/^(bo-|nx-|sx-|clip-|v-)/.test(e.id));   // every index.html overlay that is not a card/comp/blackout/audio/video (kanto-pin labels were excluded by the old ^p- filter, 17 Sep 26)
const overlapT = (a, b) => Math.min(a.start + a.dur, b.start + b.dur) - Math.max(a.start, b.start);

// fact normalization: uppercase alnum; only strings that read as a "fact" per the header above
// (dates, percentages, numbers) count — a digit is required. A bare place-name label ("TANNER ·
// AL") is not itself a fact and legitimately repeats when the same town is hit twice; requiring
// a digit means an identical REPEATED row still fails on its own time/number (PR #88 review).
const normFact = (s) => {
  const n = s.toUpperCase().replace(/[^A-Z0-9%]/g, ' ').replace(/\s+/g, ' ').trim();
  if (n.length < 3 || !/\d/.test(n)) return null;
  return n;
};

// a text leaf = no children, or only inline emphasis children (<em>/<b>/<i>/<strong>/<sup>/<sub>).
// Without this a card whose only line holds an <em> had NO leaves, fell back to the full-frame
// section rect, and "collided" with everything (p-cap-npr, 2026-08-22).
const LEAF_FN = `(el) => el.children.length === 0 ||
  [...el.children].every(k => /^(EM|B|I|STRONG|SUP|SUB)$/.test(k.tagName))`;

const browser = await chromium.launch({ headless: true, executablePath: EXE });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
await page.goto('file:///' + indexPath.replace(/\\/g, '/'));
await page.waitForTimeout(600);

// card zones + card texts measured once on the bare index page (cards are static layouts; their
// entrance tweens move them but they settle in their authored zone — the zone IS the reservation)
const cardInfo = await page.evaluate(({ ids, leafSrc }) => {
  const isLeaf = eval(leafSrc);
  const out = {};
  for (const id of ids) {
    const el = document.getElementById(id);
    if (!el) continue;
    el.style.visibility = 'visible'; el.style.opacity = '1'; el.style.display = 'block';
    for (const c of el.querySelectorAll('*')) { c.style.visibility = 'visible'; c.style.opacity = '1'; }
    let u = null; const texts = [];
    for (const c of el.querySelectorAll('div,span,text')) {
      if (!c.textContent.trim()) continue;
      if (!isLeaf(c)) continue;
      const cr = c.getBoundingClientRect();
      if (cr.width < 2 || cr.height < 2) continue;
      texts.push(c.textContent.trim());
      u = u ? { left: Math.min(u.left, cr.left), top: Math.min(u.top, cr.top),
                right: Math.max(u.right, cr.right), bottom: Math.max(u.bottom, cr.bottom) }
            : { left: cr.left, top: cr.top, right: cr.right, bottom: cr.bottom };
    }
    const r = el.getBoundingClientRect();
    out[id] = { zone: u || { left: r.left, top: r.top, right: r.right, bottom: r.bottom }, texts };
  }
  return out;
}, { ids: cards.map(c => c.id), leafSrc: LEAF_FN });
const ovInfo = await page.evaluate(({ ids, leafSrc }) => {
  const isLeaf = eval(leafSrc);
  const out = {};
  for (const id of ids) {
    const el = document.getElementById(id);
    if (!el) continue;
    el.style.visibility = 'visible'; el.style.opacity = '1'; el.style.display = 'block';
    for (const c of el.querySelectorAll('*')) { c.style.visibility = 'visible'; c.style.opacity = '1'; c.style.transform = 'none'; }
    let u = null; const bad = []; const texts = [];
    for (const c of el.querySelectorAll('div,span')) {
      if (!c.textContent.trim() || !isLeaf(c)) continue;
      const cr = c.getBoundingClientRect();
      if (cr.width < 2 || cr.height < 2) continue;
      texts.push(c.textContent.trim());
      if (cr.left < 0 || cr.right > 1920 || c.scrollWidth > c.clientWidth + 2)
        bad.push(`"${c.textContent.trim().slice(0, 40)}" x${Math.round(cr.left)}..${Math.round(cr.right)} scroll ${c.scrollWidth}/${c.clientWidth}`);
      u = u ? { left: Math.min(u.left, cr.left), top: Math.min(u.top, cr.top), right: Math.max(u.right, cr.right), bottom: Math.max(u.bottom, cr.bottom) }
            : { left: cr.left, top: cr.top, right: cr.right, bottom: cr.bottom };
    }
    if (u) out[id] = { zone: u, bad, texts };
  }
  return out;
}, { ids: overlays.map(o => o.id), leafSrc: LEAF_FN });
// Class F: overlay text off the frame or overflowing its nowrap box (the 25-char popfig / 84-char bug line, 2026-09-11)
for (const o of overlays) for (const b of (ovInfo[o.id] || {}).bad || []) findings.add(`off-frame: #${o.id} ${b}`);
// the bare index page holds ~80 <video> elements; keeping it open while comps are staged
// crashed the renderer ("Target crashed") on a 16 GB box — release it before staging
await page.close();

const interFrac = (a, b) => {
  const w = Math.min(a.right, b.right) - Math.max(a.left, b.left);
  const h = Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top);
  if (w <= 0 || h <= 0) return 0;
  const inter = w * h;
  const areaA = (a.right - a.left) * (a.bottom - a.top);
  const areaB = (b.right - b.left) * (b.bottom - b.top);
  return inter / Math.max(1, Math.min(areaA, areaB));
};

// pair findings keyed WITHOUT time so a persistent collision reports once with its time range
const pairFinds = new Map();
const addPair = (key, t) => {
  const e = pairFinds.get(key);
  if (e) { e.t1 = t; } else pairFinds.set(key, { t0: t, t1: t });
};

// Class A: card vs card (time overlap + zone intersection)
for (let i = 0; i < cards.length; i++) for (let j = i + 1; j < cards.length; j++) {
  if (cards[i].ok || cards[j].ok) continue;
  const t = overlapT(cards[i], cards[j]);
  const A = cardInfo[cards[i].id], B = cardInfo[cards[j].id];
  if (t > 0.05 && A && B && interFrac(A.zone, B.zone) > AREA_FRAC)
    findings.add(`card-vs-card: #${cards[i].id} + #${cards[j].id} co-occur ${t.toFixed(2)}s, zones intersect`);
}

// Classes B/C/D: per comp host, step the comp timeline through its whole window.
// Comps are <template>-wrapped — loading the raw file renders NOTHING (the v2.0 false-negative
// that let the AUG 23 collision ship). Stage template content into a bare gsap page, same as
// graphics_qc.standalone().
// Host-style injection: hyperframes mounts comps INSIDE index.html's DOM, so the page stylesheet
// applies to comp elements (17 Sep 26: host `.chip{bottom:300px}` stretched a comp chip into a 720 px
// panel; every standalone gate passed). stage_comp.mjs carries the host <style> blocks.
const HOST_CSS = hostCss(html);
const stage = (file) => stageComp(epDir, file, HOST_CSS, 'ov-');
for (const h of hosts) {
  const compPath = path.join(epDir, h.compSrc);
  if (!fs.existsSync(compPath)) { findings.add(`missing comp file: ${h.compSrc}`); continue; }
  const p2 = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  await p2.goto('file:///' + stage(compPath).replace(/\\/g, '/'));
  await p2.waitForTimeout(500);
  const reg = await p2.evaluate((id) => !!((window.__timelines || {})[id]), h.comp);
  if (!reg) { findings.add(`comp timeline not registered when staged: ${h.comp}`); await p2.close(); continue; }
  const activeCardsAt = (t) => cards.filter(c => t >= c.start && t <= c.start + c.dur && cardInfo[c.id]);
  for (let rel = 0.4; rel < h.dur; rel += STEP) {
    const tAbs = h.start + rel;
    const nodes = await p2.evaluate(({ compId, rel, leafSrc }) => {
      const isLeaf = eval(leafSrc);
      const tl = (window.__timelines || {})[compId];
      if (tl && tl.seek) { tl.pause && tl.pause(); tl.seek(rel, false); }
      const out = [];
      for (const el of document.querySelectorAll('div,span,text,tspan')) {
        if (!el.textContent || !el.textContent.trim()) continue;
        if (!isLeaf(el) && el.tagName.toLowerCase() !== 'text') continue;
        let vis = true, n = el;
        while (n && n !== document.body) {
          const s = getComputedStyle(n);
          if (s.visibility === 'hidden' || parseFloat(s.opacity) < 0.15 || s.display === 'none') { vis = false; break; }
          n = n.parentElement;
        }
        if (!vis) continue;
        const r = el.getBoundingClientRect();
        if (r.width < 4 || r.height < 4) continue;
        if (r.right < 0 || r.bottom < 0 || r.left > 1920 || r.top > 1080) continue;
        let ok = null, p = el;
        while (p && p !== document.body) { if (p.dataset && p.dataset.overlapOk) { ok = p.dataset.overlapOk; break; } p = p.parentElement; }
        out.push({ text: el.textContent.trim().slice(0, 60), ok,
                   box: { left: r.left, top: r.top, right: r.right, bottom: r.bottom } });
      }
      return out;
    }, { compId: h.comp, rel, leafSrc: LEAF_FN });
    // a <text> and its own <tspan> (or any other nested leaf match) read as two DOM nodes for one
    // visible instance — collapse those before either collision or dup-fact counts them
    const uniqNodes = [];
    for (const nd of nodes) {
      if (uniqNodes.some(u => u.text === nd.text && interFrac(u.box, nd.box) > 0.9)) continue;
      uniqNodes.push(nd);
    }
    // C: comp-internal pair collisions
    for (let i = 0; i < uniqNodes.length; i++) for (let j = i + 1; j < uniqNodes.length; j++) {
      const a = uniqNodes[i], b = uniqNodes[j];
      if (a.ok || b.ok) continue;
      if (interFrac(a.box, b.box) > AREA_FRAC)
        addPair(`comp-internal: ${h.comp} "${a.text.slice(0, 28)}" x "${b.text.slice(0, 28)}"`, tAbs);
    }
    // E: index.html overlay (popfig/chip/quote) vs this comp's visible text — the popfig that sat on the siren-chain card (2026-09-11)
    for (const o of overlays) {
      if (o.ok || !ovInfo[o.id] || tAbs < o.start || tAbs > o.start + o.dur) continue;
      for (const nd of uniqNodes) {
        if (nd.ok) continue;
        if (interFrac(nd.box, ovInfo[o.id].zone) > AREA_FRAC)
          addPair(`overlay-on-comp: #${o.id} over ${h.comp} text "${nd.text.slice(0, 32)}"`, tAbs);
      }
    }
    // B: comp text vs active card zone; D: duplicate facts — ANY two distinct visible instances
    // of the same normalized fact at this instant, comp-internal included (the ep6 v2 class:
    // "80%" in a headline and again in its own sub-label passed because both read as one "who").
    const act = activeCardsAt(tAbs);
    const factSeen = new Map();
    const addFact = (text, who) => {
      const f = normFact(text);
      if (!f) return;
      if (factSeen.has(f))
        addPair(`dup-fact: "${f}" shown twice (${factSeen.get(f)} + ${who})`, tAbs);
      else factSeen.set(f, who);
    };
    for (const nd of uniqNodes) addFact(nd.text, h.comp);
    for (const o of overlays) {
      if (!ovInfo[o.id] || tAbs < o.start || tAbs > o.start + o.dur) continue;
      for (const t of ovInfo[o.id].texts || []) addFact(t, '#' + o.id);
    }
    for (const c of act) {
      for (const t of cardInfo[c.id].texts) addFact(t, '#' + c.id);
      if (c.ok) continue;
      for (const nd of uniqNodes) {
        if (nd.ok) continue;
        if (interFrac(nd.box, cardInfo[c.id].zone) > AREA_FRAC)
          addPair(`sandwich: #${c.id} over ${h.comp} text "${nd.text.slice(0, 32)}"`, tAbs);
      }
    }
  }
  await p2.close();
}
await browser.close();

for (const [k, v] of pairFinds)
  findings.add(`${k} @${v.t0.toFixed(1)}${v.t1 > v.t0 ? '-' + v.t1.toFixed(1) : ''}s`);
const out = [...findings];
if (out.length) {
  console.log(`OVERLAP CHECK v2: ${out.length} finding(s)`);
  out.slice(0, 40).forEach(f => console.log('  FAIL ' + f));
  if (out.length > 40) console.log(`  ... +${out.length - 40} more`);
  process.exit(1);
}
console.log(`OVERLAP CHECK v2: PASS (${cards.length} cards, ${hosts.length} comp hosts, ${overlays.length} overlays, ${STEP}s step)`);
