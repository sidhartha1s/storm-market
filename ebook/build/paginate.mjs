/* paginate.mjs — lays the 41 manuscript files into fixed 6x9 `.page` boxes.

   Why a Python + Node split: review_pdf.py already converts this markdown dialect to HTML,
   including the citation markers and the generated Sources chapter, and that conversion is
   deliberately reused rather than re-implemented (see blocks_pipeline.py, which imports
   review_pdf.py as a library and returns one block per heading/paragraph/table/list/
   blockquote/rule, in book order). Node's only job is the thing Python cannot do without a
   layout engine: find out how TALL each block actually renders at the book's exact content
   width, then fill pages to that measured height. That measurement is done in headless
   Chrome over raw CDP — the same no-dependency technique fitcheck.mjs uses (this file does
   not import fitcheck.mjs; it duplicates its ~30-line Chrome-launch/CDP-connect helper
   instead, so the hard gate itself stays untouched).

   Algorithm:
   1. python3 blocks_pipeline.py -> JSON array of blocks (html, tag, file, part,
      chapterTitle, fileStart, heading).
   2. Render all blocks as direct children of one `<section class="page auto-page measure">`
      (exact width/padding of a real page, height:auto so nothing clips) and read back each
      block's own rendered height plus its own margin-top/margin-bottom. `.auto-page` is
      `display:flex;flex-direction:column`, which disables margin-collapsing entirely — so a
      block's measured footprint (marginTop + height + marginBottom) is the same number
      whether it ends up first on a page or buried in the middle. That is what makes one
      single-pass measurement valid for an as-yet-undecided page split.
   3. Fill pages greedily in plain JS from those numbers alone — no more Chrome calls needed.
      Rules enforced here (see README task brief):
        - a new manuscript file always starts a fresh page (chapter/part opener rule — every
          file boundary in this manuscript IS a chapter or part boundary; also applied to the
          synthetic "SOURCES" pseudo-file).
        - a heading is never the last thing on a page. Implemented as: a run of consecutive
          heading blocks plus the ONE content block that follows must fit together, or the
          whole run moves to a fresh page. (Files routinely open with an h1 immediately
          followed by an h2 with no paragraph between them, so the run can be longer than one
          heading — a pairwise "heading + immediate next" check is not sufficient, it can
          strand an earlier heading when a later one gets pushed off; see isHeadingRunStart.)
        - paragraphs, tables, blockquotes and rules are atomic: review_pdf.py's parser
          already emits exactly one block per element, so "never split one across pages" is
          automatic. The tradeoff is deliberate: this book has no cheap way to split a
          paragraph across a page boundary without risking a citation superscript or a bolded
          phrase being torn across the cut, or a stray widow/orphan line, so no paragraph is
          ever split. The cost is a little unused whitespace at the bottom of some pages
          instead of a broken paragraph; given the fixed-page/no-reflow model, that is the
          conservative side to err on.
        - bulleted/numbered lists are the one exception: blocks_pipeline.py explodes every
          <ul>/<ol> into one bare <li> block per item (see explode_lists there). A list item
          is a complete unit like a paragraph, so a break between items is exactly as safe as
          a break between paragraphs — and several hazard-playbook "Before" lists (10+
          prioritized protections) are taller than one whole page, so keeping them as a
          single opaque block would make them impossible to place at all. Tables/figures/
          numbered-protection blocks stay atomic per the brief; lists were never named there.
        - a block that does not fit even a full, empty page is a genuine content problem
          (an oversized table, say) and is logged loudly rather than clipped or shrunk to fit.
   4. Splice in Appendix B (`../appendix/out/appendix-b.html`) as already-built fixed pages —
      it is read fresh off disk on every run and never edited on disk. Two things happen to
      the in-memory copy: its own within-appendix `.folio` is dropped (book.css positions
      every `.folio` absolutely at the same spot, so keeping it would print two overlapping
      folios per page), and a book-sequence `.folio` is added in its place.
   5. Emit book.html with book.css + book-auto.css + the appendix's packet.css inlined, and
      print the page count and the per-part breakdown.

      packet.css is not optional: appendix-b.html carries the `.stblock` markup but inlines
      its own stylesheet, which is discarded when only the `<section>`s are lifted out. Without
      it the state blocks fall back to browser-default heading and paragraph metrics and
      overflow the 6x9 box by 40-194px — pages that pass fitcheck standalone and fail here.
      Its 45 selectors were checked against book.css and book-auto.css: zero overlap, so it
      cannot alter how a manuscript page measures or renders.

   Usage: node paginate.mjs [out.html]
   Requires: Chrome (CHROME_BIN env var to override), python3. No npm dependencies. */

