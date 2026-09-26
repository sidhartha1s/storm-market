// Preview fallback: the 4 GB RAM floor refused the hyperframes render, so seek the staged page frame by frame.
// usage: node dump_frames.mjs <fps>  -> .qc-tmp/frames/f%04d.jpg (then ffmpeg). Reuses shot.mjs staging (.qc-tmp/preview.html).
import { mkdirSync } from 'fs';
import { chromium, chromiumExecutable } from 'file:///C:/Users/Sidhartha/Automation%20Projects/storm-market/.worktrees/trial-mg-opus/scripts/playwright_env.mjs';
const dir = 'C:/Users/Sidhartha/Automation Projects/storm-market/.worktrees/trial-mg-opus/episodes/demo-mg-showcase';
const fps = +(process.argv[2] || 30), dur = 14;
mkdirSync(dir + '/.qc-tmp/frames', { recursive: true });
const browser = await chromium.launch({ executablePath: chromiumExecutable(), args: ['--allow-file-access-from-files'] });
try {
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  page.on('pageerror', e => console.log('PAGEERROR', String(e)));
  await page.goto('file:///' + dir + '/.qc-tmp/preview.html', { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  const t0 = Date.now();
  for (let i = 0; i < fps * dur; i++) {
    await page.evaluate((t) => window.__timelines['g-tanker-throw'].seek(t, false), i / fps);
    await page.screenshot({ type: 'jpeg', quality: 92, path: `${dir}/.qc-tmp/frames/f${String(i).padStart(4, '0')}.jpg` });
    if (i % 60 === 0) console.log('frame', i, ((Date.now() - t0) / 1000).toFixed(0) + 's');
  }
  console.log('done', ((Date.now() - t0) / 1000).toFixed(0) + 's');
} finally { await browser.close(); }
