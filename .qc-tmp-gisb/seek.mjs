import { chromium, chromiumExecutable } from '../scripts/playwright_env.mjs';
import { join } from 'node:path';
const S = process.argv[2];
const times = [0, 1.58, 2.02, 2.5, 3.56, 4.0, 4.4];
const b = await chromium.launch({ executablePath: chromiumExecutable(), args: ['--allow-file-access-from-files'] });
const sig = () => {
  const tl = window.__timelines['g-intro-strip-back'];
  const root = document.getElementById('g-intro-strip-back-root');
  return Array.from(root.querySelectorAll('*')).map((e) => { const c = getComputedStyle(e); return [e.id, c.opacity, c.visibility, e.getAttribute('transform') || '', c.transform].join('|'); }).join('\n');
};
async function run(order) {
  const p = await b.newPage({ viewport: { width: 640, height: 360 } });
  await p.goto('file:///' + join(S, '_staged.html').split('\\').join('/'), { waitUntil: 'load' });
  await p.waitForTimeout(300);
  const out = {};
  for (const t of order) {
    out[t] = await p.evaluate(([t, f]) => {
      for (const k of Object.keys(window.__timelines)) window.__timelines[k].pause();
      const tl = window.__timelines['g-intro-strip-back'];
      if (f) { tl.seek(0, false); tl.seek(4.4, false); }
      tl.seek(t, false);
      const root = document.getElementById('g-intro-strip-back-root');
      return Array.from(root.querySelectorAll('*')).map((e) => { const c = getComputedStyle(e); return [e.id, c.opacity, c.visibility, e.getAttribute('transform') || '', c.transform].join('|'); }).join('\n');
    }, [t, order !== times]);
  }
  await p.close();
  return out;
}
const fwd = await run(times);
const back = await run([...times].reverse());
let bad = 0;
for (const t of times) {
  if (fwd[t] === back[t]) continue;
  bad++;
  const a = fwd[t].split('\n'), c = back[t].split('\n');
  console.log('MISMATCH at', t);
  a.forEach((l, i) => { if (l !== c[i]) console.log('  fwd ', l, '| back', c[i]); });
}
console.log('seek-order mismatches:', bad, 'of', times.length);
await b.close();
