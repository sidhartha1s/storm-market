@echo off
set PYTHONUNBUFFERED=1
cd /d "C:\Users\Sidhartha\Automation Projects\storm-market\.claude\worktrees\ep-mayfield-2021-a6d084"
"C:\Users\Sidhartha\AppData\Local\Programs\Python\Python312\python.exe" scripts\tts_episode.py episodes\ep-mayfield-2021 > episodes\ep-mayfield-2021\logs\tts-acts.log 2>&1
echo EXIT %ERRORLEVEL% >> episodes\ep-mayfield-2021\logs\tts-acts.log
