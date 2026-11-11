# Tasks: engineering and pipeline work

Open work on the tooling, gates and pipeline, and the questions only the owner can settle. Episode state is
`python3 scripts/stage.py`. Decisions behind these tasks go in `ops/decisions.md`. Update a row the same session its state changes.

Status: `todo` · `doing` · `review` (PR open, waiting on Opus review, e2e or the owner) · `done` (merged, main green) · `parked`.
Every task number is used once; new rows take the next free number (now 49).

## Waiting on the owner
Each item: the question, the options, what is blocked meanwhile, and the reply that settles it. The session records
his answer in `ops/decisions.md` (and with `stage.py record` when it is a gate) the turn it arrives.

1. **Is the title and thumbnail a gate before the hook+intro, or a pick that blocks only the upload?** CLAUDE.md lists it as
   gate 2 before the hook+intro; the documentary skill says thumbnails block only the upload. (A) a gate: no hook+intro is
   shown until he picks; (B) a pick: it blocks only publishing. Meanwhile `stage.py` follows B. Reply: "packaging is a gate" or "packaging blocks only the upload".
2. **Are the per-insert yes/no and the voice pick owner gates?** CLAUDE.md says five gates "and no others"; DESIGN.md
   asks his yes on every `insert` clip, and the skill's picks page carries voice, inserts and thumbnails. (A) they are
   gates (add them to the list); (B) they are not (insert clips go in on the editor's call). Meanwhile inserts still wait
   for his yes per DESIGN.md. Reply: "inserts and voice are gates" or "drop the insert yes/no".
3. **CTA v10 or v9?** E04, E05 and E06 mount `paul-storm-ready-v10-oct23`, which exists only on three unmerged branches;
   main tracks and pins v9 (`config.yaml channel.cta.file`), which sits 3.1 dB under Moore's narration. (A) land v10 on
   main (asset, config, decisions row); (B) keep v9 and fix its level. Meanwhile the next episode mounts v9. Reply: "land v10" or "keep v9".
4. **Titles and thumbnails of the shipped episodes.** Titles are still "TBD by owner" on E04, E05, E06, E08, E09 and no
   thumbnail is locked on E02 to E09. (A) he names each live title and thumbnail, and the session records them;
   (B) leave as is. Blocks: `stage.py` shows OWNER packaging on all nine. Reply: per episode, "E0n: <title>, thumb <file>".
5. **Which of the nine are public on YouTube, and when?** Nothing on disk says. Buffalo's window was near Christmas
   (23 to 27 Dec), Appalachian 24 to 26 Nov, Mayfield before 10 Dec; Enderlin is recorded as published (XxD2MYco8mM).
   Blocks: the `published` lines in each `gates.md`. Reply: "E0n public on <date>" per episode, or "none yet".
6. **E07 and E08 captions.** Their shipped SRTs lack narration lines that play (E07: 2 lines, at 14:33 and 17:03; E08:
   3 lines, at 03:43, 05:24 and 14:59); `build_srt.py` now fails this. (A) rebuild the SRTs and re-upload the captions;
   (B) leave them. Nothing else is blocked. Reply: "rebuild E07 and E08 captions" or "leave them".
7. **A re-render under a default basename overwrites the review cut he was sent.** Options: (A) `render.cmd` refuses an
   existing output; (B) `dojo_draft.cmd` passes a timestamped basename; (C) both; (D) leave. Meanwhile pass a fresh
   basename by hand. Reply: "A", "B", "C" or "D".
8. **The lane-gate Stop hook is not on the ZBook** (`~/.claude/hooks/lane-gate.py` is in neither `~/.claude/hooks` nor
   settings.json there; it may be on the offline ASUS). (A) copy it from the ASUS and register it; (B) drop the rule and
   rely on `lanes.py status` before a turn ends (what the skill says meanwhile). Reply: "copy the hook" or "drop the hook".
9. **Retire or revive `ops/tracker.json`** (with `ops/tracker.html` and `ops/build_tracker.py`): hand-kept, last
   updated 19 Oct 26, none of the nine shipped episodes current; `stage.py` now shows documentary state. (A) retire (delete
   the three files); (B) revive and reseed. Meanwhile nobody updates it. Reply: "retire the tracker" or "revive it".
10. **The ZBook's main checkout has 1,591 tracked files deleted in its working tree** (old episodes ep1 to ep6, ep-1974,
    Nepal, ms-*, br-*, demos); it is otherwise at origin/main. (A) restore them (`git checkout -- .`); (B) commit their
    removal in a PR. Blocks: a clean `git status` in the main checkout. Reply: "restore" or "remove them".
