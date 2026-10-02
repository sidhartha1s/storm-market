# El Reno 2013, v4 plan (2 Oct 26)

v4 is built from scratch, per REDO-BRIEF.md and research/v3_postmortem.md. Salvaged footage may be reused, but no edit is copied.
Status: planning. Nothing is scripted, sourced or rendered yet.

## Angle (owner picks one; the default is B)
- **A. Scale:** "the widest tornado ever recorded". This is the lane Astrum Earth's "The Tornado That Changed Science" took (4.30M views, 30 Mar 26) and RealLifeLore's "How Big do Tornadoes Get?" (7.9M, tagged remake on Niche Watch).
- **B. Paradox (default):** radar measured near-record winds inside a 2.6-mile-wide tornado, and the official rating was EF3. The video explains why the EF scale rates damage, not wind.
  - It ties back to Enderlin (the EF5 drought) and is a primary-source fact no top competitor leads with (CLAUDE.md "two facts no competitor has").
  - It matches the payoff-first hook rule and the 2011 Super Outbreak data (a paradox hook held 71% at 0:33).
- **C. Chasers:** the chaser convergence and the TWISTEX deaths. HIGH RISK Chris already owns this (4.39M). Chaser footage is unlicensed, so this angle can't be illustrated well.

## Title candidates (<=52 chars, Name+Year in the first 40)
1. El Reno 2013: 302 MPH Winds, Rated Only EF3 (43) [verify: RaXPol peak, rating]
2. El Reno 2013: The Widest Tornado Ever Recorded (46) [verify: 2.6 mi width record]
3. El Reno 2013: The Tornado Too Big to See (40)

## Facts to verify before scripting (primary sources only: NWS Norman, the OU RaXPol papers, the NWS/NIST assessments)
- [verify: peak RaXPol wind and height] [verify: max width 2.6 mi] [verify: EF3 final rating, and why: damage-indicator method]
- [verify: deaths, tornado vs the same-night OKC flash flooding] [verify: path length, duration, times CDT]
- [verify: the 31 May 2013 timeline, 11 days after Moore EF5 (20 May)]

## Footage reality
- The v1 media pool (504 files, 3.5 GB) is gone and must be re-fetched. No El Reno media is on disk.
- Allowed: NWS Norman, DVIDS, FEMA/NARA, Wikimedia (attribution), stock, our own radar and map graphics.
- Not allowed: chaser footage (Robinson, Timmer, Samaras/TWISTEX, Basehunters), with no licence on record.
- Broadcast (KFOR, KOCO, CNN, TWC) is claims-budgeted only and kept short.
- 9 flagged files in licence_audit.md: treat all of them as out unless the owner re-approves.
- Rules carried from the post-mortem:
  - every b-roll `<video>` is muted
  - broadcast speech never overlaps the narration
  - one sound bed plus swells, no four-way pile-up

## Structure (script-os; one master map returned to at each act seam, one clock device, one named person per act)
- Hook (0:00-0:10): the payoff line over real motion. Narrator from 0:00, no archive audio.
- Intro: the dominant question in one sentence (the v3 post-mortem found it was missing).
- Act 1: the setup and the Moore shadow. Act 2: the storm and the radar. Act 3: the rating paradox (the g-dimethod-style explainer, cut to 90 s or less). Act 4: the people. The CTA sits in the config window, then the close.
- Target length 20-25 min. The word budget comes from probe TTS at the shipping tempo.

## Sound and pacing (owner 2 Oct 26; El Reno is the first episode to use these)
The editing agent decides where each of these goes by reasoning about the story beat. There are no code gates and no per-video quotas.
- **Pacing.** The baseline tempo stays 1.10. Key reveals drop to 1.0 by voicing them as their own segment. Demo: `C:\Users\Sidhartha\.claude\scratch\devq-retention\pace\B-110-then-100.mp3`.
- **Music.** Sets replace the one bed across the episode. Tracks are generated with deAPI ACE-Step 1.5, one per mood (dread build, storm, aftermath, the people), and swap at act seams and story turns. Only one bed plays at a time, so the post-mortem's no-pile-up rule still holds. Every paid run needs an owner go that names the run.
- **SFX.** Only from the owner-approved copyright-free kit (candidates in `C:\Users\Sidhartha\.claude\scratch\devq-retention\sfx\`). Placed by reasoning, not by count.
- **Silence drops.** About 1.0 s before each key line the agent identifies. The agent also decides per moment what drops out: music, SFX, ambience.
- **Open loops.** Each loop the script opens is tagged, and each tag must close before the end (script-quickref).
- **Motion graphics.** Each brief is written to the eval-v2 standard: px geometry, word-cue times from words.json, no number on screen before its word, and a must-be-true checklist. An Opus builder makes each graphic, then a strict Opus viewer reviews it for at most 2 rounds.

## Order of work (owner gates in caps)
1. ANGLE + TITLE + THUMB LOCK (packaging before scripting).
2. The fact sheet from primary sources, and a teardown of Astrum #3 and Chris #2 (hooks already pulled).
3. Hook and intro draft. The OWNER GATE and the fact-check fan-out run in parallel.
4. Voice: if the owner's own voice clone lands today (planned), TTS uses it, not Pharaoh.
5. Sourcing and re-fetch, with 2-3 candidates per beat and a provenance row per file.
6. Compose: Opus builders after VO, at most 5 at once.
7. Gates and frame reads, then the pin ritual (0.8.106 is out now), then a DRAFT RENDER for owner review.
