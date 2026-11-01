// One-shot: render the SPC Day 4-8 discussion text (the <pre> of the archived page) to a transparent 1240 x 780 PNG,
// and print the geometry of the lit line (Day 8/Friday) in PNG pixels. Reads the source, authors no comp HTML.
import { chromium, chromiumExecutable } from 'file:///C:/Users/Sidhartha/Automation%20Projects/storm-market/.claude/worktrees/ep-mayfield-2021-a6d084/scripts/playwright_env.mjs';
import { writeFileSync } from 'fs';

const EP = 'C:/Users/Sidhartha/Automation Projects/storm-market/.claude/worktrees/ep-mayfield-2021-a6d084/episodes/ep-mayfield-2021';
const SRC = `file:///${EP.replace(/ /g, '%20')}/media/candidates/intro/i1-s2_c1_spc-day4-8-outlook-3dec.html`;
const OUT = `${EP}/media/stills/i1-s2-spc-day4-8-page-v2.png`;
const BW = 1240, BH = 780;
const PITCH_TARGET = Number(process.env.PITCH || 19.4);   // px between lines in the 1920 x 1080 frame
const TOP_PAD = 6;

const browser = await chromium.launch({ executablePath: chromiumExecutable(), args: ['--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: BW, height: BH }, deviceScaleFactor: 1 });
await page.route('**/*', r => (r.request().url().startsWith('file:') ? r.continue() : r.abort()));
await page.goto(SRC, { waitUntil: 'domcontentloaded' });

const geo = await page.evaluate(({ BW, BH, PITCH_TARGET, TOP_PAD }) => {
  const pre = [...document.querySelectorAll('pre')].find(p => p.textContent.includes('ZCZC SPCSWOD48'));
  const text = pre.firstChild;
  const raw = text.nodeValue;
  const lines = raw.split('\n');
  let off = 0; const starts = lines.map(l => { const o = off; off += l.length + 1; return o; });
  const iFirst = lines.findIndex(l => l.includes('Day 4-8 Convective Outlook'));
  const iHdr = lines.findIndex(l => l.includes('0320 AM CST Fri Dec 03 2021'));
  const iLit = lines.findIndex(l => l.includes('Day 8/Friday'));
  const iLast = iLit + 1;  // the crop ends on the second lit line (the glass strip sits below it)
  // measure each wanted line with a Range
  const rect = i => { const r = document.createRange(); const s = starts[i] + lines[i].search(/\S/); r.setStart(text, s); r.setEnd(text, starts[i] + lines[i].trimEnd().length); const b = r.getBoundingClientRect(); return { l: b.left, r: b.right, t: b.top, b: b.bottom }; };
  const a = rect(iFirst), b = rect(iFirst + 1);
  const pitch0 = b.t - a.t;
  const s = PITCH_TARGET / pitch0;
  let minL = 1e9, maxR = 0;
  for (let i = iFirst; i <= iLast; i++) { if (!lines[i].trim()) continue; const q = rect(i); minL = Math.min(minL, q.l); maxR = Math.max(maxR, q.r); }
  const colW = maxR - minL;
  // wrap the pre in a scaled, positioned stage so the screenshot is the final 1240 x 780 bitmap
  const lineTop0 = a.t;
  const lit0 = rect(iLit);
  const preBox0 = pre.getBoundingClientRect();
  const hdr0 = rect(iHdr), last0 = rect(iLast);
  const rect2 = (i, endStr) => { const r = document.createRange(); r.setStart(text, starts[i] + lines[i].search(/\S/)); r.setEnd(text, starts[i] + lines[i].indexOf(endStr) + endStr.length); const b = r.getBoundingClientRect(); return { l: b.left, r: b.right, t: b.top, b: b.bottom }; };
  const lit2_0 = rect2(iLast, 'convection.');
  const tx = (BW / s - colW) / 2 - minL;             // centre the text column
  const ty = -lineTop0 + TOP_PAD / s;                // first kept line sits TOP_PAD px from the top
  document.documentElement.style.cssText = 'background:transparent';
  document.body.style.cssText = 'margin:0;background:transparent;overflow:hidden';
  [...document.body.children].forEach(c => { if (!c.contains(pre)) c.style.display = 'none'; });
  let p = pre; while (p && p !== document.body) { p.style.background = 'transparent'; [...p.parentElement.children].forEach(c => { if (c !== p) c.style.visibility = 'hidden'; }); p = p.parentElement; }
  const wrap = document.createElement('div');
  wrap.style.cssText = `position:fixed;left:0;top:0;width:${BW}px;height:${BH}px;overflow:hidden;z-index:9;background:transparent`;
  const inner = document.createElement('div');
  inner.style.cssText = `position:absolute;left:0;top:0;transform-origin:0 0;transform:scale(${s}) translate(${tx}px,${ty}px)`;
  const clone = pre.cloneNode(true); clone.style.cssText = 'margin:0;background:transparent;color:#000;position:absolute;left:0;top:0;white-space:pre';
  // keep only the kept lines so lines below the crop do not bleed in
  clone.textContent = lines.slice(0, iLast + 1).join('\n'); pre.style.visibility = 'hidden';
  inner.appendChild(clone); wrap.appendChild(inner); document.body.appendChild(wrap);
  clone.style.left = (preBox0.left + window.scrollX) + 'px'; clone.style.top = (preBox0.top + window.scrollY) + 'px';
  const font = getComputedStyle(pre).fontFamily + ' ' + getComputedStyle(pre).fontSize;
  const out = (q) => ({ l: (q.l + tx) * s, r: (q.r + tx) * s, t: (q.t + ty) * s, b: (q.b + ty) * s });
  return { s, pitch0, font, iFirst, iHdr, iLit, iLast, litText: lines[iLit].trim(), hdrText: lines[iHdr].trim(), lastText: lines[iLast].trim(), colW_px: colW * s, lit: out(lit0), hdr: out(hdr0), lit2: out(lit2_0), line2Text: lines[iLast].trim(), first: out(a), lastLine: out(last0) };
}, { BW, BH, PITCH_TARGET, TOP_PAD });

await page.waitForTimeout(300);
await page.screenshot({ path: OUT, omitBackground: true, clip: { x: 0, y: 0, width: BW, height: BH } });
writeFileSync(`${EP}/capture-g-i1-2/page_geo.json`, JSON.stringify(geo, null, 2));
console.log(JSON.stringify(geo, null, 2));
await browser.close();
