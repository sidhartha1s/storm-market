/* Code-level graphics QC. Loads each composition in headless Chromium, drives its GSAP
 * timeline, and asserts geometry/typography/motion from the DOM — the defects a frame
 * sweep structurally cannot find (text collision, empty containers, crop loss, idle gaps).
 * Usage: node scripts/graphics_qc.mjs episodes/<slug>
 * Exit 0 = pass. Exit 1 = defects found (printed, grouped by composition). */
import { chromium, chromiumExecutable } from './playwright_env.mjs';
import { readFileSync, readdirSync, writeFileSync, existsSync, mkdirSync } from 'fs';
import { join, resolve } from 'path';
import { CANVAS_RENDERER, hostCss, motionSpans, stageComp } from './stage_comp.mjs';

const EXECUTABLE = chromiumExecutable();
const ep = resolve(process.argv[2] || 'episodes/ep3-tristate');
const TMP = join(ep, '.qc-tmp');
if (!existsSync(TMP)) mkdirSync(TMP, { recursive: true });

const MAX_IDLE = 4.0;          // a gap this long with nothing moving fails (same number as beat_density)
const CROP_LOSS_FAIL = 0.35;   // fraction of source image cropped away by object-fit:cover
const SAFE = { w: 1920, h: 1080, pad: 24 };

/* Hard errors block the render. Stillness has one number and no warning tier (owner, 26 Sep 26):
 * any gap of MAX_IDLE or more with nothing moving is an 'idle' error. */
const HARD = new Set(['text-collision', 'out-of-frame', 'bad-crop', 'empty-container', 'fade-only',
                      'flat-type', 'no-timeline', 'js-error', 'undesigned', 'idle', 'short-duration',
                      'broken-image']);
const DURS = {};
const FRAMES = {};
const defects = [];

/* The three moments the vision pass reads (references/mg-quickref.md "Verify"), chosen from the tween
 * schedule so no frame lands mid-animation: the opening reveal has settled, a settled moment
 * halfway through the hold, and the last settled moment before the exit starts. Loops (>= 4 s) are
 * ambient motion, not reveals; "settled" means no shorter tween is running at that instant. */
function settleFrames(tweens, windowEnd) {
  const short = tweens.filter(t => t.dur < 4 && t.start < windowEnd);
  const moving = t => short.some(tw => tw.start <= t && t < tw.start + tw.dur);
  /* nearest moment in [lo, hi] with nothing moving, searching `step` direction first, then the other */
  const settleFrom = (t, step, lo, hi) => {
    t = Math.min(Math.max(t, lo), hi);
    for (const s of [step, -step]) {
      let c = t;
      while (moving(c) && c + s >= lo && c + s <= hi) c += s;
      if (!moving(c)) return c;
    }
    return t;
  };
  const clamp = t => +Math.min(Math.max(t, 0), windowEnd - 0.05).toFixed(2);
  const opening = short.filter(t => t.start < 1.5);
  const openEnd = opening.length ? Math.max(...opening.map(t => t.start + t.dur)) : 0;
  /* an exit is a tween that hides (to opacity 0 / autoAlpha 0) or slides an element off-frame, after the opening */
  const exits = short.filter(t => t.hide && t.start >= openEnd);
  const exitStart = exits.length ? Math.min(...exits.map(t => t.start)) : windowEnd;
  const first = clamp(settleFrom(opening.length ? openEnd + 0.1 : 0.5, 0.1, 0, exitStart));
  const pre = clamp(Math.max(first, settleFrom(exitStart - 0.25, -0.1, first, exitStart)));
  const mid = clamp(settleFrom((first + pre) / 2, 0.1, first, pre));
  return [
    { t: first, why: opening.length ? `opening settled: the tweens that start in the first 1.5s have finished` : 'no opening tweens: 0.5s in' },
    { t: mid, why: 'mid-hold: first settled moment from halfway between frames 1 and 3' },
    { t: pre, why: exits.length ? `pre-exit: last settled moment before the exit tween at ${exitStart.toFixed(2)}s` : `pre-exit: no exit tween, last settled moment of the ${windowEnd.toFixed(2)}s window` },
  ];
}
/* A declared exemption (flat-type: data-type-ok="reason" on the comp root; bad-crop: data-crop-ok="reason"
 * on the img) is recorded with its reason and printed, never silent. An empty reason exempts nothing;
 * no other rule takes one (idle least of all). */
