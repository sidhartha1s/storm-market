/* Motion spans per composition, read from the BUILT timeline (for beat_density.py).
 * Usage: node scripts/beat_probe.mjs <episode-dir> <comp-id>=<host window s> ...
 * Last stdout line: JSON { "<comp-id>": { "spans": [[start, end], ...] } | { "error": "..." } }.
 *
 * A source regex could not see durations via an alias, tweens made inside helper functions
 * (library/inhouse/moves) or an onUpdate hub, so each comp is staged the way graphics_qc stages it
 * and its timeline is read at run time. Motion is:
 *  1. a tween (nested timelines included) that animates a property of a DOM/SVG element, over
 *     startTime .. startTime + totalDuration (repeats included);
 *  2. the canvas-renderer rule (stage_comp.mjs CANVAS_RENDERER): one span over the whole timeline;
 *  3. anything else only where the page measurably changes: the timeline steps forward STEP s at a
 *     time with events on (onUpdate hubs, proxy tweens, tl.call fire), and a step whose body markup
 *     differs from the step before is a span.
 * A tween on a plain object (a `tl.to({}, {duration: N}, 0)` clock, a proxy, a uniform) or with no
 * animated property never counts from its schedule, only through 2 or 3. A clock changes nothing,
 * so it is not motion. */
import { chromium, chromiumExecutable } from './playwright_env.mjs';
import { readFileSync } from 'fs';
import { join, resolve } from 'path';
import { CANVAS_RENDERER, hostCss, stageComp } from './stage_comp.mjs';

const STEP = 0.1;  // resolution of rule 3; rules 1 and 2 are exact
const ep = resolve(process.argv[2]);
const HOST_CSS = hostCss(readFileSync(join(ep, 'index.html'), 'utf8'));

const PROBE = (win) => `(() => {
  const tl = window.__timelines && window.__timelines[Object.keys(window.__timelines)[0]];
  if (!tl) return { error: 'no timeline registered' };
  const spans = [];
  if (${CANVAS_RENDERER}) spans.push([0, tl.duration()]);
  const NOT_PROP = /^(on[A-Z][A-Za-z]*|callbackScope|data|defaults|delay|duration|ease|id|immediateRender|inherit|lazy|overwrite|parent|paused|repeat|repeatDelay|repeatRefresh|reversed|runBackwards|stagger|startAt|yoyo|yoyoEase)$/;
  for (const t of tl.getChildren(true, true, false)) {
    if (!t.targets().some(x => x instanceof Element) || !Object.keys(t.vars).some(k => !NOT_PROP.test(k))) continue;
    let s = t.startTime();  // ponytail: ignores a nested timeline's timeScale; add it if a comp ever scales one
    for (let p = t.parent; p && p !== tl; p = p.parent) s += p.startTime();
    spans.push([s, s + t.totalDuration()]);
  }
  tl.seek(0, false);
  let prev = document.body.innerHTML, run = null;
  for (let i = 1; i * ${STEP} <= ${win} + 1e-9; i++) {
    const a = +((i - 1) * ${STEP}).toFixed(3), b = +(i * ${STEP}).toFixed(3);
    tl.seek(b, false);
    const now = document.body.innerHTML;
    if (now !== prev) { if (run && run[1] === a) run[1] = b; else spans.push(run = [a, b]); }
    prev = now;
  }
  return { spans };
})()`;

const browser = await chromium.launch({ executablePath: chromiumExecutable(), args: ['--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
const out = {};
for (const arg of process.argv.slice(3)) {
  const [id, win] = [arg.slice(0, arg.lastIndexOf('=')), +arg.slice(arg.lastIndexOf('=') + 1)];
  await page.goto('file:///' + stageComp(ep, join(ep, 'compositions', id + '.html'), HOST_CSS, 'beat-').replace(/\\/g, '/'), { waitUntil: 'load' });
  await page.waitForTimeout(120);
  out[id] = await page.evaluate(PROBE(win));
}
await browser.close();
console.log(JSON.stringify(out));
