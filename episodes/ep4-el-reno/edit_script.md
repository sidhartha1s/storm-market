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
> **Rehooks:** `sharp-left-turns` (payoff clip, REAL), `abc-3-storm-chasers-killed-a7`, `cnn-ethics-of-chasing__0007.15-0014.55` (7.4 s), `g-turn` escape-margin diagram, `nwsdoc-cobalt-tumbles` (pending second-frame eyeball), `kfor-sutton-very-close-call-a7`.
> **Tempo:** slow-fast-slow; the act banks the mid-episode emotion, the END banks more.

> **ACT 4 — The exodus + the second disaster · 5:53 · 883 words**
> **Job:** OKC runs (11 days after Moore), the institutional "drive south" story told fairly, the near-miss on I-40 (mother + 17-day-old), then the flood nobody remembers — 13 > 8.
> **In / out:** `koco-10yr-anniversary__27-33` traffic → NWS tweet as document glasscard → AMS study popfig → aerial survey (a4-s4) → night rain (a5-s1) → "thirteen" popfig (a5-s2) → 1.0 s dip.
> **Loops:** pays L1 · plants + pays L4.
> **Rehooks:** **NEW-SOURCE gridlock chopper footage** (see sourcing), `koco-one-year-ago__0004.25-0010.14`, `kfor-retrospective-2026__0814.97-0821.06`, tweet glasscard, `wxgov-radar-loop-elreno` (training echoes), `night-flood-street-03`, `emergency-lights-rain-02`.
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

# SCRIPT — narration verbatim from DESIGN v2 (wavs in audio/, no re-TTS); 27 kept segments, 6 CUT segments listed at the end for the record

### A0-S2 — narration
> The widest tornado ever measured on this planet is on the ground right now, and almost nobody in its path can see it. It is wrapped in curtains of rain, and from the highway it looks like nothing more than a gray wall of water sliding across the fields. But inside that wall, instruments are recording winds close to three hundred miles per hour. It is growing faster than anyone has ever seen a tornado grow, and it is about to change direction without warning.

### A0-S3 — narration
> By the time the sun sets on the thirty first of May, twenty thirteen, this storm will hold a record no tornado has ever held. Two point six miles wide, edge to edge. And yet the official rating in the record books says EF three, a number that still starts arguments today. Because this tornado did something no tornado had ever done before. It killed the most careful storm chasers in the world. The men who understood this storm best were the ones it caught. This is the story of El Reno.

### A1-S1 — narration
> To understand what happened on that Friday evening, you have to go back eleven days. On the twentieth of May, an EF five tornado carved through the suburbs of Moore, Oklahoma, on the south side of Oklahoma City. It stayed on the ground for seventeen miles, and its winds passed two hundred miles per hour. It struck two elementary schools with children inside. Twenty four people died, including seven third graders at Plaza Towers Elementary. The state had barely finished counting its dead when the forecasts began pointing at the very same metro area again. So when Oklahomans looked at the sky on May thirty first, they were not looking with ordinary caution. They were looking with fresh grief, and that grief was about to shape every decision of the evening. Remember that, because it explains what a million people did next.

### A1-S1b — narration
> And Moore was not even the whole story of that May. The twentieth was the second major severe weather outbreak of the month, and the thirty first would be the third. For nearly two weeks, Oklahomans had lived inside a loop of watches, warnings, sirens, and funerals. Schools had drilled. Families had rehearsed. Hardware stores had sold out of shelter supplies. By that last Friday of the month, central Oklahoma was not a population that needed convincing that tornadoes kill. It was a population primed to act, instantly, on the next warning it heard. In most disasters, that kind of readiness saves lives. On this particular evening, it was about to do something stranger. Because what a frightened city does with a warning depends entirely on what it has been told to do. And the instructions Oklahoma City had absorbed that month pointed in a direction no textbook recommends.

