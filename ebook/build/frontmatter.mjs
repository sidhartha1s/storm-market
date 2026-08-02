/* frontmatter.mjs — standalone post-processor that prepends cover, title, copyright and
   table-of-contents pages ahead of the laid-out book, and writes book-final.html.

   Does NOT touch book.html or paginate.mjs. Re-runnable: every fact it prints (chapter
   titles, page numbers, part names) is parsed fresh out of book.html on each run, never
   hardcoded, so it stays correct as the manuscript grows and paginate.mjs re-lays-out pages.

   Usage: node frontmatter.mjs [book.html] [book-final.html] */

import { readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE      = dirname(fileURLToPath(import.meta.url));
const bookPath  = process.argv[2] || join(HERE, 'book.html');
const outPath   = process.argv[3] || join(HERE, 'book-final.html');
const coverPath = join(HERE, 'art', 'cover-v3-raymond.png');
const cssPath   = join(HERE, 'front.css');

const book = readFileSync(bookPath, 'utf8');

// Word-numeral -> digit. Covers the book's own numbering (parts to seven, chapters to
// seven) with headroom for growth; PLAYBOOK kickers are already digits and skip this map.
const WORD_NUM = {
  ZERO: 0, ONE: 1, TWO: 2, THREE: 3, FOUR: 4, FIVE: 5, SIX: 6, SEVEN: 7,
  EIGHT: 8, NINE: 9, TEN: 10, ELEVEN: 11, TWELVE: 12,
};

// ---------- 1. parse the built book into a structure map ----------

// The front matter itself states what each of the seven parts is for ("Part One — Why
// people die."). Pull those descriptions from the prose rather than retyping them, so a
// wording change upstream flows through here with no code edit.
const partDesc = {};
for (const m of book.matchAll(/<strong>Part (\w+) — ([^<]+)\.<\/strong>/g)) {
  partDesc[m[1].toUpperCase()] = m[2];
}

const bodyStart = book.indexOf('<body');
const body = book.slice(bodyStart);

// Every page is <section class="page"> or <section class="page auto-page">, ending in
// a .folio div whose second span is the printed page number — read that number rather
// than recomputing it, so the TOC always points at what's actually printed on the page.
const pageRe = /<section class="page(?: auto-page)?">([\s\S]*?)<\/section>/g;

// Chapter/part openers carry <h1 class="chapter-open"><span class="kicker">KICKER</span>Title</h1>.
// Appendix B has no such h1 — it repeats <p class="runhead">Appendix B — ...</p> on every
// one of its pages instead, so it's picked up as a "new title" transition: the first page
// whose runhead text differs from whatever section was open before it.
const openers = [];
let currentTitle = null;
let m;
while ((m = pageRe.exec(body))) {
  const content = m[1];
  const folioM = content.match(/<div class="folio"><span>[^<]*<\/span><span>([^<]*)<\/span><\/div>/);
  const page = folioM ? folioM[1] : null;

  const h1M = content.match(/<h1[^>]*class="chapter-open"[^>]*><span class="kicker">([^<]*)<\/span>([\s\S]*?)<\/h1>/);
  if (h1M) {
    const kicker = h1M[1].trim();
    const title = h1M[2].replace(/<[^>]+>/g, '').trim();
    openers.push({ kind: 'kicker', kicker, title, page });
    currentTitle = title;
    continue;
  }

  const rhM = content.match(/<p class="runhead">([^<]*)<\/p>/);
  if (rhM && rhM[1].trim() !== currentTitle) {
    openers.push({ kind: 'runhead', title: rhM[1].trim(), page });
    currentTitle = rhM[1].trim();
  }
}
if (!openers.length) throw new Error('frontmatter.mjs: found no chapter/part openers in book.html — layout shape changed?');

// ---------- 2. turn openers into TOC rows ----------
// A "PART X" kicker with no matching "PART X, CHAPTER/PLAYBOOK ..." anywhere is a single-page
// part (Front Matter, the Binder, the 60 Days) and renders as one flat row. A "PART X, ..."
// kicker groups under a part-header row (using the front matter's own description of that
// part), with each chapter/playbook indented beneath it. Back matter and Appendix B are
// top-level flat rows with no part.
const toc = [];
let openPartNum = null;

for (const o of openers) {
  if (o.kind === 'runhead') {
    toc.push({ level: 'flat', title: o.title, page: o.page });
    openPartNum = null;
    continue;
  }

  if (o.kicker === 'BACK MATTER') {
    toc.push({ level: 'flat', title: o.title, page: o.page });
    openPartNum = null;
    continue;
  }

  const bare = o.kicker.match(/^PART (\S+)$/);
  if (bare) {
    const num = bare[1];
    if (num === 'ZERO') {
      toc.push({ level: 'flat', title: o.title, page: o.page });
    } else {
      toc.push({ level: 'flat', title: `Part ${WORD_NUM[num] ?? num} — ${o.title}`, page: o.page });
    }
    openPartNum = null;
    continue;
  }

  const nested = o.kicker.match(/^PART (\S+), (CHAPTER|PLAYBOOK) (\S+)$/);
  if (nested) {
    const [, num, kind, chNum] = nested;
    if (openPartNum !== num) {
      const desc = partDesc[num] || o.title;
      toc.push({ level: 'head', title: `Part ${WORD_NUM[num] ?? num} — ${desc}` });
      openPartNum = num;
    }
    const chLabel = kind === 'CHAPTER' ? `Chapter ${WORD_NUM[chNum] ?? chNum}` : `Playbook ${chNum}`;
    toc.push({ level: 'child', title: `${chLabel} — ${o.title}`, page: o.page });
    continue;
  }

  throw new Error(`frontmatter.mjs: unrecognised kicker shape "${o.kicker}" — update the parser.`);
}

// ---------- 3. render TOC rows into pages ----------
// No headless browser available at build time to measure real layout, so pagination is
// estimated from the same point sizes book.css assigns .toc .row / .toc .part, with a
// safety margin. fitcheck.mjs (run in step 5) is the actual gate — if a future manuscript
// change ever overflows a TOC page, raise ROWS_SAFETY_MARGIN below rather than the row math.
const PAGE_CONTENT_PT = 7.68 * 72;   // 9in page - 0.72in top pad - 0.6in bottom pad, in points
const ROWS_SAFETY_MARGIN = 0.85;      // budget only 85% of the estimated content height
const ROW_PT  = 9.6 * 1.25 + 4.2 * 2; // .toc row: 9.6pt text, ~1.25 line-height, 2.1pt padding top+bottom
const HEAD_PT = 7.4 * 1.25 + 12 + 5 + 3.5; // .toc .part: 7.4pt text + its margin/padding/border

function rowHeight(entry) { return entry.level === 'head' ? HEAD_PT : ROW_PT; }

const tocPages = [];
let cur = [];
let curHeight = 0;
const budget = PAGE_CONTENT_PT * ROWS_SAFETY_MARGIN;
for (let i = 0; i < toc.length; i++) {
  const entry = toc[i];
  let h = rowHeight(entry);
  // Don't strand a part header alone at the bottom of a page — pull it and its first
  // child onto the next page together if there isn't room for both.
  if (entry.level === 'head') {
    const next = toc[i + 1];
    if (next) h += rowHeight(next);
  }
  if (cur.length && curHeight + h > budget) {
    tocPages.push(cur);
    cur = [];
    curHeight = 0;
  }
  cur.push(entry);
  curHeight += rowHeight(entry);
}
if (cur.length) tocPages.push(cur);

function tocRowHtml(entry) {
  if (entry.level === 'head') return `<div class="part">${entry.title}</div>`;
  const subClass = entry.level === 'child' ? ' sub' : '';
  return `<div class="row${subClass}"><span class="ti">${entry.title}</span><span class="dots"></span><span class="pg">${entry.page}</span></div>`;
}

function toRoman(n) {
  const table = [[10, 'x'], [9, 'ix'], [5, 'v'], [4, 'iv'], [1, 'i']];
  let s = '';
  for (const [v, sym] of table) while (n >= v) { s += sym; n -= v; }
  return s;
}

// Title/copyright pages are conventionally unnumbered (i, ii). The TOC is the first
// printed folio, starting at iii — a plain convention, not a fact read out of the book.
const ROMAN_START = 3;
const tocPagesHtml = tocPages.map((rows, i) => `
<section class="page">
  <div class="toc">
${rows.map(tocRowHtml).join('\n')}
  </div>
  <div class="folio"><span>Contents</span><span>${toRoman(ROMAN_START + i)}</span></div>
</section>`).join('\n');

// ---------- 4. cover, title, copyright ----------

const coverB64 = readFileSync(coverPath).toString('base64');
const coverHtml = `
<section class="page cover"><img class="plate" src="data:image/png;base64,${coverB64}" alt=""></section>`;

// Title and subtitle are printed on the cover art itself (ground truth for both), and the
// same subtitle line is the hero headline on the live landing page — pulled here, not
// invented. No ISBN, publisher, printing location or website exist anywhere in this repo,
// so none are printed.
const TITLE = 'The Storm-Ready Home';
const SUBTITLE = 'What the survivors did differently — and the 130 things you can do before the next one.';
const AUTHOR = 'Paul Raymond';

const titleHtml = `
<section class="page">
  <div class="fm-title">
    <h1>${TITLE}</h1>
    <p class="fm-sub">${SUBTITLE}</p>
    <p class="fm-byline">${AUTHOR}</p>
  </div>
</section>`;

const copyrightHtml = `
<section class="page">
  <div class="legal">
    <p>Copyright © 2026 ${AUTHOR}. All rights reserved.</p>
    <p>No part of this book may be reproduced, distributed, or transmitted in any form
    without the prior written permission of the author, except for brief quotations
    embedded in critical reviews.</p>
    <p>First edition.</p>
    <p><strong>Disclaimer.</strong> This book is general preparedness information. It is
    not professional engineering, medical, legal, or insurance advice, and it does not
    replace the judgment of a licensed engineer, physician, attorney, or your insurance
    carrier for decisions specific to your home, your health, your policy, or your
    situation. Agency phone numbers, program names, and state provisions described here,
    including the directory in Appendix B, were verified as of the dates printed beside
    each entry; agencies change contact details, eligibility rules, and programs over
    time. Confirm anything load-bearing — a permit requirement, a benefit, a legal
    deadline — with the issuing agency directly before you rely on it.</p>
  </div>
</section>`;

// ---------- 5. assemble and write ----------

const frontCss = readFileSync(cssPath, 'utf8');
const withCss = book.replace('</style></head>', `${frontCss}</style></head>`);

const insertAt = withCss.indexOf('<body', 0) + withCss.slice(withCss.indexOf('<body')).indexOf('>') + 1;
const finalHtml =
  withCss.slice(0, insertAt) +
  coverHtml + titleHtml + copyrightHtml + tocPagesHtml +
  withCss.slice(insertAt);

writeFileSync(outPath, finalHtml);

console.log(`frontmatter.mjs: wrote ${outPath}`);
console.log(`  front pages: 1 cover + 1 title + 1 copyright + ${tocPages.length} TOC page(s) = ${3 + tocPages.length} total`);
console.log(`  TOC entries: ${toc.length} (${toc.filter(t => t.level === 'head').length} part headers)`);
console.log(`  TOC folios: iii..${toRoman(ROMAN_START + tocPages.length - 1)}`);