11. **Mini lane: is the draft preview a gate?** CLAUDE.md and the mini skill say two gates (angle, packaging) and
    "everything else runs to a shipped private upload", yet the skill's steps 8 and 7-9 say "owner preview". (A) three
    gates; (B) the full render follows the draft without a stop. Reply: "mini preview is a gate" or "no mini preview stop".
12. **Mini stills: 4 s or 6 s?** The mini skill and FORMAT.md say no static still over 4 s; the gate fails only past 6 s
    (`references/mg-quickref.md` check 9). (A) minis keep 4 s (a gate change); (B) one number, 6 s. Reply: "4 s for minis" or "6 s everywhere".
13. **Mini CTA dip-out: 0.5 s or 1.0 s?** FORMAT.md says 0.5 s, `config.yaml channel.cta` says 1.0 s, the mini skill says
    "keep the dip out". Reply: "0.5", "1.0" or "no dip".
14. **Buffalo's angle** was recorded as "locked by the owner" from "angle is your call", which `references/angle.md` does not
    count as a lock. (A) record it as a delegation; (B) re-ask. Reply: "delegated" or "re-ask".
15. **Gemini TTS row (17 Oct 26 in `ops/decisions.md`)**: no repo code uses it and CLAUDE.md "Voice" names pocket-TTS only.
    (A) mark it superseded; (B) it is live: say which episodes used it and move the tool in. Reply: "Gemini is dead" or "Gemini is live for <episodes>".
16. **Angle gate in code** (open since 9 Oct 26): should `tts_episode.py` refuse narration when the episode has no `angle.md`?
    Today the skills and the writer's brief enforce it. Reply: "add the gate" or "no gate".
17. **Font-fidelity staging (task 14)**, waiting on his go since 24 Sep 26. Reply: "go 14" or "drop 14".
18. **The keep-out and text-margin gates (tasks 15, 16)**, owner-approved 26 Sep 26, never built; nine episodes shipped
    without them. Reply: "build 15 and 16 now" or "drop them".
19. **The 10 Oct 26 gates (tasks 27 to 30, 32)**: build or drop. Reply: "build <numbers>" or "drop <numbers>".
20. **Retention-study rule changes (task 9)**: he decides each, open since 24 Sep 26. Reply: per rule, "apply" or "skip", or "park the study".
21. **Distribution (task 26)**: the reminder was due after El Reno published. He needs to give the Facebook Page, a look at
    the monetization tabs and then the keys. Reply: "start distribution" or "park it".
22. **Shorts**: no pilot go on record; PR #179 (three Joplin shorts, unrendered) open since 17 Oct 26. (A) pilot go and
    merge #179; (B) close #179 and park the lane. Reply: "shorts go" or "park shorts".
