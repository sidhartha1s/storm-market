/* Code-level graphics QC. Loads each composition in headless Chromium, drives its GSAP
 * timeline, and asserts geometry/typography/motion from the DOM — the defects a frame
 * sweep structurally cannot find (text collision, empty containers, crop loss, idle gaps).
 * Usage: node scripts/graphics_qc.mjs episodes/<slug>
 * Exit 0 = pass. Exit 1 = defects found (printed, grouped by composition). */
import { chromium } from 'file:///C:/Users/Sidhartha/AppData/Roaming/npm/node_modules/@playwright/cli/node_modules/playwright-core/index.mjs';
import { readFileSync, readdirSync, writeFileSync, existsSync, mkdirSync } from 'fs';
import { join, resolve, basename } from 'path';

const EXECUTABLE = 'C:\\Users\\Sidhartha\\AppData\\Local\\ms-playwright\\chromium-1228\\chrome-win64\\chrome.exe';
const ep = resolve(process.argv[2] || 'episodes/ep3-tristate');
const TMP = join(ep, '.qc-tmp');
if (!existsSync(TMP)) mkdirSync(TMP, { recursive: true });

const MAX_IDLE = 3.0;          // seconds of no visual change inside a graphic
const MAX_IDLE_OPENING = 2.5;  // tighter for the first 10s of a graphic
const CROP_LOSS_FAIL = 0.35;   // fraction of source image cropped away by object-fit:cover
const SAFE = { w: 1920, h: 1080, pad: 24 };

/* Hard errors block the render. Idle gaps are reported and only fail when a graphic is
 * frozen for most of its window — ep2 (the gold standard) idles in places and still reads
 * as designed, so idling is a budget, not a tripwire. */
const HARD = new Set(['text-collision', 'out-of-frame', 'bad-crop', 'empty-container', 'fade-only',
                      'flat-type', 'no-timeline', 'js-error', 'no-continuous-motion', 'thin-motion', 'idle-budget']);
const defects = [];
const add = (comp, kind, msg) => defects.push({ comp, kind, msg, hard: HARD.has(kind) });

/* ---------- in-page probe: runs inside the composition ---------- */
const PROBE = `(() => {
  const R = { beats: [], tweens: [], type: [], eases: [] };
  const key = Object.keys(window.__timelines || {})[0];
  const tl = window.__timelines[key];
  if (!tl) return { error: 'no timeline registered' };
  R.id = key;
  R.duration = tl.duration();
  for (const t of tl.getChildren(true, true, false)) {
    const st = t.startTime();
    const props = t.vars ? Object.keys(t.vars).filter(k => !['duration','ease','onUpdate','onComplete','delay','stagger'].includes(k)) : [];
    const tgt = (t.targets && t.targets()[0]) ? (t.targets()[0].id || t.targets()[0].tagName || 'obj') : 'obj';
    R.tweens.push({ start: +st.toFixed(2), dur: +(t.duration()||0).toFixed(2), props, ease: String(t.vars && t.vars.ease || 'none'), target: tgt });
    R.beats.push(+st.toFixed(2));
    if (t.duration() > 4) R.beats.push(+(st + t.duration()).toFixed(2)); // long tweens = continuous motion
  }
  R.beats = [...new Set(R.beats)].sort((a,b)=>a-b);
  return R;
})()`;

