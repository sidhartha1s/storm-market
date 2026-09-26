# Tasks: engineering and pipeline work

Open work on the tooling, gates and pipeline. Episode slots live in `ops/tracker.json`; content strategy in
`ops/ROADMAP.md`. Decisions behind these tasks go in `ops/decisions.md`. Update a row the same session its state changes.

Status: `todo` · `doing` · `review` (PR open, waiting on Opus review, e2e or the owner) · `done` (merged, main green) · `parked`.

## Bug fixes from the Opus re-review of PRs #85-#91 (24 Sep 26)
| # | task | PR | status |
|---|---|---|---|
| 1 | pin_ritual matches the JSON `"enabled":true` streaming-gate line, so the pin can bump again | #99 | done |
| 2 | verify_render: black/freeze exempt only in declared blackouts and CTA dips; silence also in holds and the CTA body | #95 | done |
| 3 | tts_episode writes `<id>.txt` only after synthesis succeeds | #96 | done |
| 4 | comp_consts.fold evaluates arithmetic with `ast` (`10 - 2 + 3` = 11) | #100 | done |
| 5 | narration_picture_check warns loudly when nothing on screen is archival | #97 | done |
| 6 | e2e counts Node crashes as crashes and names gates that never ran | #98 | done |
| 7 | frame QC: frame 3 treats a mid-comp panel swap as the exit | - | parked: layout sweep rejected (task 10); revisit with the font-fidelity fix (task 14) |
| 8 | run_gates runs narration_picture_check; five shipped-episode render wrappers removed | #94 | done |

## Studies (owner asks 24 Sep 26)
| # | task | output | status |
|---|---|---|---|
| 9 | Independent retention/AVD study vs the repo's script rules; flag weak owner rules; face-intro and Paul-retirement path | `references/retention-study-2026-09-24.md` | review: owner decides each rule change |
| 10 | Layout sweep (text boxes every 0.25 s, pixel offsets): time to build, tradeoffs, eval on ep-1974 | eval done: full sweep not worth it (0 of 30 extra flags real on ep-1974); build the font-fidelity fix instead (task 14) | done |
| 11 | ep-1974 time breakdown with turns per phase, script iterations, MG costs | `references/time-breakdown-ep-1974.md` | done |
| 12 | MG build trial: one fresh hand-curated MG, 0 to prod quality, Opus 5.5 vs Sonnet (effort high); time, turns, quality; keep or retire Sonnet for MGs | report | done 24 Sep 26: Opus 14.19 min, 41 turns, judge 43/50 shippable; Sonnet 22.29 min, 55 turns, judge 26/50 not shippable. Reading rules was the biggest phase (38.4 % / 41.6 %) |
| 14 | Gates stage comps in system Arial but renders swap to Montserrat/Inter/EB Garamond (hyperframes alias table): shared @font-face staging for overlap_check, graphics_qc, occlusion_check. Missed shipped collisions in ep-1974 g-plane and g-map-i. Est. 2-3 h | - | todo: owner go |
| 13 | MG templates for repeated kinds (person card, citation, map with pins) | - | parked: after task 12 |

## Gates from the owner's MG rules (26 Sep 26; rules in `references/mg-quickref.md`)
| # | task | PR | status |
|---|---|---|---|
| 15 | gate: presenter-circle keep-out (only when Paul is shown) | - | todo, owner-approved 26 Sep 26 |
| 16 | gate: 5% text-safe margin (96/54 px) | - | todo, owner-approved 26 Sep 26 |
| 17 | gate: one stillness number (graphics_qc idle 3.0/2.5 s -> 4.0 s) | - | todo, owner-approved 26 Sep 26 |

## Minor findings, not scheduled
- #96: a crash after synthesis but before the manifest write labels the segment "legacy" (audio is correct).
- #97: WARN text misleading when every on-screen file is tagged modern.
- verify_render fps check fails drafts (15 fps vs a 30 fps composition).
- optimize_clips fits instead of covers, so landscape sources in shorts get upscaled.
- Remaining minors from the Opus re-review journal (13 total), triaged when a PR touches that file.

## Housekeeping
- e2e test episode fails sweep first, so 8 of 9 gates never run in e2e: pick or build a test episode that passes sweep.
- Orphan `.worktrees` folders: owner reviews the list with status and GB each before any deletion (REMIND).
- `C:\tmp_oldcode_test`: scratch folder left by an agent; owner deletes (deny rule blocks `rm -rf`).
- Catch-up `/simplify` on the #85-#98 code, one PR.
