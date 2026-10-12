@echo off
REM Draft render wrapper (hidden schtasks path) for ep-palm-sunday-1965, preview v1 (hook and intro).
REM [OVERRIDE] 12 Oct 26: preflight refused at 3.2 GB free (floor 4 GB); owner replied "override." with 3.18 GB free
REM and Firefox and Slack left open. Floor lowered to 0 for this run only, 1 worker (about half the Chrome memory of 2),
REM below-normal priority (children inherit it) so his apps stay responsive.
set RENDER_WORKERS=1
set RENDER_MIN_FREE_GB=0
start "" /b /wait /belownormal cmd /c call "%~dp0render.cmd" ep-palm-sunday-1965 draft ep-palm-sunday-1965-preview-v1
