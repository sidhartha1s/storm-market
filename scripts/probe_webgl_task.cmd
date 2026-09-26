@echo off
REM Probe wrapper: render.cmd as is (fast capture + --gpu), 1 worker, 30 fps, crf 18. Arg 1 = out basename.
set RENDER_WORKERS=1
set RENDER_FPS=30
set RENDER_CRF=18
set EP=%~dp0..\episodes\probe-webgl
echo start %DATE% %TIME% > "%EP%\timing_%~1.txt"
call "%~dp0render.cmd" probe-webgl draft %~1
echo end %DATE% %TIME% >> "%EP%\timing_%~1.txt"
copy /y "%EP%\render_draft.log" "%EP%\render_%~1.log" >nul
