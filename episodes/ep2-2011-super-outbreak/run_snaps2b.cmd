@echo off
cd /d "C:\Users\Sidhartha\Automation Projects\storm-market\episodes\ep2-2011-super-outbreak"
set PRODUCER_PAGE_NAVIGATION_TIMEOUT_MS=120000
call npx hyperframes@0.7.64 snapshot . -o snaps2h2 --timeout 90000 --no-end --at 830,850,890,910,935,955,985,1015,1060,1105,1150,1185,1210,1260,1300,1330,1345,1395,1450,1480,1505,1540,1560,1600,1650,1670,1684 > snaps2_log2.txt 2>&1
echo DONE > snaps2_done.marker
