@echo off
REM One-off preview of the no-house-rules showcase MG (owner ask 26 Sep 26). 30 fps so motion reads; 1 worker for low RAM.
set RENDER_WORKERS=1
set RENDER_FPS=30
set RENDER_CRF=20
call "%~dp0render.cmd" demo-mg-showcase draft showcase-preview
