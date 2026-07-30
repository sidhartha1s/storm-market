# DESIGN.md — storm-market editing architecture (owner-settled 2026-07-22)

## Core principle: the TIMELINE is master, narration is one element on it

The "AI-ey" failure mode (owner-named): TTS starts, talks 20 min over b-roll, TTS ends. Rejected.
This channel edits like a human documentary editor: narration blocks, breathing room, inserts,
tempo changes. The model IS the editor; hyperframes is the substrate; code is a thin utility layer.

## Edit script — the episode's source of truth

`episodes/<slug>/edit_script.md`: an ordered list of typed segments, authored (and owner-gated at
design review) before any paid generation:

| Type | Audio | Visual | Notes |
|---|---|---|---|
| `narration` | its own TTS wav | b-roll/stills/graphics cut on word timestamps | text written TTS-safe |
| `hold` | ambience/music bed only — NO voice | one clip just sits, 3-10s | the breathing room; use after emotional payoffs, before act turns |
| `insert` | the clip's OWN audio | interview / TV news / radio / 911 call | OWNER CONFIRMS every insert before it enters a render |
| `graphic` | optional VO | radar loop / map / timeline animation | self-made from NEXRAD/data = zero claim risk |

## Audio rules (hard)

- Every sourced clip is **muted by default**. Exactly one exception: `insert` segments, where the
  clip's audio IS the content.
- **Every `insert` goes to the owner before it enters any render**: frames + ~10-word transcript
  + source link, one message, wait for yes/no. No exceptions, no batching-through.
- Narration is TTS'd **per segment** (separate wavs). Per-segment atempo is allowed (0.93–1.08)
  as an editorial choice — segments are independent files, so this is NOT the banned whole-track
  stretch. Owner ear-check before ship covers it.
- Ambience/music beds: PD/licensed only, ducked under narration, audible in holds.

## Placement — LLM judgment, native hyperframes timing, no engine

1. TTS per narration segment -> wav + duration; faster-whisper -> per-segment words.json.
2. The editing agent reads words.json + the clip inventory and authors the composition directly:
   `<video>/<img>/<audio>` elements with `data-start`/`data-duration` in `index.html`.
   Cut points = word timestamps read by the model, chosen editorially. No placement.mjs port.
3. Deterministic checks stay tiny: `scripts/lint_timeline.py` (~30 lines) — every referenced file
   exists, every element's window inside composition duration, narration wavs don't overlap
   inserts' audio. Everything judgment-shaped stays with the model.

## Sourcing — agent-executed, owner never downloads

Per beat: agent pulls 2-3 candidates, extracts frames, vision-checks, picks. Tools on box:
- archive.org advancedsearch API + direct download (curl/spider) — news reels, local TV, PD film
- FEMA/NOAA/NWS/USGS media pages — direct or playwright-cli
- yt-dlp — government YouTube channels (NWS briefings, FEMA), 911/broadcast audio compilations
- stock-fetch CLI (Pexels/Pixabay keys in ~/.claude/.env) — generic storm/sky/town b-roll
- NEXRAD Level-II archive (AWS open data, free) — data for OUR radar animations
- DeAPI stills + LTX clips (keys in ./.env) — AI dramatization gaps
License check per item; storm-chaser footage NEVER without license; news-network footage
sparingly/short/narrated-over (claims budgeted, segments must survive being claimed).