### A1-S2 — narration
> Friday morning, the Storm Prediction Center in Norman drew a risk area over central Oklahoma and did not hedge. Moisture was streaming north from the Gulf, thick and unstable, the kind of air that feels like a wet blanket by mid afternoon. A dryline, the sharp boundary where desert air from the west meets that Gulf moisture, was set up just west of the metro. And overhead, the winds turned and strengthened with height, ready to spin anything that grew tall enough. Forecasters in Norman had watched this same loading of the dice eleven days earlier. Every ingredient said the same thing. If a storm formed on that dryline in the early evening, it would rotate, and it would be violent. By late afternoon, towers of cloud were already boiling up west of El Reno, and hundreds of storm chasers were already parked on the section roads, waiting.

### A2-S1 — narration
> At three minutes past six in the evening, a funnel touched down in the fields west of El Reno. Five minutes later, at six oh eight, the tornado warning went out. At first, the storm behaved exactly the way the textbooks said it would. It moved southeast at twenty to twenty five miles per hour, chewing through empty farmland, damaging a few rural homes at EF zero and EF one strength. Slow, visible from a distance, and predictable. Which is why, within minutes, it became one of the most observed tornadoes in history. Research radars, television helicopters, and hundreds of chase vehicles were all watching the same storm at the same time. No tornado had ever been studied this closely while it happened. And no tornado has ever punished its observers the way this one was about to.

### A2-S1b — narration
> Among the watchers were two machines that make this story possible. Parked on the road grid were mobile research radars, radar dishes mounted on trucks. They are built to drive up close to a storm and scan it every few seconds instead of every few minutes. One of them, a rapid scan unit from the University of Oklahoma called RaXPol, rolled into position east of the developing tornado and locked on. The Doppler on Wheels trucks were out there too. Fixed radars, the big domes that feed the warnings on your television, sit tens of miles away and see a storm in slices, high above the ground. A truck parked two miles out sees the storm's actual ground floor, where people live and die, and it sees it almost continuously. Everything you are about to hear about this tornado's true size and true winds exists because those trucks were pointed at it at the right moment. Hold onto that thought, because at the end of this story, the radar and the record books are going to tell two different truths about the same storm.

### A2-S2 — graphic with VO
> Watch what happens in the sixteen minutes after touchdown. At six oh three, the tornado is a few hundred yards across. Ordinary. Then the storm begins pulling in air faster than anyone watching has ever seen. Half a mile wide. Then a full mile. Then two. At six nineteen in the evening, south of El Reno, the circulation reaches two point six miles across. Edge to edge, that is wider than the island of Manhattan. If you stood at one edge, the far side would be beyond the horizon of most people's eyesight, even in clear air. The old record, set in Nebraska nine years earlier, was gone. No tornado in recorded history had ever been this wide. And here is the part that mattered most to the people underneath it. A tornado that wide does not look like a tornado at all.

### A2-S3 — narration
> It looked like rain. The circulation was buried inside what chasers call a rain wrapped core, sheets of water pulled around the vortex like a curtain. From the roads south and east, there was no funnel to see, just a dark gray wall a few miles wide, and walls of water do not look dangerous. Inside that curtain, the radar could see what eyes could not. This was not one vortex. It was a family of them, smaller tornadoes inside the main circulation, orbiting it like moons, each one packing winds far stronger than the parent storm. The radar even caught a separate satellite tornado circling into its northwest flank, and, on the far side, something genuinely rare. A second tornado spinning the opposite direction, clockwise, born from the same storm. The atmosphere was doing things that evening that scientists are still writing papers about. And then, at nine minutes past six, everything the people watching it knew stopped being true.

### A2-S3b — narration
> The warning system, to its credit, kept pace on paper. The first tornado warning at six oh eight was followed by stronger ones at six twenty eight and six fifty seven. The radar was showing the circulation multiply into that family of vortices. The information existed, and it was moving. But a warning describes a storm as it is, and this storm was rewriting itself faster than any bulletin could travel. A driver who heard the six oh eight warning pictured a tornado a few hundred yards wide, moving southeast, away from them, at highway speed minus half. Ten minutes later that picture was wrong in every detail that mattered. Wrong size, wrong direction, wrong speed. Out on the wet section roads west of Highway Eighty One, that gap between the pictured storm and the real one was about to close. And it was going to close on some of the most experienced observers alive.

