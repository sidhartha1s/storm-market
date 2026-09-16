import { chromium, chromiumExecutable } from '../../scripts/playwright_env.mjs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
const ep = dirname(fileURLToPath(import.meta.url));
const outFile = join(ep, '.qc-tmp', 'track-map.html');
const browser = await chromium.launch({ executablePath: chromiumExecutable(), args: ['--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
await page.goto('file:///' + outFile.split('\\').join('/'), { waitUntil: 'load' });
await page.waitForTimeout(100);
await page.evaluate(() => { window.__timelines['track-map'].seek(0, false); });
await page.waitForTimeout(50);
const info = await page.evaluate(() => {
  const x = Math.round(1920 * 0.661), y = Math.round(1080 * 0.29);
  const els = document.elementsFromPoint(x, y);
  return els.slice(0, 6).map(e => ({
    tag: e.tagName, id: e.id, cls: e.getAttribute && e.getAttribute('class'),
    r: e.getAttribute && e.getAttribute('r'), fill: e.getAttribute && e.getAttribute('fill'),
    opacity: e.getAttribute && e.getAttribute('opacity'), styleOpacity: e.style && e.style.opacity,
    cx: e.getAttribute && e.getAttribute('cx'), cy: e.getAttribute && e.getAttribute('cy'),
  }));
});
console.log(JSON.stringify(info, null, 2));
await browser.close();
