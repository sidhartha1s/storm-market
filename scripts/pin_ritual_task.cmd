@echo off
cd /d "C:\Users\Sidhartha\Automation Projects\storm-market\.worktrees\ep6-katrina"
set PYTHONUNBUFFERED=1
"C:\Users\Sidhartha\AppData\Local\Programs\Python\Python312\python.exe" scripts\pin_ritual.py > pin_ritual.log 2>&1
echo %errorlevel% > pin_ritual_done.marker