const MEASURE = `((t) => {
  const key = Object.keys(window.__timelines)[0];
  window.__timelines[key].seek(t, false);
  const out = { texts: [], oob: [], empty: [], crops: [], fonts: [] };
  const vis = (el) => {
    const s = getComputedStyle(el);
    if (s.display === 'none' || s.visibility === 'hidden') return false;
    let n = el, o = 1;
    while (n && n.nodeType === 1) { o *= parseFloat(getComputedStyle(n).opacity || '1'); n = n.parentElement; }
    return o > 0.12;
  };
  const rects = [];
  for (const el of document.querySelectorAll('body *')) {
    if (!vis(el)) continue;
    const r = el.getBoundingClientRect();
    if (r.width < 1 || r.height < 1) continue;
    const own = [...el.childNodes].filter(n => n.nodeType === 3 && n.textContent.trim()).map(n => n.textContent.trim()).join(' ');
    const cs = getComputedStyle(el);
    if (own) {
      rects.push({ el, id: el.id || el.className || el.tagName, text: own.slice(0, 42),
                   x: r.x, y: r.y, w: r.width, h: r.height, fs: parseFloat(cs.fontSize) });
      out.fonts.push(parseFloat(cs.fontSize));
      if (r.x < -SAFEPAD || r.y < -SAFEPAD || r.right > 1920 + SAFEPAD || r.bottom > 1080 + SAFEPAD)
        out.oob.push({ id: el.id || el.className, text: own.slice(0,42), x: Math.round(r.x), y: Math.round(r.y), right: Math.round(r.right), bottom: Math.round(r.bottom) });
    }
    if (el.tagName === 'IMG' && el.naturalWidth) {
      const fit = cs.objectFit;
      if (fit === 'cover' && r.width > 200) {
        const sa = el.naturalWidth / el.naturalHeight, ba = r.width / r.height;
        const keep = sa > ba ? ba / sa : sa / ba;   // fraction of source retained
        if (1 - keep > CROPFAIL) out.crops.push({ src: el.getAttribute('src').split('/').pop(), srcAspect: +sa.toFixed(2), boxAspect: +ba.toFixed(2), lost: +((1-keep)*100).toFixed(0) });
      }
    }
  }
  /* pairwise text overlap — real collisions only: skip DOM ancestor/descendant pairs
     (a parent's box always contains its child's) and skip normal-flow siblings whose
     boxes merely touch. Glyph-level overlap is what garbles text. */
  for (let i = 0; i < rects.length; i++) for (let j = i+1; j < rects.length; j++) {
    const a = rects[i], b = rects[j];
    if (a.el.contains(b.el) || b.el.contains(a.el)) continue;
    const ox = Math.min(a.x+a.w, b.x+b.w) - Math.max(a.x, b.x);
    const oy = Math.min(a.y+a.h, b.y+b.h) - Math.max(a.y, b.y);
    if (ox > 6 && oy > 6) {
      const area = ox * oy, small = Math.min(a.w*a.h, b.w*b.h);
      /* both boxes must be genuinely overlapping, not just adjacent line boxes */
      if (area / small > 0.30) out.texts.push({ a: a.text, b: b.text, overlapPct: +((area/small)*100).toFixed(0) });
    }
  }
  /* containers that are visible but hold nothing — a gradient/border IS content */
  for (const el of document.querySelectorAll('[id^="g-"], .panel, .spanel, .card')) {
    if (!vis(el)) continue;
    const r = el.getBoundingClientRect();
    const cs2 = getComputedStyle(el);
    const painted = cs2.backgroundImage !== 'none' || parseFloat(cs2.borderTopWidth) > 0 ||
                    cs2.backgroundColor !== 'rgba(0, 0, 0, 0)' || cs2.boxShadow !== 'none';
    if (r.width > 300 && r.height > 200 && !el.textContent.trim() && !el.querySelector('svg,img,canvas') && !painted)
      out.empty.push(el.id || el.className);
  }
  out.maxFont = out.fonts.length ? Math.max(...out.fonts) : 0;
  out.minFont = out.fonts.length ? Math.min(...out.fonts) : 0;
  out.tierCount = new Set(out.fonts.map(f => f >= 52 ? 'big' : f >= 26 ? 'mid' : 'small')).size;
  return out;
})`;

function standalone(file) {
  const raw = readFileSync(file, 'utf8');
  const m = raw.match(/<template>([\s\S]*?)<\/template>/);
  const body = m ? m[1] : raw;
  const html = `<!doctype html><html><head><meta charset="utf-8">
<style>html,body{margin:0;width:1920px;height:1080px;background:#000;overflow:hidden}</style>
<script src="../gsap.min.js"></script></head><body>${body}</body></html>`;
  const out = join(TMP, basename(file));
  writeFileSync(out, html, 'utf8');
  return out;
}

