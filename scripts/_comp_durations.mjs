// One-off: print each composition's registered gsap timeline duration (host windows must not exceed it).
import { chromium, chromiumExecutable } from './playwright_env.mjs';
import { readFileSync, readdirSync, writeFileSync } from 'fs';
import { join, resolve } from 'path';
const ep = resolve(process.argv[2]);
const browser = await chromium.launch({ executablePath: chromiumExecutable() });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
const out = {};
for (const f of readdirSync(join(ep, 'compositions')).filter(n => n.startsWith('g-') && n.endsWith('.html'))) {
  const raw = readFileSync(join(ep, 'compositions', f), 'utf-8');
  const body = (raw.match(/<template>([\s\S]*?)<\/template>/) || [, raw])[1];
  const html = `<!doctype html><html><head><meta charset="UTF-8"><script src="../gsap.min.js"></script></head><body style="margin:0;background:#000">${body}</body></html>`;
  const tmp = join(ep, 'compositions', '_dur_' + f);
  writeFileSync(tmp, html);
  try {
    await page.goto('file:///' + tmp.split('\\').join('/'), { waitUntil: 'load' });
    out[f] = await page.evaluate(() => { const k = Object.keys(window.__timelines || {}); return k.length ? { id: k[0], dur: window.__timelines[k[0]].duration() } : { id: null, dur: null }; });
  } catch (e) { out[f] = { error: String(e).slice(0, 120) }; }
}
await browser.close();
for (const [f, v] of Object.entries(out)) console.log(f.padEnd(30), v.id, v.dur !== undefined ? (v.dur === null ? 'NO TIMELINE' : v.dur.toFixed(2)) : v.error);
