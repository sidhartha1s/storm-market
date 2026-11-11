/* Pre-render freeze scan: the draft render's acceptance test, run on the page instead.

   Why (owner 17 Sep 26, Dujuan batch): every fix round went composer -> 13-24 min draft render ->
   ffmpeg freezedetect -> reader -> composer. Alert-levels needed four renders to find holds that
   are visible on the page. This gate stages the EPISODE the way hyperframes shows it: index.html
   (its styles, its master timeline, its popfigs / pins / lower third) with every composition's
   template mounted inside its host div, clips shown only inside their data-start window. It steps
   time forward in STEP-second steps, screenshots every step at half resolution, and runs the SAME
   detector the render check uses (freezedetect n=0.003, d=6) on the image sequence. Only
   composition windows are judged. One contact sheet per window (a tile every 3 s) goes to
   sheets-pre/ so the frame reader can work before any render exists.

   v1 staged each comp alone and was blind to index-level overlays: kanto-map's pins live in
   index.html, so the comp read as static for 35 s and a popfig/pin collision could not show.

   Footage and audio are not loaded (black under transparent comps), so the scan is stricter than
   the render: a side panel that sits unchanged beside moving footage is reported. A window where
   nothing at all is on screen and index.html has full-frame footage under it is exempt.

   Light job: one Chromium page at half resolution, no media decode. It may run beside a live render
   when RAM allows (render_busy.py --light), one scan at a time (atomic lock file), and it aborts
   if free RAM drops under ABORT_FREE_GB while it runs.

   Usage: node scripts/freeze_scan.mjs episodes/<slug> [--comp a,b] [--step 0.5] [--hold 6]
   Exit 0 = no hold >= --hold seconds in any scanned comp window. 1 = holds found. 3 = refused/aborted. */
import { readFileSync, writeFileSync, existsSync, mkdirSync, rmSync, unlinkSync } from 'node:fs';
import { join, resolve } from 'node:path';
import { tmpdir, freemem } from 'node:os';
import { spawnSync } from 'node:child_process';
import { compSize } from './stage_comp.mjs';

const args = process.argv.slice(2);
const ep = resolve(args[0] || '.');
const opt = (name, dflt) => { const i = args.indexOf(name); return i >= 0 ? args[i + 1] : dflt; };
const STEP = parseFloat(opt('--step', '0.5'));
const HOLD = parseFloat(opt('--hold', '6'));
const ABORT_FREE_GB = 1.0;
const only = opt('--comp', '') ? opt('--comp', '').split(',').map(s => s.trim().replace(/\.html$/, '')) : null;

/* one light scan at a time: exclusive create, stale lock (dead pid) is replaced */
const LOCK = join(tmpdir(), 'storm-freeze-scan.lock');
const alive = (pid) => { try { process.kill(pid, 0); return true; } catch { return false; } };
const takeLock = () => { try { writeFileSync(LOCK, String(process.pid), { flag: 'wx' }); return true; } catch { return false; } };
if (!takeLock()) {
  const pid = parseInt(readFileSync(LOCK, 'utf8'), 10);
  if (pid && alive(pid)) {
    console.log(`[freeze_scan] REFUSING - another freeze scan is running (pid ${pid}); retry when it ends`);
    process.exit(3);
  }
  try { unlinkSync(LOCK); } catch { /* raced with its owner */ }
  if (!takeLock()) { console.log('[freeze_scan] REFUSING - lost the lock race; retry'); process.exit(3); }
}
const unlock = () => { try { if (readFileSync(LOCK, 'utf8') === String(process.pid)) unlinkSync(LOCK); } catch { /* gone */ } };
process.on('exit', unlock);
process.on('SIGINT', () => process.exit(130));

process.env.QC_LIGHT = '1';                       // playwright_env -> render_busy.py --light
const { chromium, chromiumExecutable } = await import('./playwright_env.mjs');

let html = readFileSync(join(ep, 'index.html'), 'utf8');
const { w: W, h: H } = compSize(html);
const attr = (tag, name) => { const m = new RegExp(`\\b${name}="([^"]*)"`).exec(tag); return m ? m[1] : null; };

