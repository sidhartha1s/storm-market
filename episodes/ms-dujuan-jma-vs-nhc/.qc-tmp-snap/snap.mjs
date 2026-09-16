import { chromium, chromiumExecutable } from '../../../scripts/playwright_env.mjs';
import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'fs';
import { join, resolve, basename, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const EXECUTABLE = chromiumExecutable();
const ep = resolve(__dirname, '..');
const compDir = join(ep, 'compositions');
const OUT = process.env.QC_OUT || 'C:/Users/Sidhartha/AppData/Local/Temp/claude/dujuan/qc-jma';
if (!existsSync(OUT)) mkdirSync(OUT, { recursive: true });

const TMP = join(ep, '.qc-tmp-snap', 'html');
if (!existsSync(TMP)) mkdirSync(TMP, { recursive: true });

function standalone(file) {
  const raw = readFileSync(file, 'utf8');
  const m = raw.match(/<template>([\s\S]*?)<\/template>/);
  const body = m ? m[1] : raw;
  const html = `<!doctype html><html><head><meta charset="utf-8">
<style>html,body{margin:0;width:1920px;height:1080px;background:#111;overflow:hidden}</style>
<script src="../../gsap.min.js"></script></head><body>${body}</body></html>`;
  const out = join(TMP, basename(file));
  writeFileSync(out, html, 'utf8');
  return out;
}

const COMPS = {
  'jma-quote': 51.418,
  'ladder': 49.782,
  'wind-window': 21.0,
  'compare-card': 42.273,
  'translate-table': 63.127,
  'tracking': 19.2,
  'g-close': 16.025,
};

const only = process.argv[2];
const list = only ? [only] : Object.keys(COMPS);

const browser = await chromium.launch({ executablePath: EXECUTABLE, args: ['--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
page.on('pageerror', e => console.error('[pageerror]', String(e).slice(0, 300)));

for (const name of list) {
  const dur = COMPS[name];
  const file = join(compDir, name + '.html');
  const url = 'file:///' + standalone(file).replace(/\\/g, '/');
  await page.goto(url, { waitUntil: 'load' });
  await page.waitForTimeout(150);
  const key = await page.evaluate(() => Object.keys(window.__timelines || {})[0]);
  if (!key) { console.error(`[${name}] NO TIMELINE FOUND`); continue; }
  const points = [0.5, dur * 0.25, dur * 0.5, dur * 0.75, Math.max(0, dur - 0.3)];
  let n = 1;
  for (const t of points) {
    await page.evaluate(([k, tt]) => { window.__timelines[k].seek(tt, false); }, [key, t]);
    await page.waitForTimeout(50);
    const outPath = join(OUT, `${name}-${n}.png`);
    await page.screenshot({ path: outPath });
    console.log(`[${name}] n=${n} t=${t.toFixed(2)}s -> ${outPath}`);
    n++;
  }
}

await browser.close();
