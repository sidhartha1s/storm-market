"""Self-check: a browser gate never leaves a Chromium or its temp profile behind. python3 scripts/test_browser_leak.py

Why: 94 frozen orphan Playwright Chromes (2.8 GB commit) and 285 playwright_chromiumdev_profile-* dirs (1.2 GB) sat on
the ZBook on 18 Oct 26, left by gates whose node was killed mid-run or exited between launch and close.
Each case runs real node + Chromium with TEMP pointed at its own folder, then asks Windows whether any chrome.exe still
names that folder on its command line, and lists what is left in it.
"""
import os
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

S = Path(__file__).resolve().parent
FAILS = []


def check(name, cond, detail=""):
    if not cond:
        FAILS.append(name)
    print(("ok   " if cond else "FAIL ") + name + (f" ({detail})" if detail and not cond else ""))


def chromes_naming(folder):
    """chrome.exe processes whose command line holds folder (read-only CIM query)."""
    q = ("@(Get-CimInstance Win32_Process -Filter \"Name='chrome.exe'\" | Where-Object { $_.CommandLine -and "
         f"$_.CommandLine.Contains('{folder}') }}).Count")
    out = subprocess.run(["powershell", "-NoProfile", "-NonInteractive", "-Command", q],
                         capture_output=True, text=True).stdout.strip()
    return int(out) if out.isdigit() else -1


def run_node(args, temp, timeout):
    env = dict(os.environ, TEMP=str(temp), TMP=str(temp))
    t0 = time.time()
    r = subprocess.run(["node", *args], capture_output=True, text=True, encoding="utf-8", errors="replace",
                       env=env, timeout=timeout)
    time.sleep(2)  # a browser killed on exit may take a moment to leave the process table
    return r.returncode, r.stdout + r.stderr, time.time() - t0


def leftovers(temp):
    return sorted(p.name for p in Path(temp).glob("playwright_chromiumdev_profile-*"))


# 1. static: every gate launches Chromium through launchGate (deadline) and closes it in a finally
for f in sorted(S.glob("*.mjs")):
    src = f.read_text(encoding="utf-8")
    if f.name == "playwright_env.mjs" or not re.search(r"chromium\.launch\(|launchGate\(", src):
        continue
    check(f"{f.name}: no raw chromium.launch (only launchGate, which carries the deadline)", "chromium.launch(" not in src)
    check(f"{f.name}: names its deadline", re.search(r"launchGate\('[a-z_]+', [A-Z_]+_S\b", src) is not None)
    check(f"{f.name}: closes the browser in a finally", re.search(r"finally\s*\{\s*await browser\.close\(\)", src) is not None)
    check(f"{f.name}: no process.exit inside the browser's life",
          not re.search(r"process\.exit\(", src[src.find("launchGate("):src.rfind("await browser.close()")]))

with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)
    # 2. graphics_qc on an episode with no compositions: it used to process.exit(1) right after the launch
    ep, temp = tmp / "ep-empty", tmp / "t1"
    ep.mkdir()
    temp.mkdir()
    (ep / "index.html").write_text("<!doctype html><html><body></body></html>", encoding="utf-8")
    code, out, _ = run_node([str(S / "graphics_qc.mjs"), str(ep)], temp, 120)
    check("graphics_qc with no compositions fails loud", code == 1 and "no compositions/ dir" in out, out[-300:])
    check("graphics_qc with no compositions leaves no chrome running", chromes_naming(temp) == 0)
    check("graphics_qc with no compositions leaves no temp profile", not leftovers(temp), str(leftovers(temp)))

    # 3. a gate that hangs past its deadline closes its browser and exits non-zero by itself
    temp = tmp / "t2"
    temp.mkdir()
    hang = tmp / "hang.mjs"
    env_url = (S / "playwright_env.mjs").as_uri()
    hang.write_text(f"""import {{ launchGate }} from '{env_url}';
const browser = await launchGate('hang_test', 3);
try {{
  const page = await browser.newPage();
  await page.evaluate(() => new Promise(() => {{}}));  // never settles, like a gate stuck on a page
}} finally {{ await browser.close(); }}
""", encoding="utf-8")
    code, out, secs = run_node([str(hang)], temp, 90)
    check("a hung gate exits non-zero at its deadline", code not in (0, None) and "deadline" in out, f"exit {code}: {out[-300:]}")
    check("a hung gate ends within 30 s of a 3 s deadline", secs < 30, f"{secs:.0f} s")
    check("a hung gate leaves no chrome running", chromes_naming(temp) == 0)
    check("a hung gate leaves no temp profile", not leftovers(temp), str(leftovers(temp)))

if FAILS:
    sys.exit(f"[test_browser_leak] FAIL: {FAILS}")
print("[test_browser_leak] all checks passed")