/* full-frame footage windows, read BEFORE the media tags are neutralised */
const footage = [...html.matchAll(/<video\b[^>]*>/g)].map(m => m[0])
  .filter(v => !/\/(pip|cta)\//.test(v) && !/class="[^"]*pip/.test(v))
  .map(v => [parseFloat(attr(v, 'data-start')), parseFloat(attr(v, 'data-duration'))])
  .filter(([s, d]) => !isNaN(s) && !isNaN(d));
const overFootage = (a, b) => footage.some(([s, d]) => s <= a + 0.6 && s + d >= b - 0.6);

/* mount every composition's template inside its host div (first mount of each comp only) */
const comps = [];
html = html.replace(/<div\b[^>]*\bdata-composition-src="compositions\/([^"]+)\.html"[^>]*>/g, (tag, name) => {
  if (comps.some(c => c.name === name)) { console.log(`   (note) ${name} is mounted more than once; only the first mount is scanned`); return tag; }
  const raw = readFileSync(join(ep, 'compositions', `${name}.html`), 'utf8');
  const t0 = raw.indexOf('<template>');
  let inner = t0 >= 0 ? raw.slice(t0 + 10, raw.lastIndexOf('</template>')) : raw;
  /* comp-relative asset urls (../media/x from compositions/) become episode-root urls, as hyperframes resolves them */
  inner = inner.replace(/(url\(\s*['"]?|\b(?:src|href)=["'])\.\.\//g, '$1');
  comps.push({ name, start: parseFloat(attr(tag, 'data-start')), dur: parseFloat(attr(tag, 'data-duration')) });
  return tag + inner;
});
if (!comps.length) { console.error('[freeze_scan] index.html mounts no compositions'); process.exit(1); }
const scanned = comps.filter(c => !only || only.includes(c.name));
if (!scanned.length) { console.error('[freeze_scan] no compositions matched --comp'); process.exit(1); }

/* no media decode: footage and audio never load */
html = html.replace(/<(video|audio)\b([^>]*?)\bsrc=/g, '<$1$2data-src=').replace(/<source\b[^>]*>/g, '');
html = html.replace(/<head>/i, '<head><base href="../../">');

const TMP = join(ep, '.qc-tmp', 'freeze');
const SHEETS = join(ep, 'sheets-pre');
rmSync(TMP, { recursive: true, force: true });
mkdirSync(TMP, { recursive: true });
mkdirSync(SHEETS, { recursive: true });
const staged = join(TMP, '_episode.html');
writeFileSync(staged, html, 'utf8');

