// One-off: screenshot the staged popfig mock pages (old vs new eyebrow treatment).
import { chromium, chromiumExecutable } from './playwright_env.mjs';
import { resolve } from 'path';
import { pathToFileURL } from 'url';
const ep = resolve(process.argv[2]);
const browser = await chromium.launch({ executablePath: chromiumExecutable() });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
for (const n of ['popfig_old', 'popfig_new']) {
  await page.goto(pathToFileURL(resolve(ep, '_' + n + '_tmp.html')).href, { waitUntil: 'load' });
  await page.screenshot({ path: resolve(ep, '_framesweep', n + '.png') });
}
await browser.close();
console.log('shot');