const add = (comp, kind, msg, ok = '') => defects.push({ comp, kind, msg, ok, hard: !ok && HARD.has(kind) });

/* ---------- in-page probe: runs inside the composition ---------- */
const PROBE = `(() => {
  const R = { beats: [], tweens: [], type: [], eases: [] };
  const key = Object.keys(window.__timelines || {})[0];
  const tl = window.__timelines[key];
  if (!tl) return { error: 'no timeline registered' };
  R.id = key;
  R.duration = tl.duration();
  // a canvas redrawn from the timeline onUpdate moves every frame though no DOM tween does:
  // one continuous kinetic span (MG eval 3, 26 Sep 26; rule in stage_comp.mjs)
  if (${CANVAS_RENDERER})
    R.tweens.push({ start: 0, dur: R.duration, props: ['canvas-render'], ease: 'none', target: 'canvas', hide: false });
  for (const t of tl.getChildren(true, true, false)) {
    const st = t.startTime();
    /* totalDuration(), not duration(): a repeating tween (ambient loops) reports its ONE-cycle
       duration from duration(), which reads as a short tween that stops covering the idle gap
       it's actually animating through for the rest of the comp's window. */
    const td = (t.totalDuration ? t.totalDuration() : t.duration()) || 0;
    const props = t.vars ? Object.keys(t.vars).filter(k => !['duration','ease','onUpdate','onComplete','delay','stagger'].includes(k)) : [];
    const tgt = (t.targets && t.targets()[0]) ? (t.targets()[0].id || t.targets()[0].tagName || 'obj') : 'obj';
    const v = t.vars || {};
    const off = (x) => typeof x === 'number' && Math.abs(x) >= 1000 || /^[-+]?(1\\d\\d|[2-9]\\d\\d)%$/.test(String(x));
    const hide = v.opacity === 0 || v.autoAlpha === 0 || off(v.x) || off(v.y) || Math.abs(v.xPercent || 0) >= 100 || Math.abs(v.yPercent || 0) >= 100;
    R.tweens.push({ start: +st.toFixed(2), dur: +td.toFixed(2), props, ease: String(t.vars && t.vars.ease || 'none'), target: tgt, hide });
    R.beats.push(+st.toFixed(2));
    if (td > 4) R.beats.push(+(st + td).toFixed(2)); // long tweens = continuous motion
  }
  R.beats = [...new Set(R.beats)].sort((a,b)=>a-b);
  return R;
})()`;

