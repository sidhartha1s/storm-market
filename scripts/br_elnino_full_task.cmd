@echo off
REM br-elnino-california FULL render wrapper (hidden schtasks/wscript path), ep6_full_task.cmd pattern.
REM 2 workers: box carries the Texas TTS + a sourcing agent alongside this render.
set RENDER_WORKERS=2
call "%~dp0render.cmd" br-elnino-california full br-elnino-california-final
