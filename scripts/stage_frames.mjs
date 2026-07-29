/* One-shot: screenshot specific compositions at specific timeline seconds, for a spacing
   eyeball on rebuilt graphics. Not a gate — deleted after use. */
import { chromium, chromiumExecutable } from './playwright_env.mjs';
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const EXECUTABLE = chromiumExecutable();
const ep = process.argv[2];
const outdir = process.argv[3];
mkdirSync(outdir, { recursive: true });
const gsap = readFileSync(join(ep, 'gsap.min.js'), 'utf8');
const tmp = join(ep, '_stage_tmp.html');

// comp -> [seconds to shoot]
const SHOTS = {
  'g-wordban': [8, 17, 24],
  'g-forecast': [10, 13, 19],
  'g-sources': [12, 22, 27],
  'g-panel-cost': [7, 12, 20],
  'g-wires': [15, 27],
};

const browser = await chromium.launch({ executablePath: EXECUTABLE, args: ['--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });

for (const [name, secs] of Object.entries(SHOTS)) {
  const raw = readFileSync(join(ep, 'compositions', `${name}.html`), 'utf8');
  const inner = raw.replace(/[\s\S]*<template>/, '').replace(/<\/template>[\s\S]*/, '');
  const html = `<!doctype html><html><head><meta charset="utf-8">
    <script>${gsap}</script></head><body style="margin:0;background:#05070a">${inner}</body></html>`;
  writeFileSync(tmp, html);
  await page.goto('file://' + tmp.replace(/\\/g, '/'));
  await page.waitForFunction(() => window.__timelines && Object.keys(window.__timelines).length, { timeout: 8000 });
  const key = await page.evaluate(() => Object.keys(window.__timelines)[0]);
  for (const t of secs) {
    await page.evaluate(([k, tt]) => window.__timelines[k].seek(tt, false), [key, t]);
    await page.waitForTimeout(120);
    await page.screenshot({ path: join(outdir, `${name}_${t}s.png`) });
  }
  console.log(`${name}: ${secs.length} frames`);
}
await browser.close();
console.log('done ->', outdir);
