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
const pts = [[1120,454],[1288,591],[1493,643],[1538,733],[1500,817]];
const info = await page.evaluate((pts) => {
  return pts.map(([x,y]) => {
    const els = document.elementsFromPoint(x, y);
    const e = els[0];
    return { x, y, tag: e && e.tagName, id: e && e.id,
      r: e && e.getAttribute && e.getAttribute('r'), fill: e && e.getAttribute && e.getAttribute('fill'),
      styleR: e && e.style && e.style.r, computedR: e && getComputedStyle(e).r };
  });
}, pts);
console.log(JSON.stringify(info, null, 2));

// also dump every forecast-related circle's actual r right now
const dump = await page.evaluate(() => {
  const fc = document.getElementById('tm-jma-forecast');
  return Array.from(fc.querySelectorAll('circle')).map(c => ({
    cx: c.getAttribute('cx'), cy: c.getAttribute('cy'), r_attr: c.getAttribute('r'),
    r_style: c.style.r, r_computed: getComputedStyle(c).r, fill: c.getAttribute('fill'),
  }));
});
console.log('CIRCLES', JSON.stringify(dump, null, 2));
await browser.close();
