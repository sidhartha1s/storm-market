// usage: node shot.mjs <pose|tl> <prefix> t1 t2 ...   (stages the comp template in a bare gsap page, screenshots to shots/)
import { readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
const here = dirname(fileURLToPath(import.meta.url));
const { chromium } = await import(pathToFileURL(join(here, '..', '..', 'scripts', 'playwright_env.mjs')).href);
const [mode, prefix, ...ts] = process.argv.slice(2);
const src = readFileSync(join(here, 'compositions', 'g-tanker-throw.html'), 'utf8');
const inner = src.slice(src.indexOf('<template>') + 10, src.indexOf('</template>'));
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
const errs = [];
page.on('pageerror', (e) => errs.push(String(e)));
for (const t of ts) {
  const pre = mode === 'pose' ? `<script>window.__POSE=${t};</script>` : '';
  writeFileSync(join(here, '_stage.html'), `<!doctype html><html><head><meta charset="utf-8"><style>body{margin:0;background:#000}</style><script src="gsap.min.js"></script>${pre}</head><body>${inner}</body></html>`);
  await page.goto(pathToFileURL(join(here, '_stage.html')).href);
  await page.evaluate(() => document.fonts.ready);
  if (mode === 'tl') await page.evaluate((t) => { const tl = window.__timelines['g-tanker-throw']; tl.time(0); tl.time(t); }, Number(t));
  await page.screenshot({ path: join(here, 'shots', `${prefix}-${t}.png`) });
}
console.log('errors:', errs.length ? errs.join(' | ') : 'none');
await browser.close();
