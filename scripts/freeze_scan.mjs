/* Pre-render freeze scan: the draft render's acceptance test, run on the page instead.

   Why (owner 17 Sep 26, Dujuan batch): every fix round went composer -> 13-18 min draft render ->
   ffmpeg freezedetect -> reader -> composer. Alert-levels needed four renders to find holds that
   are visible on the staged comp. This gate stages each composition exactly like blank_scan
   (template body + the host <style> blocks, because hyperframes mounts comps inside index.html),
   seeks the master timeline forward in STEP-second steps, screenshots every step at half
   resolution, and runs the SAME detector the render check uses (freezedetect n=0.003, d=6) on the
   image sequence. It also writes one contact sheet per comp (a tile every 3 s) to sheets-pre/ so
   the frame reader can work before any render exists.

   It is stricter than the render: the lower third and the presenter circle are not on the staged
   page, so nothing but the comp's own content can break a hold.

   Light job: one Chromium page at half resolution. It may run beside a live render when RAM allows
   (render_busy.py --light) and only one light scan runs at a time (lock file).

   Usage: node scripts/freeze_scan.mjs episodes/<slug> [--comp a,b] [--step 0.5] [--hold 6]
   Exit 0 = no hold >= --hold seconds in any scanned comp. Exit 1 = holds found. Exit 3 = refused. */
import { readFileSync, writeFileSync, readdirSync, existsSync, mkdirSync, rmSync, unlinkSync } from 'node:fs';
import { join, resolve } from 'node:path';
import { tmpdir } from 'node:os';
import { spawnSync } from 'node:child_process';

const args = process.argv.slice(2);
const ep = resolve(args[0] || '.');
const opt = (name, dflt) => { const i = args.indexOf(name); return i >= 0 ? args[i + 1] : dflt; };
const STEP = parseFloat(opt('--step', '0.5'));
const HOLD = parseFloat(opt('--hold', '6'));
const only = opt('--comp', '') ? opt('--comp', '').split(',').map(s => s.trim().replace(/\.html$/, '')) : null;

/* one light scan at a time */
const LOCK = join(tmpdir(), 'storm-freeze-scan.lock');
const alive = (pid) => { try { process.kill(pid, 0); return true; } catch { return false; } };
if (existsSync(LOCK)) {
  const pid = parseInt(readFileSync(LOCK, 'utf8'), 10);
  if (pid && pid !== process.pid && alive(pid)) {
    console.log(`[freeze_scan] REFUSING - another freeze scan is running (pid ${pid}); retry when it ends`);
    process.exit(3);
  }
}
writeFileSync(LOCK, String(process.pid));
const unlock = () => { try { if (readFileSync(LOCK, 'utf8') === String(process.pid)) unlinkSync(LOCK); } catch { /* gone */ } };
process.on('exit', unlock);
process.on('SIGINT', () => process.exit(130));

process.env.QC_LIGHT = '1';                       // playwright_env -> render_busy.py --light
const { chromium, chromiumExecutable } = await import('./playwright_env.mjs');

const indexHtml = readFileSync(join(ep, 'index.html'), 'utf8');
const HOST_CSS = [...indexHtml.matchAll(/<style[^>]*>([\s\S]*?)<\/style>/g)].map(x => x[1]).join('\n');
const hostStart = {};
for (const m of indexHtml.matchAll(/<div\b[^>]*data-composition-src="compositions\/([^"]+)\.html"[^>]*>/g)) {
  const s = /data-start="([\d.]+)"/.exec(m[0]);
  if (s && !(m[1] in hostStart)) hostStart[m[1]] = parseFloat(s[1]);
}

const TMP = join(ep, '.qc-tmp', 'freeze');
const SHEETS = join(ep, 'sheets-pre');
mkdirSync(TMP, { recursive: true });
mkdirSync(SHEETS, { recursive: true });

const files = readdirSync(join(ep, 'compositions')).filter(f => f.endsWith('.html'))
  .filter(f => !only || only.includes(f.replace('.html', '')));
if (!files.length) { console.error('[freeze_scan] no compositions matched'); process.exit(1); }

