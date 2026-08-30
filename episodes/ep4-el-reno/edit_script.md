# edit_script.md — ep4 · "El Reno 2013" (The Warning Hour) — DESIGN v3 (rewire, 2026-08-30)

> **DESIGN GATE ARTIFACT.** Owner signs off this design BEFORE any sourcing spend or render.
> Inserts (audio-carrying clips) each get individual owner confirmation before entering a render.
> v3 = total rewire of the picture track on main's architecture (ep6 conventions, GRAPHICS CONTRACT,
> glasscard/popfig text rules, MG library-first, CTA contract). Narration is the owner-approved
> DESIGN v2 wording (2026-08-01), 27 of 33 segments kept verbatim, zero new TTS.
> Salvaged design + fact ledger: `edit_script_v2_salvage.md` (positioning, FACT LEDGER, banned list —
> all still binding). Research corpus: `research/` (facts.md, licence_audit.md, insert_gate_packet.md,
> transcripts/, clip_hunt*.md, replacement_plan.md).

## Spec
- **Channel:** The Warning Hour. **Slug:** `ep4-el-reno`. Episode 4.
- **Working title:** *The Widest Tornado Ever Recorded — El Reno 2013* (superlative anchored to a
  checkable metric). Alt: *The Tornado That Killed the Experts — El Reno 2013*.
- **Runtime target: ≈25 min (owner 2026-08-30); lands ≈25:53** (owner accepted the ~1 min over when
  choosing to keep both `a4-s4` and `a1-s1b`). Arithmetic in "Runtime" below.
- **Voice:** existing Pharaoh pocket-TTS wavs in `audio/` (33 segments, words.json each, manifest.json).
  Measured 2026-08-01: 166 wpm delivered.
- **Why v3 (owner verdict on the 08-03 draft):** "clips are off, mostly images (bad quality) or
  full-text graphics." Measured: video 11.2 min / stills 11.2 min / text comps 10.8 min; 13 stills
  held >8 s; `lint_timeline` failing at 30 % repeat-share. v3 is **video-first**: real clips ≥65 % of
  runtime, stills ≤15 % (3–6 s, always moving), ≤3 graphics comps and every one a diagram.
- **Positioning / wedge / anti-patterns / FACT LEDGER:** unchanged from v2 (see salvage file). Wedge
  facts that must survive the cut: Henderson (4th chaser), DI-method resolution, "chaser traffic
  non-factor", not NOAA-funded, NWS 1 PM tweet, the forgotten 13, AMS evacuation study.

## Hook contract compliance (DESIGN.md)
- [x] **NO black start — frame one mid-action:** `broadcast/cuts/graded/kfor-sutton-very-close-call-hookcut` (3.9 s, KFOR live, claims-budgeted) already rolling; anchor line "please do not ride this out in any interior closet or bathroom" intelligible by 1 s.
- [x] **Date/place popfig inside the first second:** "EL RENO, OKLAHOMA · MAY 31, 2013".
- [x] **Second anchor on an audio event:** `hook-anchor-voice` (4.0 s) lands as the KFOR line ends; then `twc-bettes-suv-toss-hookcut` (3.5 s: "...heading right at Bettes and his team") — three inserts, each ends on its complete statement. No two inserts back-to-back without a picture cut between them (each is its own picture window).
- [x] **Sonic spine:** NOAA Weather Radio warning bed (PD) fades in under frame one, ducks under each anchor, swells into the radar bloom, dies into the void.
- [x] Narrator enters at ≈10.5 s over our KTLX re-plot blooming (`a0-s2`), thesis lands in `a0-s3` at ≈40–74 s ("It killed the most careful storm chasers in the world" — the episode loop).
- [x] **1.5 s VOID at hook END only** (≈74.0–75.5 s), then A1.
- [x] Every cut on an audio event; captions (glasscard) only for the words they cover.

