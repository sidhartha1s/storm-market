@echo off
REM Full render wrapper (hidden schtasks path) for ep-nepal-floods-2026.
REM Owner 29 Sep 26 "ship it. render is a go" with ~2.9 GB free while he works in parallel: 1 worker (about half the
REM Chrome memory of 2) and the free-RAM floor lowered to 2.5 GB for this run only. Below-normal priority (children
REM inherit it) so his apps stay responsive.
set RENDER_WORKERS=1
set RENDER_MIN_FREE_GB=2.5
start "" /b /wait /belownormal cmd /c call "%~dp0render.cmd" ep-nepal-floods-2026 full ep-nepal-floods-2026-final