const MEASURE = `((t) => {
  const key = Object.keys(window.__timelines)[0];
  window.__timelines[key].seek(t, false);
  const out = { texts: [], oob: [], empty: [], crops: [], fonts: [], broken: [] };
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
    const cs = getComputedStyle(el);
    /* glyph-level ink boxes, not element boxes: line-height padding and block width
       make element rects overlap constantly without any visible garbling */
    for (const node of el.childNodes) {
      if (node.nodeType !== 3 || !node.textContent.trim()) continue;
      const rng = document.createRange(); rng.selectNodeContents(node);
      for (const ir of rng.getClientRects()) {
        if (ir.width < 2 || ir.height < 2) continue;
        rects.push({ el, id: el.id || el.className || el.tagName, text: node.textContent.trim().slice(0, 42),
                     x: ir.x, y: ir.y, w: ir.width, h: ir.height, fs: parseFloat(cs.fontSize) });
        if (ir.x < -SAFEPAD || ir.y < -SAFEPAD || ir.right > 1920 + SAFEPAD || ir.bottom > 1080 + SAFEPAD)
          out.oob.push({ id: el.id || el.className, text: node.textContent.trim().slice(0,42),
                         x: Math.round(ir.x), y: Math.round(ir.y), right: Math.round(ir.right), bottom: Math.round(ir.bottom) });
      }
      out.fonts.push(parseFloat(cs.fontSize));
    }
    if (el.tagName === 'IMG') {
      const src = el.getAttribute('src');
      if (src && !el.naturalWidth) {
        // a 404'd image (wrong staged-path prefix, most often) silently reads as naturalWidth 0
        // and every check below it was skipped without a word — fail loud instead
        out.broken.push(src.split('/').pop());
      } else if (el.naturalWidth) {
        const fit = cs.objectFit;
        if (fit === 'cover' && r.width > 200) {
          const sa = el.naturalWidth / el.naturalHeight, ba = r.width / r.height;
          const keep = sa > ba ? ba / sa : sa / ba;   // fraction of source retained
          if (1 - keep > CROPFAIL) out.crops.push({ src: src.split('/').pop(), srcAspect: +sa.toFixed(2), boxAspect: +ba.toFixed(2), lost: +((1-keep)*100).toFixed(0) });
        }
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
      /* Stacked lines whose boxes kiss are not garbled text. Real garbling means the ink
         boxes overlap deeply in BOTH axes, or one sits well inside the other. */
      const vFrac = oy / Math.min(a.h, b.h), hFrac = ox / Math.min(a.w, b.w);
      const area = ox * oy, small = Math.min(a.w*a.h, b.w*b.h);
      if (vFrac > 0.45 && hFrac > 0.35)
        out.texts.push({ a: a.text, b: b.text, overlapPct: +((area/small)*100).toFixed(0) });
    }
  }
  /* containers that are visible but hold nothing — a gradient/border IS content */
  for (const el of document.querySelectorAll('[id^="g-"], .panel, .spanel, .card')) {
    if (!vis(el) || el instanceof SVGElement) continue;
    const r = el.getBoundingClientRect();
    const cs2 = getComputedStyle(el);
    const painted = cs2.backgroundImage !== 'none' || parseFloat(cs2.borderTopWidth) > 0 ||
                    cs2.backgroundColor !== 'rgba(0, 0, 0, 0)' || cs2.boxShadow !== 'none';
    if (r.width > 300 && r.height > 200 && !el.textContent.trim() && !el.querySelector('svg,img,canvas') && !painted &&
        ![...el.querySelectorAll('*')].some(c => { const s = getComputedStyle(c); return s.backgroundImage !== 'none' ||
          s.backgroundColor !== 'rgba(0, 0, 0, 0)' || parseFloat(s.borderTopWidth) > 0; }))   // painted children ARE content (ep-1974 tile grid, red X)
      out.empty.push(el.id || el.className);
  }
  /* opaque coverage: a panel overlay lets the moving photo underneath carry the motion;
     a full-frame graphic must animate something itself */
  let cover = 0;
  for (const el of document.querySelectorAll('body *')) {
    if (!vis(el) || el.tagName === 'SCRIPT' || el.tagName === 'STYLE') continue;
    const cs3 = getComputedStyle(el), r3 = el.getBoundingClientRect();
    const solid = (cs3.backgroundColor && !/rgba\(0, 0, 0, 0\)/.test(cs3.backgroundColor) &&
                   !/rgba\([^)]+,\s*0?\.[0-5]\d*\)/.test(cs3.backgroundColor)) ||
                  (cs3.backgroundImage !== 'none' && !/transparent/.test(cs3.backgroundImage));
    if (solid) cover = Math.max(cover, (Math.min(r3.width,1920) * Math.min(r3.height,1080)) / (1920*1080));
  }
  out.coverage = +cover.toFixed(2);
  let painted = 0, grad = false;
  for (const el of document.querySelectorAll('body *')) {
    if (!vis(el) || el.tagName === 'SCRIPT' || el.tagName === 'STYLE') continue;
    const r4 = el.getBoundingClientRect();
    if (r4.width >= 2 && r4.height >= 2) painted++;
    const cs = getComputedStyle(el);
    // a gradient OR a frosted-glass panel (backdrop-filter blur over footage) is a designed background —
    // the glass cards were flagged 'undesigned' for two episodes on this line alone (2026-09-11)
    if (/gradient/.test(cs.backgroundImage) || /blur/.test(cs.backdropFilter || cs.webkitBackdropFilter || '')) grad = true;
    // a canvas covering a quarter of the frame or more (Three.js/WebGL) is a rendered background the DOM
    // cannot read; without this every WebGL comp read as "flat background" (MG eval 2, 26 Sep 26)
    if (el.tagName === 'CANVAS' && r4.width * r4.height >= 0.25 * 1920 * 1080) grad = true;
  }
  out.elements = painted; out.gradient = grad;
  out.textNodes = out.fonts.length;
  out.maxFont = out.fonts.length ? Math.max(...out.fonts) : 0;
  out.minFont = out.fonts.length ? Math.min(...out.fonts) : 0;
  out.tierCount = new Set(out.fonts.map(f => f >= 52 ? 'big' : f >= 26 ? 'mid' : 'small')).size;
  return out;
})`;