## Insert-transcription rule (binding)
Every `insert` is transcribed (faster-whisper) before cut selection — transcripts in
`research/transcripts/*.md`, cut windows in the graded filenames (`__ssss.ss-ssss.ss`). Cut chosen at
the transcript's action/emotion peak; excerpt + transcript path logged in `provenance.csv`.

## The open-loop registry (script-scaling.md)
| id | plant | pay |
|---|---|---|
| L-ep (episode loop) | `a0-s3` "the men who understood this storm best were the ones it caught" | `a7-s2` the bitter symmetry (A6) → `a7-s3` "you cannot outdrive what you cannot see" |
| **cta-hinge (REQUIRED)** | `a2-s3b` last lines: "...that gap between the pictured storm and the real one was about to close. And it was going to close on some of the most experienced observers alive." | **CTA (15.1 s)** → `a3-s1` first sentence: "At nine minutes past six, the tornado did something that rewrote every escape plan on Highway Eighty One." |
| L1 (A1) | Moore dread: "the state is an open wound" | `a4-s1` the exodus: 11 days later everyone runs (A4) |
| L2 (A2) | the width record is radar-measured — "instruments are recording winds close to three hundred" | `a6-s1/s2` why the rating still says EF3 (A5) |
| L3 (A3) | "chaser traffic was a non-factor" — then what killed them? | `a3-s3` the geometry (same act, paid honestly), echoed `a7-s3` |
| L4 (A4) | the flood is teased in `a4-s2` (SA Finding 6: media focused on tornadoes, not flooding) | `a5-s1/s2` the forgotten 13 (same act, second half) |
| L5 (A6) | Henderson's phone photo at 6:05 | `a7-s1` the line goes dead |

