@echo off
REM ep6 FULL render wrapper for the hidden schtasks path (wscript run_hidden.vbs cmd /c <this>).
REM 2 workers: box had ~2.5 GB free at launch (other sessions + browsers resident).
set RENDER_WORKERS=2
call "%~dp0render.cmd" ep6-katrina-2005 full
