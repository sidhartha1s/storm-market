// Stage the composition as a standalone page (like graphics_qc's .qc-tmp) and screenshot seek times.
// usage: node shot.mjs name@t [name@t ...]   -> shots/<name>.png
import { readFileSync, writeFileSync } from 'fs';
import { chromium, chromiumExecutable } from 'file:///C:/Users/Sidhartha/Automation%20Projects/storm-market/.worktrees/trial-mg-opus/scripts/playwright_env.mjs';
const dir = 'C:/Users/Sidhartha/Automation Projects/storm-market/.worktrees/trial-mg-opus/episodes/demo-mg-showcase';
const comp = readFileSync(dir + '/compositions/g-tanker-throw.html', 'utf8');
const inner = comp.split('<template>')[1].split('</template>')[0];
const head = ['gsap', 'DrawSVGPlugin', 'CustomEase', 'SplitText'].map(n => `<script src="${n}.min.js"></script>`).join('');
writeFileSync(dir + '/.qc-tmp/preview.html', `<!doctype html><html><head><meta charset="utf-8"><base href="../"><style>html,body{margin:0;width:1920px;height:1080px;overflow:hidden;background:#000}</style>${head}</head><body><div style="position:relative;width:1920px;height:1080px">${inner}</div></body></html>`);
const browser = await chromium.launch({ executablePath: chromiumExecutable(), args: ['--allow-file-access-from-files'] });
try {
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  page.on('pageerror', e => console.log('PAGEERROR', String(e)));
  page.on('console', m => { if (m.type() === 'error' || m.type() === 'warning') console.log('CONSOLE', m.text()); });
  await page.goto('file:///' + dir + '/.qc-tmp/preview.html', { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(300);
  for (const p of process.argv.slice(2)) {
    const [name, t] = p.split('@');
    await page.evaluate((t) => window.__timelines['g-tanker-throw'].seek(+t, false), t);
    await page.waitForTimeout(60);
    await page.screenshot({ path: `${dir}/shots/${name}.png` });
    console.log('shot', name, t);
  }
} finally { await browser.close(); }
