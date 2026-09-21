import { chromium, chromiumExecutable } from './playwright_env.mjs';
import { readFileSync, writeFileSync } from 'fs';
import os from 'os';
import path from 'path';

const E = 'C:/Users/Sidhartha/Automation Projects/storm-market/.worktrees/ep-1974-super-outbreak/episodes/ep-1974-super-outbreak';
const raw = readFileSync(E + '/compositions/g-plane.html', 'utf-8');
const body = raw.match(/<template>([\s\S]*?)<\/template>/)[1];
const html = `<!doctype html><html><head><meta charset="UTF-8"><script src="../gsap.min.js"></script></head><body style="margin:0;background:#000">${body}</body></html>`;
const tmp = path.join(os.tmpdir(), 'mg2', '_scratch_plane.html');
writeFileSync(tmp, html);

const browser = await chromium.launch({ executablePath: chromiumExecutable() });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
await page.goto('file:///' + tmp.split('\\').join('/'), { waitUntil: 'load' });
const out = await page.evaluate(() => {
  const tl = window.__timelines['g-plane'];
  const trail = document.getElementById('g-plane-trail');
  const plane = document.getElementById('g-plane-plane');
  const mapgroup = document.getElementById('g-plane-mapgroup');
  const totalLen = trail.getTotalLength();
  const results = [];
  for (const t of [2, 10, 22]) {
    tl.seek(t, false);
    const cs = getComputedStyle(trail);
    const dashoffset = parseFloat(cs.strokeDashoffset || trail.getAttribute('stroke-dashoffset') || '0');
    const drawnLen = Math.max(0, Math.min(totalLen, totalLen - dashoffset));
    const headLocal = trail.getPointAtLength(drawnLen);
    const svg = trail.ownerSVGElement;
    const ctm = mapgroup.getScreenCTM();
    const pt = svg.createSVGPoint();
    pt.x = headLocal.x; pt.y = headLocal.y;
    const headScreen = pt.matrixTransform(ctm);
    const pr = plane.getBoundingClientRect();
    const planeCenter = { x: (pr.left + pr.right) / 2, y: (pr.top + pr.bottom) / 2 };
    const planeTransform = getComputedStyle(plane).transform;
    const planeAttr = plane.getAttribute('transform');
    const dist = Math.hypot(headScreen.x - planeCenter.x, headScreen.y - planeCenter.y);
    results.push({ t, dashoffset, drawnLen, headLocal: { x: headLocal.x, y: headLocal.y }, headScreen: { x: headScreen.x, y: headScreen.y }, planeCenter, planeTransform, planeAttr, dist });
  }
  return results;
});
console.log(JSON.stringify(out, null, 2));
await browser.close();
