/* pagecheck — verifies a published Gumroad custom page actually RENDERS.

   Gumroad serves the product page as a React shell and mounts the custom HTML in a
   sandboxed iframe, so `curl` sees none of it: the only honest check is a real
   browser that runs the page's JS and then reads every frame's DOM.

   The two pages assert different things — a product page MUST carry a buy element or the
   product is unpurchasable; a profile page never has one — so the kind is explicit rather
   than guessed. Passing the wrong kind is a loud failure, not a silent pass.

   Usage: node pagecheck.mjs <url> [product|packet|profile] [screenshot-out.png] */

import { spawn } from 'node:child_process';
import { mkdtempSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const URL_TO_CHECK = process.argv[2];
const KIND = process.argv[3] || 'product';
const SHOT = process.argv[4];
if (!URL_TO_CHECK || !['product', 'packet', 'profile'].includes(KIND)) {
  console.error('usage: node pagecheck.mjs <url> [product|packet|profile] [out.png]');
  process.exit(2);
}

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

const { ready, send, attached, close } = connect(await endpoint());
await ready;
const { targetId } = await send('Target.createTarget', { url: 'about:blank' });
const { sessionId } = await send('Target.attachToTarget', { targetId, flatten: true });
await send('Page.enable', {}, sessionId);

// Gumroad mounts the custom HTML in a CROSS-ORIGIN sandboxed iframe, so the parent
// document cannot read it (contentDocument is null by design). Auto-attach gives us a
// session per out-of-process frame, which is the only way to inspect what actually rendered.
await send('Target.setAutoAttach',
  { autoAttach: true, waitForDebuggerOnStart: false, flatten: true }, sessionId);
const VW = Number(process.env.VIEW_W || 1280);
await send('Emulation.setDeviceMetricsOverride',
  { width: VW, height: 1000, deviceScaleFactor: 1, mobile: VW < 700 }, sessionId);
await send('Page.navigate', { url: URL_TO_CHECK }, sessionId);
await sleep(6000); // React shell + iframe mount

// Collect the top document plus every attached (out-of-process) frame's document.
const READ = `(() => {
  let html = document.documentElement.outerHTML;
  for (const f of document.querySelectorAll('iframe')) {
    try { if (f.contentDocument) html += f.contentDocument.documentElement.outerHTML; } catch (e) {}
  }
  return html;
})()`;
let dom = '';
let frameUrl = null; // standalone URL of the frame holding our custom HTML
for (const s of [sessionId, ...attached]) {
  try {
    const { result: r } = await send('Runtime.evaluate', { expression: READ, returnByValue: true }, s);
    const html = r?.value || '';
    if (!frameUrl && /class="(srh|prp)"/.test(html)) {
      const { result: u } = await send('Runtime.evaluate', { expression: 'location.href', returnByValue: true }, s);
      frameUrl = u?.value || null;
    }
    dom += html;
  } catch {} // a frame can detach mid-read; the others still answer
}
console.log(`frames inspected: ${1 + attached.length}`);
// packet's own layout carries 2 media-library images; product/profile carry more.
const MIN_IMAGES = KIND === 'packet' ? 2 : 3;
const common = [
  ['media-library images', (dom.match(/public-files\.gumroad\.com/g) || []).length >= MIN_IMAGES],
  // Light-locked 2026-08-16: pages.dev has no dark mode, so an adaptive checkout broke
  // brand continuity for dark-OS visitors at the payment moment. Assert the lock holds.
  ['light-locked (no dark palette)', !dom.includes('prefers-color-scheme:dark')],
  ['paper palette present', dom.includes('#f4eee1')],
  ['author byline', dom.includes('Paul Raymond')],
];
const checks = KIND === 'product'
  ? [['custom page mounted (.srh wrapper)', dom.includes('class="srh"')],
     ['buy elements present', (dom.match(/data-gumroad-action="buy"/g) || []).length >= 1],
     ['price shown', dom.includes('$9.99')],
     ['Joplin story', dom.includes('Joplin')],
     ...common]
  : KIND === 'packet'
  ? [['custom page mounted (.srh wrapper)', dom.includes('class="srh"')],
     ['buy elements present', (dom.match(/data-gumroad-action="buy"/g) || []).length >= 1],
     ['cross-sell to the manual', dom.includes('/l/ebook')],
     ...common]
  : [['custom page mounted (.prp wrapper)', dom.includes('class="prp"')],
     ['links to the product', dom.includes('/l/ebook')],
     ...common];
let fail = 0;
for (const [label, ok] of checks) { console.log(`${ok ? 'ok  ' : 'FAIL'}  ${label}`); if (!ok) fail++; }

if (SHOT) {
  // A full-page shot of the PARENT captures only the fold — its scrollHeight is just the
  // viewport, and forcing a tall viewport makes the host app paint blank (measured).
  // Capturing the frame's own session is refused outright: "Command can only be executed on
  // top-level targets". So load the frame's URL AS a top-level page. It is a real server
  // route (…/l/<permalink>/landing/embed) and our HTML carries its own <style>, so it renders
  // standalone exactly as it does embedded.
  if (!frameUrl) throw new Error('no content frame found — nothing to screenshot');
  const { targetId: shotTarget } = await send('Target.createTarget', { url: 'about:blank' });
  const { sessionId: shotSession } = await send('Target.attachToTarget', { targetId: shotTarget, flatten: true });
  await send('Page.enable', {}, shotSession);
  await send('Emulation.setDeviceMetricsOverride',
    { width: VW, height: 1000, deviceScaleFactor: 1, mobile: VW < 700 }, shotSession);
  await send('Page.navigate', { url: frameUrl }, shotSession);
  await sleep(4000);
  const { result: h } = await send('Runtime.evaluate',
    { expression: 'Math.max(document.documentElement.scrollHeight, document.body.scrollHeight)',
      returnByValue: true }, shotSession);
  const { data } = await send('Page.captureScreenshot', { format: 'png', captureBeyondViewport: true,
    clip: { x: 0, y: 0, width: VW, height: Math.min(h.value, 16000), scale: 1 } }, shotSession);
  writeFileSync(SHOT, Buffer.from(data, 'base64'));
  console.log(`screenshot -> ${SHOT}  (${VW}x${h.value}, from ${frameUrl})`);
}
close();
console.log(fail ? `\n${fail} check(s) FAILED` : '\nPASS — custom page is live and rendering.');
process.exit(fail ? 1 : 0);
