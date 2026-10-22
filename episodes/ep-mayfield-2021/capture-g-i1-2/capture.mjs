// Capture frames of g-i1-2 (staged alone on its own ground) in both seek orders, compare, and measure frame coverage.
import { chromium, chromiumExecutable } from 'file:///C:/Users/Sidhartha/Automation%20Projects/storm-market/.claude/worktrees/ep-mayfield-2021-a6d084/scripts/playwright_env.mjs';
import { hostCss, stageComp } from 'file:///C:/Users/Sidhartha/Automation%20Projects/storm-market/.claude/worktrees/ep-mayfield-2021-a6d084/scripts/stage_comp.mjs';
import { readFileSync, mkdirSync, writeFileSync } from 'fs';
import { createHash } from 'crypto';

const EP = 'C:/Users/Sidhartha/Automation Projects/storm-market/.claude/worktrees/ep-mayfield-2021-a6d084/episodes/ep-mayfield-2021';
const OUT = `${EP}/capture-g-i1-2/frames`; mkdirSync(OUT, { recursive: true });
const css = hostCss(readFileSync(`${EP}/index.html`, 'utf8'));
const file = stageComp(EP, `${EP}/compositions/g-i1-2.html`, css, '_cap_');
const T = [0, 0.033, 1.18, 2.56, 3.12, 3.8, 4.3, 4.5, 4.68, 5.1];

const browser = await chromium.launch({ executablePath: chromiumExecutable(), args: ['--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
page.on('console',m=>console.log('console:',m.text()));page.on('pageerror',e=>console.log('pageerror:',e.message));
await page.goto('file:///' + file.replaceAll('\\', '/'));
await page.waitForTimeout(800);
await page.waitForTimeout(500);
const seek = async t => { await page.evaluate(t => { window.__timelines['g-i1-2'].seek(t, false); }, t); await page.waitForTimeout(80); };
const shot = async (name) => { const b = await page.screenshot({ path: `${OUT}/${name}.png` }); return b; };
const h = b => createHash('md5').update(b).digest('hex');
const res = {};
const fwd = {};
for (const t of T) { await seek(t); fwd[t] = h(await shot(`fwd_${t}`)); }
for (const t of T) {
  await seek(0); await seek(Math.min(t + 1.5, 5.17)); await seek(t);
  const b2 = h(await shot(`back_${t}`));
  res[t] = { fwd: fwd[t], back: b2, match: fwd[t] === b2 };
}
// geometry readout at the key times
const geo = {};
for (const t of [0, 1.18, 3.62, 4.2, 5.1]) {
  await seek(t);
  geo[t] = await page.evaluate(() => {
    const q = id => document.getElementById(id); const r = e => { const b = e.getBoundingClientRect(); return [b.left, b.top, b.right, b.bottom].map(v => +v.toFixed(1)); };
    const cs = id => { const s = getComputedStyle(q(id)); return { op: s.opacity, vis: s.visibility }; };
    return { sheet: r(q('g-i1-2-sheet')), band: r(q('g-i1-2-band1')), band2: r(q('g-i1-2-band2')), strip: r(q('g-i1-2-strip')), eyebrow: r(q('g-i1-2-eyebrow')), source: r(q('g-i1-2-source')), quote: r(q('g-i1-2-quote')), stage: cs('g-i1-2-stage'), eyebrowS: cs('g-i1-2-eyebrow'), bandS: cs('g-i1-2-band1'), stripS: cs('g-i1-2-strip') };
  });
}
writeFileSync(`${OUT}/seek_and_geo.json`, JSON.stringify({ res, geo }, null, 2));
console.log(JSON.stringify(res, null, 1)); console.log(JSON.stringify(geo, null, 1));
await browser.close();
