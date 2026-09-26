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

export const hostCss = (indexHtml) =>
  [...indexHtml.matchAll(/<style[^>]*>([\s\S]*?)<\/style>/g)].map(x => x[1]).join('\n');

export function stageComp(ep, file, css, prefix = '') {
  const raw = readFileSync(file, 'utf8');
  const m = raw.match(/<template>([\s\S]*?)<\/template>/);
  const body = (m ? m[1] : raw).replace(/(url\(\s*['"]?|\b(?:src|href)=["'])\.\.\//g, '$1');
  const dir = join(ep, '.qc-tmp');
  mkdirSync(dir, { recursive: true });
  const out = join(dir, prefix + basename(file));
  writeFileSync(out, `<!doctype html><html><head><meta charset="utf-8"><base href="../">
<style>${css}</style>
<style>html,body{margin:0;width:1920px;height:1080px;background:#111;overflow:hidden}</style>
<script src="gsap.min.js"></script></head><body>${body}</body></html>`, 'utf8');
  return out;
}
