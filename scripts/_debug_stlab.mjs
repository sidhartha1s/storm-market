import { chromium, chromiumExecutable } from './playwright_env.mjs';
import { readFileSync, writeFileSync } from 'fs';

const E = 'C:/Users/Sidhartha/Automation Projects/storm-market/.worktrees/ep-1974-super-outbreak/episodes/ep-1974-super-outbreak';

async function inspect(name, times) {
  const raw = readFileSync(`${E}/compositions/${name}.html`, 'utf-8');
  const body = raw.match(/<template>([\s\S]*?)<\/template>/)[1];
  const html = `<!doctype html><html><head><meta charset="UTF-8"><script src="../gsap.min.js"></script></head><body style="margin:0;background:#000">${body}</body></html>`;
  const tmpFile = `${E}/compositions/_debug_stlab_${name}.html`;
  writeFileSync(tmpFile, html);
  const browser = await chromium.launch({ executablePath: chromiumExecutable() });
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  await page.goto('file:///' + tmpFile.split('\\').join('/'), { waitUntil: 'load' });
  const out = {};
  for (const t of times) {
    const r = await page.evaluate(([n, tt]) => {
      window.__timelines[n].seek(tt, false);
      const root = document.querySelector('#root').getBoundingClientRect();
      const eb = document.querySelector('.eyebrow').getBoundingClientRect();
      const hl = document.querySelector('.hl').getBoundingClientRect();
      const labs = [...document.querySelectorAll('.stlab')].map(el => {
        const r = el.getBoundingClientRect();
        return { text: el.textContent, left: r.left - root.left, top: r.top - root.top, right: r.right - root.left, bottom: r.bottom - root.top };
      });
      return { eb: { left: eb.left - root.left, top: eb.top - root.top, right: eb.right - root.left, bottom: eb.bottom - root.top },
               hl: { left: hl.left - root.left, top: hl.top - root.top, right: hl.right - root.left, bottom: hl.bottom - root.top },
               labs };
    }, [name, t]);
    out[t] = r;
  }
  await browser.close();
  return out;
}

const results = {};
results['g-map-a6'] = await inspect('g-map-a6', [0, 5, 20]);
results['g-map-a4'] = await inspect('g-map-a4', [0, 0.5, 1, 1.5, 2, 3, 66.0, 66.3, 66.6, 66.9, 67.2, 67.5]);
console.log(JSON.stringify(results, null, 2));
