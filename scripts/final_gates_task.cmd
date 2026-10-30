@echo off
REM Pre-render gates for batch A's finals on this laptop (30 Oct 26), hidden; the renders wait on the owner's laptop pick.
set PY=C:\Users\Sidhartha\AppData\Local\Programs\Python\Python312\python.exe
set S=C:\Users\Sidhartha\Automation Projects\storm-market
set LOG=%TEMP%\final-gates-30oct.log
echo ===== gates start %date% %time% >> "%LOG%"
for %%e in (ep-buffalo-2022 ep-galveston-1900 ep-appalachian-1950) do (
  echo == %%e gates start %date% %time% >> "%LOG%"
  "%PY%" "%S%\.worktrees\%%e\scripts\run_gates.py" "%S%\.worktrees\%%e\episodes\%%e" >> "%LOG%" 2>&1
  if errorlevel 1 (echo == %%e GATES FAIL %date% %time% >> "%LOG%") else (echo == %%e GATES PASS %date% %time% >> "%LOG%")
)
echo ===== gates end %date% %time% >> "%LOG%"