const browser = await chromium.launch({ executablePath: chromiumExecutable(), args: ['--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 0.5 });
const pageErrors = [];
page.on('pageerror', e => pageErrors.push(String(e.message).slice(0, 160)));
await page.goto('file:///' + staged.replace(/\\/g, '/'), { waitUntil: 'load' });
await page.waitForTimeout(300);

const missing = await page.evaluate((names) => {
  document.documentElement.style.background = '#000';
  for (const tl of Object.values(window.__timelines || {})) tl.pause();
  /* track order is paint order when the author set no z-index */
  for (const e of document.querySelectorAll('[data-track-index]')) {
    if (getComputedStyle(e).zIndex === 'auto') { e.style.zIndex = e.dataset.trackIndex; if (getComputedStyle(e).position === 'static') e.style.position = 'absolute'; }
  }
  for (const e of document.querySelectorAll('[data-composition-src]')) { e.style.position = 'absolute'; e.style.inset = '0'; }
  window.__fzClips = [...document.querySelectorAll('[data-start][data-duration]')].filter(e => e.id !== 'root' && !e.parentElement.closest('[data-composition-src]') || e.hasAttribute('data-composition-src'))
    .map(e => ({ e, s: parseFloat(e.dataset.start), d: parseFloat(e.dataset.duration), comp: e.dataset.compositionId && e.hasAttribute('data-composition-src') ? e.dataset.compositionId : null }));
  window.__fzSeek = (t) => {
    for (const c of window.__fzClips) {
      const on = t >= c.s - 1e-6 && t < c.s + c.d;
      c.e.style.display = on ? '' : 'none';
      if (on && c.comp && window.__timelines[c.comp]) window.__timelines[c.comp].seek(Math.max(0, t - c.s), false);
    }
    const host = Object.keys(window.__timelines).find(k => !window.__fzClips.some(c => c.comp === k));
    if (host) window.__timelines[host].seek(t, false);          // events ON: the render plays callbacks too
  };
  return names.filter(n => !window.__timelines || !window.__timelines[n]);
}, scanned.map(c => c.name));

const findings = missing.map(n => [n, 'no timeline registered on the mounted page' + (pageErrors.length ? ` (page error: ${pageErrors[0]})` : '')]);
const fmt = (t) => `${Math.floor(t / 60)}:${(t % 60).toFixed(1).padStart(4, '0')}`;
const fps = (1 / STEP).toString();
let aborted = false;

for (const c of scanned.filter(c => !missing.includes(c.name))) {
  const dir = join(TMP, c.name);
  mkdirSync(dir, { recursive: true });
  let n = 0;
  const hasContent = [];
  for (let t = 0; t <= c.dur + 1e-6; t += STEP) {
    if (n % 20 === 0 && freemem() / 2 ** 30 < ABORT_FREE_GB) { aborted = true; break; }
    await page.evaluate((tt) => new Promise(res => { window.__fzSeek(tt); requestAnimationFrame(() => requestAnimationFrame(res)); }), c.start + t);
    await page.screenshot({ path: join(dir, `f_${String(n).padStart(5, '0')}.jpg`), type: 'jpeg', quality: 72 });
    hasContent.push(await page.evaluate(({ W, H }) => [...document.querySelectorAll('body *')].some(e => {
      if (/^(SCRIPT|STYLE|TEMPLATE|VIDEO|AUDIO)$/.test(e.tagName) || /drift|bgplate|grain/.test(e.id + ' ' + e.className)) return false;
      if (!(e.children.length === 0 && e.textContent.trim()) && !/^(IMG|CANVAS)$/.test(e.tagName) && !e.closest('svg')) return false;
      let o = 1;
      for (let p = e; p; p = p.parentElement) { const cs = getComputedStyle(p); if (cs.display === 'none' || cs.visibility === 'hidden') return false; o *= parseFloat(cs.opacity); }
      const r = e.getBoundingClientRect();
      return o > 0.06 && r.width > 1 && r.height > 1 && r.bottom > 0 && r.top < H && r.right > 0 && r.left < W;
    }), { W, H }));
    n += 1;
  }
  if (aborted) break;

  const fd = spawnSync('ffmpeg', ['-v', 'info', '-framerate', fps, '-i', join(dir, 'f_%05d.jpg'),
    '-vf', `freezedetect=n=0.003:d=${HOLD}`, '-f', 'null', '-'], { encoding: 'utf8', windowsHide: true });
  if (fd.status !== 0) { findings.push([c.name, `ffmpeg freezedetect failed (exit ${fd.status})`]); continue; }
  const log = (fd.stderr || '') + (fd.stdout || '');
  const starts = [...log.matchAll(/freeze_start: ([\d.]+)/g)].map(m => parseFloat(m[1]));
  const ends = [...log.matchAll(/freeze_end: ([\d.]+)/g)].map(m => parseFloat(m[1]));
  const holds = starts.map((s, i) => [s, ends[i] ?? c.dur]);
  let real = 0;
  for (const [s, e] of holds) {
    const i0 = Math.round(s / STEP), i1 = Math.min(n - 1, Math.round(e / STEP));
    const empty = hasContent.slice(i0, i1 + 1).every(v => !v);
    if (empty && overFootage(c.start + s, c.start + e)) {
      console.log(`   (exempt) ${c.name} ${s.toFixed(1)}-${e.toFixed(1)}s: nothing mounted over index.html footage`);
      continue;
    }
    real += 1;
    findings.push([c.name, `static ${s.toFixed(1)}-${e.toFixed(1)}s comp-local (${(e - s).toFixed(1)}s) = ${fmt(c.start + s)}-${fmt(c.start + e)} in the episode${empty ? ' - NOTHING on screen and no footage under it' : ''}`]);
  }

  const every = Math.max(1, Math.round(3 / STEP));
  const rows = Math.ceil(Math.ceil(n / every) / 6);
  spawnSync('ffmpeg', ['-y', '-v', 'error', '-framerate', fps, '-i', join(dir, 'f_%05d.jpg'),
    '-vf', `select='not(mod(n\\,${every}))',scale=480:-1,tile=6x${rows}:color=0x505050`,
    '-frames:v', '1', '-q:v', '4', join(SHEETS, `${c.name}_${Math.floor(c.start)}s.jpg`)], { encoding: 'utf8', windowsHide: true });
  console.log(`${c.name.padEnd(24)} ${fmt(c.start).padStart(7)}  dur ${c.dur.toFixed(1).padStart(6)}s  frames ${String(n).padStart(4)}  holds>=${HOLD}s: ${real}`);
}
await browser.close();
rmSync(TMP, { recursive: true, force: true });

console.log('');
if (pageErrors.length) console.log(`   (page errors on the mounted episode: ${[...new Set(pageErrors)].slice(0, 3).join(' | ')})`);
if (aborted) { console.log(`[freeze_scan] ABORTED - free RAM fell under ${ABORT_FREE_GB} GB during the scan; nothing is concluded, rerun when the box has room`); process.exit(3); }
if (!findings.length) console.log(`FREEZE SCAN PASS - no composition window holds a static picture for >= ${HOLD}s (${scanned.length} comps, step ${STEP}s, host overlays included); sheets in sheets-pre/`);
else {
  console.log(`FREEZE SCAN FAIL - ${findings.length} finding(s); sheets in sheets-pre/`);
  for (const [c, d] of findings) console.log('   ', c, '-', d);
}
process.exit(findings.length ? 1 : 0);
