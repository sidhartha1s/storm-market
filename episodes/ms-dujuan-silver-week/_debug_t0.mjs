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
await page.goto('file:///' + outFile.split('\\').join('/'), { waitUntil: 'load' });
await page.waitForTimeout(100);
await page.evaluate(() => { window.__timelines['track-map'].seek(0, false); });
await page.waitForTimeout(50);

const dump = await page.evaluate(() => {
  const fc = document.getElementById('tm-jma-forecast');
  return Array.from(fc.querySelectorAll('circle')).map(c => ({
    cx: c.getAttribute('cx'), cy: c.getAttribute('cy'),
    r_attr: c.getAttribute('r'), opacity_attr: c.getAttribute('opacity'),
    style_opacity: c.style.opacity, computed_opacity: getComputedStyle(c).opacity,
    computed_display: getComputedStyle(c).display, computed_visibility: getComputedStyle(c).visibility,
  }));
});
console.log('DUMP', JSON.stringify(dump, null, 2));
await browser.close();
