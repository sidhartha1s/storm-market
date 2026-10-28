/* roomcheck — spare-space report for the binder's fixed pages.
   fitcheck.mjs is the hard overflow gate; this is its complement, for a different
   defect: a page that fits but wastes most of its box. These are print pages a reader
   fills in with a pen — "spend the leftover on row height, not blank paper" (owner
   2026-08-03) — so a page sitting at 20% full while its form's next page is packed is
   as much a mistake as an overflow, just a silent one fitcheck doesn't catch.

   Reuses fitcheck.mjs's ~30-line Chrome-launch/CDP-connect helper rather than
   importing it, for the same reason paginate.mjs does: the hard gate itself stays
   untouched.

   Usage: node roomcheck.mjs <file.html> [--json] [--threshold 40]
   Requires: Chrome. No npm dependencies — raw CDP over the built-in WebSocket. */

import { spawn } from 'node:child_process';
import { mkdtempSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

const CHROME = process.env.CHROME_BIN
  || 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9611 + (process.pid % 120);

const args = process.argv.slice(2);
const target = args.find(a => !a.startsWith('--'));
const asJson = args.includes('--json');
const thresholdIdx = args.indexOf('--threshold');
const THRESHOLD = thresholdIdx >= 0 ? Number(args[thresholdIdx + 1]) : 40;
if (!target) { console.error('usage: node roomcheck.mjs <file.html> [--json] [--threshold 40]'); process.exit(2); }
const url = pathToFileURL(resolve(target)).href;

const profile = mkdtempSync(join(tmpdir(), 'roomcheck-'));
const chrome = spawn(CHROME, [
  '--headless=new', '--disable-gpu', '--hide-scrollbars', '--mute-audio',
  '--no-first-run', '--no-default-browser-check',
  `--remote-debugging-port=${PORT}`, `--user-data-dir=${profile}`,
  '--window-size=700,1000', 'about:blank',
], { stdio: 'ignore', windowsHide: true });

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

// Same geometry fitcheck.mjs and paginate.mjs use: content runs from the page's own
// top padding down to the reserved footer band. usedPx is the bottom edge of the
// last real content child (never the folio/runhead furniture); emptyPx is what's left.
const PROBE = `(() => {
  const FOOTER_RESERVE = 0.52 * 96;
  const PAD_TOP = 0.72 * 96;
  return [...document.querySelectorAll('.page')].map((page, i) => {
    if (page.classList.contains('cover')) return null;
    const pr = page.getBoundingClientRect();
    const budget = pr.height - PAD_TOP - FOOTER_RESERVE;
    const limit = pr.bottom - FOOTER_RESERVE;
    let usedBottom = pr.top + PAD_TOP; // floor: at least the top padding itself
    for (const el of page.children) {
      if (el.classList.contains('folio') || el.classList.contains('runhead')) continue;
      const r = el.getBoundingClientRect();
      if (r.height === 0) continue;
      if (r.bottom > usedBottom) usedBottom = r.bottom;
    }
    const usedPx = Math.min(usedBottom, limit) - (pr.top + PAD_TOP);
    const emptyPx = Math.max(0, budget - usedPx);
    const kicker = page.querySelector('.b-kicker');
    const title = page.querySelector('.form-title, .b-cont');
    const label = [kicker && kicker.textContent.trim(), title && title.textContent.trim()]
      .filter(Boolean).join(' — ') || '(no form label)';
    return {
      page: i + 1, label,
      usedPx: Math.round(usedPx), budgetPx: Math.round(budget),
      emptyPx: Math.round(emptyPx), emptyPct: Math.round((emptyPx / budget) * 100),
    };
  }).filter(Boolean);
})()`;

const wsUrl = await endpoint();
const { ready, send, close } = connect(wsUrl);
await ready;

const { targetId } = await send('Target.createTarget', { url });
const { sessionId } = await send('Target.attachToTarget', { targetId, flatten: true });
await send('Page.enable', {}, sessionId);
await sleep(900);

const { result } = await send('Runtime.evaluate',
  { expression: PROBE, returnByValue: true }, sessionId);
close();

const pages = result.value;
const bad = pages.filter(p => p.emptyPct > THRESHOLD);

if (asJson) {
  console.log(JSON.stringify({ total: pages.length, threshold: THRESHOLD, over: bad, pages }, null, 2));
} else {
  console.log(`roomcheck — ${pages.length} pages in ${target}, threshold ${THRESHOLD}% empty`);
  if (!bad.length) console.log('PASS — no page exceeds the empty-space threshold.');
  else {
    console.log(`${bad.length} page(s) over threshold:\n`);
    for (const p of bad) {
      console.log(`  page ${String(p.page).padStart(3)}  ${p.emptyPct}% empty ` +
        `(${p.emptyPx}px of ${p.budgetPx}px unused) — ${p.label}`);
    }
  }
}
process.exit(0); // informational — never blocks a build the way fitcheck does
