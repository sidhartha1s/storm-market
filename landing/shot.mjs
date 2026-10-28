/* shot — full-page screenshots at real device widths.
   `chrome --headless --screenshot --window-size=390,...` does NOT give you a 390px layout:
   desktop Chrome enforces a minimum window width, so it renders wider and crops, which looks
   exactly like a horizontal-overflow bug and is not one. This uses CDP device emulation, which
   is the only way to see what a phone actually sees.

   Usage: node shot.mjs <file.html> <outDir> [width...]     default widths: 390 768 1280 */

import { spawn } from 'node:child_process';
import { mkdtempSync, rmSync, writeFileSync, mkdirSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

const CHROME = process.env.CHROME_BIN || 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9651 + (process.pid % 120);

const target = process.argv[2], outDir = process.argv[3];
if (!target || !outDir) { console.error('usage: node shot.mjs <file.html> <outDir> [width...]'); process.exit(2); }
const widths = process.argv.slice(4).map(Number).filter(Boolean);
const WIDTHS = widths.length ? widths : [390, 768, 1280];
const url = pathToFileURL(resolve(target)).href;
mkdirSync(outDir, { recursive: true });

const profile = mkdtempSync(join(tmpdir(), 'shot-'));
const chrome = spawn(CHROME, ['--headless=new','--disable-gpu','--hide-scrollbars','--mute-audio',
  '--no-first-run','--no-default-browser-check',
  `--remote-debugging-port=${PORT}`,`--user-data-dir=${profile}`,'about:blank'], { stdio: 'ignore', windowsHide: true });
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
  const ready = new Promise((res, rej) => { ws.onopen = res; ws.onerror = rej; });
  ws.onmessage = e => { const m = JSON.parse(e.data);
    if (m.id && pending.has(m.id)) { const { res, rej } = pending.get(m.id); pending.delete(m.id);
      m.error ? rej(new Error(m.error.message)) : res(m.result); } };
  const send = (method, params = {}, sessionId) => new Promise((res, rej) => {
    const msg = { id: ++id, method, params }; if (sessionId) msg.sessionId = sessionId;
    pending.set(msg.id, { res, rej }); ws.send(JSON.stringify(msg)); });
  return { ready, send, close: () => ws.close() };
}

const wsUrl = await endpoint();
const { ready, send, close } = connect(wsUrl);
await ready;
const { targetId } = await send('Target.createTarget', { url });
const { sessionId } = await send('Target.attachToTarget', { targetId, flatten: true });
await send('Page.enable', {}, sessionId);

for (const w of WIDTHS) {
  await send('Emulation.setDeviceMetricsOverride',
    { width: w, height: 900, deviceScaleFactor: 1, mobile: w < 700 }, sessionId);
  await sleep(600);
  const { result } = await send('Runtime.evaluate',
    { expression: 'document.documentElement.scrollHeight', returnByValue: true }, sessionId);
  const full = Math.min(result.value, 16000); // cap: CDP refuses very tall captures
  const { data } = await send('Page.captureScreenshot',
    { format: 'png', captureBeyondViewport: true,
      clip: { x: 0, y: 0, width: w, height: full, scale: 1 } }, sessionId);
  const path = join(outDir, `lp-${w}.png`);
  writeFileSync(path, Buffer.from(data, 'base64'));
  console.log(`${w}px  ${full}px tall  ->  ${path}`);
}
close();
process.exit(0); // the WebSocket close alone leaves the process alive and it hangs