### A3-S1 — narration
> At nine minutes past six, the tornado did something that rewrote every escape plan on Highway Eighty One. It turned hard to the left, and as it turned, it accelerated. The federal report is precise about this moment. Forward speed climbed from roughly thirty five miles per hour to more than fifty, and the inflow winds made driving away from it difficult. Every chaser on that road grid had built their position around a storm moving southeast at twenty five miles per hour. That storm no longer existed. In its place was something wider than their escape margin, faster than their vehicles on wet section roads, and completely hidden in rain. The mathematics of every escape route on that grid had just been rewritten, and nobody's map had updated yet. For most of the chasers, the mistake cost them a story they would tell for the rest of their lives. For four of them, it cost everything.

### A3-S1b — narration
> To understand why a faster, wider storm was a death sentence rather than an inconvenience, you have to picture the roads. Western Canadian County is a grid of section roads, gravel and dirt lines drawn a mile apart across the farmland. By evening, the rain had turned the dirt ones to grease. The paved escape routes were few, and Highway Eighty One, running north to south through the storm's new path, was the spine most of them fed into. A chase position that assumed a slow storm left you with options, turn south, drop east, wait it out. A storm suddenly two and a half miles wide, moving fifty miles per hour, swallowed those options whole. The math is brutal and simple. Picture the circulation's edge a mile away, expanding toward you faster than your car can safely move on wet gravel. The road you are on has already decided your next few minutes. Dozens of chasers that evening escaped by margins they still talk about. Vehicles were damaged, windows blown out, cars shoved off roads. The evening produced more close calls among experienced chasers than any storm before or since.

### A3-S2 — narration
> Tim Samaras was not a thrill seeker. He was an engineer, and in the storm chasing world he was famous for the opposite of recklessness. He built instrument probes designed to survive a direct hit from a tornado core, placed them in the storm's path, and got out. His pressure measurements inside a tornado still stand among the most valuable ever taken. National Geographic had funded his field work for years. Colleagues described him as the careful one, the man who preached margins and turned back when the margins closed. That evening his team, called TWISTEX, was three people. Tim, fifty five years old. His son Paul, twenty four, behind the camera. And meteorologist Carl Young, forty five, driving. Here is a detail almost nobody mentions. The federal review of that day records that none of the people chasing were operating under a government research project at that moment. The safety structure of an official mission was not there. It was three men, a small white Chevrolet Cobalt, and a storm about to break every rule they had built their careers on.

### A3-S3 — narration
> Just ahead of them on the same road was another veteran chaser, Dan Robinson. His account, quoted in the federal report, matters, because it kills a myth. People assume the chasers died because of chaser traffic, hundreds of cars clogging the escape roads. Robinson is explicit. At his position, other than the TWISTEX car behind him and one parked pickup, the road was empty. Chaser traffic was a non factor, his words. The report reaches the same conclusion. What caught them was the storm itself. The circulation widened so fast, and turned so sharply, that a road which had been outside the tornado became inside it in under a minute. Robinson's car took the edge and survived. The Cobalt, seconds behind, took a sub vortex, one of those embedded cores the radar had been tracking. Its winds were measured at more than two hundred and fifty miles per hour. Tim Samaras was found still in the car, his seat belt fastened. He had done everything right, the way he always did. Paul and Carl were carried from the vehicle by the wind. The careful one, and the storm that finally out ran care.

### A4-S1 — narration
> While that was happening in the fields, something very different was going wrong twenty five miles east, in Oklahoma City. It was a little after six on a Friday evening. Rush hour. And the city was eleven days removed from watching an EF five bury schoolchildren in Moore. As the warnings spread, television coverage told people in the storm's path to get south, to get out of its way. And this time, people did not shelter. They ran. Tens of thousands of them got into cars, all at once, onto Interstate thirty five, Interstate forty, Interstate forty four. Within the hour, the highways south of the city had locked into a standstill, bumper to bumper for miles. Above them, a tornado warned supercell was bearing down. A parking lot of families, sitting in the open, in the path of a storm that had just killed four professional storm chasers. It is remembered as one of the most dangerous traffic jams in American history.

