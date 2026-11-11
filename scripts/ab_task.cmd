@echo off
REM A/B for the owner's 29 Oct question "should act-by-act render continue or be killed": the same Appalachian
REM index.html rendered whole (render.cmd) and by act (render_acts.py) on the same box, same 2 workers, back to back.
set RENDER_WORKERS=2
set W=C:\Users\Sidhartha\Automation Projects\storm-market\.worktrees\ep-appalachian-1950
set LOG=%W%\episodes\ep-appalachian-1950\renders\ab-1029.log
echo whole start %date% %time% >> "%LOG%"
start "" /b /wait /belownormal cmd /c call "%W%\scripts\render.cmd" ep-appalachian-1950 draft ab-whole-1029 >> "%LOG%" 2>&1
echo whole end %date% %time% >> "%LOG%"
echo acts start %date% %time% >> "%LOG%"
start "" /b /wait /belownormal cmd /c python3 "%W%\scripts\render_acts.py" ep-appalachian-1950 draft ab-acts-1029 >> "%LOG%" 2>&1
echo acts end %date% %time% >> "%LOG%"
