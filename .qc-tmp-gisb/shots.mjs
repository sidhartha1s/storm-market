import { chromium, chromiumExecutable } from '../scripts/playwright_env.mjs';
import { readFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
const S = process.argv[2];
const times = process.argv.slice(3).map(Number);
let html = readFileSync(join(S, 'index.html'), 'utf8');
const raw = readFileSync(join(S, 'compositions/g-intro-strip-back.html'), 'utf8');
const inner = raw.slice(raw.indexOf('<template>') + 10, raw.lastIndexOf('</template>'));
const i = html.indexOf('id="host-intro-strip-back"');
const j = html.indexOf('>', i) + 1;
html = html.slice(0, j) + inner + html.slice(j);
html = html.replace('<head>', '<head><base href="./">');
const staged = join(S, '_staged.html');
writeFileSync(staged, html, 'utf8');
const b = await chromium.launch({ executablePath: chromiumExecutable(), args: ['--allow-file-access-from-files'] });
const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
const errs = [];
p.on('pageerror', e => errs.push(String(e.message)));
await p.goto('file:///' + staged.split('\\').join('/'), { waitUntil: 'load' });
await p.waitForTimeout(300);
await p.evaluate(() => {
  document.documentElement.style.background = '#000';
  const host = document.getElementById('host-intro-strip-back');
  for (const e of document.body.children) { if (e !== host && !e.contains(host)) e.style.display = 'none'; }
  let a = host; while (a && a !== document.body) { a.style.display = 'block'; a.style.opacity = 1; a.style.visibility = 'visible'; a = a.parentElement; }
  host.style.position = 'absolute'; host.style.left = '0'; host.style.top = '0'; host.style.width = '1920px'; host.style.height = '1080px';
});
for (const t of times) {
  await p.evaluate((t) => {
    for (const k of Object.keys(window.__timelines)) window.__timelines[k].pause();
    window.__timelines['g-intro-strip-back'].seek(t, false);
  }, t);
  await p.screenshot({ path: join(S, 't' + t + '.png') });
}
console.log('errors:', JSON.stringify(errs));
await b.close();
