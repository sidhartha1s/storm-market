// Stage the composition alone and screenshot it at given times. Usage: node shots/shoot.mjs <prefix> t1 t2 ...
import { readFileSync, writeFileSync } from 'node:fs';
import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';
const here = path.dirname(fileURLToPath(import.meta.url));
const ep = path.dirname(here);
const env = await import(pathToFileURL(path.join(ep, '..', '..', 'scripts', 'playwright_env.mjs')).href);
const src = readFileSync(path.join(ep, 'compositions', 'g-elreno-width.html'), 'utf8');
const inner = src.split('<template>')[1].split('</template>')[0];
writeFileSync(path.join(here, 'stage.html'), `<!doctype html><html><head><meta charset="UTF-8"><base href="../">
<script src="vendor/gsap.min.js"></script><style>body{margin:0;background:#000}#stage-root{position:relative;width:1920px;height:1080px;overflow:hidden}</style>
</head><body><div id="stage-root">${inner}</div></body></html>`);
const [prefix, ...times] = process.argv.slice(2);
const browser = await env.chromium.launch({ executablePath: env.chromiumExecutable(), args: ['--use-angle=d3d11', '--ignore-gpu-blocklist'] });
try {
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  page.on('pageerror', (e) => console.log('PAGEERROR', e.message));
  page.on('console', (m) => { if (m.type() === 'error') console.log('CONSOLE', m.text()); });
  await page.goto(pathToFileURL(path.join(here, 'stage.html')).href);
  await page.waitForFunction(() => window.__timelines && window.__timelines['g-elreno-width']);
  console.log('GL', await page.evaluate(() => { const g = document.createElement('canvas').getContext('webgl'); const d = g.getExtension('WEBGL_debug_renderer_info'); return d ? g.getParameter(d.UNMASKED_RENDERER_WEBGL) : 'n/a'; }));
  for (const t of times) {
    await page.evaluate((tt) => window.__timelines['g-elreno-width'].time(tt), Number(t));
    const out = path.join(here, `${prefix}-${t}.png`);
    await page.screenshot({ path: out });
    console.log('shot', out);
  }
} finally { await browser.close(); }
