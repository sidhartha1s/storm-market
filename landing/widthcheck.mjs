/* widthcheck — horizontal-overflow gate for the landing page.
   A page that scrolls sideways on a phone is a broken page, and the cause is almost never the
   element you suspect. This measures instead of guessing.

   Usage: node widthcheck.mjs <file.html> [width...]     default widths: 390 768 1280
   Requires: Chrome. No npm dependencies — raw CDP over the built-in WebSocket. */

import { spawn } from 'node:child_process';
import { mkdtempSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

const CHROME = process.env.CHROME_BIN || 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9531 + (process.pid % 120);

const target = process.argv[2];
if (!target) { console.error('usage: node widthcheck.mjs <file.html> [width...]'); process.exit(2); }
const widths = process.argv.slice(3).map(Number).filter(Boolean);
const WIDTHS = widths.length ? widths : [390, 768, 1280];
const url = pathToFileURL(resolve(target)).href;

const profile = mkdtempSync(join(tmpdir(), 'widthcheck-'));
const chrome = spawn(CHROME, [
  '--headless=new', '--disable-gpu', '--hide-scrollbars', '--mute-audio',
  '--no-first-run', '--no-default-browser-check',
  `--remote-debugging-port=${PORT}`, `--user-data-dir=${profile}`, 'about:blank',
], { stdio: 'ignore' });
process.on('exit', () => {
  try { chrome.kill(); } catch {}
  try { rmSync(profile, { recursive: true, force: true }); } catch {}
});

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
  let id = 0; const pending = new Map();
  const ready = new Promise((res, rej) => { ws.onopen = res; ws.onerror = rej; });
  ws.onmessage = e => {
    const m = JSON.parse(e.data);
    if (m.id && pending.has(m.id)) {
      const { res, rej } = pending.get(m.id); pending.delete(m.id);
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

// Reports the document overflow plus every element whose box crosses the viewport's right edge.
// Skips descendants of an already-reported culprit so the output names causes, not symptoms.
const PROBE = `(() => {
  const vw = document.documentElement.clientWidth;
  const over = document.documentElement.scrollWidth - vw;
  const bad = [];
  for (const el of document.querySelectorAll('body *')) {
    const r = el.getBoundingClientRect();
    if (r.width === 0 || r.height === 0) continue;
    if (r.right <= vw + 1 && r.left >= -1) continue;
    if (bad.some(b => b.el.contains(el))) continue;
    bad.push({ el, desc:
      el.tagName.toLowerCase()
      + (el.id ? '#' + el.id : '')
      + (el.className && typeof el.className === 'string' ? '.' + el.className.trim().split(/\\s+/).join('.') : '')
      + '  [' + Math.round(r.left) + ' .. ' + Math.round(r.right) + ']'
      + '  w=' + Math.round(r.width) });
  }
  return { vw, over, culprits: bad.slice(0, 12).map(b => b.desc) };
})()`;

const wsUrl = await endpoint();
const { ready, send, close } = connect(wsUrl);
await ready;
const { targetId } = await send('Target.createTarget', { url });
const { sessionId } = await send('Target.attachToTarget', { targetId, flatten: true });
await send('Page.enable', {}, sessionId);

let failures = 0;
console.log(`widthcheck — ${target}`);
for (const w of WIDTHS) {
  await send('Emulation.setDeviceMetricsOverride',
    { width: w, height: 900, deviceScaleFactor: 1, mobile: w < 700 }, sessionId);
  await sleep(500);
  const { result } = await send('Runtime.evaluate',
    { expression: PROBE, returnByValue: true }, sessionId);
  const { vw, over, culprits } = result.value;
  if (over > 1 || culprits.length) {
    failures++;
    console.log(`\n  ${w}px  FAIL — document overflows by ${over}px (viewport ${vw})`);
    for (const c of culprits) console.log(`         ${c}`);
  } else {
    console.log(`  ${w}px  ok`);
  }
}
close();
console.log(failures ? `\nFAIL — ${failures} width(s) overflow.` : '\nPASS — no horizontal overflow.');
process.exit(failures ? 1 : 0);
