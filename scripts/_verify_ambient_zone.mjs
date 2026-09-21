import { chromium, chromiumExecutable } from './playwright_env.mjs';
import { readFileSync, writeFileSync, mkdirSync } from 'fs';
import os from 'os';
import path from 'path';
import { execSync } from 'child_process';

const E = 'C:/Users/Sidhartha/Automation Projects/storm-market/.worktrees/ep-1974-super-outbreak/episodes/ep-1974-super-outbreak';
const SCRATCH = path.join(os.tmpdir(), 'mg2', 'ambient_zone');
mkdirSync(SCRATCH, { recursive: true });

const FILES = {
  'g-map-i':  { dur: 83.492,  cues: [10.90, 46.85, 49.61, 51.59, 74.93] },
  'g-map-a1': { dur: 137.273, cues: [2.76, 36.80, 61.27] },
  'g-map-a2': { dur: 29.946,  cues: [15.20, 19.36] },
  'g-map-a3': { dur: 126.290, cues: [1.68, 30.84, 33.37, 78.03, 114.70] },
  'g-map-a4': { dur: 78.5,    cues: [8.63, 16.95, 28.42, 31.92, 66.0, 66.77] },
  'g-map-a6': { dur: 49.072,  cues: [3.72, 19.44, 43.86] },
  'g-plane':  { dur: 28.163,  cues: [14.92, 17.12, 20.72, 25.82] },
};

function pickTime(base, cues, dur) {
  const offsets = [0, -1, 1, -2, 2, -2.5, 2.5, -3, 3, -4, 4, -5, 5];
  for (const off of offsets) {
    const t = base + off;
    if (t < 1 || t > dur - 1.5) continue;
    const minDist = Math.min(...cues.map(c => Math.abs(t - c)));
    if (minDist >= 2) return t;
  }
  return base; // fallback
}

function pngDiff(pathA, pathB) {
  // ffmpeg psnr filter: identical frames -> psnr average "inf" (no motion); any visible change lowers it.
  let out = '';
  try {
    out = execSync(`ffmpeg -i "${pathA}" -i "${pathB}" -lavfi psnr -f null - 2>&1`, { encoding: 'utf-8' });
  } catch (e) {
    out = (e.stdout || '') + (e.stderr || '');
  }
  const m = out.match(/average:([\d.]+|inf)/);
  return m ? m[1] : 'unknown';
}

const browser = await chromium.launch({ executablePath: chromiumExecutable() });
const zoneReport = {};
const ambientReport = {};

for (const [name, { dur, cues }] of Object.entries(FILES)) {
  const raw = readFileSync(`${E}/compositions/${name}.html`, 'utf-8');
  const body = raw.match(/<template>([\s\S]*?)<\/template>/)[1];
  const html = `<!doctype html><html><head><meta charset="UTF-8"><script src="../gsap.min.js"></script></head><body style="margin:0;background:#000">${body}</body></html>`;
  const tmp = path.join(SCRATCH, `${name}.html`);
  writeFileSync(tmp, html);
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  await page.goto('file:///' + tmp.split('\\').join('/'), { waitUntil: 'load' });

  // --- presenter zone check across the whole DUR, fine steps ---
  const zoneHits = await page.evaluate(([name, dur]) => {
    const tl = window.__timelines[name];
    const root = document.querySelector('#root').getBoundingClientRect();
    const sel = '.row, .caption, .foot, .ticker, .hl, .eyebrow, .sub, .val, .maplab, .lab';
    const hits = [];
    const steps = Math.min(400, Math.ceil(dur / 0.25));
    for (let i = 0; i <= steps; i++) {
      const t = Math.min(dur, i * (dur / steps));
      tl.seek(t, false);
      document.querySelectorAll(sel).forEach(el => {
        const cs = getComputedStyle(el);
        if (parseFloat(cs.opacity) < 0.05) return;
        const r = el.getBoundingClientRect();
        const rect = { left: r.left - root.left, top: r.top - root.top, right: r.right - root.left, bottom: r.bottom - root.top };
        if (rect.right >= 1600 && rect.bottom >= 680) {
          hits.push({ t, id: el.id || el.className, rect });
        }
      });
    }
    return hits;
  }, [name, dur]);
  zoneReport[name] = zoneHits.length ? zoneHits.slice(0, 5) : [];

  // --- ambient motion diff check at 25/50/85% of DUR, t and t+2 ---
  const points = [0.25, 0.5, 0.85].map(f => pickTime(dur * f, cues, dur));
  const pairShots = [];
  for (const t of points) {
    await page.evaluate(([name, t]) => window.__timelines[name].seek(t, false), [name, t]);
    const fA = path.join(SCRATCH, `${name}__${t.toFixed(2)}_a.png`);
    await page.screenshot({ path: fA });
    await page.evaluate(([name, t]) => window.__timelines[name].seek(t + 2, false), [name, t]);
    const fB = path.join(SCRATCH, `${name}__${t.toFixed(2)}_b.png`);
    await page.screenshot({ path: fB });
    const psnrAvg = pngDiff(fA, fB);
    pairShots.push({ t, tPlus2: t + 2, psnrAvg });
  }
  ambientReport[name] = pairShots;
  await page.close();
}
await browser.close();
console.log(JSON.stringify({ ambientReport, zoneReport }, null, 2));
