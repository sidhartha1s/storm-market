@echo off
REM Full render wrapper template (hidden schtasks path). Copy to scripts/<ep>_full_task.cmd, set the slug. Workers 2: 16 GB box.
set RENDER_WORKERS=2
call "%~dp0render.cmd" ep-1974-super-outbreak full
