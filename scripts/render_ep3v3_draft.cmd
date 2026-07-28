@echo off
cd /d "C:\Users\Sidhartha\Automation Projects\storm-market\.worktrees\ep3-v2\episodes\ep3-tristate"
set PRODUCER_PAGE_NAVIGATION_TIMEOUT_MS=120000
set PRODUCER_PUPPETEER_PROTOCOL_TIMEOUT_MS=900000
if not exist renders mkdir renders
call npx hyperframes@0.7.64 render . --gpu --browser-gpu --experimental-fast-capture=true --quality draft --crf 32 --fps 15 --workers 3 -o renders/ep3-tristate-v3-draft.mp4 >> renders/render_v3_draft.log 2>&1
echo %ERRORLEVEL% > renders\render_v3_draft_done.marker
