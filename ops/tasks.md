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
| 26 | Other platforms for the same videos, long and short, and one tool that posts to all of them (owner 10 Oct 26: "I will be giving you all the API keys and stuff, you will automate all those things") | `references/distribution.md`: first check of Facebook, Spotify, X, TikTok, Snapchat, Rumble, Dailymotion and three ways to post | todo: reminder, raise with the owner after El Reno publishes. Waiting on him: the Facebook Page, a look at the monetization tab on Facebook and Spotify from his account (is his country in), then the keys |
| 15 | Thumbnail study of 13 channels and a design system for Paul on the thumbnail (owner 7 Oct 26) | `references/teardowns/2026-10-08-thumbnails-13-channels/README.md`, `references/packaging-rules.md` "Paul on the thumbnail", `references/thumbnail-prompts.md` | owner kept Field Notes and On the Ground on 8 Oct 26. Open: build the step that lays Paul and the words over the untouched photograph (On the Ground); make the no-face version for each video and run it in Test and Compare; run the slotted prompts once in ChatGPT (only the filled demo prompts have been run); the webgen `batch` command the demos used sits on an unmerged branch of that project |

## Gates from the owner's MG rules (26 Sep 26; rules in `references/mg-quickref.md`)
| # | task | PR | status |
|---|---|---|---|
| 15 | gate: presenter-circle keep-out (only when Paul is shown) | - | todo, owner-approved 26 Sep 26 |
| 16 | gate: 5% text-safe margin (96/54 px) | - | todo, owner-approved 26 Sep 26 |
| 17 | gate: one stillness number (graphics_qc idle 3.0/2.5 s -> 4.0 s, idle hard, idle-budget removed) | - | done 26 Sep 26, PR fix/stillness-4s |
| 18 | library sweep: dark chips and colour-block stamps left in bulletin-typewriter.html, ranked-bars.html, ef-ladder.html, cards.css .stamp, snippets/usage-examples.html | - | todo |

## Gates from El Reno (owner 10 Oct 26: "improve it. like CICD"; findings in `learnings/mg.md` and `learnings/script-process.md`, 10 Oct 26)
| # | task | PR | status |
|---|---|---|---|
| 27 | Seek-order gate: stage each comp, capture every cue second forward-only and after a seek to 0, fail on a differing state (prototype, run on 11 comps and 1,795 sample times: `docs/backlog/seekcheck-prototype.mjs`) | | todo |
| 28 | Label-over-painted-shape check in `graphics_qc.mjs`: sample points across every visible text box at each cue and through the first 0.5 s, fail when a line, ring or dot paints under it | | todo |
| 29 | `lint_timeline.py`: a comp that declares a transparent span needs a track 1 picture under that span (today the track 2 host counts as picture and the hole renders black) | | todo |
| 30 | Media probe: fail a JPEG that does not end with the end marker (headless Chrome left a truncated one unpainted in 3 of 4 loads) | | todo |
| 31 | `overlap_check.mjs`: `data-repeat-ok="reason"` declares one label that sits on several different things | #154 | done |
| 32 | Script picture notes are not walked by any gate (`learnings/script-process.md` 10 Oct 26). A read-only check that lists every `**Picture:**` ask beside what is mounted in its window, for the editor to tick | | todo |
| 33 | Paul's screen time is not checked by any gate: El Reno's first draft had no corner circle and no face between 0:07 and 5:26, and the owner found it in the draft (10 Oct 26). `sweep_episode.py`: fail a documentary whose corner circle is missing outside his full-frame clips, the book ad and the stretches `references/mg-quickref.md` "Corner circle" lists as off | | todo |

## Parked until the new laptop (owner 28 Sep 26; source review: howseen-ai/claude-motion-design)
Current box: 16 GB RAM, GTX 1650 4 GB; full renders already hit the commit-memory limit. Revisit when the new laptop arrives.
| # | task | why parked | status |
|---|---|---|---|
| 19 | Motion blur on fast MG moves: 6 to 8 subframes per frame blended with ffmpeg `tmix`, MG scenes only, one graphic as the first test | about 8x the capture work per blurred frame | parked |
| 20 | 60 fps masters, only if motion blur alone is not enough | 2x frames for a small gain in narrated docs | parked |

## Studio (`hyperframes preview`) on a small box (owner 1 Oct 26)
Never tested on this box because it always died (learnings/render.md "HF studio": a 32-min comp fired 2,200+ media
requests at once, black canvas, no audio; that was 0.7.x). Goal: scrub the real timeline without a render. Cheapest first;
stop at the first one that works. Every row runs alone (one heavy job at a time) and logs peak RAM, so the new laptop has a baseline.
| # | task | why | status |
|---|---|---|---|
| 21 | Re-test full studio on this box at the current pin with `--no-open --no-browser-gpu`, on the newest finished episode: open it, scrub to 3 points, log peak RAM and time to first frame. 0.8.93 loads only media near the playhead, which is the exact 0.7.x failure | may already be fixed upstream; zero code | todo (this box) |
| 22 | Per-act studio: open one act's sub-composition at a time instead of index.html (the trimmed-scaffold recipe in learnings/render.md, scripted once if it gets used twice) | a 3 to 5 min window holds a fraction of the media | todo, only if #21 fails |
| 23 | Preview proxies: 540p low-bitrate copies of `media/` served in place of the originals for preview only (renders keep the originals) | decode cost is most of the RAM; the studio's own `--proxy` only converts codecs, not size | todo, only if #22 is still heavy |
| 24 | Our own scrubber page: a static page that loads index.html in an iframe and seeks its paused GSAP timelines plus video currentTime from one slider; no studio server, lint, filmstrips or thumbnails | lightest way to "see the timeline"; read-only, never writes episode HTML | idea, only if #21 to #23 fail |
| 25 | New laptop: full studio on a finished 20+ min episode, same 3-point scrub, compared with the #21 numbers | the real fix is RAM | parked until the new laptop |

