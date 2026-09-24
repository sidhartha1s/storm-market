# Tasks: engineering and pipeline work

Open work on the tooling, gates and pipeline. Episode slots live in `ops/tracker.json`; content strategy in
`ops/ROADMAP.md`. Decisions behind these tasks go in `ops/decisions.md`. Update a row the same session its state changes.

Status: `todo` · `doing` · `review` (PR open, waiting on Opus review, e2e or the owner) · `done` (merged, main green) · `parked`.

## Bug fixes from the Opus re-review of PRs #85-#94 (24 Sep 26)
| # | task | PR | status |
|---|---|---|---|
| 1 | pin_ritual matches the JSON `"enabled":true` streaming-gate line, so the pin can bump again | - | doing |
| 2 | verify_render: black/freeze exempt only in declared blackouts and CTA dips; silence also in holds and the CTA body | #95 | review |
| 3 | tts_episode writes `<id>.txt` only after synthesis succeeds | #96 | review |
| 4 | comp_consts.fold evaluates arithmetic with `ast` (`10 - 2 + 3` = 11) | - | doing |
| 5 | narration_picture_check warns loudly when nothing on screen is archival | #97 | review |
| 6 | e2e counts Node crashes as crashes and names gates that never ran | #98 | review |
| 7 | frame QC: frame 3 treats a mid-comp panel swap as the exit | - | parked: owner deciding on the layout sweep (task 10) |
| 8 | run_gates runs narration_picture_check; five shipped-episode render wrappers removed | #94 | review |

## Studies (owner asks 24 Sep 26)
| # | task | output | status |
|---|---|---|---|
| 9 | Independent retention/AVD study vs the repo's script rules; flag weak owner rules; face-intro and Paul-retirement path | `references/retention-study-2026-09-24.md` | doing |
| 10 | Layout sweep (text boxes every 0.25 s, pixel offsets): time to build, tradeoffs, eval on ep-1974 | report in this PR thread | todo (after e2e, RAM) |
| 11 | ep-1974 time breakdown with turns per phase, script iterations, MG costs | `references/time-breakdown-ep-1974.md` | doing |
| 12 | MG build trial: one fresh hand-curated MG, 0 to prod quality, Opus 5.5 vs Sonnet (effort high); time, turns, quality; keep or retire Sonnet for MGs | report | todo (after e2e, RAM) |
| 13 | MG templates for repeated kinds (person card, citation, map with pins) | - | parked: after task 12 |

## Minor findings, not scheduled
- #96: a crash after synthesis but before the manifest write labels the segment "legacy" (audio is correct).
- #97: WARN text misleading when every on-screen file is tagged modern.
- verify_render fps check fails drafts (15 fps vs a 30 fps composition).
- optimize_clips fits instead of covers, so landscape sources in shorts get upscaled.
- Remaining minors from the Opus re-review journal (13 total), triaged when a PR touches that file.

## Housekeeping
- Orphan `.worktrees` folders: owner reviews the list with status and GB each before any deletion (REMIND).
- `C:\tmp_oldcode_test`: scratch folder left by an agent; owner deletes (deny rule blocks `rm -rf`).
- Catch-up `/simplify` on the #85-#98 code, one PR.
