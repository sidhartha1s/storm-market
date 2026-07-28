@echo off
cd /d "C:\Users\Sidhartha\Automation Projects\storm-market\.worktrees\ep3-v2\episodes\ep3-tristate"
set PRODUCER_PAGE_NAVIGATION_TIMEOUT_MS=120000
set PRODUCER_PUPPETEER_PROTOCOL_TIMEOUT_MS=900000
call npx hyperframes@0.7.64 snapshot . --frames 105 --timeout 120000 --describe false -o snapshots/sweepv2 >> snapshots/sweepv2.log 2>&1
echo %ERRORLEVEL% > snapshots\sweepv2_done.marker