const browser = await chromium.launch({ executablePath: chromiumExecutable(), args: ['--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 0.5 });
const findings = [];
const fmt = (t) => `${Math.floor(t / 60)}:${(t % 60).toFixed(1).padStart(4, '0')}`;

for (const f of files) {
  const name = f.replace('.html', '');
  const raw = readFileSync(join(ep, 'compositions', f), 'utf8');
  const t0 = raw.indexOf('<template>');
  const inner = t0 >= 0 ? raw.slice(t0 + 10, raw.lastIndexOf('</template>')) : raw;
  const dir = join(TMP, name);
  rmSync(dir, { recursive: true, force: true });
  mkdirSync(dir, { recursive: true });
  const staged = join(TMP, `${name}.html`);
  /* <base> points at the episode root so the comp's media/ and font urls resolve as they do when mounted */
  writeFileSync(staged, `<!doctype html><html><head><meta charset="utf-8"><base href="../../">
<style>${HOST_CSS}</style>
<style>html,body{margin:0;background:#000;width:1920px;height:1080px;overflow:hidden}</style>
<script src="gsap.min.js"></script></head><body>${inner}</body></html>`, 'utf8');
  await page.goto('file:///' + staged.replace(/\\/g, '/'), { waitUntil: 'load' });
  await page.waitForTimeout(200);
  const dur = await page.evaluate(() => {
    const k = Object.keys(window.__timelines || {})[0];
    if (!k) return null;
    window.__fz = window.__timelines[k];
    window.__fz.pause();
    return window.__fz.duration();
  });
  if (dur === null) { findings.push([name, 'no timeline registered']); continue; }

  let n = 0;
  for (let t = 0; t <= dur + 1e-6; t += STEP) {
    /* forward seek WITH events (suppressEvents=false): the render plays callbacks too */
    await page.evaluate((tt) => new Promise(res => {
      window.__fz.seek(tt, false);
      requestAnimationFrame(() => requestAnimationFrame(res));
    }), t);
    await page.screenshot({ path: join(dir, `f_${String(n).padStart(5, '0')}.jpg`), type: 'jpeg', quality: 72 });
    n += 1;
  }

  const fps = (1 / STEP).toString();
  const fd = spawnSync('ffmpeg', ['-v', 'info', '-framerate', fps, '-i', join(dir, 'f_%05d.jpg'),
    '-vf', `freezedetect=n=0.003:d=${HOLD}`, '-f', 'null', '-'], { encoding: 'utf8' });
  const log = (fd.stderr || '') + (fd.stdout || '');
  const starts = [...log.matchAll(/freeze_start: ([\d.]+)/g)].map(m => parseFloat(m[1]));
  const ends = [...log.matchAll(/freeze_end: ([\d.]+)/g)].map(m => parseFloat(m[1]));
  const holds = starts.map((s, i) => [s, ends[i] ?? dur]);
  const abs = hostStart[name] ?? 0;
  for (const [s, e] of holds)
    findings.push([name, `static ${s.toFixed(1)}-${e.toFixed(1)}s comp-local (${(e - s).toFixed(1)}s) = ${fmt(abs + s)}-${fmt(abs + e)} in the episode`]);

  const every = Math.max(1, Math.round(3 / STEP));
  const tiles = Math.ceil(n / every);
  const rows = Math.ceil(tiles / 6);
  spawnSync('ffmpeg', ['-y', '-v', 'error', '-framerate', fps, '-i', join(dir, 'f_%05d.jpg'),
    '-vf', `select='not(mod(n\\,${every}))',scale=480:-1,tile=6x${rows}:color=0x505050`,
    '-frames:v', '1', '-q:v', '4', join(SHEETS, `${name}_${Math.floor(abs)}s.jpg`)], { encoding: 'utf8' });

  console.log(`${name.padEnd(24)} dur ${dur.toFixed(1).padStart(6)}s  frames ${String(n).padStart(4)}  holds>=${HOLD}s: ${holds.length}`);
}
await browser.close();
rmSync(TMP, { recursive: true, force: true });

console.log('');
if (!findings.length) console.log(`FREEZE SCAN PASS - no composition holds a static picture for >= ${HOLD}s (${files.length} comps, step ${STEP}s); sheets in sheets-pre/`);
else {
  console.log(`FREEZE SCAN FAIL - ${findings.length} finding(s); sheets in sheets-pre/`);
  for (const [c, d] of findings) console.log('   ', c, '-', d);
}
process.exit(findings.length ? 1 : 0);
