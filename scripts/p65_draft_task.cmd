@echo off
REM Draft render wrapper (hidden schtasks path) for ep-palm-sunday-1965, preview v1 (hook and intro). Workers 2: 16 GB box, stay clear of OOM.
set RENDER_WORKERS=2
call "%~dp0render.cmd" ep-palm-sunday-1965 draft ep-palm-sunday-1965-preview-v1