23. **Things still outside the repo** (task 47): the book ad editing project and Paul source clips
    (`C:\Users\Sidhartha\Videos\paul-v2-test`), the narration voice-conversion script and the Flow clip driver
    (`~/.claude/scratch/flowdrv/`; PR #213 closed unmerged). (A) move them in; (B) list them as exceptions in CLAUDE.md. Reply: "move in" or "exceptions".
24. **Cleanup, each on his word**: dead old-voice `_segments` (143 MB); on the ZBook `.models\lipsync` (MuseTalk 10.31 GB,
    JoyVASA 8.36 GB, uv cache 17.96 GB); about 35 stale branches on origin (not before item 3 is settled: v10 sits on three of
    them); the two no-face thumbnails left in E02 `thumbs/`; `C:\tmp_oldcode_test` (absent on the ZBook 11 Nov 26; the ASUS
    was offline). Reply: "delete <items>".

## Render runs on what it asked for (owner 26 Oct 26, ZBook QSV fallback)
| # | task | PR | status |
|---|---|---|---|
| 34 | `stream_gate.py check`: fail a render whose encoder, capture GPU or streaming differs from the ask; watch stops it at the gate line | branch render-fallback-gate | done (merged, 5c8f9109) |
| 35 | every render asks `--experimental-fast-capture=true` and falls back to screenshot capture (mix-blend-mode, backdrop-filter): dropped the flag (2 workers 5.56 to 3.68 s per output second, streaming on) | render-no-fast-capture | done (merged, 259b6645) |
| 36 | ZBook NVIDIA driver to 610+ (595.95 was too old for ffmpeg 8.1.2's NVENC) | owner (admin on the ZBook) | done: driver 616.92, ffmpeg `h264_nvenc` test passed 11 Nov 26; the first real render on it must pass `stream_gate.py check` |

## Bug fixes from the Opus re-review of PRs #85-#91 (24 Sep 26)
| # | task | PR | status |
|---|---|---|---|
| 1 | pin_ritual matches the JSON `"enabled":true` streaming-gate line, so the pin can bump again | #99 | done |
| 2 | verify_render: black/freeze exempt only in declared blackouts and CTA dips; silence also in holds, the CTA body and the closing 4 s end card (owner 21 Oct 26) | #95 | done |
| 3 | tts_episode writes `<id>.txt` only after synthesis succeeds | #96 | done |
| 4 | comp_consts.fold evaluates arithmetic with `ast` (`10 - 2 + 3` = 11) | #100 | done |
| 5 | narration_picture_check warns loudly when nothing on screen is archival | #97 | done |
| 6 | e2e counts Node crashes as crashes and names gates that never ran | #98 | done |
| 7 | frame QC: frame 3 treats a mid-comp panel swap as the exit | - | parked: layout sweep rejected (task 10); revisit with the font-fidelity fix (task 14) |
| 8 | run_gates runs narration_picture_check; five shipped-episode render wrappers removed | #94 | done |

## Studies (owner asks 24 Sep 26)
| # | task | output | status |
|---|---|---|---|
| 9 | Independent retention/AVD study vs the repo's script rules; flag weak owner rules; face-intro and Paul-retirement path | `references/retention-study-2026-09-24.md` | review: owner decides each rule change ("Waiting on the owner" 20) |
| 10 | Layout sweep (text boxes every 0.25 s, pixel offsets): time to build, tradeoffs, eval on ep-1974 | eval done: full sweep not worth it (0 of 30 extra flags real on ep-1974); build the font-fidelity fix instead (task 14) | done |
| 11 | ep-1974 time breakdown with turns per phase, script iterations, MG costs | `references/time-breakdown-ep-1974.md` | done |
| 12 | MG build trial: one fresh hand-curated MG, 0 to prod quality, Opus 5.5 vs Sonnet (effort high); time, turns, quality; keep or retire Sonnet for MGs | report | done 24 Sep 26: Opus 14.19 min, 41 turns, judge 43/50 shippable; Sonnet 22.29 min, 55 turns, judge 26/50 not shippable. Reading rules was the biggest phase (38.4 % / 41.6 %) |
| 13 | MG templates for repeated kinds (person card, citation, map with pins) | - | parked: after task 12 |
| 14 | Gates stage comps in system Arial but renders swap to Montserrat/Inter/EB Garamond (hyperframes alias table): shared @font-face staging for overlap_check, graphics_qc, occlusion_check. Missed shipped collisions in ep-1974 g-plane and g-map-i. Est. 2-3 h | - | todo: owner go ("Waiting on the owner" 17) |
| 26 | Other platforms for the same videos, long and short, and one tool that posts to all of them (owner 10 Oct 26: "I will be giving you all the API keys and stuff, you will automate all those things") | `references/distribution.md`: first check of Facebook, Spotify, X, TikTok, Snapchat, Rumble, Dailymotion and three ways to post | todo: the "after El Reno publishes" reminder is due ("Waiting on the owner" 21). Waiting on him: the Facebook Page, a look at the monetization tab on Facebook and Spotify from his account (is his country in), then the keys |
| 37 | Thumbnail study of 13 channels and a design system for Paul on the thumbnail (owner 7 Oct 26) | `references/teardowns/2026-10-08-thumbnails-13-channels/README.md`, `references/packaging-rules.md` "Paul on the thumbnail", `references/thumbnail-prompts.md` | owner kept Field Notes and On the Ground on 8 Oct 26; the no-face variant was withdrawn 2 Nov 26. Open: build the step that lays Paul and the words over the untouched photograph (On the Ground); run the slotted prompts once in ChatGPT (only the filled demo prompts have been run); the webgen `batch` command the demos used sits on an unmerged branch of that project |

## Gates from the owner's MG rules (26 Sep 26; rules in `references/mg-quickref.md`)
| # | task | PR | status |
|---|---|---|---|
| 15 | gate: presenter-circle keep-out (only when Paul is shown) | - | todo, owner-approved 26 Sep 26 ("Waiting on the owner" 18) |
| 16 | gate: 5% text-safe margin (96/54 px; `graphics_qc.mjs` checks 24 px today) | - | todo, owner-approved 26 Sep 26 ("Waiting on the owner" 18) |
| 17 | gate: one stillness number (graphics_qc idle 3.0/2.5 s -> 4.0 s, idle hard, idle-budget removed) | - | done 26 Sep 26, PR fix/stillness-4s |
| 18 | library sweep: dark chips and colour-block stamps left in bulletin-typewriter.html, ranked-bars.html, ef-ladder.html, cards.css .stamp, snippets/usage-examples.html | - | todo |

## Gates from El Reno (owner 10 Oct 26: "improve it. like CICD"; findings in `learnings/mg.md` and `learnings/script-process.md`, 10 Oct 26)
| # | task | PR | status |
|---|---|---|---|
| 27 | Seek-order gate: stage each comp, capture every cue second forward-only and after a seek to 0, fail on a differing state (prototype, run on 11 comps and 1,795 sample times: `docs/backlog/seekcheck-prototype.mjs`) | | todo ("Waiting on the owner" 19) |
| 28 | Label-over-painted-shape check in `graphics_qc.mjs`: sample points across every visible text box at each cue and through the first 0.5 s, fail when a line, ring or dot paints under it | | todo ("Waiting on the owner" 19) |
| 29 | `lint_timeline.py`: a comp that declares a transparent span needs a track 1 picture under that span (today the track 2 host counts as picture and the hole renders black) | | todo ("Waiting on the owner" 19) |
| 30 | Media probe: fail a JPEG that does not end with the end marker (headless Chrome left a truncated one unpainted in 3 of 4 loads) | | todo ("Waiting on the owner" 19) |
| 31 | `overlap_check.mjs`: `data-repeat-ok="reason"` declares one label that sits on several different things | #154 | done |
| 32 | Script picture notes are not walked by any gate (`learnings/script-process.md` 10 Oct 26). A read-only check that lists every `**Picture:**` ask beside what is mounted in its window, for the editor to tick | | todo ("Waiting on the owner" 19) |
| 33 | Paul's screen time: El Reno's first draft had no corner circle and no face between 0:07 and 5:26 (10 Oct 26). `sweep_episode.py`: fail a documentary whose corner circle is missing outside his full-frame clips, the book ad and the stretches `references/mg-quickref.md` "Corner circle" lists as off | | partly done: `render_preflight.py` `LAYERS` fails a missing or frozen circle (18 Oct 26); the per-stretch check is todo |

## e2e runs every gate (owner 26 Oct 26, skeptic finding 27 "do")
| # | task | PR | status |
|---|---|---|---|
| 38 | e2e fails on a gate that fails or never runs; pinned fixture `scripts/fixtures/e2e/ep-e2e-moore` passes all of them | #222 | done (merged) |
| 39 | config's CTA (v9) is 3.1 dB under Moore's narration, past audio_levels' 2.5 dB insert band; Moore shipped the unmerged v10 | | waiting on the owner (item 3) |

## Left open by the 11 Nov 26 code fixes
| # | task | status |
|---|---|---|
| 40 | `blank_scan.mjs` still carries its own staging copy instead of `stage_comp.mjs` (audit G12) | review (branch `sweep-2-gates`; fixture output identical before and after) |
| 41 | `graphics_qc.mjs` rewrites the tracked `compositions/_durations.json` on every run, so e2e leaves the fixture's copy modified (audit G17); until fixed, restore it with `git checkout` | todo |
| 42 | `sweep_episode.py` close-card exemptions are names in code, not config (audit G16) | todo |
| 43 | Every lane of every episode still starts on claude1 (audit L11) | todo |
| 44 | `paul_voice.py` and `transcribe_episode.py` do not book the heavy lock (audit L10) | todo |
| 45 | `paul_voice.py` cannot import on the ZBook: the OpenVoice weights are missing from `hf_home` (audit L14) | todo |
| 46 | `lanes.py status` on a shipped episode lists READY jobs and exits 2: lanes has no shipped state (audit L6) | todo |
| 47 | Everything-in-the-repo rule (owner 7 Oct 26): still outside are the book ad editing project and Paul source clips (`C:\Users\Sidhartha\Videos\paul-v2-test`, 778 MB), the stock-fetch keys (`~/.claude/.env`), the narration voice-conversion script (`.worktrees/ep-el-reno-v4b/episodes/ep4-el-reno/.qc-tmp/voice-sid/convert_one.py`) and the Flow clip driver (`~/.claude/scratch/flowdrv/`, PR #213 closed unmerged). Rebuilding `.venv-pocket` from `scripts/voice_requirements.txt` has never been run | todo ("Waiting on the owner" 23) |
| 48 | `npx` without `--yes` may wait on "Ok to proceed?" on a hidden console after a pin bump (`pin_ritual.py` records a 40 min hang from this prompt); not proven for render.cmd | todo |

## Parked until the new laptop (owner 28 Sep 26; source review: howseen-ai/claude-motion-design)
Box at the time: the ASUS, 16 GB RAM, GTX 1650 4 GB; full renders hit the commit-memory limit. The ZBook (RTX A2000 8 GB) is that new laptop: revisit.
| # | task | why parked | status |
|---|---|---|---|
| 19 | Motion blur on fast MG moves: 6 to 8 subframes per frame blended with ffmpeg `tmix`, MG scenes only, one graphic as the first test | about 8x the capture work per blurred frame | parked |
| 20 | 60 fps masters, only if motion blur alone is not enough | 2x frames for a small gain in narrated docs | parked |

## Studio (`hyperframes preview`) on a small box (owner 1 Oct 26)
Never tested on the ASUS because it always died (learnings/render.md "HF studio": a 32-min comp fired 2,200+ media
requests at once, black canvas, no audio; that was 0.7.x). Goal: scrub the real timeline without a render. Cheapest first;
stop at the first one that works. Every row runs alone (one heavy job at a time) and logs peak RAM.
| # | task | why | status |
|---|---|---|---|
| 21 | Re-test full studio at the current pin with `--no-open --no-browser-gpu`, on the newest finished episode: open it, scrub to 3 points, log peak RAM and time to first frame. 0.8.93 loads only media near the playhead, which is the exact 0.7.x failure | may already be fixed upstream; zero code | todo |
| 22 | Per-act studio: open one act's sub-composition at a time instead of index.html (the trimmed-scaffold recipe in learnings/render.md, scripted once if it gets used twice) | a 3 to 5 min window holds a fraction of the media | todo, only if #21 fails |
| 23 | Preview proxies: 540p low-bitrate copies of `media/` served in place of the originals for preview only (renders keep the originals) | decode cost is most of the RAM; the studio's own `--proxy` only converts codecs, not size | todo, only if #22 is still heavy |
| 24 | Our own scrubber page: a static page that loads index.html in an iframe and seeks its paused GSAP timelines plus video currentTime from one slider; no studio server, lint, filmstrips or thumbnails | lightest way to "see the timeline"; read-only, never writes episode HTML | idea, only if #21 to #23 fail |
| 25 | Full studio on a finished 20+ min episode on the ZBook, same 3-point scrub, compared with the #21 numbers | the real fix is RAM | todo |

## Minor findings, not scheduled
- #96: a crash after synthesis but before the manifest write labels the segment "legacy" (audio is correct).
- #97: WARN text misleading when every on-screen file is tagged modern.
- `master_deliverables.py` has no frame-rate check, so a draft verified as `draft` can be mastered; add a check that the file matches the composition's `data-fps`. It still carries the unused `--hevc` path (no HEVC archive, CLAUDE.md step 7).
- optimize_clips fits instead of covers, so landscape sources in shorts get upscaled.
- Remaining minors from the Opus re-review journal (13 total), triaged when a PR touches that file.

## Housekeeping
- `.worktrees/` on the ZBook holds no worktree folders; loose scratch files there (bundles, logs, `zbook_*.py`) go on the owner's word ("Waiting on the owner" 24).
- Catch-up `/simplify` on the #85-#98 code, one PR.
- `/yt/` went live on 7 Oct 26 and `channel.cta.first_link` points at it. The minis' presenter circle is still cut from the v5 clip (`references/mini-storms/FORMAT.md` "Presenter circle"), an older face than the ad's, and needs a new source. (todo)
- Book ad window moved to the halfway mark (7 Oct 26): the minis' `window_ms` is still 0.85 to 0.95 (the owner's order named the documentary); ask before moving it.
- Voice switch (8 Oct 26): old-voice sentence clips in `episodes/*/audio/_raw/_segments` are dead disk (143 MB in ep3 and ep6): the owner decides whether to delete ("Waiting on the owner" 24).
- Voice switch follow-ups (8 Oct 26 review): eight older episodes (ep1, ep2, ep3, ep5, ep6, ep-1974, br-elnino-california, ms-elnino-texas) have manifests with no tempo, which `tts_episode.py` adopts on text alone, so one edited line there would come back in the new voice among old-voice lines (shipped episodes are never edited, so nothing is wrong today). `references/shorts/PLAN.md` says shorts deliver about 150 wpm; the config numbers give about 195 on both voices. Measure a short before any pilot.
- Paul on screen (7 Oct 26): the second Flow account is not set up yet (the owner types the login); until it is, one account's free credits do not cover a video's full-frame clips in a day. Two gaps, not re-checked 11 Nov 26: `build_srt.py` captions a whole Paul clip as one cue (up to about 26 words), and no gate fails narration laid under an `ins-paul-` clip.
- Presenter circle face (10 Oct 26, `references/mg-quickref.md` "Corner circle"): the FlashHead install exists only on the ZBook and was built by hand (recipe in `learnings/render.md`); no install script is tracked, so a rebuilt machine repeats it from that entry. Task 15 (the keep-out gate) now guards most of a documentary's runtime. The minis' circle is still cut from the v5 ad clip and could move to the same tool. Both deAPI accounts in the repo `.env` answered `403 Client account is suspended` on 10 Oct 26, so LTX clips and DeAPI music are out until the owner reinstates one (CLAUDE.md "Sound" and "Footage rules" say so). (todo)
