import { chromium, chromiumExecutable } from './playwright_env.mjs';
import { readFileSync, writeFileSync, mkdirSync } from 'fs';
import os from 'os';
import path from 'path';

const E = 'C:/Users/Sidhartha/Automation Projects/storm-market/.worktrees/ep-1974-super-outbreak/episodes/ep-1974-super-outbreak';
const OUT = path.join(os.tmpdir(), 'mg2', 'r3shots');
mkdirSync(OUT, { recursive: true });

// [file, [ [label, seekTime], ... ] ]  -- seek to cue+0.35 (mid-fade-in) to visually confirm each new row
const plan = [
  ['g-map-i', [
    ['r0-148tornadoes', 47.2],
    ['r3-2600miles', 53.55],
    ['r4-216pm-f5', 75.28],
    ['exit', 83.2],
  ]],
  ['g-map-a1', [
    ['f1-15min', 20.55],
    ['f2-330pm', 61.82],
  ]],
  ['g-map-a2', [
    ['r1-30min', 7.45],
  ]],
  ['g-map-a3', [
    ['fact1-540pm', 2.2],
    ['fact4-361000', 38.05],
    ['fact6-18dead', 109.9],
    ['fact8-4states', 122.8],
  ]],
  ['g-map-a4', [
    ['fact1-630pm', 1.5],
    ['fact2-28dead', 12.0],
    ['fact4-101miles', 60.5],
    ['fact-cleared-before-guin', 66.5],
  ]],
];

const browser = await chromium.launch({ executablePath: chromiumExecutable() });
const results = {};
for (const [name, shots] of plan) {
  const raw = readFileSync(`${E}/compositions/${name}.html`, 'utf-8');
  const body = raw.match(/<template>([\s\S]*?)<\/template>/)[1];
  const html = `<!doctype html><html><head><meta charset="UTF-8"><script src="../gsap.min.js"></script></head><body style="margin:0;background:#000">${body}</body></html>`;
  const tmpFile = `${E}/compositions/_debug_${name}.html`;
  writeFileSync(tmpFile, html);
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  await page.goto('file:///' + tmpFile.split('\\').join('/'), { waitUntil: 'load' });
  const dur = await page.evaluate((n) => window.__timelines[n].duration(), name);
  results[name] = { duration: dur, shots: [] };
  for (const [label, t] of shots) {
    await page.evaluate(([n, tt]) => window.__timelines[n].seek(tt, false), [name, t]);
    const file = path.join(OUT, `${name}__${label}.png`);
    await page.screenshot({ path: file });
    results[name].shots.push({ label, t, file });
  }
  await page.close();
}
await browser.close();
console.log(JSON.stringify(results, null, 2));
