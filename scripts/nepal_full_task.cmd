@echo off
REM Full render wrapper (hidden schtasks path) for ep-nepal-floods-2026. Workers 2: 16 GB box, stay clear of OOM.
REM Below-normal priority (children inherit it) so the owner's parallel work stays responsive (owner 29 Sep 26).
set RENDER_WORKERS=2
start "" /b /wait /belownormal cmd /c call "%~dp0render.cmd" ep-nepal-floods-2026 full ep-nepal-floods-2026-final