### A4-S2 — narration
> The television advice that evening has a name attached to it, a local chief meteorologist who twice told viewers without underground shelter to drive south. He was blamed for the gridlock for years afterward. But the record tells a messier story. At one o'clock that afternoon, hours before the tornado formed, the National Weather Service's own Norman office posted safety guidance. It began, if you choose to flee in your car, plan for traffic jams, hail, heavy rain and flooding. The government's own messaging that day allowed for fleeing by car. Meanwhile a senior government scientist argued the opposite, that telling people they would not survive above ground was dangerous. Read that again. In the same city, on the same afternoon, the official guidance pointed in two directions at once. The federal review of the event does not pin the exodus on one broadcaster. It finds that the message system itself, government and media together, had never agreed on what a terrified city should actually do. A million people filled that silence with the Moore tornado, and chose their cars.

### A4-S3 — graphic with VO
> Years later, researchers studied vehicle movement across six American metro areas hit by tornado warnings, and they found nothing anywhere that compared to this evening. It stands as the largest tornado evacuation ever measured in an American city. Their conclusion echoes an older disaster. After Hurricane Katrina drowned New Orleans, the next storm sent Houston fleeing, and the evacuation itself killed dozens. Fear from the last disaster drives behavior in the next one. Moore was eleven days old. Oklahoma City ran.

### A4-S4 — narration
> Now put the two halves of this evening together, because they nearly met. The tornado, still enormous, was tracking east toward the exact interstates those families were parked on. It crossed Interstate forty near Banner Road as it weakened. Even then, it found the one cluster of buildings on its path, a group of manufactured homes just south of the interstate. The damage survey there recorded the densest destruction of the entire track. Among the eight people killed by this tornado, every single one was in a vehicle. A father driving home. A young woman and her infant daughter, seventeen days old, parked along Interstate forty. The storm chasers on the section roads. Eight lives, all of them on wheels. And the terrible truth of the evening is this. If the tornado had held its record size and strength for another twenty minutes, it would have arrived on a jammed interstate holding thousands of stationary cars. Oklahoma came within a margin of minutes of the deadliest tornado disaster in its history. What actually happened next killed more people than the tornado did, and almost nobody outside Oklahoma remembers it.

### A5-S1 — narration
> The supercell that built the widest tornado ever measured did not stop working when the funnel lifted. Storms kept forming and passing over the same ground, hour after hour into the night. Meteorologists call the pattern training, like railcars rolling over one crossing. It wrung the Gulf's moisture out over the city at rates the drains were never built for. And here the evening's tragedies began to feed each other. All over Oklahoma City, people had taken shelter from the tornado the only way they could. Some had climbed into storm drains and drainage ditches, the lowest ground available, exactly where you hide from wind, and exactly where you die in water. Others were still out on the flooded roads, in the cars they had fled in. As the tornado threat faded from the news coverage, the water was already rising in the dark.

### A5-S2 — narration
> Thirteen people drowned that night, twelve of them in Oklahoma City. More than the tornado killed. It remains the deadliest flood event in the city's history, and the deadliest flash flood anywhere in that forecast region since nineteen thirty four. The federal review afterward made a finding that should sting every newsroom. The public said the broadcast coverage that evening was about tornadoes, almost entirely. The flood warnings were issued, and they were drowned out by the louder story. A city that had just run from the wind walked into the water. When people tell the story of El Reno, they count eight dead. The full number for that night is twenty one, and the larger half of it fell on the disaster nobody was watching.

### A6-S1 — narration
> Months later, the record books closed on a number that still makes people angry. EF three. A tornado two point six miles wide, with radar measured winds near three hundred miles per hour. And it sits in the official database two full steps below the top of the scale. Comment sections have been fighting about it ever since. The engineers who rated it were not confused, and they were not covering anything up. The answer is stranger than the controversy. Officially, the most violent winds of the widest tornado ever recorded never happened, because they never hit anything.

