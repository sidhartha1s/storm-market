import { chromium, chromiumExecutable } from './playwright_env.mjs';
import { readFileSync, writeFileSync } from 'fs';
import os from 'os';
import path from 'path';

const E = 'C:/Users/Sidhartha/Automation Projects/storm-market/.worktrees/ep-1974-super-outbreak/episodes/ep-1974-super-outbreak';
const raw = readFileSync(E + '/compositions/g-map-i.html', 'utf-8');
const body = raw.match(/<template>([\s\S]*?)<\/template>/)[1];
const html = `<!doctype html><html><head><meta charset="UTF-8"><script src="../gsap.min.js"></script></head><body style="margin:0;background:#000">${body}</body></html>`;
const tmp = path.join(os.tmpdir(), 'mg2', 'check_i.html');
writeFileSync(tmp, html);

const browser = await chromium.launch({ executablePath: chromiumExecutable() });
const page = await browser.newPage();
page.on('console', m => console.log('CONSOLE:', m.text()));
page.on('pageerror', e => console.log('PAGEERROR:', e.message));
await page.goto('file:///' + tmp.split('\\').join('/'), { waitUntil: 'load' });
const keys = await page.evaluate(() => Object.keys(window.__timelines || {}));
console.log('keys', keys);
await browser.close();
