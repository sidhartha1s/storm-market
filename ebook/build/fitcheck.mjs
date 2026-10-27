/* fitcheck — overflow gate for fixed-page book layout.
   Every .page is a hard 6x9 box with overflow:hidden, so content that does not fit is
   SILENTLY CLIPPED. Across ~490 pages that is unacceptable, so this is a hard gate:
   exit 1 if any page overflows its content box or collides with the folio.

   Usage: node fitcheck.mjs <file.html> [--json]
   Requires: Chrome. No npm dependencies — raw CDP over the built-in WebSocket. */

import { spawn } from 'node:child_process';
import { mkdtempSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

const CHROME = process.env.CHROME_BIN
  || 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9411 + (process.pid % 120);

const target = process.argv[2];
const asJson = process.argv.includes('--json');
if (!target) { console.error('usage: node fitcheck.mjs <file.html>'); process.exit(2); }
const url = pathToFileURL(resolve(target)).href;

const profile = mkdtempSync(join(tmpdir(), 'fitcheck-'));
const chrome = spawn(CHROME, [
  '--headless=new', '--disable-gpu', '--hide-scrollbars', '--mute-audio',
  '--no-first-run', '--no-default-browser-check',
  `--remote-debugging-port=${PORT}`, `--user-data-dir=${profile}`,
  '--window-size=700,1000', 'about:blank',
], { stdio: 'ignore' });

const cleanup = () => {
  try { chrome.kill(); } catch {}
  try { rmSync(profile, { recursive: true, force: true }); } catch {}
};
process.on('exit', cleanup);

const sleep = ms => new Promise(r => setTimeout(r, ms));

async function endpoint() {
  for (let i = 0; i < 60; i++) {
    try {
      const r = await fetch(`http://127.0.0.1:${PORT}/json/version`);
      if (r.ok) return (await r.json()).webSocketDebuggerUrl;
    } catch {}
    await sleep(250);
  }
  throw new Error('Chrome DevTools endpoint never came up');
}

function connect(wsUrl) {
  const ws = new WebSocket(wsUrl);
  let id = 0;
  const pending = new Map();
  const ready = new Promise((res, rej) => { ws.onopen = res; ws.onerror = rej; });
  ws.onmessage = e => {
    const m = JSON.parse(e.data);
    if (m.id && pending.has(m.id)) {
      const { res, rej } = pending.get(m.id);
      pending.delete(m.id);
      m.error ? rej(new Error(m.error.message)) : res(m.result);
    }
  };
  const send = (method, params = {}, sessionId) => new Promise((res, rej) => {
    const msg = { id: ++id, method, params };
    if (sessionId) msg.sessionId = sessionId;
    pending.set(msg.id, { res, rej });
    ws.send(JSON.stringify(msg));
  });
  return { ready, send, close: () => ws.close() };
}

// Runs inside the page. Bottom padding of .page is the reserved footer band; anything
// whose box crosses into it is either clipped or colliding with the folio.
const PROBE = `(() => {
  const FOOTER_RESERVE = 0.52 * 96;           // inches -> css px at 96dpi
  return [...document.querySelectorAll('.page')].map((page, i) => {
    // Full-bleed pages (cover) carry no folio and are allowed to run to the trim edge.
    if (page.classList.contains('cover')) return { page: i + 1, overflowPx: 0, culprit: '' };
    const pr = page.getBoundingClientRect();
    const limit = pr.bottom - FOOTER_RESERVE;
    let worst = 0, culprit = '';
    for (const el of page.children) {
      if (el.classList.contains('folio') || el.classList.contains('runhead')) continue;
      const r = el.getBoundingClientRect();
      if (r.height === 0) continue;
      const over = r.bottom - limit;
      if (over > worst) {
        worst = over;
        culprit = el.tagName.toLowerCase()
          + (el.className ? '.' + String(el.className).split(' ').join('.') : '')
          + ' — "' + (el.textContent || '').trim().slice(0, 46).replace(/\\s+/g, ' ') + '"';
      }
    }
    // NOTE: scrollHeight is NOT a usable signal here — it adds the box's bottom padding after
    // the last in-flow child, so a page that fits perfectly still reports ~58px of phantom
    // overflow. Geometry against the reserved footer band is the real test.
    return { page: i + 1, overflowPx: Math.round(worst), culprit };
  });
})()`;

const wsUrl = await endpoint();
const { ready, send, close } = connect(wsUrl);
await ready;

const { targetId } = await send('Target.createTarget', { url });
const { sessionId } = await send('Target.attachToTarget', { targetId, flatten: true });
await send('Page.enable', {}, sessionId);
await sleep(900); // fonts + layout settle

const { result } = await send('Runtime.evaluate',
  { expression: PROBE, returnByValue: true }, sessionId);
close();

const pages = result.value;
const bad = pages.filter(p => p.overflowPx > 1);

if (asJson) {
  console.log(JSON.stringify({ total: pages.length, failing: bad }, null, 2));
} else {
  console.log(`fitcheck — ${pages.length} pages in ${target}`);
  if (!bad.length) console.log('PASS — every page fits its 6x9 box.');
  else {
    console.log(`FAIL — ${bad.length} page(s) overflow:\n`);
    for (const p of bad) {
      console.log(`  page ${String(p.page).padStart(3)}  +${p.overflowPx}px past the safe area`);
      console.log(`            ${p.culprit}\n`);
    }
  }
}
process.exit(bad.length ? 1 : 0);