## Minor findings, not scheduled
- #96: a crash after synthesis but before the manifest write labels the segment "legacy" (audio is correct).
- #97: WARN text misleading when every on-screen file is tagged modern.
- `master_deliverables.py` has no frame-rate check, so a draft verified as `draft` can be mastered; add a check that the file matches the composition's `data-fps`.
- optimize_clips fits instead of covers, so landscape sources in shorts get upscaled.
- Remaining minors from the Opus re-review journal (13 total), triaged when a PR touches that file.

## Housekeeping
- e2e test episode fails sweep first, so 8 of 9 gates never run in e2e: pick or build a test episode that passes sweep.
- Orphan `.worktrees` folders: owner reviews the list with status and GB each before any deletion (REMIND).
- `C:\tmp_oldcode_test`: scratch folder left by an agent; owner deletes (deny rule blocks `rm -rf`).
- Catch-up `/simplify` on the #85-#98 code, one PR.
- `/yt/` went live on 7 Oct 26 and `channel.cta.first_link` points at it. Still open after the 7 Oct 26 swap to the book ad v3: every unpublished episode restages `media/cta/` and retimes what follows the longer CTA; the minis' presenter circle is still cut from the v5 clip (`references/mini-storms/FORMAT.md` "Presenter circle"), an older face than the ad's, and needs a new source; the first render with v6 checks that `verify_render.sh` accepts the ad's silent tail plus the 1.0 s dip. (todo)
- Everything-in-the-repo rule (owner 7 Oct 26, `CLAUDE.md`): still outside are the book ad editing project and Paul source clips (`C:\Users\Sidhartha\Videos\paul-v2-test`, 778 MB) and the stock-fetch keys (`~/.claude/.env`). Rebuilding `.venv-pocket` from `scripts/voice_requirements.txt` has never been run; the current venv is a copy. Also outside (12 Oct 26, used for the Palm Sunday preview): the script that converts narration to the owner's voice (scratch in the El Reno worktree, `.worktrees/ep-el-reno-v4b/episodes/ep4-el-reno/.qc-tmp/voice-sid/convert_one.py`: move it before that worktree is removed) and the Flow clip driver (`~/.claude/scratch/flowdrv/`). Both move in before the next episode uses them. (todo)
- Book ad window moved to the halfway mark (7 Oct 26): the minis' `window_ms` is still 0.85 to 0.95 (the owner's order named the documentary); ask before moving it.
- Voice switch (8 Oct 26): the El Reno v4 plan (`episodes/ep4-el-reno/PLAN-v4.md` on branch `ep-el-reno-v4`) still says the lane tempo is 1.10 and key reveals drop to 1.0. On the Paul clone the lane is 0.94 and a slow reveal is `(tempo 0.85)`; `(tempo 1.0)` would now speed the line up. Fix the plan when that branch takes main. Old-voice sentence clips in `episodes/*/audio/_raw/_segments` are dead disk (143 MB in ep3 and ep6): the owner decides whether to delete.
- Voice switch follow-ups (8 Oct 26 review): eight older episodes (ep1, ep2, ep3, ep5, ep6, ep-1974, br-elnino-california, ms-elnino-texas) have manifests with no tempo, which `tts_episode.py` adopts on text alone, so one edited line there would come back in the new voice among old-voice lines (shipped episodes are never edited, so nothing is wrong today). `references/shorts/PLAN.md` says shorts deliver about 150 wpm; the config numbers give about 195 on both voices. Measure a short before the pilot.
- Paul on screen (7 Oct 26): the second Flow account is not set up yet (the owner types the login); until it is, one account's free credits do not cover a video's full-frame clips in a day. No episode has opened on Paul yet: El Reno v4 is the first, and its hook plan predates this rule. Two gaps to close on that first build: `build_srt.py` captions a whole Paul clip as one cue (up to about 26 words), and no gate fails narration laid under an `ins-paul-` clip.
- Presenter circle face (10 Oct 26, `references/mg-quickref.md` "Corner circle"): the FlashHead install exists only on the ZBook and was built by hand (recipe in `learnings/render.md`); no install script is tracked, so a rebuilt machine repeats it from that entry. The two models that lost the comparison (MuseTalk 10.31 GB, JoyVASA 8.36 GB) and the uv cache (17.96 GB) still sit under `.models\lipsync\` on the ZBook: delete on the owner's word. Task 15 (the keep-out gate) now guards most of a documentary's runtime, not a minute of it. The minis' circle is still cut from the v5 ad clip and could move to the same tool. Both deAPI accounts in the repo `.env` answered `403 Client account is suspended` on 10 Oct 26, so LTX clips and DeAPI music are out until the owner reinstates one; `CLAUDE.md` "Sound" and `DESIGN.md` still list DeAPI as a source. (todo)
- Angle first (9 Oct 26, `references/angle.md`): one open question for the owner. Should a gate refuse narration when the episode has no `angle.md`? Today the rule is enforced by the two skills and the writer's brief, not by code. (Minis: answered 9 Oct 26, "yes minis too"; the mini skill has the gate as step 0.)
