@echo off
REM ep4 DRAFT render wrapper for the hidden schtasks path (wscript run_hidden.vbs cmd /c <this>).
REM Same shape as ep6_full_task.cmd. Draft mode; pin 0.7.109 (owner 2026-08-30: "hf 0.7.109 is fine").
REM 3 workers: draft recipe default; box had ~4 GB free at launch.
set RENDER_WORKERS=3
call "%~dp0render.cmd" ep4-el-reno draft
