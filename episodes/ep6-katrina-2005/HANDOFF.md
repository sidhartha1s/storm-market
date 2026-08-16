# ep6-katrina-2005 — session handoff (2026-08-16)

New session: read this FIRST, then repo CLAUDE.md + DESIGN.md + LEARNINGS.md (top section
"2026-08-16 — ep6 render-failure ledger" is this episode's hard-won gotchas).

## State — where things stand

- **Worktree**: `C:\Users\Sidhartha\Automation Projects\storm-market\.worktrees\ep6-katrina`
  (branch `ep6-katrina`, ~170 commits ahead of origin/main, auto-commit hook makes 1 commit/edit).
  ALL work stays in this worktree. Never touch the main checkout.
- **DELIVERED: draft preview** at
  `episodes\ep6-katrina-2005\renders\ep6-katrina-2005-draft.mp4`
  (269.6 MB, 28m59s, 1080p15 draft encode, render #6, exit 0).
- **Owner reaction**: "Amazing work! i have some nitpicks" — nitpicks NOT yet given.
  **Pipeline is PARKED at the draft gate. Do NOT full-render until the owner lists his
  nitpicks and approves.** First action of the new session: ask the owner for the nitpick
  list (ONE message, batched — standing rule).

## Verification already done on the draft (don't redo)

- lint_timeline PASS exit 0 (hard gate) · graphics_qc PASS 0 errors · blank_scan PASS ·
  beat_density 0/15 dead · sweep: 6 advisory fails all verified-benign (parser phantoms on
  no-src divs, designed dark sections read as stills, 0.02s butt-joins)
- media_budget PASS 138/150 MB
- Post-render: blackdetect 0, silencedetect 0, no freeze >6s, volumedetect mean −16.5 / max −0.4 dB
- Frames eyeballed: sub-comp cards animate correctly (g-bowl mid-draw @55s, g-receipt piles @890s)

## The 6-render failure chain (all root-caused — full detail in LEARNINGS.md 2026-08-16)

1. GIF transcode timeout (300s hardcoded) → all 3 GIFs converted (2 static→PNG, radar→padded mp4)
2. `ASSET_MEDIA_TYPE_MISMATCH (expected: audio)` → radar mp4 had no audio stream; CLI doesn't
   name the culprit — found by instrumenting `mismatches.push` in the npx-cached cli.js
   (patch REVERTED after use). Fix: mux `anullsrc` silence. Every mounted video needs an
   audio stream under 0.7.109.
3. (same failure, diagnostic run)
4. 25/44 videos extracted 0 frames → BATTERY power-throttle (~3 min/video). schtasks tasks
   also don't start on battery by default (task `ep6draft` now has AllowStartIfOnBatteries).
   Renders want AC power.
5. Render "succeeded" but ALL 16 timelines static → master driver threw `popIn is not
   defined` before registering `window.__timelines` → hyperframes never rebinds ANY timeline
   (warning: `sub_timeline_readiness_timeout`). Fixed: popIn helper defined in index.html
   driver (next to reveal/drift). **Verify-the-artifact lesson: exit 0 + green log ≠ animated
   cards — eyeball frames at known card moments.** Headless check script:
   `node scripts/_check_driver.mjs` (loads index.html, prints registered timelines + page
   errors — must show `["ep6-katrina2005"]` and "no page errors").
6. SUCCESS.

## Known deferred nits (owner's list comes on top of these)

- g-bowl: "LAKE PONTCHARTRAIN" label clips at right frame edge (x=1400 in the SVG; nudge
  left or shrink) — compositions/g-bowl.html
- Audio peak −0.4 dB (gate wants ≤ −1.5): handled by master_deliverables −14 LUFS pass, or
  drop the loudest bed's data-volume a notch before the full render
- sweep_episode's 6 advisory FAILs are benign but noisy — optional: teach it no-src divs and
  designed dark sections (checker-only script, allowed)
- provenance rows for evac3/ppwide re-extract windows are stale vs actual cuts; merge the
  provenance-*.csv shards → provenance.csv before publish

## TODO — remaining pipeline (in order, after owner nitpicks)

1. Owner nitpicks → apply fixes → re-run static suite (lint/graphics_qc/blank_scan/
   beat_density/media_budget) → re-draft ONLY if visuals changed materially, else proceed
2. Full render: `scripts\render.cmd ep6-katrina-2005 full` via schtasks task `ep6draft`
   pattern (create ep6full task with battery settings; AC power; box otherwise idle;
   budget ~1.5–2h wall)
3. verify_render.sh + volumedetect + dense eyeball pass + hook watch + 3 random minutes listened
4. `python3 scripts/master_deliverables.py episodes/ep6-katrina-2005 ep6-katrina-2005-full --hevc`
   (−14 LUFS master + SRT + HEVC)
5. metadata.md (no-spoiler, dual-scope death-toll stat self-disambiguating: 1,392 official
   2023 count, scope Gulf states; courtesy credits: WWL-TV, NOAA, FEMA, USCG, NASA, DVIDS)
6. Commit sweep, PR from `ep6-katrina` branch (as sidhartha1s, rebase-merge, docs sweep in
   same PR — LEARNINGS.md is already updated), delete worktree after merge
7. Private upload + Content-ID Checks soak before public

## Mechanics the new session must know

- Render launch: schtasks task `ep6draft` exists (draft mode, battery-enabled). Pattern:
  `MSYS_NO_PATHCONV=1 schtasks /run /tn ep6draft`; marker `render_draft_done.marker`
  (contents = exit code), log `render_draft.log`. Monitor log-mtime for stalls (>12 min).
- Cheap render monitoring: /loop 3m cron reading the log tail (ScheduleWakeup is INVISIBLE
  to the owner — use CronCreate loops).
- optimize_clips.py strips audio from EVERYTHING (`-an`) — audible clips (hook-hoist,
  wwl-breach-water-1, ins04a/b, ins05, ins06 — all data-volume>0 in index.html) must get
  audio re-muxed from media/_orig/ after any optimize pass.
- Owner rules active this episode: batch ALL approval asks into ONE early message; hook has
  ZERO muted elements; a work order is a standing goal until verified done; deliver = artifact
  path the owner can eyeball.
- Failed-render artifacts (fail1–5 logs/markers + the static-cards mp4) are in the OLD
  session's scratchpad — treat as gone; everything needed is in LEARNINGS.md.
