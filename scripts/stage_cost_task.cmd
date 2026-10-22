@echo off
REM stage_cost_task.cmd: start the stage measurement hidden, in the logged-in session (GPU visible), as a one-shot task
REM that is deleted in the same command (repo CLAUDE.md "the render is the LAST step": create && run /i && delete).
REM The arguments go into ops\measure\run.cmd because schtasks /tr is capped at 261 characters.
REM Usage: scripts\stage_cost_task.cmd <slug> <out-json-relative> [--stages a+b+c]
setlocal
set R=%~dp0..
if not exist "%R%\ops\measure" mkdir "%R%\ops\measure"
echo @call "%R%\scripts\stage_cost.cmd" %* > "%R%\ops\measure\run.cmd"
schtasks /create /tn storm-stage-cost /tr "wscript.exe \"%R%\scripts\run_hidden.vbs\" cmd.exe /c \"%R%\ops\measure\run.cmd\"" /sc once /st 23:59 /f && schtasks /run /i /tn storm-stage-cost && schtasks /delete /tn storm-stage-cost /f
