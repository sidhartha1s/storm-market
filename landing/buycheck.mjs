/* buycheck — loads a live URL in headless Chrome, lets its JS run, and reports the
   RESOLVED href of every checkout CTA plus whether that URL actually responds.

   The buy button's href is set at runtime from GUMROAD_URL, so grepping the HTML
   proves nothing: this is the only check that fails when the money path is broken.

   Usage: node buycheck.mjs [url]        default: https://paulraymond.pages.dev/ */

import { spawn } from 'node:child_process';
import { mkdtempSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const URL_TO_CHECK = process.argv[2] || 'https://paulraymond.pages.dev/';
const PRODUCT_NAME = process.env.PRODUCT_NAME || 'The Storm-Ready Home';
const CHROME = process.env.CHROME_BIN || 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9700 + (process.pid % 90);

const profile = mkdtempSync(join(tmpdir(), 'buycheck-'));
const chrome = spawn(CHROME, ['--headless=new', '--disable-gpu', '--mute-audio', '--no-first-run',
  '--no-default-browser-check', `--remote-debugging-port=${PORT}`, `--user-data-dir=${profile}`,
  'about:blank'], { stdio: 'ignore' });
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

const { ready, send, close } = connect(await endpoint());
await ready;
const { targetId } = await send('Target.createTarget', { url: URL_TO_CHECK });
const { sessionId } = await send('Target.attachToTarget', { targetId, flatten: true });
await send('Page.enable', {}, sessionId);
await sleep(3500); // let the page's inline script wire the CTAs

const { result } = await send('Runtime.evaluate', {
  expression: `JSON.stringify({
    buy:      document.getElementById('buy')?.getAttribute('href') ?? null,
    band:     document.querySelector('.band .go')?.getAttribute('href') ?? null,
    dock:     document.querySelector('.pill .btn')?.getAttribute('href') ?? null,
    buyLabel: document.getElementById('buy')?.textContent.trim() ?? null,
    viewers:  document.getElementById('live-n')?.textContent ?? null,
    countdown:document.getElementById('countdown')?.textContent ?? null
  })`, returnByValue: true }, sessionId);
close();

const state = JSON.parse(result.value);
console.log(`page      ${URL_TO_CHECK}`);
console.log(`buy       ${state.buy}   (${state.buyLabel})`);
console.log(`band CTA ${state.band}`);
console.log(`dock CTA ${state.dock}`);
console.log(`live band viewers=${state.viewers} countdown=${state.countdown}`);

let fail = 0;
for (const [label, href] of [['buy', state.buy], ['band', state.band], ['dock', state.dock]]) {
  if (!href || href === '#' || href.startsWith('#')) {
    console.log(`FAIL  ${label} CTA is not wired to a checkout (href=${href})`); fail++; continue;
  }
  // a page opened with ?src=<tag> must hand the tag to Gumroad as all three utm fields, or the sale is untraceable
  if (/[?&]src=/.test(URL_TO_CHECK) && !['utm_source', 'utm_medium', 'utm_campaign'].every(k => new URL(href).searchParams.get(k))) {
    console.log(`FAIL  ${label} CTA lost the src tag (href=${href})`); fail++; continue;
  }
  const r = await fetch(href, { redirect: 'follow' });
  const body = await r.text();
  // `?wanted=true` serves Gumroad's CHECKOUT page, not the product page, so the
  // product-page JSON blob is absent by design. What must be true of the checkout:
  // it names this product and it carries checkout machinery.
  const namesProduct = body.includes(PRODUCT_NAME);
  const isCheckout = /cart|checkout/i.test(body);
  const ok = r.ok && namesProduct && isCheckout;
  console.log(`${ok ? 'ok  ' : 'FAIL'}  ${label} -> ${r.status}  ` +
    `names "${PRODUCT_NAME}": ${namesProduct}  checkout page: ${isCheckout}`);
  if (!ok) fail++;
}
console.log(fail ? `\n${fail} check(s) FAILED` : '\nPASS — every checkout CTA resolves to the live product.');
process.exit(fail ? 1 : 0);
