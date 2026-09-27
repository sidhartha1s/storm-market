/* Locate playwright-core and a chromium build without pinning a version number.

   Both QC gates used to hardcode `chromium-1228` and an absolute path into the npm
   global tree; a playwright bump renamed the directory and the gates died with ENOENT,
   which reads like a broken gate rather than a stale path. Resolve at run time instead:
   newest installed chromium wins, and either env var overrides for an odd box. */
import { readdirSync, existsSync } from 'node:fs';
import { execSync } from 'node:child_process';
import { join } from 'node:path';
import { pathToFileURL } from 'node:url';
import { execFileSync } from 'node:child_process';
import { dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

// One heavy job at a time: refuse to open a headless Chromium while a hyperframes render is alive (owner 2026-09-11, OOM).
try {
  // bare python3 is the MS Store stub under cmd/node (exit 9009) — same full path render.cmd uses
  const PY = 'C:/Users/Sidhartha/AppData/Local/Programs/Python/Python312/python.exe';
  execFileSync(existsSync(PY) ? PY : 'python', [join(dirname(fileURLToPath(import.meta.url)), 'render_busy.py'), ...(process.env.QC_LIGHT === '1' ? ['--light'] : [])], { stdio: 'inherit' });
} catch (e) {
  process.exit(e.status ?? 3);
}

function npmGlobalRoot() {
  try {
    return execSync('npm root -g', { encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] }).trim();
  } catch {
    return join(process.env.APPDATA || '', 'npm', 'node_modules');
  }
}

export function playwrightCoreUrl() {
  if (process.env.PLAYWRIGHT_CORE) return pathToFileURL(process.env.PLAYWRIGHT_CORE).href;
  const root = npmGlobalRoot();  // once: each `npm root -g` spawn costs ~1.1 s per gate launch
  const candidates = [
    join(root, '@playwright', 'cli', 'node_modules', 'playwright-core', 'index.mjs'),
    join(root, 'playwright-core', 'index.mjs'),
  ];
  const hit = candidates.find(existsSync);
  if (!hit) throw new Error(`playwright-core not found; tried:\n  ${candidates.join('\n  ')}`);
  return pathToFileURL(hit).href;
}

export function chromiumExecutable() {
  if (process.env.PLAYWRIGHT_CHROMIUM) return process.env.PLAYWRIGHT_CHROMIUM;
  const root = process.env.PLAYWRIGHT_BROWSERS_PATH
    || join(process.env.LOCALAPPDATA || '', 'ms-playwright');
  const builds = readdirSync(root)
    .filter(d => /^chromium-\d+$/.test(d))
    .sort((a, b) => Number(b.split('-')[1]) - Number(a.split('-')[1]));
  for (const b of builds) {
    const exe = join(root, b, 'chrome-win64', 'chrome.exe');
    if (existsSync(exe)) return exe;
  }
  throw new Error(`no chromium build under ${root} (found: ${builds.join(', ') || 'none'})`);
}

export const chromium = (await import(playwrightCoreUrl())).chromium;