// Host-style injection: hyperframes mounts comps INSIDE index.html's DOM, so the page stylesheet
// applies to comp elements (17 Sep 26: host `.chip{bottom:300px}` stretched a comp chip into a 720 px
// panel; every standalone gate passed). Staging must carry the host <style> blocks.
const INDEX_HTML = readFileSync(join(ep, 'index.html'), 'utf8');
const HOST_CSS = hostCss(INDEX_HTML);
// per-composition host window: the duration the master timeline mounts it for (assets-comps-05)
const HOSTS = {};
for (const m of INDEX_HTML.matchAll(/<[a-z]+\b[^>]*\bdata-composition-src="compositions\/([^"]+)\.html"[^>]*>/g)) {
  const dur = parseFloat((/\bdata-duration="([\d.]+)"/.exec(m[0]) || [])[1]);
  if (!isNaN(dur)) HOSTS[m[1]] = Math.max(HOSTS[m[1]] || 0, dur);
}

const browser = await chromium.launch({ executablePath: EXECUTABLE, args: ['--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
page.on('pageerror', e => add('RUNTIME', 'js-error', String(e).slice(0, 200)));

const compDir = join(ep, 'compositions');
const files = existsSync(compDir) ? readdirSync(compDir).filter(f => f.endsWith('.html')) : [];
if (!files.length) { console.error('[graphics_qc] no compositions/ dir — graphics must be sub-comps (references/mg-quickref.md File contract)'); process.exit(1); }

for (const f of files) {
  const name = f.replace('.html', '');
  const url = 'file:///' + stageComp(ep, join(compDir, f), HOST_CSS).replace(/\\/g, '/');
  await page.goto(url, { waitUntil: 'load' });
  await page.waitForTimeout(120);
  const probe = await page.evaluate(PROBE);
  if (probe.error) { add(name, 'no-timeline', probe.error); continue; }
  DURS[name] = +probe.duration.toFixed(2);

  /* --- host window: references/mg-quickref.md (File contract, Motion and exits) requires the comp to outlast the window it's mounted for,
     or the panel freezes/vanishes before the cut instead of sliding out on it. --- */
  const hostDur = HOSTS[name];
  if (hostDur != null && probe.duration < hostDur - 0.05)
    add(name, 'short-duration', `timeline ${probe.duration.toFixed(2)}s ends before its host window ${hostDur.toFixed(2)}s — ${(hostDur - probe.duration).toFixed(2)}s frozen tail before the cut (mg-quickref File contract)`);
  const windowEnd = Math.max(probe.duration, hostDur || 0);
  /* frames come from what is ON SCREEN: a comp cut by a shorter host (g-plane: 50 s timeline in a
     28.9 s host) must never be sampled after its host window ends, or the reader judges another graphic */
  FRAMES[name] = settleFrames(probe.tweens, hostDur ?? probe.duration);

  /* --- motion vocabulary --- */
  const kinetic = probe.tweens.filter(t => t.props.some(p => ['scale','scaleX','scaleY','x','y','rotation','width','strokeDashoffset','attr','canvas-render'].includes(p)));
  const reveals = probe.tweens.filter(t => t.props.some(p => ['autoAlpha','opacity'].includes(p)));
  if (kinetic.length === 0) add(name, 'fade-only', `${reveals.length} fades, 0 kinetic tweens — mg-quickref Motion`);
  else if (reveals.length > 2 && kinetic.length < reveals.length / 2)
    add(name, 'thin-motion', `${kinetic.length} kinetic vs ${reveals.length} fades (need ≥1 per 2)`);
  /* deferred: needs coverage from the measure pass (set below) */
  const punchy = probe.tweens.filter(t => /power[34]|back|elastic|expo/.test(t.ease)).length;
  if (probe.tweens.length >= 6 && punchy === 0) add(name, 'limp-easing', 'no power3/power4 easing anywhere — mg-quickref Motion');

  /* --- stillness: the same spans as beat_density (stage_comp.mjs motionSpans; a {} clock is not
     motion), walked from the end of motion to the next start, over what is ON SCREEN (the host
     window, or the timeline when unmounted). --- */
  const beats = probe.beats.filter(b => b <= windowEnd + 0.01);
  const idleEnd = hostDur ?? probe.duration;
  // ponytail: rule 3 samples at most 600 s; an unmounted repeat:-1 comp is covered by rule 1 anyway
  const spans = (await page.evaluate(`(() => { const tl = window.__timelines[${JSON.stringify(probe.id)}]; return ${motionSpans(Math.min(idleEnd, 600))}; })()`))
    .sort((a, b) => a[0] - b[0]);
  let still = 0, frozen = 0;
  const idle = (a, b) => {
    if (b - a < MAX_IDLE) return;
    frozen += b - a;
    add(name, 'idle', `${(b - a).toFixed(1)}s frozen at ${a.toFixed(1)}s–${b.toFixed(1)}s (nothing in motion) — mg-quickref Motion`);
  };
  for (const [s, e] of spans) {
    if (s >= idleEnd) break;
    idle(still, s);
    still = Math.max(still, e);
  }
  idle(still, idleEnd);
  const idleFrac = frozen / idleEnd;

  /* --- geometry + typography at every beat and each midpoint --- */
  const samples = [...new Set(beats.flatMap((b, i) => [b + 0.35, i < beats.length - 1 ? (b + beats[i+1]) / 2 : b + 0.9]))]
    .filter(t => t >= 0.4 && t <= probe.duration - 1.0)
    /* entry/exit slides intentionally park elements off-frame; don't audit geometry mid-slide */
    .filter(t => !probe.tweens.some(tw => tw.props.includes('x') && tw.dur <= 1.2 &&
                 tw.start - 0.15 <= t && t <= tw.start + tw.dur + 0.35));
  const seenOverlap = new Set(), seenCrop = new Set(), seenOob = new Set(), seenEmpty = new Set(), seenBroken = new Set();
  let tierMax = 0, maxCoverage = 0, maxTextNodes = 0; const elemSamples = []; let gradAny = false;
  for (const t of samples) {
    const m = await page.evaluate(`${MEASURE.replace(/SAFEPAD/g, SAFE.pad).replace(/CROPFAIL/g, CROP_LOSS_FAIL)}(${t})`);
    tierMax = Math.max(tierMax, m.tierCount);
    maxCoverage = Math.max(maxCoverage, m.coverage || 0);
    maxTextNodes = Math.max(maxTextNodes, m.textNodes || 0);
    elemSamples.push(m.elements || 0); gradAny = gradAny || !!m.gradient;
    for (const o of m.texts) { const k = o.a + '|' + o.b; if (!seenOverlap.has(k)) { seenOverlap.add(k); add(name, 'text-collision', `"${o.a}" ⨯ "${o.b}" (${o.overlapPct}% at ${t.toFixed(1)}s)`); } }
    for (const o of m.oob) { const k = o.text; if (!seenOob.has(k)) { seenOob.add(k); add(name, 'out-of-frame', `"${o.text}" at x${o.x} y${o.y} → ${o.right}×${o.bottom} (${t.toFixed(1)}s)`); } }
    for (const c of m.crops) { if (!seenCrop.has(c.src)) { seenCrop.add(c.src); add(name, 'bad-crop', `${c.src} loses ${c.lost}% (source ${c.srcAspect}:1 in ${c.boxAspect}:1 box)`); } }
    for (const e of m.empty) { if (!seenEmpty.has(e)) { seenEmpty.add(e); add(name, 'empty-container', `${e} visible but empty (first at ${t.toFixed(1)}s)`); } }
    for (const b of m.broken) { if (!seenBroken.has(b)) { seenBroken.add(b); add(name, 'broken-image', `${b} failed to load (naturalWidth 0) — staged-path 404, not a crop/empty defect (${t.toFixed(1)}s)`); } }
  }
  if (tierMax < 3 && maxTextNodes >= 4)
    add(name, 'flat-type', `only ${tierMax} type tier(s) across ${maxTextNodes} text elements — mg-quickref Type tiers`);
  if (maxCoverage >= 0.9 && probe.duration > 20 && !probe.tweens.some(t => t.dur >= 8))
    add(name, 'no-continuous-motion', `full-frame ${probe.duration.toFixed(0)}s graphic (${(maxCoverage*100).toFixed(0)}% opaque), longest tween ${Math.max(...probe.tweens.map(t=>t.dur)).toFixed(1)}s; see references/mg-quickref.md "Motion and exits". Either animate something continuously or let a moving photo carry it (ep2 panels cover ~43%).`);
  const avgElems = elemSamples.length ? elemSamples.reduce((a,b)=>a+b,0)/elemSamples.length : 0;
  const kineticRatio = probe.tweens.length ? kinetic.length / probe.tweens.length : 0;
  const flags = [];
  if (!gradAny) flags.push('flat background');
  if (tierMax < 3) flags.push(`${tierMax} type tier(s)`);
  if (kineticRatio < 0.25) flags.push(`${(kineticRatio*100).toFixed(0)}% kinetic tweens`);
  if (avgElems < 12) flags.push(`${avgElems.toFixed(0)} elements on screen`);
  if (idleFrac > 0.6) flags.push(`${(idleFrac*100).toFixed(0)}% frozen`);
  if (flags.length >= 3)
    add(name, 'undesigned', `${flags.join(' · ')} — reads as a wireframe, not a designed card (mg-quickref)`);
  if (process.env.QC_STATS) console.log(`  [stats] ${name}: dur ${probe.duration.toFixed(0)}s cover ${maxCoverage} elems ${avgElems.toFixed(0)} tiers ${tierMax} kinetic ${(kineticRatio*100).toFixed(0)}% idle ${(idleFrac*100).toFixed(0)}% grad ${gradAny}`);
}

await browser.close();

/* publish measured composition durations so the episode builder can cut away from a
   graphic the moment it finishes instead of parking on a dead frame */
writeFileSync(join(compDir, '_durations.json'), JSON.stringify(DURS, null, 1), 'utf8');
/* settle-frame times per composition, comp-local seconds; the pre-render snapshot step reads them (mg-quickref "Verify") */
writeFileSync(join(TMP, 'frame_times.json'), JSON.stringify(FRAMES, null, 1), 'utf8');

/* ---------- report ---------- */
const hard = defects.filter(d => d.hard), soft = defects.filter(d => !d.hard);
const byComp = {};
for (const d of defects) (byComp[d.comp] ||= []).push(d);
for (const [c, list] of Object.entries(byComp)) {
  const h = list.filter(d => d.hard).length;
  console.log(`  ${c}  — ${h} error${h === 1 ? '' : 's'}, ${list.length - h} warning${list.length - h === 1 ? '' : 's'}`);
  for (const d of list.filter(d => d.hard)) console.log(`    ERROR [${d.kind}] ${d.msg}`);
  for (const d of list.filter(d => !d.hard)) console.log(`    warn  [${d.kind}] ${d.msg}`);
}
if (!hard.length) { console.log(`\n[graphics_qc] PASS — ${files.length} compositions, 0 errors, ${soft.length} warnings`); process.exit(0); }
console.log(`\n[graphics_qc] FAIL — ${hard.length} errors, ${soft.length} warnings across ${files.length} compositions`);
process.exit(1);
