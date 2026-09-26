/* Pre-render blank check: seek every composition across its whole timeline and measure
   how much visible ink is on screen. Catches a graphic that renders empty or near-empty
   at some point without waiting 40 minutes for a render to prove it. */
import { chromium, chromiumExecutable } from './playwright_env.mjs';
import { readFileSync, writeFileSync, readdirSync, existsSync } from 'node:fs';
import { join } from 'node:path';
import { hostCss } from './stage_comp.mjs';

const EXECUTABLE = chromiumExecutable();
const ep = process.argv[2];
const STEP = 0.25;
const gsap = readFileSync(join(ep, 'gsap.min.js'), 'utf8');
const tmp = join(ep, '_blank_tmp.html');
// Host-style injection: hyperframes mounts comps INSIDE index.html's DOM, so the page stylesheet
// applies to comp elements (17 Sep 26: host `.chip{bottom:300px}` stretched a comp chip into a 720 px
// panel; every standalone gate passed). Staging must carry the host <style> blocks.
const HOST_CSS = hostCss(readFileSync(join(ep, 'index.html'), 'utf8'));

const browser = await chromium.launch({ executablePath: EXECUTABLE, args: ['--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
const findings = [];

for (const f of readdirSync(join(ep, 'compositions')).filter(f => f.endsWith('.html'))) {
  const name = f.replace('.html', '');
  const raw = readFileSync(join(ep, 'compositions', f), 'utf8');
  const inner = raw.slice(raw.indexOf('<template>') + 10, raw.lastIndexOf('</template>'));
  writeFileSync(tmp, `<!doctype html><html><head><meta charset="utf-8">
<style>${HOST_CSS}</style>
<style>html,body{margin:0;background:#000;width:1920px;height:1080px;overflow:hidden}</style>
<script>${gsap}</script></head><body>${inner}</body></html>`, 'utf8');
  await page.goto('file:///' + tmp.replace(/\\/g, '/'), { waitUntil: 'load' });
  await page.waitForTimeout(120);

  const res = await page.evaluate(async (step) => {
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
        if (r.bottom < 0 || r.top > 1080 || r.right < 0 || r.left > 1920) continue;
        /* leaf-ish only: a wrapper double-counts its children's area */
        if (e.children.length && e.textContent.trim() === '') continue;
        /* an <img> that failed to load still has a layout box — it is not ink */
        if (e.tagName === 'IMG' && !e.naturalWidth) continue;
        ink += Math.min(r.width, 1920) * Math.min(r.height, 1080);
      }
      out.push([+t.toFixed(2), Math.round(ink)]);
    }
    return { dur: +dur.toFixed(2), samples: out };
  }, STEP);

  if (res.error) { findings.push([name, res.error]); continue; }
  const FLOOR = 1920 * 1080 * 0.004;          // ~0.4% of frame = effectively empty
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
