import { chromium, chromiumExecutable } from '../../scripts/playwright_env.mjs';
import fs from 'fs';
import path from 'path';

const ep = process.argv[2];
const idx = fs.readFileSync(path.join(ep, 'index.html'), 'utf8');
const hostCss = [...idx.matchAll(/<style>([\s\S]*?)<\/style>/g)].map(m => m[1]).join('\n');
const gsapSrc = fs.readFileSync(path.join(ep, 'gsap.min.js'), 'utf8');

async function stage(compName) {
  const comp = fs.readFileSync(path.join(ep, 'compositions', compName + '.html'), 'utf8');
  const tpl = comp.match(/<template>([\s\S]*?)<\/template>/)[1];
  const stageHtml = `<!doctype html><html><head><meta charset="utf-8"><style>body{margin:0;width:1920px;height:1080px;overflow:hidden;background:#000}
  .pip{left:1640px !important;top:708px !important;width:240px !important;height:240px !important;border-radius:50%;position:absolute;background:rgba(0,255,0,0.3);}
  ${hostCss}</style>
  <script>${gsapSrc}</script></head><body><div style="position:relative;width:1920px;height:1080px;">${tpl}<div class="pip"></div></div>
  </body></html>`;
  const p = path.join(ep, `_verify_stage_${compName}.html`);
  fs.writeFileSync(p, stageHtml);
  return p;
}

const EXECUTABLE = chromiumExecutable();
const browser = await chromium.launch({ executablePath: EXECUTABLE, args: ['--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
page.on('pageerror', e => console.log('PAGEERROR', e.message));
page.on('console', m => console.log('CONSOLE', m.type(), m.text()));

// --- ladder-intro clearance check ---
{
  const p = await stage('ladder-intro');
  await page.goto('file:///' + p.split(path.sep).join('/'), { waitUntil: 'load' });
  await page.waitForTimeout(200);
  const data = await page.evaluate(() => {
    const tl = window.__timelines['ladder-intro'];
    tl.seek(50.0); // teaser fully visible, row5 dim state settled
    const r5 = document.getElementById('li-r5').getBoundingClientRect();
    const teaser = document.getElementById('li-teaser').getBoundingClientRect();
    return { r5bottom: r5.bottom, teaserTop: teaser.top, gap: teaser.top - r5.bottom, teaserVis: getComputedStyle(document.getElementById('li-teaser')).visibility };
  });
  console.log('ladder-intro clearance:', JSON.stringify(data));
}

// --- ladder-l5 screenshot-diff freeze check (every 2s, flag 6s+ of identical frames) ---
{
  const p = await stage('ladder-l5');
  await page.goto('file:///' + p.split(path.sep).join('/'), { waitUntil: 'load' });
  await page.waitForTimeout(200);
  const hashes = [];
  for (let t = 0; t <= 54.6; t += 2) {
    await page.evaluate((tt) => window.__timelines['ladder-l5'].seek(tt), t);
    const buf = await page.screenshot({ clip: { x: 300, y: 480, width: 1320, height: 400 } });
    const crypto = await import('node:crypto');
    hashes.push({ t, hash: crypto.createHash('md5').update(buf).digest('hex') });
  }
  let maxStreak = 1, streak = 1, streakStart = hashes[0].t;
  let worstStart = null, worstLen = 0;
  for (let i = 1; i < hashes.length; i++) {
    if (hashes[i].hash === hashes[i-1].hash) {
      streak++;
      if (streak > maxStreak) { maxStreak = streak; worstStart = streakStart; worstLen = (streak-1)*2; }
    } else {
      streak = 1; streakStart = hashes[i].t;
    }
  }
  console.log('ladder-l5 screenshot-diff (2s step, region y480-880):', hashes.map(h => h.t + ':' + h.hash.slice(0,6)).join(' '));
  console.log('ladder-l5 longest identical-frame streak:', worstLen + 's starting at ' + worstStart + 's (fail if >=6)');
}

await browser.close();