const browser = await chromium.launch({ executablePath: EXECUTABLE, args: ['--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
page.on('pageerror', e => add('RUNTIME', 'js-error', String(e).slice(0, 200)));

const compDir = join(ep, 'compositions');
const files = existsSync(compDir) ? readdirSync(compDir).filter(f => f.endsWith('.html')) : [];
if (!files.length) { console.error('[graphics_qc] no compositions/ dir — graphics must be sub-comps (DESIGN.md §1)'); process.exit(1); }

for (const f of files) {
  const name = f.replace('.html', '');
  const url = 'file:///' + standalone(join(compDir, f)).replace(/\\/g, '/');
  await page.goto(url, { waitUntil: 'load' });
  await page.waitForTimeout(120);
  const probe = await page.evaluate(PROBE);
  if (probe.error) { add(name, 'no-timeline', probe.error); continue; }

  /* --- motion vocabulary --- */
  const kinetic = probe.tweens.filter(t => t.props.some(p => ['scale','scaleX','scaleY','x','y','rotation','width','strokeDashoffset','attr'].includes(p)));
  const reveals = probe.tweens.filter(t => t.props.some(p => ['autoAlpha','opacity'].includes(p)));
  if (kinetic.length === 0) add(name, 'fade-only', `${reveals.length} fades, 0 kinetic tweens — DESIGN.md §5`);
  else if (reveals.length > 2 && kinetic.length < reveals.length / 2)
    add(name, 'thin-motion', `${kinetic.length} kinetic vs ${reveals.length} fades (need ≥1 per 2)`);
  if (probe.duration > 20 && !probe.tweens.some(t => t.dur >= 8))
    add(name, 'no-continuous-motion', `${probe.duration.toFixed(1)}s graphic, longest tween ${Math.max(...probe.tweens.map(t=>t.dur)).toFixed(1)}s — §5 needs a continuous element`);
  const punchy = probe.tweens.filter(t => /power[34]|back|elastic|expo/.test(t.ease)).length;
  if (probe.tweens.length >= 6 && punchy === 0) add(name, 'limp-easing', 'no power3/power4 easing anywhere — §5');

  /* --- beat cadence. A gap is only idle if NOTHING is moving through it: a continuous
     tween spanning the gap (ep2's 26s rotation) keeps the frame alive. --- */
  const spans = probe.tweens.filter(t => t.dur >= 4).map(t => [t.start, t.start + t.dur]);
  const covered = (a, b) => spans.some(([s, e]) => s <= a + 0.25 && e >= b - 0.25);
  const beats = probe.beats.filter(b => b <= probe.duration + 0.01);
  let prev = 0;
  for (const b of beats) {
    const gap = b - prev;
    const limit = prev < 10 ? MAX_IDLE_OPENING : MAX_IDLE;
    if (gap > limit && !covered(prev, b))
      add(name, 'idle', `${gap.toFixed(1)}s frozen at ${prev.toFixed(1)}s–${b.toFixed(1)}s (limit ${limit}s, nothing in motion) — §6`);
    prev = b;
  }
  if (probe.duration - prev > MAX_IDLE && !covered(prev, probe.duration))
    add(name, 'idle-tail', `${(probe.duration - prev).toFixed(1)}s frozen tail after last beat — §6`);

  /* --- geometry + typography at every beat and each midpoint --- */
  const samples = [...new Set(beats.flatMap((b, i) => [b + 0.35, i < beats.length - 1 ? (b + beats[i+1]) / 2 : b + 0.9]))]
    .filter(t => t >= 0 && t <= probe.duration);
  const seenOverlap = new Set(), seenCrop = new Set(), seenOob = new Set();
  let tierMax = 0;
  for (const t of samples) {
    const m = await page.evaluate(`${MEASURE.replace(/SAFEPAD/g, SAFE.pad).replace(/CROPFAIL/g, CROP_LOSS_FAIL)}(${t})`);
    tierMax = Math.max(tierMax, m.tierCount);
    for (const o of m.texts) { const k = o.a + '|' + o.b; if (!seenOverlap.has(k)) { seenOverlap.add(k); add(name, 'text-collision', `"${o.a}" ⨯ "${o.b}" (${o.overlapPct}% at ${t.toFixed(1)}s)`); } }
    for (const o of m.oob) { const k = o.text; if (!seenOob.has(k)) { seenOob.add(k); add(name, 'out-of-frame', `"${o.text}" at x${o.x} y${o.y} → ${o.right}×${o.bottom} (${t.toFixed(1)}s)`); } }
    for (const c of m.crops) { if (!seenCrop.has(c.src)) { seenCrop.add(c.src); add(name, 'bad-crop', `${c.src} loses ${c.lost}% (source ${c.srcAspect}:1 in ${c.boxAspect}:1 box)`); } }
    for (const e of m.empty) add(name, 'empty-container', `${e} visible but empty at ${t.toFixed(1)}s`);
  }
  if (tierMax < 3) add(name, 'flat-type', `only ${tierMax} type tier(s) — §3 needs ≥52px, 26–30px and ≤22px together`);
}

await browser.close();

/* ---------- report ---------- */
if (!defects.length) { console.log(`[graphics_qc] PASS — ${files.length} compositions, 0 defects`); process.exit(0); }
const byComp = {};
for (const d of defects) (byComp[d.comp] ||= []).push(d);
console.log(`[graphics_qc] FAIL — ${defects.length} defects across ${Object.keys(byComp).length} compositions\n`);
for (const [c, list] of Object.entries(byComp)) {
  console.log(`  ${c}  (${list.length})`);
  for (const d of list) console.log(`    [${d.kind}] ${d.msg}`);
}
process.exit(1);
