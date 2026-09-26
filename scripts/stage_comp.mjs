// Stage a <template>-wrapped composition as a bare page so a gate can load it standalone.
// One copy for every gate: overlap_check once staged without <base href>, so every comp that loads
// a script or asset by relative path (Three.js vendor files) failed "timeline not registered".
// The page lands in <ep>/.qc-tmp/, one level down like compositions/, so <base href="../"> points
// every relative url at the episode root; a leading ../ is stripped so both path conventions
// (`media/x` and `../media/x`) land there (qc-gates-08). hostCss carries index.html's <style>
// blocks, because hyperframes mounts comps inside that DOM.
import { readFileSync, writeFileSync, mkdirSync } from 'fs';
import { join, basename } from 'path';

// In-page expression (needs `tl` in scope), shared by graphics_qc and beat_probe: a timeline-level
// onUpdate plus a canvas covering a quarter of the frame is a renderer redrawn every frame (the
// Three.js/WebGL pattern), one continuous span. The quarter keeps a grain tile beside a counter
// onUpdate from excusing a frozen comp. It does not check that the callback draws.
export const CANVAS_RENDERER = `(typeof tl.eventCallback('onUpdate') === 'function' && [...document.querySelectorAll('canvas')]
  .some(c => { const r = c.getBoundingClientRect(); return r.width * r.height >= 0.25 * 1920 * 1080; }))`;

/* In-page expression (needs `tl`): the [start, end] spans in which something moves over [0, win] s.
 * The one stillness rule, shared by beat_density (via beat_probe) and graphics_qc's idle check:
 *  1. a tween (nested timelines included) that animates a property of a DOM/SVG element, over
 *     startTime .. startTime + totalDuration (repeats included);
 *  2. CANVAS_RENDERER: one span over the whole timeline;
 *  3. anything else only where the page measurably changes: the timeline steps forward 0.1 s at a
 *     time with events on (onUpdate hubs, proxy tweens, tl.call fire), and a step whose body markup
 *     differs from the step before is a span.
 * A tween on a plain object (a `tl.to({}, {duration: N}, 0)` clock, a proxy, a uniform) or with no
 * animated property never counts from its schedule, only through 2 or 3. A clock changes nothing,
 * so it is not motion. Rule 3 moves the playhead: seek again before measuring anything. */
export const motionSpans = (win) => `(() => {
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
  for (let i = 1; i * 0.1 <= ${win} + 1e-9; i++) {
    const a = +((i - 1) * 0.1).toFixed(3), b = +(i * 0.1).toFixed(3);
    tl.seek(b, false);
    const now = document.body.innerHTML;
    if (now !== prev) { if (run && run[1] === a) run[1] = b; else spans.push(run = [a, b]); }
    prev = now;
  }
  return spans;
})()`;

export const hostCss = (indexHtml) =>
  [...indexHtml.matchAll(/<style[^>]*>([\s\S]*?)<\/style>/g)].map(x => x[1]).join('\n');

export function stageComp(ep, file, css, prefix = '') {
  const raw = readFileSync(file, 'utf8');
  const m = raw.match(/<template>([\s\S]*?)<\/template>/);
  const body = (m ? m[1] : raw).replace(/(url\(\s*['"]?|\b(?:src|href)=["'])\.\.\//g, '$1');
  const dir = join(ep, '.qc-tmp');
  mkdirSync(dir, { recursive: true });
  const out = join(dir, prefix + basename(file));
  // the host's own <script src> tags too (GSAP plugins): a moves comp calling DrawSVGPlugin died
  // "no timeline registered" standalone although it renders fine inside index.html
  const hostJs = [...readFileSync(join(ep, 'index.html'), 'utf8').matchAll(/<script\b[^>]*\bsrc="([^"]+)"/g)]
    .map(x => x[1]).filter(s => s !== 'gsap.min.js').map(s => `<script src="${s}"></script>`).join('');
  writeFileSync(out, `<!doctype html><html><head><meta charset="utf-8"><base href="../">
<style>${css}</style>
<style>html,body{margin:0;width:1920px;height:1080px;background:#111;overflow:hidden}</style>
<script src="gsap.min.js"></script>${hostJs}</head><body>${body}</body></html>`, 'utf8');
  return out;
}
