/* pagecheck — verifies a published Gumroad custom page actually RENDERS.

   Gumroad serves the product page as a React shell and mounts the custom HTML in a
   sandboxed iframe, so `curl` sees none of it: the only honest check is a real
   browser that runs the page's JS and then reads every frame's DOM.

   Usage: node pagecheck.mjs <url> [screenshot-out.png] */

import { spawn } from 'node:child_process';
import { mkdtempSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const URL_TO_CHECK = process.argv[2];
const SHOT = process.argv[3];
if (!URL_TO_CHECK) { console.error('usage: node pagecheck.mjs <url> [out.png]'); process.exit(2); }

const CHROME = process.env.CHROME_BIN || 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9810 + (process.pid % 80);
const profile = mkdtempSync(join(tmpdir(), 'pagecheck-'));
const chrome = spawn(CHROME, ['--headless=new', '--disable-gpu', '--mute-audio', '--no-first-run',
  '--hide-scrollbars', '--no-default-browser-check', `--remote-debugging-port=${PORT}`,
  `--user-data-dir=${profile}`, 'about:blank'], { stdio: 'ignore' });
process.on('exit', () => {
  try { chrome.kill(); } catch {}
  try { rmSync(profile, { recursive: true, force: true }); } catch {}
});

const sleep = ms => new Promise(r => setTimeout(r, ms));
async function endpoint() {
  for (let i = 0; i < 60; i++) {
    try { const r = await fetch(`http://127.0.0.1:${PORT}/json/version`); if (r.ok) return (await r.json()).webSocketDebuggerUrl; } catch {}
    await sleep(250);
  }
  throw new Error('Chrome DevTools endpoint never came up');
}
function connect(wsUrl) {
  const ws = new WebSocket(wsUrl); let id = 0; const pending = new Map();
  const attached = []; // sessionIds of auto-attached child frame targets
  const ready = new Promise((res, rej) => { ws.onopen = res; ws.onerror = rej; });
  ws.onmessage = e => { const m = JSON.parse(e.data);
    if (m.method === 'Target.attachedToTarget') attached.push(m.params.sessionId);
    if (m.id && pending.has(m.id)) { const { res, rej } = pending.get(m.id); pending.delete(m.id);
      m.error ? rej(new Error(m.error.message)) : res(m.result); } };
  const send = (method, params = {}, sessionId) => new Promise((res, rej) => {
    const msg = { id: ++id, method, params }; if (sessionId) msg.sessionId = sessionId;
    pending.set(msg.id, { res, rej }); ws.send(JSON.stringify(msg)); });
  return { ready, send, attached, close: () => ws.close() };
}

const { ready, send, close } = connect(await endpoint());
await ready;
const { targetId } = await send('Target.createTarget', { url: 'about:blank' });
const { sessionId } = await send('Target.attachToTarget', { targetId, flatten: true });
await send('Page.enable', {}, sessionId);

// Gumroad mounts the custom HTML in a CROSS-ORIGIN sandboxed iframe, so the parent
// document cannot read it (contentDocument is null by design). Auto-attach gives us a
// session per out-of-process frame, which is the only way to inspect what actually rendered.
const frameSessions = [];
ws_onAttach: {
  // collected via the raw socket below
}
await send('Target.setAutoAttach',
  { autoAttach: true, waitForDebuggerOnStart: false, flatten: true }, sessionId);
await send('Emulation.setDeviceMetricsOverride',
  { width: 1280, height: 1000, deviceScaleFactor: 1, mobile: false }, sessionId);
await send('Page.navigate', { url: URL_TO_CHECK }, sessionId);
await sleep(6000); // React shell + iframe mount

// Walk the top document AND every same-process frame, concatenating their HTML.
const { result } = await send('Runtime.evaluate', {
  expression: `(() => {
    let html = document.documentElement.outerHTML;
    for (const f of document.querySelectorAll('iframe')) {
      try { if (f.contentDocument) html += f.contentDocument.documentElement.outerHTML; } catch (e) {}
    }
    return html;
  })()`, returnByValue: true }, sessionId);

const dom = result.value || '';
const checks = [
  ['custom page mounted (.srh wrapper)', dom.includes('class="srh"')],
  ['buy elements present', (dom.match(/data-gumroad-action="buy"/g) || []).length >= 1],
  ['price shown', dom.includes('$47')],
  ['media-library images', (dom.match(/public-files\.gumroad\.com/g) || []).length >= 3],
  ['Joplin story', dom.includes('Joplin')],
  ['dark-mode rules', dom.includes('prefers-color-scheme:dark')],
  ['author byline', dom.includes('Paul Raymond')],
];
let fail = 0;
for (const [label, ok] of checks) { console.log(`${ok ? 'ok  ' : 'FAIL'}  ${label}`); if (!ok) fail++; }

if (SHOT) {
  const { result: h } = await send('Runtime.evaluate',
    { expression: 'document.documentElement.scrollHeight', returnByValue: true }, sessionId);
  const { data } = await send('Page.captureScreenshot', { format: 'png', captureBeyondViewport: true,
    clip: { x: 0, y: 0, width: 1280, height: Math.min(h.value, 16000), scale: 1 } }, sessionId);
  writeFileSync(SHOT, Buffer.from(data, 'base64'));
  console.log(`screenshot -> ${SHOT}`);
}
close();
console.log(fail ? `\n${fail} check(s) FAILED` : '\nPASS — custom page is live and rendering.');
process.exit(fail ? 1 : 0);
