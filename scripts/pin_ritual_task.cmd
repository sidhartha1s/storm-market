@echo off
REM pin_ritual_task.cmd — hidden schtasks wrapper for the pin ritual. Runs against the checkout
REM this script LIVES in (%~dp0..), so it works from any worktree or the main checkout — never a
REM hardcoded path (review finding 2026-08-23: a worktree path dies when the worktree is removed,
REM and a failed `cd /d` does NOT abort cmd, so the task would misbehave from System32).
cd /d "%~dp0.."
if not exist "scripts\pin_ritual.py" (
  echo ERROR: scripts\pin_ritual.py not found from %~dp0.. — refusing to run
  echo 2 > pin_ritual_done.marker
  exit /b 2
)
set PYTHONUNBUFFERED=1
"C:\Users\Sidhartha\AppData\Local\Programs\Python\Python312\python.exe" scripts\pin_ritual.py %* > pin_ritual.log 2>&1
echo %errorlevel% > pin_ritual_done.marker
