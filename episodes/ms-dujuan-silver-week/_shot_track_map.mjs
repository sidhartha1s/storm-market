// One-off: screenshot compositions/track-map.html at t=8 (verify-the-artifact gate).
import { chromium, chromiumExecutable } from '../../scripts/playwright_env.mjs';
import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const ep = dirname(fileURLToPath(import.meta.url));
const TMP = join(ep, '.qc-tmp');
if (!existsSync(TMP)) mkdirSync(TMP, { recursive: true });

const raw = readFileSync(join(ep, 'compositions', 'track-map.html'), 'utf8');
const body = raw.match(/<template>([\s\S]*?)<\/template>/)[1];
const html = `<!doctype html><html><head><meta charset="utf-8">
<style>html,body{margin:0;width:1920px;height:1080px;background:#111;overflow:hidden}</style>
<script src="../gsap.min.js"></script></head><body>${body}</body></html>`;
const outFile = join(TMP, 'track-map.html');
writeFileSync(outFile, html, 'utf8');

const browser = await chromium.launch({ executablePath: chromiumExecutable(), args: ['--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
const errors = [];
page.on('pageerror', e => errors.push(String(e)));

await page.goto('file:///' + outFile.replace(/\\/g, '/'), { waitUntil: 'load' });
await page.waitForTimeout(150);
console.log('ERRORS-EARLY', JSON.stringify(errors));

for (const t of [8]) {
  await page.evaluate((tt) => { const k = Object.keys(window.__timelines)[0]; window.__timelines[k].seek(tt, false); }, t);
  await page.waitForTimeout(60);
  const shotPath = join(ep, 'compositions', `track-map-t${t}.png`);
  await page.screenshot({ path: shotPath });
  console.log('shot', shotPath);
}
await browser.close();
