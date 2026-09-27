/* Motion spans per composition, read from the BUILT timeline (for beat_density.py).
 * Usage: node scripts/beat_probe.mjs <episode-dir> <comp-id>=<host window s> ...
 * Last stdout line: JSON { "<comp-id>": { "spans": [[start, end], ...] } | { "error": "..." } }.
 * Each comp is staged like graphics_qc stages it; what counts as motion is stage_comp.mjs motionSpans. */
import { chromium, chromiumExecutable } from './playwright_env.mjs';
import { readFileSync } from 'fs';
import { join, resolve } from 'path';
import { hostCss, motionSpans, stageComp } from './stage_comp.mjs';

const ep = resolve(process.argv[2]);
const HOST_CSS = hostCss(readFileSync(join(ep, 'index.html'), 'utf8'));

const PROBE = (win) => `(() => {
  const tl = window.__timelines && window.__timelines[Object.keys(window.__timelines)[0]];
  if (!tl) return { error: 'no timeline registered' };
  return { spans: ${motionSpans(win)} };
})()`;

const browser = await chromium.launch({ executablePath: chromiumExecutable(), args: ['--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
const out = {};
for (const arg of process.argv.slice(3)) {
  const [id, win] = [arg.slice(0, arg.lastIndexOf('=')), +arg.slice(arg.lastIndexOf('=') + 1)];
  await page.goto('file:///' + stageComp(ep, join(ep, 'compositions', id + '.html'), HOST_CSS, 'beat-').replace(/\\/g, '/'), { waitUntil: 'load' });
  await page.waitForTimeout(120);
  out[id] = await page.evaluate(PROBE(win)).catch(e => ({ error: String(e).split('\n')[0].slice(0, 200) }));
}
await browser.close();
console.log(JSON.stringify(out));
