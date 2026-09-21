@echo off
REM ep-1974 DRAFT render wrapper for the hidden schtasks path (wscript run_hidden.vbs). Workers 2: the box
REM had 4.5 GB free and the harness reaped a 3-worker launch for low RAM (21 Sep 26).
set RENDER_WORKERS=2
call "%~dp0render.cmd" ep-1974-super-outbreak draft
