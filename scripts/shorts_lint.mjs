// shorts_lint.mjs — runtime text lint for 9:16 compositions (owner 16 Sep 26: "need a new mech for
// shorts for linting these auto per 9:16 AR"). overlap_check.mjs measures static layout; a label that
// gsap translates off-frame at runtime passed it (sh-hawaii-lowell-1 v3). This gate loads the episode
// in headless Chromium, emulates the section windows, SEEKS the timeline every 0.25 s and measures the
// rendered rect (transforms included) of every visible text element against:
//   1. the frame itself (nothing cut off, 24 px tolerance),
//   2. the Shorts / Reels UI safe zone: top 220 px, bottom 420 px, right rail 150 px below y 900,
//   3. other visible text (no rect intersections between separate elements).
// Usage: node scripts/shorts_lint.mjs episodes/<slug>   -> exit 0 clean, 1 findings (loud).
import { launchGate } from './playwright_env.mjs';
import { readFileSync } from 'node:fs';
import { resolve, join } from 'node:path';
import { pathToFileURL } from 'node:url';
const SHORTS_LINT_DEADLINE_S = 120;  // ends itself (browser closed, exit 124) before a caller has to kill node; 24x its 5 s on sh-hawaii-lowell-1 (ASUS, 18 Oct 26)

const ep = resolve(process.argv[2]);
const html = readFileSync(join(ep, 'index.html'), 'utf-8');
const W = +(html.match(/data-width="(\d+)"/)?.[1] ?? 0), H = +(html.match(/data-height="(\d+)"/)?.[1] ?? 0);
if (!(W && H && H > W)) { console.log(`[shorts_lint] not a portrait composition (${W}x${H}) — nothing to do`); process.exit(0); }
const DUR = +(html.match(/data-duration="([\d.]+)"/)?.[1] ?? 0);
if (!DUR) { console.log('[shorts_lint] no data-duration on the root — cannot sample'); process.exit(2); }
const TEXT = '.cap, .chip, .popfig, .quotecard, .closecard, .head, .lab, .quote, .q';
const SAFE = { top: 220, bottom: H - 420, railX: W - 150, railY: 900, tol: 24 };

const findings = [];
let registered = false;
const browser = await launchGate('shorts_lint', SHORTS_LINT_DEADLINE_S, { args: [] });
try {
  const page = await browser.newPage({ viewport: { width: W, height: H } });
  await page.goto(pathToFileURL(join(ep, 'index.html')).href, { waitUntil: 'load' });
  await page.waitForTimeout(600); // hyperframes registers __timelines after load (same wait as overlap_check.mjs)
  registered = await page.evaluate(() => Object.keys(window.__timelines || {}).length) > 0;
  for (let t = 0; registered && t <= DUR; t += 0.25) {
    const rows = await page.evaluate(({ t, TEXT }) => {
      // emulate the player: a windowed element is on screen only inside [start, start+duration)
      for (const el of document.querySelectorAll('[data-start][data-duration]')) {
        if (el.id === 'root') continue;
        const s = +el.dataset.start, d = +el.dataset.duration;
        el.style.display = (t >= s && t < s + d) ? '' : 'none';
      }
      const k = Object.keys(window.__timelines)[0]; window.__timelines[k].seek(t, false);
      const out = [];
      for (const el of document.querySelectorAll(TEXT)) {
        if (!el.textContent.trim() || el.querySelector(TEXT)) continue; // leaf text elements only
        const cs = getComputedStyle(el); let node = el, alpha = 1;
        while (node && node !== document.body) { const c = getComputedStyle(node); if (c.display === 'none') { alpha = 0; break; } alpha *= +c.opacity; if (c.visibility === 'hidden') alpha = 0; node = node.parentElement; }
        if (alpha < 0.05) continue;
        const r = el.getBoundingClientRect();
        if (r.width < 2 || r.height < 2) continue;
        out.push({ id: el.id || el.className, text: el.textContent.trim().slice(0, 40), x1: r.left, y1: r.top, x2: r.right, y2: r.bottom });
      }
      return out;
    }, { t, TEXT });
    const tt = t.toFixed(2);
    for (const r of rows) {
      if (r.x1 < -SAFE.tol || r.y1 < -SAFE.tol || r.x2 > W + SAFE.tol || r.y2 > H + SAFE.tol)
        findings.push(`${tt}s OFF-FRAME ${r.id} "${r.text}" x${r.x1 | 0}..${r.x2 | 0} y${r.y1 | 0}..${r.y2 | 0}`);
      else if (r.y1 < SAFE.top - SAFE.tol || r.y2 > SAFE.bottom + SAFE.tol || (r.y2 > SAFE.railY && r.x2 > SAFE.railX + SAFE.tol))
        findings.push(`${tt}s UI-ZONE ${r.id} "${r.text}" x${r.x1 | 0}..${r.x2 | 0} y${r.y1 | 0}..${r.y2 | 0}`);
    }
    for (let i = 0; i < rows.length; i++) for (let j = i + 1; j < rows.length; j++) {
      const a = rows[i], b = rows[j];
      if (a.x1 < b.x2 && b.x1 < a.x2 && a.y1 < b.y2 && b.y1 < a.y2)
        findings.push(`${tt}s OVERLAP ${a.id} "${a.text}" × ${b.id} "${b.text}"`);
    }
  }
} finally {
  await browser.close();
}
if (!registered) { console.log('[shorts_lint] no timeline registered in window.__timelines'); process.exit(2); }
const seen = new Map(); for (const f of findings) { const k = f.replace(/^[\d.]+s /, '').replace(/ x-?\d+\.\.-?\d+ y-?\d+\.\.-?\d+$/, ''); if (!seen.has(k)) seen.set(k, f); }
const uniq = [...seen.values()];
if (uniq.length) {
  console.log(`[shorts_lint] ${uniq.length} finding(s) over ${findings.length} samples:`);
  for (const f of uniq) console.log('  FAIL ' + f);
  process.exit(1);
}
console.log(`[shorts_lint] PASS — ${W}x${H}, ${Math.round(DUR / 0.25) + 1} samples, every visible text inside the frame and the Shorts UI safe zone, no text collisions`);
