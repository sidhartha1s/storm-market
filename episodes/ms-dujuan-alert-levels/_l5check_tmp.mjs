import { chromium, chromiumExecutable } from '../../scripts/playwright_env.mjs';
const EXECUTABLE = chromiumExecutable();
import fs from 'fs';
import path from 'path';

const ep = process.argv[2];
const idx = fs.readFileSync(path.join(ep, 'index.html'), 'utf8');
const comp = fs.readFileSync(path.join(ep, 'compositions', 'ladder-l5.html'), 'utf8');
const hostCss = [...idx.matchAll(/<style>([\s\S]*?)<\/style>/g)].map(m => m[1]).join('\n');
const tpl = comp.match(/<template>([\s\S]*?)<\/template>/)[1];

const stage = `<!doctype html><html><head><meta charset="utf-8">
<style>body{margin:0;width:1920px;height:1080px;overflow:hidden;background:#000}
.pip{left:1640px !important;top:708px !important;width:240px !important;height:240px !important;border-radius:50%;position:absolute;background:rgba(0,255,0,0.3);}
${hostCss}</style></head><body>
<div style="position:relative;width:1920px;height:1080px;">${tpl.replace(/<style>[\s\S]*?<\/style>/, m=>m)}<div class="pip"></div></div>
<script src="https://unpkg.com/gsap@3/dist/gsap.min.js"></script>
</body></html>`;
const stagePath = path.join(ep, '_l5check_stage.html');
fs.writeFileSync(stagePath, stage);

const browser = await chromium.launch({ executablePath: EXECUTABLE, args: ['--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
page.on('pageerror', e => console.log('PAGEERROR', e.message));
await page.goto('file:///' + stagePath.split(path.sep).join('/'));
await page.waitForFunction(() => window.__timelines && window.__timelines['ladder-l5']);

const times = [3.9, 6.0, 11.7, 18.4, 23.5, 35.0, 35.6, 44.3, 48.2];
for (const t of times) {
  const data = await page.evaluate((tt) => {
    const tl = window.__timelines['ladder-l5'];
    tl.seek(tt);
    const note = document.getElementById('l5-note');
    const rule = document.getElementById('l5-rule');
    const n1 = document.getElementById('l5-n1');
    const r = note.getBoundingClientRect();
    const cs = getComputedStyle(note);
    const ruleR = rule ? rule.getBoundingClientRect() : null;
    return {
      t: tt,
      noteVis: cs.visibility, noteOpacity: cs.opacity, noteFontPx: parseFloat(cs.fontSize),
      noteRect: { top: r.top, bottom: r.bottom, left: r.left, right: r.right },
      ruleLeft: ruleR ? ruleR.left : null,
      n1text: n1.textContent
    };
  }, t);
  console.log(JSON.stringify(data));
}
await browser.close();