### Cold-open hook contract (owner-rated, ep2 rebuild — 2026-07-27)
The first 25-30s decide the video. Owner rated ep2's first hook 0.6/10 and the rebuilt one
shipped; these are the standing requirements for every episode's cold open:
- **An intelligible, high-stakes ANCHOR line starts by ~2.5s** — a real broadcast/dispatch
  voice saying something a viewer cannot skip (ep2: Spann's live "tornado emergency"). Not
  ambience, not music, not a fragment.
- **Date/place title card inside the first second** (viewer must know where/when instantly).
- **Every cut lands ON an audio event** (a line ends, a roar starts, a siren swells) — never
  cut mid-sentence, never let commentary "just start" and get cut off.
- **A sonic spine runs the whole hook** (ep2: siren — fade in from black, duck under the
  anchor voice, swell at impact, die into the void). No silent clips, no dead air.
- **Inserts end on their complete emotional statement** — trim orphan tails ruthlessly
  ("we knew something was coming." — stop. Nothing after).
- **End the hook with a 2-3s VOID (black + fading spine) before the narrator enters** — the
  contrast is the hook's punctuation.
- Few clips, each earning its slot (ep2: warning → impact → dispatch → void). More clips ≠
  more captivating; undifferentiated montage is what scored 0.6.

### Broadcast-clip rehook cadence (owner order 2026-07-26)
Core audience is 40–70+ — they watched these events on live TV; real broadcast/news/PD/survivor
clips are the nostalgia rehook, stock footage only fills between them. **A real clip lands every
45–60s (or as the beat needs), never long stretches of pure stock.** Network news: 3–4s max per
use, narrated-over, courtesy credit in description — credit manages goodwill, it does NOT remove
claim risk, and it never substitutes for a license. **Claims-vs-strikes distinction (Oldshue
ruling): network/TV material draws Content ID revenue claims (budgeted, survivable); independent
chaser/streamer footage draws manual copyright strikes (channel-fatal) — the NEVER-without-license
rule covers streamers, not just "storm chasers" by job title. Disguising a source (grain, crops,
short cuts) to dodge detection is prohibited — safety comes from structural immunity, not
obfuscation.**

## Composition authoring rules

- Animations JS/WAAPI only — CSS @keyframes disables fast-capture (measured 2026-07-21).
- Render: `scripts\render.cmd <slug> <draft|full>` — full recipe (flags, env vars, `--workers 3`
  pin) baked in; see repo CLAUDE.md step 5. Never hand-type render commands.
- Each episode's index.html is authored fresh (agent-as-editor). Reusable CSS snippets may
  accumulate in `assets/styles/` but NO scene templates — template-ification is the failure mode
  this design exists to avoid.
- **Exit animations end fully gone (owner review 2026-07-26):** every panel/graphic exit tween
  finishes at `autoAlpha:0` AND overshoots any slide (a 660px slide on an 820px panel left a
  stuck sliver for ~1s). Verify each sub-comp with a snapshot at host-window-end − 0.5s.
- Text-over-media always gets a dark backing chip; panel gradients use `box-sizing:border-box`
  with text inside the solid zone.
- **AI-first, code-second (owner directive 2026-07-26, from 6-channel experience):** scripts
  exist for deterministic checks (lint) ONLY. Pacing, grading, clip choice, placement, SFX are
  per-case editor judgment — never encode editorial baselines as enforcement, never constrain
  the editor with code before it has seen the specific problem.
- **Render QC density:** eyeball ≈ 1 frame / 15-20s of runtime on every render (dense sweep or
  `hyperframes check` + snapshot grid), plus targeted frames at every region changed since the
  last render. 18 frames on a 28-min cut is not a review (owner, ep2 v1).

## Content ID / claims protocol (owner-settled 2026-07-22)

Content ID cannot be scanned offline — the protocol is layered:
1. **Structural immunity**: PD / stock / self-made / AI assets are un-claimable by construction.
   Only `insert` segments carry any risk.
2. **Provenance ledger**: every sourced file gets a row in `episodes/<slug>/media/provenance.csv`
   (file, source_url, license, fetched date) — claims become instantly traceable/disputable.
3. **Pre-publish check**: upload **private/unlisted** first; YouTube's Studio "Checks" step runs
   Content ID before publish. Wait for Checks to pass (+ a few hours soak — matches can lag),
   swap any claimed segment while still private, THEN flip public. Never publish blind.

## Look: grain layer (owner order 2026-07-22)

Every clip renders under a unified film layer: animated grain (SVG turbulence or canvas noise,
JS-driven — never CSS @keyframes), subtle vignette, occasional drifting dust specks. Purpose:
one filmic look that also hides stock/archive/AI seams. Reusable snippet `assets/styles/grain.js`
— a snippet, not a scene template.

## Music (owner order 2026-07-22)

Tense/curious instrumental bed per episode — generate via DeAPI ACE music when available
(keys in ./.env), else PD/CC0 fallback (attribution logged in provenance). Ducked under
narration (~-14dB), rises during holds. Bed choice is an editorial call, owner ear-checks at
preview.

## Character sub-arcs (owner-settled 2026-07-22 — include them)

The hit videos' vignettes about real people ARE the banked emotional payoff + net-info-gain.
**Memorial portrait dwell (owner 2026-07-22): a real person's face stays on screen briefly —
~4-5s max, once — then cut to symbolic/context imagery. Never linger on a victim's face.**
Rules: real, named, publicly documented people only; verified quotes/facts (NWS service
assessments, news archives, memorials); respectful framing — narrate the record, never
dramatize beyond it; NO fabricated composites; no real-person likeness in generated imagery.

## Beat bands (measured from teardowns; editor agent decides each rotation)

hook cuts 2-3s · body 4-8s · holds 3-10s · inserts 5-15s. The editing agent picks every cut
point from that segment's words.json (cut on the word being spoken). Lint enforces only hard
floors/ceilings; taste stays with the model.

## Cadence + sync rules (owner review, ep1 v1 — 2026-07-22)

- **Reason every hold**: any shot >8s carries a written justification in the edit script
  ("lets the beat land" is valid; "clip was that long" is not). Vary rhythm — 1.5s stingers
  exist for a reason.
- **No visual repeats** in an episode. One reuse allowed only as intentional callback:
  different crop/grade, >5 min apart, flagged with `data-callback="reason"` on the element
  (lint-enforced; max 2 uses; last 90s = summary zone, exempt — owner OK'd recap reuse).
- **No SUBJECT repeats either (ep1 v2 RCA)**: two different files of the same visual subject
  (two night-lamp-rain shots, two town aerials of the same look) read as a repeat to the
  viewer. Dedup by what the FRAME shows, not the filename. When authoring, group the shot
  list by subject family (night-rain, town-aerial, siren, rubble...) and use each family
  ≤2 non-adjacent times per act stretch.
- **Sync rule**: the frame must not contradict the narration — named store, time-of-day,
  burned-in timestamps. Match the visual or use a neutral one.
- **Burned-in radar/satellite timestamps (owner order 2026-07-26): map to the narration or
  crop/cut them out of frame** — cropping is a legitimate alternative to honest-labeling when
  the clock itself isn't the story. Watch UTC-vs-local (NEXRAD burns UTC). Grain filter over
  archive graphics as needed to unify the look.
- **Graphics never idle — graphics are SEQUENCES, not posters (owner, ep1 v3 planning).**
  The clock is INFORMATION, not motion: something the viewer didn't know yet must land every
  2-3s (a label, a number, the polygon, an annotation, a state change). Motion without new
  information is an animated still. Reveal every element ON its spoken word; text cards build
  line-by-line, never all-at-once; a finished graphic exits, it does not sit.
- **Mandatory self-audit before render (owner order 2026-07-23): after authoring, re-walk every
  graphic/text/quote element as a viewer** — for each one ask: landing, idling, or minor fix?
  Table the verdicts (the "is it sitting for the egg to hatch" pass). Same pass re-checks clip
  pacing. This is an AI-judgment step — never enforced by script.
- **Cut-pacing baselines (guidance for the editor's reasoning, NOT code-enforced):** stills
  4-7s · video clips 8-12s (motion earns time) · hooks 2-4s · graphics for as long as they
  keep delivering new information. Deviate whenever the beat demands it — reason per shot.
- **Naming: one asset = one exact filename, cited by filename always** — never prose aliases
  ("cupcake renamed fruit-cake" ban). Different stock files of similar subjects are legitimate
  different shots; the sin is re-showing ONE file under different references. Edit script
  carries a shot ledger: filename → subject-family → uses.
- **Numbers**: no eyebrow pre-reveal; counters roll fast then slow dramatically into the final
  figure; secondary stats appear after the landing.
- **Lower-third sub-lines**: high contrast or backing bar — no dark italic on busy ground.
- **Outro**: match-cut the channel title to the closing line; card does not sit.

## Editing grammar (seed — grows via LEARNINGS.md)

- Hook: cold-open insert (911 audio / broadcast) or present-tense stat over motion. ≤15s to thesis.
- After an emotional payoff: hold 2-4s, ambience up, then cut hard to the next act.
- **Chapter blackout (documentary breath — ep1/ep2 device, MANDATORY ep4+; owner order
  2026-07-31):** between acts, and on a key beat, cut to a full 2-3s BLACK. It resets the eye and
  is what makes ep1/ep2 read like a documentary. ep1/ep2 place a plain black section on the
  picture track:
  `<section class="clip blackout" data-start="X" data-duration="2.4"–"3.0" data-track-index="1"></section>`
  with `.blackout { position:absolute; inset:0; background:#000; }`. Cut TO black hard (no fade),
  hold 2-3s in silence or low ambience, cut OUT to the next act. **ep3 dropped this entirely** —
  its `build_ep3.py` generator never emitted blackout sections. A regression, not a style choice:
  the next episode's builder MUST insert act-boundary blackouts (a `black`/`blackout` beat kind in
  the shot table, or hand-placed). ep3 stays as shipped; do not re-render it for this.
- Never two inserts back-to-back; narration re-anchors between them.
- Stats mid-video, emotion banked at the end (teardown-verified pattern).
- Micro-loops every 30-45s, phrasing varied; no recap; CTA short.
- **Signature closing footnote (owner order 2026-07-22, channel = The Warning Hour):** every
  episode ends on a short, punchy, WARM and positive beat — preparedness, never fearmongering —
  landing on the channel name. Canonical shape (tweak per episode, keep the cadence):
  "Disasters don't ask permission. But they do send warnings. Learn what yours sounds like —
  so when it comes, you already know what to do. This was The Warning Hour." It plays over the
  title card; it IS the outro (still no recap, no content summary).

---
# GRAPHICS CONTRACT (binding, from ep2 — owner order 2026-07-29 after ep3 v2 scored 2/10)
**Source of truth = `episodes/ep2-2011-super-outbreak/compositions/*.html`. READ THEM before
authoring any graphic. Do not infer this language from a previous episode's index.html.**

## 1. Authoring form — sub-composition files, always
One graphic = one file `episodes/<slug>/compositions/g-<name>.html` with `<template>`, own
`<style>`, own `#root[data-composition-id]`, own paused GSAP timeline registered to
`window.__timelines["g-<name>"]`. Mounted from index.html as:
`<div id="host-x" data-composition-id="g-x" data-composition-src="compositions/g-x.html"
 data-start data-duration data-track-index data-width="1920" data-height="1080"></div>`
NEVER build graphic DOM from JS `innerHTML` strings inside index.html — it kills the per-graphic
design pass and makes code QC impossible. (ep3 v2 regression.)

## 2. Panel anatomy — the stat card (ep2 g-stat-philly)
Full-height right panel, NOT a floating box: `right:0; top:0; bottom:0; width:820px;
background:linear-gradient(270deg, rgba(6,9,13,0.94) 72%, rgba(6,9,13,0));
padding:90px 70px 0 170px`. Content order, top to bottom:
eyebrow → place name → serif-italic sub → stamp → labelled rows → counter → counter label.

## 3. Type scale (literal, per role)
| role | font | size | color | tracking |
|---|---|---|---|---|
| eyebrow | Arial 700 | 22px | #93a3b2 | 6px |
| place/headline | Arial Black | 52px | #f2f5f8 | — |
| serif sub | Georgia italic | 26px | #d8a13a | — |
| stamp | Arial Black on #8e2020 | 96px | #fff | 2px |
| row value | Arial 700 | 30px | #dfe7ee | 1px |
| row label | Arial 700 | 19px | #93a3b2 | 4px |
| counter | Courier New 700 | 84px | #e74c3c | — |
| counter label | Arial 700 | 20px | #c8d3e0 | 6px |
| section header | Arial 700 | 26px | #93a3b2 | 8px |
Three tiers must be visible in every graphic: something ≥52px, something 26–30px, something ≤22px.
Uniform small text = automatic fail.

## 4. Palette semantics (fixed meaning, ≤10 colors per episode)
`#8e2020` stamp block · `#c0392b`/`#e74c3c` death & danger · `#d8a13a`/`#e8c56a` serif subs,
values, warm air · `#5a768f`/`#7fb2e5` cold air, cool diagram parts · `#93a3b2` labels/eyebrows ·
`#f2f5f8` headlines · `#dfe7ee` body · bg `radial-gradient(ellipse at 50% 45%, #0b1016, #030507 78%)`.
Never a flat `#000`/`#0a1017` fill behind a graphic — always the textured radial.

## 5. Motion vocabulary (the thing ep3 v2 lacked)
- panel enters `fromTo(x:660 → 0, 0.7, power3.out)`, exits `to(x:980, autoAlpha:0, 0.6, power3.in)`
- stamp slams `fromTo(scale:2.6, autoAlpha:0 → scale:1, 0.35, power4.in)`
- rows `fromTo(autoAlpha:0, y:24 → 0, 0.4)`, staggered ~0.6s apart
- bars/arrows/gauges grow by `scaleX 0→1` with `transformOrigin:"left center"`, 0.5s
- counters `to({v}, power4.out / power3.out)` with `onUpdate` writing `textContent`
- one CONTINUOUS motion per long graphic (ep2: `rotation:200, duration:26, ease:"none"` on the
  spin column; `scale+rotation` over 12s on the supercell). A graphic longer than ~20s MUST carry
  a continuous element, not just discrete reveals.
Fade-only graphics are a fail. Target ≥1 scale/slide tween per 2 reveals.
- **Panel exit TIMING (owner, ep3 v4→v5, 2026-07-31):** the slide-right exit above is REQUIRED —
  a panel slides out `x:980, autoAlpha:0`, it does not vanish. But time it to the END of the
  panel's window: anchor the exit to the comp's last ~0.6s AND keep the comp duration ≥ its host
  window, so the panel never leaves while its beat is still being spoken. ep3 v4's exit fired
  early (the host window was extended past the comp by `close_picture_gaps`, so the exit landed
  mid-beat); ep3 v5 over-corrected by DELETING the exit, so panels just disappear. Neither is the
  contract — keep the slide-right exit, land it on the cut. (ep3 stays as shipped; ep4+ restore
  the timed exit.)

## 6. Beat cadence + duration
Beat = a visible change. Max 3s of no change inside any graphic window; ≤2.5s in the first 10s.
Long graphics are allowed (ep2 g-met = 81s) ONLY with a continuous motion element plus
word-synced beats. Author beats against `audio/<seg>.words.json` and leave the spoken timestamp
in a code comment, ep2-style: `/* FUEL @4.74; 1,000 @16.6; 2,000 @20.8 */`.

## 7. Explain with a diagram, never a label on a shape
ep2 built real widgets: a CAPE gauge with gradient fill, a layered lid cross-section, staggered
shear arrows + rotating column, a conic-gradient supercell. A cone captioned "tornado" or a line
captioned "warm air" conveys nothing — build the mechanism, animate it, let the label name it.

## 8. Hard gate — code QC, not frame QC
`node scripts/graphics_qc.mjs .` (from the episode dir) must exit 0 before any render. Frame renders
CONFIRM; they never DISCOVER. Sampling 105 frames of a 35-min cut inspects 0.3% of the runtime and
cannot see text collision, empty containers, or crop errors — those are `getBoundingClientRect`
assertions in the DOM. (ep3 v2 root cause.)
