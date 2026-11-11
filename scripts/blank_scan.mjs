/* Pre-render blank check: seek every composition across its whole timeline and measure
   how much visible ink is on screen. Catches a graphic that renders empty or near-empty
   at some point without waiting 40 minutes for a render to prove it. */
import { chromium, chromiumExecutable } from './playwright_env.mjs';
import { readFileSync, readdirSync } from 'node:fs';
import { join } from 'node:path';
import { compSize, hostCss, stageComp } from './stage_comp.mjs';

const EXECUTABLE = chromiumExecutable();
const ep = process.argv[2];
const STEP = 0.25;
// staging (host <style> blocks, <base href>, host scripts) is stage_comp.mjs's, shared by every gate
const INDEX_HTML = readFileSync(join(ep, 'index.html'), 'utf8');
const HOST_CSS = hostCss(INDEX_HTML);
const { w: W, h: H } = compSize(INDEX_HTML);

const browser = await chromium.launch({ executablePath: EXECUTABLE, args: ['--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: W, height: H } });
const findings = [];

for (const f of readdirSync(join(ep, 'compositions')).filter(f => f.endsWith('.html'))) {
  const name = f.replace('.html', '');
  await page.goto('file:///' + stageComp(ep, join(ep, 'compositions', f), HOST_CSS).replace(/\\/g, '/'), { waitUntil: 'load' });
  await page.waitForTimeout(120);

  const res = await page.evaluate(async ({ step, W, H }) => {
    const k = Object.keys(window.__timelines || {})[0];
    if (!k) return { error: 'no timeline' };
    const tl = window.__timelines[k];
    const dur = tl.duration();
    /* Only CONTENT counts as ink. Decoration is present in every frame by construction,
       so counting it masks exactly the failure this gate exists to find.
       .drift is the background texture. The vignette/fade layers in g-lone and
       g-centennial are full-bleed divs whose transparency lives in an rgba gradient in
       `background`, not in `opacity` — getComputedStyle reports opacity 1, so each was
       contributing a full 1920x1080 box (~250x the blank floor) on every single frame and
       would have reported PASS even if the map and every marker failed to appear.
       The rule that separates them: real content carries an id or text. */
    /* comps no longer carry id="root" (class/id scoping, 17 Sep 26): walk the whole body. */
    const nodes = [...document.querySelectorAll('body *')].filter(e => !/^(SCRIPT|STYLE|TEMPLATE)$/.test(e.tagName)).filter(
      /* content = readable text or media. An id alone is not content: #sl-drift (a rotating
         background) carried the scale-ladder comp through a 17 s window with no card on
         screen and this gate said PASS (Dujuan U1, 7:02-7:20, 17 Sep 26). */
      e => e.id !== 'root' && !/drift/.test(e.id + ' ' + e.className)
           && (e.textContent.trim() || /^(IMG|VIDEO|CANVAS|svg)$/.test(e.tagName) || e.closest('svg')));
    const out = [];
    for (let t = 0; t <= dur; t += step) {
      tl.seek(t, false);
      let ink = 0;
      for (const e of nodes) {
        const cs = getComputedStyle(e);
        if (cs.visibility === 'hidden' || cs.display === 'none') continue;
        /* opacity is not inherited in computed style: a `{opacity:0}` tween on an ancestor
           (plain opacity, not autoAlpha) still reports the element's OWN opacity as 1, so its
           text children counted as ink while the card was invisible (qc-gates-09). Multiply up
           the chain like graphics_qc.mjs vis() does. */
        let op = 1;
        for (let n = e; n && n.nodeType === 1; n = n.parentElement) op *= parseFloat(getComputedStyle(n).opacity || '1');
        if (op < 0.06) continue;
        const r = e.getBoundingClientRect();
        if (r.width < 1 || r.height < 1) continue;
        if (r.bottom < 0 || r.top > H || r.right < 0 || r.left > W) continue;
        /* leaf-ish only: a wrapper double-counts its children's area */
        if (e.children.length && e.textContent.trim() === '') continue;
        /* an <img> that failed to load still has a layout box — it is not ink */
        if (e.tagName === 'IMG' && !e.naturalWidth) continue;
        ink += Math.min(r.width, W) * Math.min(r.height, H);
      }
      out.push([+t.toFixed(2), Math.round(ink)]);
    }
    return { dur: +dur.toFixed(2), samples: out };
  }, { step: STEP, W, H });

  if (res.error) { findings.push([name, res.error]); continue; }
  const FLOOR = W * H * 0.004;          // ~0.4% of frame = effectively empty
  let run = null;
  for (const [t, ink] of res.samples) {
    if (ink < FLOOR) { if (run === null) run = t; }
    else if (run !== null) {
      if (t - run >= 0.75) findings.push([name, `blank ${run}s -> ${t}s (${(t - run).toFixed(2)}s)`]);
      run = null;
    }
  }
  if (run !== null && res.dur - run >= 0.75)
    findings.push([name, `blank ${run}s -> end ${res.dur}s (${(res.dur - run).toFixed(2)}s)`]);
  console.log(`${name.padEnd(22)} dur ${String(res.dur).padStart(6)}s  samples ${res.samples.length}`);
}
await browser.close();

console.log('');
if (!findings.length) console.log('BLANK SCAN PASS - no composition goes empty for >= 0.75s');
else {
  console.log(`BLANK SCAN FAIL - ${findings.length} finding(s)`);
  for (const [n, d] of findings) console.log('   ', n, '-', d);
}
process.exit(findings.length ? 1 : 0);
