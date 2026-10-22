@echo off
REM stage_cost.cmd: run the stage measurement on this box as a scheduled task in the logged-in session (GPU visible).
REM Usage: scripts\stage_cost.cmd <slug> <out-json>   (schtasks /tr "powershell -WindowStyle Hidden -Command cmd /c \"...stage_cost.cmd\" ep6-katrina-2005 ops\measure\zbook-2026-10-23.json")
setlocal
cd /d "%~dp0.."
py -3.12 scripts\stage_cost.py episodes\%~1 %~2 > "%~2.stdout.txt" 2>&1
echo %ERRORLEVEL% > "%~2.done"
