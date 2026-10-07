@echo off
REM Draft render wrapper (hidden schtasks path) for ep-nepal-floods-2026. Workers 2: 16 GB box, stay clear of OOM.
set RENDER_WORKERS=2
call "%~dp0render.cmd" ep-nepal-floods-2026 draft ep-nepal-floods-2026-draft-v3