## Cut list (owner decision 2026-08-30: keep `a4-s4` AND `a1-s1b`)
CUT — 6 segments, −6.9 min narration, whole segments only, no dangling references (checked against each following segment's opening):
| seg | s | why |
|---|---|---|
| a1-s3 | 42.6 | "ingredients" explainer — v3 carries the setup with docmine map clips, no text card |
| a2-s3c | 68.2 | anticyclonic-twin footnote (self-labelled trivia) |
| a3-s3b | 56.1 | Bettes beat, redundant with the TWISTEX beat; the SUV-toss hookcut already carries Bettes in the hook |
| a5-s2b | 65.3 | flood rumination restating a5-s2 |
| a6-s2b | 69.6 | restates the DI-method payoff of a6-s2 |
| a7-s2b | 56.1 | redundant with a4-s2 / a6-s3 |
KEEP — 27 segments (see SCRIPT section; verbatim wavs).

## Runtime (narration 1518.1 s + overhead 35.5 s ≈ 1553.6 s = 25:53)
| Act | narration segs | narration s | starts at | ends at | out-transition |
|---|---|---|---|---|---|
| A0 hook + thesis | inserts 0–10.5 · a0-s2 · a0-s3 | 63.9 | 0:00 | 1:14 | 1.5 s VOID |
| A1 Moore, eleven days earlier | a1-s1 · a1-s1b · a1-s2 | 171.2 | 1:16 | 4:07 | 0.8 s chapter dip |
| A2 the storm | a2-s1 · a2-s1b · a2-s2 · a2-s3 · a2-s3b | 301.5 | 4:08 | 9:09 | 1.0 s dip → CTA |
| **CTA** | `assets/cta/paul-storm-ready-v4c.mp4` | 15.1 | **9:10 (35 %)** | 9:25 | 1.0 s dip |
| A3 the turn | a3-s1 · a3-s1b · a3-s2 · a3-s3 | 284.5 | 9:26 | 14:11 | 2.5 s (heaviest, post-Cobalt) |
| A4 exodus + the second disaster | a4-s1 · a4-s2 · a4-s3 · a4-s4 · a5-s1 · a5-s2 | 352.5 | 14:13 | 20:06 | 1.0 s |
| A5 why EF3 | a6-s1 · a6-s2 · a6-s3 | 175.7 | 20:07 | 23:02 | 1.0 s |
| A6 the reckoning | a7-s1 · a7-s2 · a7-s3 | 148.2 | 23:03 | 25:32 | 0.8 s |
| A7 Warning Hour footnote | a8-s1 | 20.6 | 25:32 | 25:53 | match-cut, end |
Blackout table (DESIGN.md): 0.6–0.9 chapter · 1.0–1.3 punctuation · 1.5+ only the hook void and the post-Cobalt shutdown (2.5 s, the episode's one deliberate dead-air beat).

## Act briefs

> **ACT 0 — Hook + thesis · 1:14 · 177 words**
> **Job:** three real anchor voices + our radar bloom + the thesis. Viewer knows where/when in second one and why this episode exists by 1:10.
> **In / out:** KFOR mid-sentence → radar bloom → thesis → 1.5 s void.
> **Loops:** plants L-ep.
> **Rehooks:** KFOR anchor (0 s), TWC "heading right at Bettes" (7 s), radar bloom on "growing faster than anyone has ever seen" (a0-s2), title popfig "2.6 MILES" on "edge to edge" (a0-s3).
> **Tempo:** fast, cuts on audio events only; emotion low, curiosity max.

> **ACT 1 — Eleven days earlier: Moore · 2:51 · 399 words**
> **Job:** the wound that explains May 31 — Moore EF5, the loaded week, the forecasters' dread.
> **In / out:** narrator over DVIDS Guard footage (labelled MOORE · MAY 20 glasscard) → SPC outlook build → darkening Friday sky → 0.8 s dip.
> **Loops:** plants L1 · pays the hook's "why is everyone on the road" implicitly.
> **Rehooks:** `nwsnorman-moore-may20-briefing-a` (real briefing), `nwsnorman-briefing-may30-noon` (forecaster on camera the day before), `docmine/nws-outlook` + `surface-overview-map` as the setup diagram (no text card).
> **Tempo:** medium; info act, banks little.

> **ACT 2 — The storm · 5:01 · 781 words**
> **Job:** touchdown → warning → the width record → rain-wrap and multi-vortex → the tease that sets up the CTA and the turn.
> **In / out:** KTLX re-plot march with timestamps (a2-s1) → width counter comp on the 2.6-mile landing (a2-s2) → rain-wrap/multi-vortex with `kfor-sutton-josefy-up-close` (a2-s3) → a2-s3b ends on "...the most experienced observers alive" → 1.0 s dip → **CTA**.
> **Loops:** plants L2 + cta-hinge.
> **CTA hinge:** tease = last two sentences of `a2-s3b` → CTA → payoff = first sentence of `a3-s1`.
> **Rehooks:** `nwsnorman-elreno-radar-loop-a/b` (real NWS radar), `kfor-sutton-josefy-up-close` (6 s, the storm on air), `docmine/dow-subvortex-path`, `g-width` counter reveal, `wxgov-satellite-loop-elreno`.
> **Tempo:** builds; the width counter is the act's spike; ends on a held breath.

> **ACT 3 — The turn · 4:45 · 723 words**
> **Job:** the payoff — left turn + acceleration, TWISTEX introduced properly, the geometry of the trap, the Cobalt. Emotion restrained; the record speaks.
> **In / out:** hard cut from the CTA out-dip into `docmine/sharp-left-turns` (real NWS path animation) on "At nine minutes past six" → Samaras photos (memorial rule ≤5 s) → Robinson quote glasscard → NWS crash-scene photo (brief) → open sky → 2.5 s shutdown.
> **Loops:** pays cta-hinge · plants + pays L3.
> **Rehooks:** `sharp-left-turns` (payoff clip, REAL), `abc-3-storm-chasers-killed-a7`, `cnn-ethics-of-chasing__0007-0014` (7.4 s), `g-turn` escape-margin diagram, `nwsdoc-cobalt-tumbles` (pending second-frame eyeball), `kfor-sutton-very-close-call-a7`.
> **Tempo:** slow-fast-slow; the act banks the mid-episode emotion, the END banks more.

> **ACT 4 — The exodus + the second disaster · 5:53 · 883 words**
> **Job:** OKC runs (11 days after Moore), the institutional "drive south" story told fairly, the near-miss on I-40 (mother + 17-day-old), then the flood nobody remembers — 13 > 8.
> **In / out:** `koco-10yr-anniversary__27-33` traffic → NWS tweet as document glasscard → AMS study popfig → aerial survey (a4-s4) → night rain (a5-s1) → "thirteen" popfig (a5-s2) → 1.0 s dip.
> **Loops:** pays L1 · plants + pays L4.
> **Rehooks:** **NEW-SOURCE gridlock chopper footage** (see sourcing), `koco-one-year-ago__0004-0010`, `kfor-retrospective-2026__0814-0821`, tweet glasscard, `wxgov-radar-loop-elreno` (training echoes), `night-flood-street-03`, `emergency-lights-rain-02`.
> **Tempo:** two waves (exodus spike, flood spike), stats mid-act per formula.

> **ACT 5 — Why EF3 · 2:56 · 425 words**
> **Job:** resolve the rating fight with the DI method — the one thing no competitor explains.
> **In / out:** RaXPol/NOAA figures (a6-s1) → `g-dimethod` diagram built to narration (a6-s2) → `koco-reshaped-8s` + `lessons-most-dangerous-tornado` for "what changed" (a6-s3) → 1.0 s dip.
> **Loops:** pays L2.
> **Rehooks:** `docmine/ef0-contour-map`, `docmine/inflow-winds-callout`, `g-dimethod` reveal, `koco-reshaped-8s`.
> **Tempo:** explainer pace, one concept per screen.

> **ACT 6 — The reckoning · 2:29 · 393 words**
> **Job:** Henderson, the TWISTEX legacy, the eight and the thirteen — emotion banked HERE.
> **In / out:** empty section road (stock, moving) → Henderson beat (`nwsdoc-henderson-overtaken`, second-frame check owed) → `cnn-samaras-family-interview-a7` → names glasscard one at a time (a7-s3) → 0.8 s dip.
> **Loops:** pays L-ep, L5.
> **Rehooks:** `nwsdoc-henderson-overtaken`, `cnn-samaras-family-interview-a7` (6.5 s), `wikimedia-samaras-car-PDgov` (≤5 s, moving push-in), names glasscard.
> **Tempo:** slow, descending stakes into the close; no recap.

> **ACT 7 — Warning Hour footnote · 0:21 · 53 words** — `a8-s1` unchanged; episode card "Episode 4 — El Reno 2013"; match-cut, end. (The CTA already carried the book; the footnote stays the channel sign-off, no second pitch.)

## Visual plan — video-first, per act (named sources in `media/`)
| Act | Real video (spine) | Stock connective (≤1 per 45 s) | Stills (3–6 s, moving) | Comp |
|---|---|---|---|---|
| A0 | `graded/kfor-sutton-very-close-call-hookcut` 3.9 · `graded/hook-anchor-voice` 4.0 · `graded/twc-bettes-suv-toss-hookcut` 3.5 · KTLX re-plot (radar/, our render) · `nwsnorman-elreno-radar-loop-a` | `supercell-timelapse-02` | AI rain-wrapped wedge (1 variant, 4 s push-in) | — |
| A1 | `dvids/` Moore Guard footage (stills → need the DVIDS mp4s: see sourcing) · `nwsnorman-moore-may20-briefing-a` 8.5 · `nwsnorman-moore-may20-office-broll` 7.5 · `nwsnorman-briefing-may30-noon` 8.5 · `nwsnorman-briefing-may29-a` (trim 8 s) · `docmine/nws-outlook`, `surface-overview-map`, `cape-map`, `shear-map` | `plains-wheat-02`, `dawn-dusk-sky-04` | FEMA Moore stills ×2 (4 s each) | — |
| A2 | KTLX re-plot march ×3 windows · `nwsnorman-elreno-radar-loop-a/b` · `docmine/ktlx-wide-loop`, `storm-relative-velocity`, `satellite-timelapse`, `dow-subvortex-path`, `vortex-horseshoe-updraft` · `graded/kfor-sutton-josefy-up-close__3-9` 6.0 · `wxgov-satellite-loop-elreno` 8.0 · `spc-satellite-tornado-9frame-anim` | `rainwall-pavement-02`, `stormsky-timelapse-03` | NWS storm photos ×2 (PD, 4 s) | **g-width** (2.6 mi vs Manhattan counter) |
| A3 | `docmine/sharp-left-turns` (payoff, first frame after the CTA) · `graded/abc-3-storm-chasers-killed-a7` · `graded/cnn-ethics-of-chasing__0007.15-0014.55` · `graded/kfor-sutton-very-close-call-a7` · `graded/nwsdoc-cobalt-tumbles` (2nd-frame check) · `docmine/clean-radar-loop-i40` | `dashboard-pov-rain-02`, `storm-debris-wind-03` | Samaras portrait (wikimedia PD-gov, ≤5 s) · NWS crash-scene photo (3 s, static-document exception) | **g-turn** (left-turn / escape-margin geometry) |
| A4 | **NEW: 2013 I-35/I-40/I-44 gridlock chopper** (KFOR/KOCO official) · `graded/koco-10yr-anniversary__27-33` · `graded/koco-one-year-ago__0004.25-0010.14` · `graded/kfor-retrospective-2026__0814.97-0821.06` · `wxgov-radar-loop-elreno` · `nwsnorman-elreno-may31-745am-update` · **NEW: OKC flood night footage (KOCO/KFOR official)** | `highway-traffic-rain-04`, `night-flood-street-03`, `emergency-lights-rain-02`, `night-flood-street-01` | NOAA aerial survey (a4-s4, 5 s push) · rainfall map (4 s) | — (tweet + AMS stat as glasscard/popfig, not comps) |
| A5 | `docmine/ef0-contour-map`, `inflow-winds-callout`, `dow-subvortex-path` (callback ≥3 min after A2 use, data-callback) · `graded/koco-reshaped-8s` · `nwsnorman/lessons-most-dangerous-tornado` 8.5 · `graded/kfor-retrospective-2026__1286.67-1293.84` | `supercell-timelapse-05` | RaXPol figure (NOAA PD, 5 s) | **g-dimethod** (radar wind vs damage-indicator) |
| A6 | `graded/nwsdoc-henderson-overtaken` (2nd-frame check) · `graded/cnn-samaras-family-interview-a7` · `graded/kfor-sutton-studio-interview__0122.19-0125.94` · `graded/survivor-broll-1` | `plains-wheat-05` (empty road), `dawn-dusk-sky-02` | `wikimedia-samaras-car-PDgov` (≤5 s) · memorial photo (≤5 s) | — (names as glasscard, one at a time) |
| A7 | `stormsky-timelapse-01` → episode card | — | — | — |
Rules applied: a REAL clip every 45–60 s (broadcast/NWS/PD, not stock); non-PD broadcast pulls 3–4 s narrated-over except owner-gated inserts; no still >6 s; every still moves (push/pan); AI stills ≤4 (hook wedge, multi-vortex, night underpass, empty road) and never static; **banned:** `kfor-10yr-recap.mp4` (provenance-laundering flag), the 9 FLAGGED files in `licence_audit.md`, all chaser/streamer footage.

## Graphics (GRAPHICS CONTRACT + library-first) — 3 comps, each a diagram
| Comp | Concept | Library starting point | Versions |
|---|---|---|---|
| `g-width` | the counter rolls 0.5 → 1 → 2.6 mi over a map plate, then Manhattan's width drops in for scale; single figure on screen | `library/inhouse` numbers-card / `ep2-numbers-card.html` + `ep3-map-route-fit.html` | 3 (counter-over-map / side-by-side bars / overlay ring) |
| `g-turn` | path elbow drawn on the spoken word, 35 → 50 mph, the escape margin closing on Hwy 81 | `ep3-map-route-fit.html` + `ep5-terrain-map.html` | 3 |
| `g-dimethod` | radar velocity column vs damage-indicator column; the violent core over open fields with nothing to break | `ep5-grid-rightrail.html` / `ep2-met-explainer.html` | 2 |
All other on-screen text: `.glasscard` over footage (tweet, Robinson quote, names) and `popfig` date/figure popups (≤3 words). No text-wall cards, no eyebrows, one fact one instance (overlap_check v2).

## Inserts requiring owner confirmation (each gated individually — frames + transcript)
1. Hook: `kfor-sutton-very-close-call-hookcut` (3.9 s), `hook-anchor-voice` (4.0 s), `twc-bettes-suv-toss-hookcut` (3.5 s) — audio featured.
2. `kfor-sutton-josefy-up-close__3-9` (A2, 6 s, audio under narration or featured — owner call).
3. `abc-3-storm-chasers-killed-a7` (A3), `cnn-ethics-of-chasing__0007.15-0014.55` (A3), `cnn-samaras-family-interview-a7` (A6), `koco-reshaped-8s` (A5) — from the 08-03 shortlist (`insert_gate_packet.md`), re-presented with frames.
4. **The CTA** (`assets/cta/paul-storm-ready-v4c.mp4`, 15.1 s at 9:10) — contract element; owner previews it in place in the draft.
5. New-source pulls (gridlock chopper, flood night) — gated once sourced.

## Sourcing (Phase 4) — video-first + owner order 2026-08-30: **30–40 % more clips than the wire needs**
- Slots: ≈25:53 at a real clip every 45–60 s ≈ 30 real-clip windows + ~45 connective windows. Pool target: **≥42 distinct usable REAL clips** (30 × 1.4) and ≥60 distinct assets overall, so every beat has a swap and repeat-share stays under the 12 % cap without forcing a cut. Unused extras stay in `media/` with provenance rows, listed in `research/clip_bench.md`.
- **Must-find (no candidate today):** 2013 OKC interstate gridlock (KFOR/KOCO official uploads only — chopper/skycam, 3–4 s pulls); May 31 night flood footage OKC (KOCO/KFOR official; NWS Norman flood photos as fallback); DVIDS Moore Guard VIDEO (only stills salvaged).
- **Radar:** `C:/nexrad-t/render_radar.py` is KSGF/ep1-hardcoded — parameterize (site KTLX, 2013-05-31 22:00–00:59 UTC, El Reno bbox) and render 3 windows (touchdown, width peak 23:19 UTC, the turn). Radar IS the story here (the record was radar-measured).
- **Provenance audit before wiring:** every `broadcast/cuts/graded/*` cut that gets used needs its own derived-asset row (parent, URL, claims class, transcript window) — 44 files on disk, 27 rows mention "graded". Deterministic diff of wired `src=` vs `provenance.csv` before the static suite.
- **AI stills:** ≤4, self-generated (DeAPI keys), motion only, no likenesses. Existing `media/ai/` (10) re-eyeballed; keep at most 4.
- Standing: PD + stock only, nothing paid; chaser/streamer footage NEVER; no disguise; repeats ≥3–4 min apart with `data-callback`.

## Packaging (draft — final at publish)
Title as above. Thumbnail: real NWS/NOAA storm photo or our radar re-plot + "EL RENO 2013" (no AI thumbnail — ep6 lesson). Description: **first URL = https://paulraymond.online** (CTA contract), "📘 The book mentioned at 9:10 — Storm-Ready Home...", courtesy credits (NOAA/NWS/FEMA/DVIDS, KFOR/KOCO/CNN/ABC/TWC), Education metadata. Chapters: A1 1:16 · A2 4:08 · A3 **9:26** (starts on the payoff sentence, not the CTA) · A4 14:13 · A5 20:07 · A6 23:03.

---
