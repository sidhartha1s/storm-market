@echo off
cd /d "C:\Users\Sidhartha\Automation Projects\storm-market\episodes\ep2-2011-super-outbreak"
set PRODUCER_PAGE_NAVIGATION_TIMEOUT_MS=120000
call npx hyperframes@0.7.64 render . --gpu --browser-gpu --experimental-fast-capture=true --quality draft --crf 32 --fps 15 --workers 3 -o renders/ep2-v1-draft.mp4 > render_draft.log 2>&1
echo DONE > render_draft_done.marker
