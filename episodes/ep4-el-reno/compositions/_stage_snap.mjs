import { readFileSync, mkdirSync, existsSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { chromium } from '../../../scripts/playwright_env.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const gsapPath = join(__dirname, '..', 'gsap.min.js');
const gsapSrc = readFileSync(gsapPath, 'utf8');
const durations = JSON.parse(readFileSync(join(__dirname, '_durations.json'), 'utf8'));

const comps = process.argv.slice(2);
if (!comps.length) { console.error('usage: node _stage_snap.mjs <comp1> <comp2> ...'); process.exit(1); }

const outRoot = join(__dirname, 'media', '_snap');
mkdirSync(outRoot, { recursive: true });

const browser = await chromium.launch();
for (const compFile of comps) {
  const id = compFile.replace(/\.html$/, '');
  const html = readFileSync(join(__dirname, compFile), 'utf8');
  const m = html.match(/<template>([\s\S]*)<\/template>/);
  if (!m) { console.error(`${id}: no <template> found`); continue; }
  const templateInner = m[1];

  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  page.on('pageerror', e => console.error(`${id} pageerror:`, e.message));
  page.on('console', msg => { if (msg.type() === 'error') console.error(`${id} console:`, msg.text()); });

  await page.setContent('<!doctype html><html><head><meta charset="UTF-8"></head><body></body></html>');
  await page.addScriptTag({ content: gsapSrc });
  await page.evaluate((inner) => {
    document.body.innerHTML = inner;
  }, templateInner);

  const dur = await page.evaluate((id) => {
    const tl = window.__timelines && window.__timelines[id];
    return tl ? tl.duration() : null;
  }, id);

  if (dur == null) { console.error(`${id}: timeline not found in window.__timelines["${id}"]`); await page.close(); continue; }

  const total = durations[id] ?? dur;
  const n = 6;
  const seeks = Array.from({ length: n }, (_, i) => +(total * i / (n - 1)).toFixed(2));
  // avoid exact 0 and exact end edge cases
  seeks[0] = 0.05;
  seeks[n - 1] = Math.max(0.05, total - 0.1);

  const dir = join(outRoot, id);
  mkdirSync(dir, { recursive: true });

  for (const t of seeks) {
    await page.evaluate(({ id, t }) => {
      const tl = window.__timelines[id];
      tl.seek(t, false);
    }, { id, t });
    await page.waitForTimeout(50);
    const file = join(dir, `${t}.png`);
    await page.screenshot({ path: file });
    console.log(`${id} @ ${t}s -> ${file}`);
  }
  await page.close();
}
await browser.close();