import { spawn, spawnSync } from 'node:child_process';
import { mkdtempSync, rmSync, readFileSync, writeFileSync, existsSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const HERE = dirname(fileURLToPath(import.meta.url));
const CHROME = process.env.CHROME_BIN
  || 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9531 + (process.pid % 120);

const cliArgs = process.argv.slice(2).filter(a => !a.startsWith('--'));
const OUT = resolve(cliArgs[0] || join(HERE, 'book.html'));
const APPENDIX_HTML = resolve(HERE, '../appendix/out/appendix-b.html');
const PACKET_CSS = resolve(HERE, '../appendix/templates/packet.css');
const BINDER_HTML = resolve(HERE, '../binder/out/binder.html');
const BINDER_CSS = resolve(HERE, '../binder/templates/binder.css');

// Page geometry — must match book.css's .page and fitcheck.mjs's PROBE exactly.
const PAGE_H_IN = 9, PAD_TOP_IN = 0.72, FOOTER_RESERVE_IN = 0.52, DPI = 96;
// Small conservative margin below fitcheck's own limit: this measurement pass and
// fitcheck's later pass both use the same Chrome, but running at different window sizes,
// so a few px of headroom absorbs any sub-pixel font-hinting difference between the two
// runs rather than shipping a book that passes by half a pixel. Documented, not a mask —
// tightened to 0 once measured to be unnecessary would be a fine follow-up, not required now.
const SAFETY_PX = 8;
const BUDGET_PX = (PAGE_H_IN - PAD_TOP_IN - FOOTER_RESERVE_IN) * DPI - SAFETY_PX;

const PART_LABEL = {
  P0: 'Part Zero — Front Matter',
  P1: 'Part One — Why People Die',
  P2: 'Part Two — The Core Six',
  P3: 'Part Three — The Hazard Playbooks',
  P4: 'Part Four — People and Places',
  P5: 'Part Five — Warning, Documents, Money',
  P6: 'Part Six — The Binder',
  P7: 'Part Seven — The 60 Days',
  P8: 'Part Eight — Credits',
  SOURCES: 'Sources',
  BINDER: 'The Binder — fillable pages',
  APPENDIX: 'Appendix B — State Directory',
};

// ---------------------------------------------------------------- CDP (from fitcheck.mjs)
const sleep = ms => new Promise(r => setTimeout(r, ms));

function launchChrome() {
  const profile = mkdtempSync(join(tmpdir(), 'paginate-'));
  const chrome = spawn(CHROME, [
    '--headless=new', '--disable-gpu', '--hide-scrollbars', '--mute-audio',
    '--no-first-run', '--no-default-browser-check',
    `--remote-debugging-port=${PORT}`, `--user-data-dir=${profile}`,
    '--window-size=700,1000', 'about:blank',
  ], { stdio: 'ignore' });
  return { chrome, profile };
}

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

async function measureInChrome(url) {
  const { chrome, profile } = launchChrome();
  try {
    const wsUrl = await endpoint();
    const { ready, send, close } = connect(wsUrl);
    await ready;
    const { targetId } = await send('Target.createTarget', { url });
    const { sessionId } = await send('Target.attachToTarget', { targetId, flatten: true });
    await send('Page.enable', {}, sessionId);
    await sleep(1200); // fonts + layout settle on a much larger DOM than fitcheck's
    const PROBE = `(() => {
      const page = document.querySelector('.page.measure');
      return [...page.children].map(el => {
        const cs = getComputedStyle(el);
        const r = el.getBoundingClientRect();
        return { h: r.height, mt: parseFloat(cs.marginTop) || 0, mb: parseFloat(cs.marginBottom) || 0 };
      });
    })()`;
    const { result } = await send('Runtime.evaluate', { expression: PROBE, returnByValue: true }, sessionId);
    close();
    return result.value;
  } finally {
    try { chrome.kill(); } catch {}
    try { rmSync(profile, { recursive: true, force: true }); } catch {}
  }
}

// ---------------------------------------------------------------- 1. blocks from Python
function loadBlocks() {
  // Plain spawnSync('python3', ...) resolves to a Microsoft Store app-execution-alias
  // stub ahead of the real interpreter on this box's PATH (it prints "Python was not
  // found" and exits 9009) — Node's own Windows executable search order disagrees with
  // the shell's. Routing through `cmd.exe /c` reuses cmd's PATH resolution, which finds
  // the real python3 first, matching what running `python3` in a terminal actually does.
  const r = spawnSync('cmd.exe', ['/c', 'python3', join(HERE, 'blocks_pipeline.py')], {
    maxBuffer: 64 * 1024 * 1024, encoding: 'utf-8',
  });
  if (r.status !== 0) {
    throw new Error(`blocks_pipeline.py failed (exit ${r.status}):\n${r.stderr}`);
  }
  return JSON.parse(r.stdout);
}

// ---------------------------------------------------------------- 2. measure
async function measureBlocks(blocks, css) {
  const tmp = mkdtempSync(join(tmpdir(), 'paginate-measure-'));
  const htmlPath = join(tmp, 'measure.html');
  const doc = `<!doctype html><html><head><meta charset="utf-8"><style>${css}</style></head>` +
    `<body><section class="page measure auto-page">${blocks.map(b => b.html).join('')}` +
    `</section></body></html>`;
  writeFileSync(htmlPath, doc, 'utf-8');
  try {
    const url = pathToFileURL(htmlPath).href;
    const measured = await measureInChrome(url);
    if (measured.length !== blocks.length) {
      throw new Error(`measured ${measured.length} boxes but have ${blocks.length} blocks — DOM/JSON mismatch`);
    }
    return measured;
  } finally {
    rmSync(tmp, { recursive: true, force: true });
  }
}

// ---------------------------------------------------------------- 3. greedy fill
function paginateBlocks(blocks, meas) {
  const N = blocks.length;
  const pages = [];
  const oversizedBlocks = [];
  const oversizedGroups = [];
  let cur = [];
  let cursor = 0;

  const footprint = i => meas[i].mt + meas[i].h + meas[i].mb;
  const bottomEdge = (i, atCursor) => atCursor + meas[i].mt + meas[i].h;
  const fits = (i, atCursor) => bottomEdge(i, atCursor) <= BUDGET_PX;
  const newPage = () => { if (cur.length) pages.push(cur); cur = []; cursor = 0; };

  // Full-group atomicity for h3-anchored spans (numbered protections, binder forms, the
  // timeline's phase subheads — see assign_groups in blocks_pipeline.py): the whole span
  // must land on one page or move together. Narrower "heading + immediate next block"
  // atomicity for any other heading (h1/h2), so a big h2 section (which can contain a
  // list already taller than a page) is not forced into one unsplittable mega-block.
  const isGroupStart = i => blocks[i].group !== null && blocks[i].group !== undefined &&
    (i === 0 || blocks[i - 1].group !== blocks[i].group);
  const groupEnd = i => { const g = blocks[i].group; let j = i; while (j + 1 < N && blocks[j + 1].group === g) j++; return j; };
  const isHeadingRunStart = i => blocks[i].heading && (i === 0 || !blocks[i - 1].heading);
  const headingRunEnd = i => { let j = i; while (j < N && blocks[j].heading) j++; return Math.min(j, N - 1); };
  const spanHeight = (i, j) => {
    let h = 0;
    for (let k = i; k <= j; k++) h += meas[k].mt + meas[k].h + (k < j ? meas[k].mb : 0);
    return h;
  };

  // Tries to keep [i..j] together. If it doesn't fit where we are but WOULD fit a fresh
  // page, starts one. If it wouldn't fit even a fresh page, that's a genuine oversized
  // span — flag it loudly and let the per-block loop place as much as fits (there is no
  // clipping/shrinking option), rather than silently letting it split unremarked. Must
  // re-check against a *fresh* budget (cursor 0) rather than assuming "moved to a new
  // page" alone is sufficient — a span that is simply too tall for any one page will
  // still overflow after the move, and that case needs its own report, not a shrug.
  function tryKeepTogether(i, j, html, file) {
    if (spanHeight(i, j) + cursor <= BUDGET_PX) return; // already fits where we are
    if (cur.length > 0) newPage();
    if (spanHeight(i, j) > BUDGET_PX) {
      oversizedGroups.push({ file, html, neededPx: Math.round(spanHeight(i, j)) });
    }
  }

  let i = 0;
  while (i < N) {
    const b = blocks[i];
    if (b.fileStart && cur.length) newPage();

    if (isGroupStart(i)) {
      tryKeepTogether(i, groupEnd(i), b.html, b.file);
    } else if (isHeadingRunStart(i)) {
      tryKeepTogether(i, headingRunEnd(i), b.html, b.file);
    }

    if (fits(i, cursor)) {
      cur.push(i);
      cursor += footprint(i);
      i++;
    } else if (cur.length === 0) {
      oversizedBlocks.push({ file: b.file, tag: b.tag, html: b.html, neededPx: Math.round(bottomEdge(i, 0)) });
      cur.push(i);
      cursor += footprint(i);
      i++;
    } else {
      newPage();
    }
  }
  if (cur.length) pages.push(cur);
  return { pages, oversizedBlocks, oversizedGroups };
}

// ---------------------------------------------------------------- 4. pre-built splices
// Both Appendix B and the Binder are already-built fixed pages (../appendix/build.py,
// ../binder/build.py) read fresh off disk on every run and never edited in place — the
// same shape, just two different insertion points in the book (the Binder lands mid-
// book, right after Part Six's own manuscript pages; Appendix B stays at the very end).
function loadPrebuiltPages(path, disableFlag) {
  if (process.argv.includes(disableFlag)) return [];
  // A missing file used to return [] and ship a book without the Binder or Appendix B, silently
  // (2026-10-27: a fresh worktree built 438 pages, not 517). Missing is an error; the flag opts out.
  if (!existsSync(path)) throw new Error(`missing ${path} -- build it first (binder/build.py, appendix/build.py) or pass ${disableFlag}`);
  const html = readFileSync(path, 'utf-8');
  return html.match(/<section class="page">[\s\S]*?<\/section>/g) || [];
}

// Finds the last manuscript page (in fillResult.pages) carrying any P6-the-binder.md
// content — the Binder's own 41 form pages are spliced in immediately after it, ahead
// of Part Seven. Throws rather than silently splicing at the wrong spot if P6 stops
// contributing any pages (e.g. blocks_pipeline.py's truncation ate the whole file).
function findBinderSplitIndex(blocks, pages) {
  let splitIdx = -1;
  pages.forEach((idxs, i) => {
    if (idxs.some(k => blocks[k].file === 'P6-the-binder.md')) splitIdx = i;
  });
  if (splitIdx === -1) {
    throw new Error('no manuscript page carries P6-the-binder.md content -- cannot ' +
      'find where to splice in the Binder pages.');
  }
  return splitIdx;
}

// ---------------------------------------------------------------- 5. assemble book.html
function folioHtml(left, right) {
  return `<div class="folio"><span>${left}</span><span>${right}</span></div>`;
}

// Renders one contiguous run of manuscript pages, numbering folios from startFolio+1.
// Called twice (before and after the Binder splice) so the folio sequence stays
// continuous across the inserted pages.
function renderPageRange(blocks, pages, startFolio) {
  const out = [];
  const partCounts = {};
  let pageNo = startFolio;
  for (const idxs of pages) {
    pageNo++;
    const first = blocks[idxs[0]];
    partCounts[first.part] = (partCounts[first.part] || 0) + 1;
    const body = idxs.map(k => blocks[k].html).join('');
    out.push(`<section class="page auto-page">${body}${folioHtml(first.chapterTitle, pageNo)}</section>`);
  }
  return { html: out.join('\n'), partCounts, lastPageNo: pageNo };
}

function splicePrebuiltPages(sections, startPageNo, label) {
  const out = [];
  let pageNo = startPageNo;
  for (const section of sections) {
    pageNo++;
    // Its own within-file folio is dropped and replaced with one carrying the book's
    // running sequence — book.css positions every .folio at the same spot, so keeping
    // both would print two overlapping folios per page.
    const own = section.match(/<p class="folio">\d+<\/p>\s*/);
    if (!own) {
      throw new Error(
        `${label} page ${pageNo - startPageNo} carries no within-page folio to replace — ` +
        'its build.py changed its page footer, so this splice needs rechecking.');
    }
    out.push(section
      .replace(own[0], '')
      .replace('</section>', `${folioHtml(label, pageNo)}</section>`));
  }
  return { html: out.join('\n'), count: sections.length, lastPageNo: pageNo };
}

// ---------------------------------------------------------------- main
async function main() {
  const bookCss = readFileSync(join(HERE, 'book.css'), 'utf-8');
  const autoCss = readFileSync(join(HERE, 'book-auto.css'), 'utf-8');
  const packetCss = readFileSync(PACKET_CSS, 'utf-8');
  // binder.css is not optional the same way packetCss isn't (see the module docstring's
  // note on Appendix B): the Binder's 41 pages carry .bgroup/.btable/.bchecklist markup
  // but inline their own stylesheet standalone, which is discarded when only the
  // <section>s are lifted out here. Missing it fails loudly rather than shipping
  // unstyled/overflowing binder pages into the book.
  if (!existsSync(BINDER_CSS)) throw new Error(`missing ${BINDER_CSS} -- run binder/build.py first.`);
  const binderCss = readFileSync(BINDER_CSS, 'utf-8');
  const css = bookCss + '\n' + autoCss + '\n' + packetCss + '\n' + binderCss;

  console.log('reading manuscript blocks (python3 blocks_pipeline.py)...');
  const blocks = loadBlocks();
  console.log(`  ${blocks.length} blocks from ${new Set(blocks.map(b => b.file)).size} files`);

  console.log('measuring rendered block heights in headless Chrome...');
  const meas = await measureBlocks(blocks, css);

  console.log('laying out pages...');
  const fillResult = paginateBlocks(blocks, meas);

  const splitIdx = process.argv.includes('--no-binder')
    ? fillResult.pages.length - 1
    : findBinderSplitIndex(blocks, fillResult.pages);
  const before = renderPageRange(blocks, fillResult.pages.slice(0, splitIdx + 1), 0);

  const binderSections = loadPrebuiltPages(BINDER_HTML, '--no-binder');
  const binderResult = binderSections.length
    ? splicePrebuiltPages(binderSections, before.lastPageNo, 'The Binder')
    : { html: '', count: 0, lastPageNo: before.lastPageNo };

  const after = renderPageRange(blocks, fillResult.pages.slice(splitIdx + 1), binderResult.lastPageNo);

  const partCounts = { ...before.partCounts };
  for (const [part, n] of Object.entries(after.partCounts)) partCounts[part] = (partCounts[part] || 0) + n;
  if (binderResult.count) partCounts.BINDER = binderResult.count;

  const appendixSections = loadPrebuiltPages(APPENDIX_HTML, '--no-appendix');
  const appendixResult = appendixSections.length
    ? splicePrebuiltPages(appendixSections, after.lastPageNo, 'Appendix B')
    : { html: '', count: 0, lastPageNo: after.lastPageNo };
  if (appendixResult.count) partCounts.APPENDIX = appendixResult.count;

  const doc = `<!doctype html><html lang="en"><head><meta charset="utf-8">` +
    `<title>The Storm-Ready Home</title><style>${css}</style></head><body>\n` +
    `${before.html}\n${binderResult.html}\n${after.html}\n${appendixResult.html}\n</body></html>`;
  writeFileSync(OUT, doc, 'utf-8');

  console.log(`\nwrote ${OUT}`);
  console.log(`\n${appendixResult.lastPageNo} pages total\n`);
  console.log('Per part:');
  for (const [part, label] of Object.entries(PART_LABEL)) {
    if (partCounts[part]) console.log(`  ${label.padEnd(38)} ${partCounts[part]}`);
  }

  if (fillResult.oversizedBlocks.length || fillResult.oversizedGroups.length) {
    console.log('\n[CONTENT OVERFLOW] the following do not fit a full empty page and were NOT ' +
      'clipped, shrunk, or skipped — they are placed as-is and WILL fail fitcheck. This is a ' +
      'content problem (oversized table/heading-run), not a paginator bug:');
    for (const o of fillResult.oversizedBlocks) {
      console.log(`  ${o.file} <${o.tag}> needs ~${o.neededPx}px (budget ${Math.round(BUDGET_PX)}px): ` +
        `${o.html.replace(/<[^>]+>/g, '').slice(0, 80)}`);
    }
    for (const o of fillResult.oversizedGroups) {
      console.log(`  ${o.file} heading-run needs ~${o.neededPx}px: ${o.html.replace(/<[^>]+>/g, '').slice(0, 80)}`);
    }
  }
}

main().catch(e => { console.error(e); process.exit(1); });
