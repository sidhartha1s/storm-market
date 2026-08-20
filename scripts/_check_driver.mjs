// Usage: node scripts/_check_driver.mjs <episode-dir>
// Loads the episode page headless and reports registered timelines + page errors.
import { pathToFileURL } from 'node:url';
import { resolve } from 'node:path';
import { chromium, chromiumExecutable } from './playwright_env.mjs';
const epDir = process.argv[2];
if (!epDir) { console.error('usage: node scripts/_check_driver.mjs <episode-dir>'); process.exit(2); }
const browser = await chromium.launch({ headless: true, executablePath: chromiumExecutable() });
const page = await browser.newPage();
const errs = [];
page.on('pageerror', e => errs.push('PAGEERROR: ' + e.message));
page.on('console', m => { if (m.type() === 'error') errs.push('CONSOLE: ' + m.text()); });
await page.goto(pathToFileURL(resolve(epDir, 'index.html')).href, { waitUntil: 'load', timeout: 30000 });
await page.waitForTimeout(2500);
const reg = await page.evaluate(() => Object.keys(window.__timelines || {}));
console.log('registered timelines:', JSON.stringify(reg));
console.log(errs.slice(0, 6).join('\n') || 'no page errors');
await browser.close();
