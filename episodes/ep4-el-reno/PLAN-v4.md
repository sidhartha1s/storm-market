# El Reno 2013, v4 plan (2 Oct 26)

v4 is built from scratch, per REDO-BRIEF.md and research/v3_postmortem.md. Salvaged footage may be reused, but no edit is copied.
Status: planning. Nothing is scripted, sourced or rendered yet. Updated 9 Oct 26 for the rules merged on 8 Oct 26 (PRs #147, #149, #151, #152): see "Rules that changed since this plan was written". The angle was locked by the owner on 9 Oct 26: `angle.md`. Title, thumbnail and hook are open until he picks them.

## Angle: LOCKED 9 Oct 26, see `angle.md`
Nobody lost their life indoors (spine), two vehicles inside the same tornado (middle), the tornado inside the tornado (science arc). Checked facts: `research/angle-facts-2026-10-09.md`.
The three candidates below are the first list (2 Oct 26). A and B are now the leads the angle rules out; they stay in the video as facts.
- **A. Scale:** "the widest tornado ever recorded". This is the lane Astrum Earth's "The Tornado That Changed Science" took (4.30M views, 30 Mar 26) and RealLifeLore's "How Big do Tornadoes Get?" (7.9M, tagged remake on Niche Watch).
- **B. Paradox:** radar measured near-record winds inside a 2.6-mile-wide tornado, and the official rating was EF3. The video explains why the EF scale rates damage, not wind.
  - It ties back to Enderlin (the EF5 drought) and is a primary-source fact no top competitor leads with (CLAUDE.md "two facts no competitor has").
  - It matches the payoff-first hook rule and the 2011 Super Outbreak data (a paradox hook held 71% at 0:33).
- **C. Chasers:** the chaser convergence and the TWISTEX deaths. HIGH RISK Chris already owns this (4.39M). Chaser footage is unlicensed, so this angle can't be illustrated well.

## Title candidates: VOID, written for angle B before the lock
New options on the locked angle wait for the owner's pick (devq page `elreno-angle.html`, 9 Oct 26).
1. El Reno 2013: 302 MPH Winds, Rated Only EF3 (43). NOT SUPPORTED as written: `research/facts.md` confirms 130 m/s (about 291 mph) from the survey paper and marks 296 mph unverified; 302 appears in no source pulled. Use a figure the fact sheet confirms
2. El Reno 2013: The Widest Tornado Ever Recorded (46) [verify: 2.6 mi width record]
3. El Reno 2013: The Tornado Too Big to See (40)

## Facts to verify before scripting (primary sources only: NWS Norman, the OU RaXPol papers, the NWS/NIST assessments)
Done 9 Oct 26 for everything the angle rests on: `research/angle-facts-2026-10-09.md`. Still open there: the two NWS rating statements and their dates, the local reports on the family of seven, the exact broadcast words against the recording, one name against one age, the June 1 flood death.

## Footage reality
- The v1 media pool (504 files, 3.5 GB) is gone and must be re-fetched. No El Reno media is on disk.
- Allowed: NWS Norman, DVIDS, FEMA/NARA, Wikimedia (attribution), stock, our own radar and map graphics.
- Not allowed: chaser footage (Robinson, Timmer, Samaras/TWISTEX, Basehunters), with no licence on record.
- Broadcast (KFOR, KOCO, CNN, TWC) is claims-budgeted only and kept short. Owner 9 Oct 26 on the TV crew's own footage: "TV crews footage is fine ... with the overlay, with the ... narration, it is just fine to use ... Not the entire video though." So it is narrated over or carries an overlay, and it is one sequence, not the spine.
- 9 flagged files in licence_audit.md: treat all of them as out unless the owner re-approves.
- Rules carried from the post-mortem:
  - every b-roll `<video>` is muted
  - broadcast speech never overlaps the narration
  - one sound bed plus swells, no four-way pile-up

## Structure (script-os; one master map returned to at each act seam, one clock device, one named person per act)
- Hook (0:00-0:10): frame one is Paul, full frame, speaking the one hook sentence; then the highest-intent real motion with the narrator. No archive audio (DESIGN.md "Cold-open hook contract").
- Intro: the dominant question in one sentence (the v3 post-mortem found it was missing).
- Acts on the locked angle (a sketch until the script exists): Act 1, the count and the Moore shadow, why a city already hit eleven days earlier got into its cars. Act 2, the storm and the tornado inside the tornado. Act 3, two vehicles minutes apart. Act 4, the twelve in the drains and the warning gap. Act 5, the map with 21 pins and the answer. Three open questions are paid in order: why one crew lived, who the twelve were, why nobody lost their life indoors.
- The book ad sits between a tease and its payoff around the halfway mark (`channel.cta.window` 0.40 to 0.60, DESIGN.md "CTA contract"). Owner-approved hinge (9 Oct 26): the line that the home was the safe place. Paul speaks the tease, the ad runs, the payoff opens the next act.
- Death words go the soft way from the first draft (`references/flag-words.md`, owner 9 Oct 26). Children may be included (owner 9 Oct 26).
- Target length about 25-30 min, or as the story fits (owner 3 Oct 26). The word budget comes from probe TTS at the shipping tempo.

## Sound and pacing (owner 2 Oct 26; El Reno is the first episode to use these)
The editing agent decides where each of these goes by reasoning about the story beat. There are no code gates and no per-video quotas.
- **Pacing.** The lane tempo is 0.94 on the Paul clone voice (same delivered pace as the old voice at 1.10). Key reveals drop to 0.85 by voicing them as their own segment with `(tempo 0.85)` on the heading. Demo: `C:\Users\Sidhartha\.claude\scratch\devq-retention\pace\B-110-then-100.mp3`.
- **Music.** Sets replace the one bed across the episode. Tracks are generated with deAPI ACE-Step 1.5, one per mood (dread build, storm, aftermath, the people), and swap at act seams and story turns. Only one bed plays at a time, so the post-mortem's no-pile-up rule still holds. Every paid run needs an owner go that names the run. BLOCKED 2 Oct 26: all three deAPI keys return 403 "Client account is suspended". The owner's go covered 4 tracks; 0 were made and $0 was spent. Waits on a new account or support.
- **SFX.** Only from the owner-approved copyright-free kit (candidates in `C:\Users\Sidhartha\.claude\scratch\devq-retention\sfx\`). Placed by reasoning, not by count.
- **Silence drops.** About 1.0 s before each key line the agent identifies. The agent also decides per moment what drops out: music, SFX, ambience.
- **Open loops.** Each loop the script opens is tagged, and each tag must close before the end (script-quickref).
- **Sketch explainers (owner approved 3 Oct 26: "love it ... use accordingly alongside MGs").** Hand-drawn style
  explainers built in code (SVG draw-on, pencil/chalk/ink textures, no image model). Samples and kit:
  `C:\Users\Sidhartha\.claude\scratch\devq-retention\sketch\` (`sketch-kit.js`, field notebook, chalkboard, blueprint).
  The editor reasons per beat which one a beat gets:
  - MG (glass card, map, radar, stat panel): exact data on top of footage, such as a number the viewer must read, a
    place on a map, a time on a clock, or a radar loop.
  - Sketch: a mechanism, a comparison of scale, a counterfactual or a "why", with no footage to sit on, such as why
    EF3, how wide it got, or what the turn did to an escape route. One idea per sketch, drawn as the narration
    says it.
  - Same Opus builder and viewer chain as MGs; numbers on screen follow the same cue rule.
- **Motion graphics.** Each brief is written to the eval-v2 standard: px geometry, word-cue times from words.json, no number on screen before its word, and a must-be-true checklist. An Opus builder makes each graphic, then a strict Opus viewer reviews it for at most 2 rounds.

## Order of work (owner gates in caps)
1. ANGLE LOCK: done 9 Oct 26 (`angle.md`). Then HOOK + TITLE + THUMB PICK by the owner, built on that angle and nothing else.
2. The fact sheet from primary sources, and a teardown of Astrum #3 and Chris #2 (hooks already pulled).
3. Hook and intro draft. The OWNER GATE and the fact-check fan-out run in parallel.
4. Voice: the clone of on-camera Paul (`config.yaml external.voice_ref`, merged 8 Oct 26). Paul's own on-camera lines are Flow clips, not TTS: 6 clips, 90 credits, made once the lines are locked and the second Flow account is in.
5. Sourcing and re-fetch, with 2-3 candidates per beat and a provenance row per file. In parallel: SFX KIT APPROVAL and MUSIC TRACKS (a deAPI run on an owner go).
6. Compose: Opus builders after VO, at most 5 at once.
7. Gates and frame reads, then the pin ritual (0.8.106 is out now), then a DRAFT RENDER for owner review.

## Rules that changed since this plan was written (merged 8 Oct 26)
- **Paul on screen** (`references/mg-quickref.md` "Paul on screen"): about 10 % of the runtime. 6 full-frame clips of 10 s: clip 1 is frame one with the hook sentence, 4 sit at turning points and one of those is the tease before the book ad; about 1 min of corner circle, 40 s of it in the first 3 min. Mounted as `ins-paul-<n>` with `data-volume="1"`.
- **Voice and tempo:** see Pacing and step 4 above.
- **Book ad:** halfway, between a tease and its payoff; see Structure.
- **Thumbnail** (`references/packaging-rules.md` "Paul on the thumbnail"): Field Notes or On the Ground, plus a no-face version for Test and Compare. Two El Reno demos exist from the study (words "2.6 MILES / WIDE" and "TOO WIDE / TO SEE"); both sell angle A (scale), which the locked angle rules out as the lead, so the locked angle needs its own words and its own photograph.
- **Fact sheet:** `research/facts.md` is salvaged from the first build (audited 2 Aug 26). Two clock conversions in it disagree with their own UTC times (2309 UTC and 2319 UTC are 6:09 and 6:19 PM CDT) and must be fixed against the NWS Norman page before any time is spoken.
- **Music:** four generated tracks (`elreno-dread-build`, `-storm`, `-aftermath`, `-people`, .mp3) and an updated `assets/music/call_budget.json` sit uncommitted in the old worktree `.worktrees/ep-el-reno-v4`, left by an earlier session. Not yet listened to or carried over here.