### A6-S2 — graphic with VO
> The Enhanced Fujita scale does not measure wind. It measures what wind does. Survey teams walk the path after the storm, find damaged structures, and work backward. A well built house swept from its foundation implies one wind speed. A snapped power pole implies another. No damage, no evidence, no rating. Now look at this tornado's path. Sixteen miles, almost all of it open farmland. The survey teams catalogued hundreds of damage points, and the worst of them, a handful of rural homes, supported EF three. But the mobile research radar sitting on that storm measured winds above two hundred ninety miles per hour near the ground, in sub vortices that spun across empty fields. Where the radar saw the most violent winds, the surveyors found nothing to inspect. Grass does not testify. Across the whole path, the radar's numbers ran ten to thirty percent above what the damage implied. The scale worked exactly as designed. It is just designed to measure a tornado by what it destroys, and this one spent its fury on emptiness. The record width stands, measured by radar. The violence stays officially invisible.

### A6-S3 — narration
> El Reno changed storm chasing the way a funeral changes a family. The community had spent two decades getting closer and closer to tornadoes, and the cost had somehow stayed at zero. Then the storm that killed the careful one proved that the margins everyone trusted could vanish in sixty seconds. The National Weather Service office in Norman built an entire retrospective around the lessons, and the lessons were blunt. A tornado can be wider than your escape plan. It can be invisible inside rain. It can turn and accelerate faster than a car on a wet section road. In the years since, the culture has shifted, more distance, more respect for rain wrapped storms, more reliance on radar over eyesight. The storm rewrote the rules by demonstrating, on the community's own cameras, that the old rules were wishes.

### A7-S1 — narration
> There is a fourth name among the chasers who died that evening, and it almost never gets told. Richard Henderson was not famous. He was a truck driver from the El Reno area who loved storms. A hobbyist who decided, that Friday, to drive out from his own home and watch this one. At five minutes past six, right after the funnel came down, he sent a friend a photo of it from his phone. A gray column over green fields, taken through a windshield. About ten minutes later, on the phone with that same friend, he said he could hear debris hitting his pickup. Then the line went dead. His family believes the tornado pulled him from the truck. He left two young sons. The famous storm that evening took the world's most careful chaser. And it took a man who just wanted to see it, from the roads he had driven his whole life. The storm did not distinguish.

### A7-S2 — narration
> What survives of the TWISTEX team is not the crash site photographs. It is data. Tim Samaras's probes recorded pressure drops inside tornado cores that had never been captured before, numbers that are still cited, still teaching. His measurements are in the textbooks that today's forecasters learned from. Paul's cameras documented storms with an artist's eye. Carl Young's forecasting put the team where the science needed them, hundreds of times, safely, until the one storm that redefined what safely meant. The chasing community still marks the anniversary every May. And when researchers argue for keeping instruments and radars on tornadoes, so that warnings keep getting better, they cite his work. A careful engineer from Colorado who believed the inside of a tornado was worth knowing.

### A7-S3 — narration
> Eight names in the tornado's column. Thirteen in the flood's. Every one of the tornado's dead was in a vehicle, and that is the sentence this storm wrote into history. A car feels like safety because it moves, and this tornado was the proof that moving is not the same as escaping. You cannot outdrive what you cannot see, and you cannot out guess a storm that changes the rules mid game. The people who survived that evening in Oklahoma City were, overwhelmingly, the ones who stayed low, stayed home, and stayed out of the water. The widest tornado ever recorded killed no one in a house.

### A8-S1 — narration
> Disasters don't ask permission. But they do send warnings. Know where you would shelter before the sky ever asks the question, and let the car be your last answer, never your first. Learn what your warning sounds like, so when it comes, you already know what to do. This was The Warning Hour.

## CUT segments (not wired, wavs stay on disk)
- A1-S3 — graphic with VO
- A2-S3c — graphic with VO
- A3-S3b — narration
- A5-S2b — narration
- A6-S2b — narration
- A7-S2b — narration
