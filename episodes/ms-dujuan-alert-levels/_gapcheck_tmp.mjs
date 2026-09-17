/* One-shot scratch verifier (not committed, deleted after use): loads each composition the same
   way blank_scan.mjs does and captures the console.log("[gap-check] ...") line each comp's own
   timeline script prints, so the round-2 max-gap numbers are read from the real page, not hand math. */
import { chromium, chromiumExecutable } from '../../../scripts/playwright_env.mjs';
import { readFileSync, writeFileSync, readdirSync } from 'node:fs';
import { join } from 'node:path';

const EXECUTABLE = chromiumExecutable();
const ep = process.argv[2];
const gsap = readFileSync(join(ep, 'gsap.min.js'), 'utf8');
const tmp = join(ep, '_gapcheck_stage.html');
const HOST_CSS = [...readFileSync(join(ep, 'index.html'), 'utf8').matchAll(/<style[^>]*>([\s\S]*?)<\/style>/g)].map(x => x[1]).join('\n');

const browser = await chromium.launch({ executablePath: EXECUTABLE, args: ['--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
const lines = [];
page.on('console', msg => { if (msg.text().includes('[gap-check]')) lines.push(msg.text()); });

for (const f of readdirSync(join(ep, 'compositions')).filter(f => f.endsWith('.html'))) {
  const raw = readFileSync(join(ep, 'compositions', f), 'utf8');
  const inner = raw.slice(raw.indexOf('<template>') + 10, raw.lastIndexOf('</template>'));
  writeFileSync(tmp, `<!doctype html><html><head><meta charset="utf-8">
<style>${HOST_CSS}</style>
<style>html,body{margin:0;background:#000;width:1920px;height:1080px;overflow:hidden}</style>
<script>${gsap}</script></head><body>${inner}</body></html>`, 'utf8');
  await page.goto('file:///' + tmp.replace(/\\/g, '/'), { waitUntil: 'load' });
  await page.waitForTimeout(150);
}
await browser.close();
for (const l of lines) console.log(l);
