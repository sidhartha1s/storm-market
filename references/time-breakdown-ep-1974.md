# Time breakdown — ep-1974-super-outbreak (17:30 tornado documentary, shipped 22 Sep 2026)

Read-only measurement. Numbers below come from three tools, all run against disk:
1. A Python scan of every Claude Code transcript (`.jsonl`) across all 7 profile dirs (`~/.claude/projects` + 6 `.claude-accounts/*/projects`) whose lines contain the literal substring `ep-1974-super-outbreak`, mtime ≥ 2026-09-18. 104 files matched, 561.7 MB total, 14,014 events extracted.
2. `git log --author-date-order --date=iso-strict --name-only -- episodes/ep-1974-super-outbreak` in the episode worktree (committer dates were rewritten by rebase per the task brief, so only `%ad` is used). 447 commits.
3. On-disk logs/markers in `episodes/ep-1974-super-outbreak/`: `tts.log`, `tts_rerun.log`, `tts_rerun2.log`, `render_draft.log`, `render_full.log` (elapsedMs traces), and the two `*_done.marker` mtimes.

Analysis scripts ran from `%TEMP%` (`analyze_ep1974.py`, `phase_classify2.py`, `parse_git_log.py`) and are **not** committed to the repo, per instructions.

**Production window vs post-ship**: the transcript scan picked up two distinct clusters. Production (research → ship) runs 2026-09-20T16:48:33 → 2026-09-22T14:58:21 IST. A second cluster starts 2026-09-22T16:43 and is a *separate, still-running* remediation pass on a `fix-run-2026-09-23` branch (this very session's siblings: `fix-b-audio`, `fix-c1-gates`, `fix-c2-render`, `fix-d-detectors`, `diag-frame-qc`). All tables below are the **production window** unless marked "post-ship". Cutoff used: 2026-09-22T15:00 IST (after the last full-render marker 02:41 and the "final QC round" commit at 13:34).

## Classification rule (stated, as required)

Each transcript event (real user message, or assistant turn + its tool calls) is matched against ordered keyword/target rules; first match wins. Order (most-specific first): `render_full` → `draft_render` → `frame_vision_qc` (`_compshots`, screenshot, occlusion) → `gates_qc` (gate/lint/qc_/validate/detector) → `assembly` (index.html/schedule/timeline) → `mg_authoring` (`/compositions/`) → `tts` (`/audio/`, .wav, tts) → `sourcing` (`/media/`, b-roll, spider, stock) → `script` (edit_script.md, script_review, "script v", independent grade) → `research` (`/research/`, fact_sheet, NOAA/SPC) → `fixes` (fix/bug/wrong/broken) → `deliverables` (metadata.md, upload, master.mp4) → `other`. Events whose text/target hit nothing fall back to a subagent-name lookup (e.g. any event from `agent-amg-*.jsonl` → `mg_authoring`, `agent-afs-1974*` → `research`) before landing in `other`. `other` (46% of production events) is dominated by orchestration/routing chatter (idle notifications, `<teammate-message>` envelopes, permission/system reminders) — it still holds 13.28h of the 14.82h global active time, i.e. most of the calendar-time activity is coordination overhead between the 20+ parallel subagents, not classifiable content.

"Active time" = sum of gaps <10 min between consecutive events. Two numbers are reported per phase: **wall** (last event − first event of that phase) and **active** (computed on that phase's own sub-timeline). Because ~20 subagents ran concurrently, per-phase active-hours are **not mutually exclusive** — they overcount vs. the single canonical **global active time** (computed once on the full merged timeline across all 104 files), which is the authoritative "how much was actually happening" number.

## (a) Phase table — production window (2026-09-20T16:48 → 2026-09-22T14:58 IST, wall span 46.16h)

| Phase | Wall span | Active (own timeline) | Iterations (clusters, gap≥10min) | User turns | Asst turns | Tool calls | First → Last |
|---|---|---|---|---|---|---|---|
| research | 45.42h | 1.56h | 16 | 11 | 91 | 87 | 20 Sep 16:49 → 22 Sep 14:14 |
| script | 45.59h | 2.18h | 14 | 3 | 148 | 141 | 20 Sep 17:19 → 22 Sep 14:55 |
| tts | 45.86h | 1.88h | 12 | 3 | 178 | 139 | 20 Sep 17:00 → 22 Sep 14:52 |
| sourcing | 19.52h | 3.15h | 10 | 12 | 302 | 250 | 21 Sep 00:45 → 21 Sep 20:16 |
| mg_authoring | 18.50h | **5.81h** | 6 | 21 | 1772 | 1057 | 21 Sep 01:05 → 21 Sep 19:35 |
| assembly | 37.26h | 3.76h | 15 | 22 | 217 | 86 | 21 Sep 01:28 → 22 Sep 14:43 |
| gates_qc | 40.77h | 3.05h | 26 | 14 | 92 | 23 | 20 Sep 22:05 → 22 Sep 14:51 |
| frame_vision_qc | 36.56h | 3.41h | 14 | 36 | 587 | 526 | 21 Sep 01:44 → 22 Sep 14:17 |
| draft_render | 22.12h | 1.36h | 11 | 13 | 47 | 31 | 21 Sep 03:53 → 22 Sep 02:00 |
| full_render | 9.90h | 0.99h | 7 | 5 | 22 | 8 | 21 Sep 16:48 → 22 Sep 02:42 |
| fixes | 19.21h | 1.82h | 15 | 4 | 69 | 33 | 21 Sep 01:26 → 21 Sep 20:39 |
| deliverables | 34.72h | 0.17h | 7 | 1 | 10 | 6 | 20 Sep 17:08 → 22 Sep 03:51 |
| other (orchestration/unclassified) | 46.16h | 13.28h | 22 | 162 | 1346 | 580 | 20 Sep 16:48 → 22 Sep 14:58 |
| **Sum of classified phases' own active-hours** | — | **29.14h** | — | 145 | 3535 | 2387 | (not mutually exclusive — parallel subagents) |
| **Global active time (single merged timeline)** | 46.16h | **14.82h** | 16 idle gaps | 307 | 4881 | 2967 | canonical figure |

Totals (all events, production): 307 real user turns, 4,881 assistant turns, 2,967 tool calls, 63 total subagent/workflow spawns across the whole episode (`Agent`/`Task`), of which 6 were `mg-1..4` + `mg-map-fix`/`mg-trackmap`, 3 were `src-a/b/c` (+`src-people`), 2 `fs-1974`/`fs-1974-b`, up to `grader-1974-v4` for the script grader, `film-cut`/`film-cut-2`, `audio-cut`.

## (b) Script: versions and review rounds

Git (`edit_script.md`, 48 auto-commits, 7 distinct paths touched) plus `research/script_review_v*.md` give a clean version ladder:

| Version | Commit time (IST) | Independent-grader verdict |
|---|---|---|
| v1 (initial draft) | 20 Sep 17:19:58 | `research/script_review_v1.md`: **FIX THEN RE-GRADE** |
| v2 | 20 Sep 17:53:59 | "after the independent grade (carried question per act, A3 jeopardy-first...)" |
| v3 | (rapid edits 18:13–18:17) | `script_review_v3.md`: hook 8/10, overall **7/10** — FIX THEN RE-GRADE |
| v4 | 20 Sep 19:57:04 / 19:57:38 | hook to 58 words, visual event on every spike |
| v5 | 20 Sep 21:10:02 | `script_review_v5.md`: overall **7/10** — 6 hard fact errors flagged (2011 EF5 birthplace, Tanner tornadoes swapped, 28-vs-16 count, 74 vs 90 minutes, 5 vs 4 states) |
| v6 | 20 Sep 21:27:04 | `script_review_v6.md`: **7/10** — 1 timeline contradiction, banned rhetorical devices used |
| v7 | 20 Sep 21:38:50 | `script_review_v7.md`: **7/10** — 9 fact/chronology errors, opener device used 7x vs cap of 3 |
| v8 | 20 Sep 21:52:04 | `script_review_v8.md`: **8/10** |
| v9 | 20 Sep 22:03:08 | "apply the v8 independent grade (7/10, hook 8)"; docs atempo 1.10 note |
| v10 | 21 Sep 01:20:53 | fact-QC pass applied: **9 corrected, 5 unsourced claims rewritten**; MG briefs handed off; TTS prep+run started |
| final (hand-authored) | 21 Sep 03:50:28 | index.html, schedule, comp retimes, gate fixes |

10 explicit versions + 1 final hand-authoring pass = **11 iterations**, **6 independent-grader rounds** (v1, v3, v5, v6, v7, v8), plus one owner pass ("owner edits to the hook and the intro", 21 Sep 00:43:55) between v9 and v10. Script phase active time: **2.18h** (own-timeline), spanning 20 Sep 17:19 → 20 Sep 22:03 for the version ladder itself (v10/fact-QC folds into the 21 Sep 01:20 research/MG handoff).

## (c) MG authoring: per-composition edit counts

Cross-validated two ways — transcript Edit/Write target counts (production window) and independent git per-path commit counts. Both rank the same files at the top:

| Composition | Transcript edits | Git commits |
|---|---|---|
| g-combed.html | 25 | 19 |
| g-cite-paper.html | 21 | 19 |
| g-f4f5.html | 21 | 15 |
| g-engine.html | 20 | 12 |
| g-cite-tape.html | 20 | 18 |
| g-outro.html | 20 | 12 |
| g-map-i.html | 20 | (part of the g-map-* map batch, 19 commits on g-map-a4 alone) |

**Top 5 costliest comps and why** (from message evidence):
1. **g-combed.html** — the tornado-vs-microburst tree-fall schematic. Hit twice: built in batch 4 (21 Sep ~01:05), then explicitly named in the 16:26 owner-review message *"Owner reviewed the draft. Work on your files only (g-f4f5, g-engine, g-combed, g-legacy, g-thennow-16-4, g-thennow-rooms...)"* for title-contrast fixes, then flagged again at 17:05 by the verify-gate Stop hook for an un-verified edit.
2. **g-cite-paper.html** — a citation card. QC'd via 6-screenshot Read rounds (05:05), then in the owner-review-round-1 pass *"beige cite cards, ambient motion"* (16:25), then again for the "240 px Paul presenter circle" addition (17:04) — three separate touch-waves.
3. **g-f4f5.html** — F4-vs-F5 tornado damage schematic. Multiple screenshot-QC rounds ("Read these 6 PNG screenshots... F4 vs F5 tornado damage schematic", 02:11), then re-touched in the batch-4 retime receipt (03:49) and again post owner-review.
4. **g-engine.html** — the 3-band meteorological cross-section diagram; same batch-4 build + retime-receipt + owner-review cycle as g-f4f5.
5. **g-cite-tape.html** — citation card, hit by the same "beige cite cards" owner note (16:25) and flagged unverified by the Stop hook at 18:25 alongside g-cite-paper and 3 person-cards.

Pattern: every comp in the top 5 was touched in **3 separate waves** — (1) initial batch build, (2) a dedicated 6-shot-per-comp screenshot QC round, (3) the single 16:21–18:35 owner-review-round-1 rework ("motion graphics need some motion... add Paul's [circle]"). The owner-review rework wave, not the initial build, is what pushed these particular files to the top of the edit count — it touched nearly all 62 comp files at once but landed hardest on the diagram/schematic and citation-card comps because those needed both motion *and* the new presenter-circle layout rule.

## (d) Biggest 5 time sinks (evidence + timestamps)

1. **Owner-review / overnight idle gaps — 31.34h of the 46.16h wall span (68%).** Two gaps alone account for 18.8h: 21 Sep 06:40 → 16:21 (9.67h, ends with the owner's own dictated note: *"motion graphics need some motion mate. currently they stay longer to tell the storry but after sometime, it is static... add Paul's [circle]"*) and 22 Sep 03:55 → 13:04 (9.17h, ends with *"good. uplaoded. whats next on the list."* — the ship confirmation). These are the single biggest driver of calendar time; the work itself is comparatively fast.
2. **MG authoring — 5.81h active, 1,057 tool calls, 1,772 assistant turns, 6 parallel subagents, 373 git commits touching 62 comp files.** The largest true labor sink. Driven by the 3-wave pattern above (build → screenshot QC → owner-review rework) repeated across dozens of files simultaneously.
3. **Script iteration to a usable draft — 2.18h active across 10 named versions + 6 independent-grader rounds before it cleared.** v5 alone surfaced 6 hard fact errors (birthplace of the 2011 EF5, Tanner tornadoes swapped, 28-vs-16 count, 74-vs-90 minutes, 5-vs-4 states) and v7 surfaced 9 more fact/chronology errors — repeated fact-checking failures, not prose polish, were the bottleneck (final fact-QC at v10 still found "9 corrected, 5 unsourced [claims] rewritten").
4. **Frame/vision QC — 3.41h active, 526 tool calls, 587 assistant turns**, almost all `Read` calls against `_compshots/` PNGs (6 screenshots per comp, per round) — e.g. *"Read these 6 PNG screenshots (frames of one GSAP motion-graphic composition... at different seek times)"* repeated per comp, per QC pass.
5. **Render compute (not labor, but real wall-clock machine time) — draft render 20.1 min (1,208,553ms per `render_draft.log`), full render 39.9 min (2,394,301ms per `render_full.log`).** Inside the full render, `capture_streaming` (frame-by-frame screenshot capture) alone took 2,034,902ms = 33.9 min — 85% of the full-render's total time — with `audio_process` (44 tracks) a distant second at 63.6s. Single render attempt each (one `renderJobId` per log, no retries recorded in these files). A TTS segment (a4-s1) failed twice with `FileNotFoundError` and had to be split into a4-s1a/a4-s1b to rerun successfully (`tts_rerun.log`, `tts_rerun2.log`) — a small but concrete fix cycle.

## (e) Idle vs active time

Global merged timeline, production window (46.16h wall span, 2026-09-20T16:48:33 → 2026-09-22T14:58:21 IST):

| | Hours | % of wall span |
|---|---|---|
| Active (gaps <10 min) | 14.82h | 32% |
| Idle (16 gaps ≥10 min) | 31.34h | 68% |

Top idle gaps: 9.67h (21 Sep, owner review + rework brief), 9.17h (22 Sep, ship + confirmation), 2.68h (21–22 Sep overnight), 2.62h (20–21 Sep overnight), 1.70h, 1.65h — all six together = 27.99h of the 31.34h idle total; the other 10 gaps are ≤52 min each (routine short pauses, not flagged as sinks).

Post-ship remediation (separate, still running as of this report — 2026-09-22T16:43 → 2026-09-24T18:12, wall 49.48h): 4.35h active / 45.13h idle so far, on `fix-c1-gates` (gates_qc, 1.25h active), `fix-b-audio`/`fix-c2-render` (fixes, 0.66h active), `diag-frame-qc` (frame QC, negligible so far). This is out of scope for the "shipped 22 Sep" measurement above and not included in any of the totals in (a)-(d).
