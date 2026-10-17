// scratch: blank_scan's staging for g-a2-countdown only, print the timeline duration
import { readFileSync, writeFileSync } from 'node:fs'; import { join } from 'node:path'; import { pathToFileURL } from 'node:url';
const R = 'C:/Users/Sidhartha/Automation Projects/storm-market/.worktrees/ep-joplin-2011';
const { chromium, chromiumExecutable } = await import(pathToFileURL(R + '/scripts/playwright_env.mjs'));
const { hostCss } = await import(pathToFileURL(R + '/scripts/stage_comp.mjs'));
const ep = join(R, 'episodes/ep-joplin-2011'); const tmp = join(R, '.qc-tmp-a2cd', '_b.html');
const raw = readFileSync(join(ep, 'compositions/g-a2-countdown.html'), 'utf8');
const inner = raw.slice(raw.indexOf('<template>') + 10, raw.lastIndexOf('</template>'));
writeFileSync(tmp, `<!doctype html><html><head><meta charset="utf-8"><style>${hostCss(readFileSync(join(ep, 'index.html'), 'utf8'))}</style><script>${readFileSync(join(ep, 'gsap.min.js'), 'utf8')}</script></head><body>${inner}</body></html>`);
const b = await chromium.launch({ executablePath: chromiumExecutable(), args: ['--allow-file-access-from-files'] });
const page = await b.newPage(); const errs = []; page.on('pageerror', e => errs.push(String(e)));
await page.goto(pathToFileURL(tmp).href, { waitUntil: 'load' });
console.log(await page.evaluate(() => { const k = Object.keys(window.__timelines); const tl = window.__timelines[k[0]];
  return { k, ver: gsap.version, dur: tl.duration(), long: tl.getChildren(false).filter(c => c.endTime() > 16).map(c => [c.startTime(), c.endTime(), c.targets ? c.targets().map(t => t.id) : ''] ) }; }), errs);
await b.close();
