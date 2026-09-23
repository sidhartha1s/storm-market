# DESIGN.md — storm-market editing architecture

## Core principle: the TIMELINE is master, narration is one element on it

The "AI-ey" failure mode: TTS starts, talks 20 min over b-roll, TTS ends. Rejected.
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

## Script writing (ep5+)

**Read `references/script-scaling.md` before writing any script** — the retention lattice:
per-minute invariant cadences, 3–6 min self-similar acts, loop-table plant/pay, text-only act
briefs (no JSON/code), 4th-grader language, spice = clarifying footnote not filler. It also
carries the **pre-TTS fact-QC layer** (eyeball pass + verification verdicts; zero open
`[verify]` markers before TTS) and the **insert-transcription rule** (transcribe every insert
in full BEFORE cut selection; cut at the transcript's action/emotion peak).

## Audio rules (hard)

- Every sourced clip is **muted by default**, and "muted" means the `muted` attribute on the `<video>`:
  hyperframes plays any video's track unless the element says otherwise, and `sweep_episode.py` fails a
  `<video>` with neither `muted` nor `data-volume` (El Reno v3 shipped audible stock footage that way).
  Exactly one exception: `insert` segments, where the clip's audio IS the content.
- **Every `insert` goes to the owner before it enters any render**: frames + ~10-word transcript
  + source link, one message, wait for yes/no. No exceptions, no batching-through.
- Narration is TTS'd **per segment** (separate wavs). Tempo is per lane (`config.yaml channel.tempo`,
  applied by `scripts/tts_episode.py`); a per-segment deviation is the owner's call. Owner ear-check before ship covers it.
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

### Cold-open hook contract
The first 25-30s decide the video. Owner rated ep2's first hook 0.6/10 and the rebuilt one
shipped; these are the standing requirements for every episode's cold open:
- **NO black start: frame one is MID-ACTION** — the episode's
  defining shot already moving. High curiosity, high impact from the first frame. The VOID
  below survives only as the hook's END punctuation.
- **The NARRATOR's first line starts at 0:00. No broadcast, radio or archive audio anywhere in
  the hook** (owner 22 Sep 26, replaces the old "anchor line by 2.5 s" rule): archive audio is
  low quality, and a 10/10 narrated hook is worthless if viewers leave before it starts.
  Archive audio belongs inside the acts, as `insert` segments.
- **Date/place title card inside the first second** (viewer must know where/when instantly).
- **Every cut lands ON an audio event** (a line ends, a roar starts, a siren swells) — never
  cut mid-sentence, never let commentary "just start" and get cut off.
- **A sonic spine runs the whole hook** (ep2: siren — fade in from black, duck under the
  narrator, swell at impact, die into the void). No silent clips, no dead air.
- **Inserts end on their complete emotional statement** — trim orphan tails ruthlessly
  ("we knew something was coming." — stop. Nothing after).
- **End the hook with a 1.5s VOID (black + fading spine) before the intro** — the
  contrast is the hook's punctuation (was 2-3s; 1.5s+ anywhere else reads as dead air).
- **Date/place popup (popfig) inside the first second**, sized to clear before the first
  designed graphic arrives.
- Few clips, each earning its slot (ep2: warning → impact → dispatch → void). More clips ≠
  more captivating; undifferentiated montage is what scored 0.6.

### CTA contract (must-keep, every episode from ep4 on)
The ebook CTA (Paul on camera, 15.1s, QR + "first link in the description") is a fixed element of
every episode from ep4 on. File, duration, window and labels live in `config.yaml channel.cta`
(current: `assets/cta/paul-storm-ready-v4c.mp4`, README + transcript beside it) — never a
per-episode copy of the rule, never a hand-edited path. Shape: **hook > CTA > payoff**.
- **Window: the CTA starts inside 30–40% of total runtime** — after the episode has earned it,
  before the first big payoff lands. `sweep_episode.py` fails outside the window (episodes shipped
  before the contract are listed in `channel.cta.exempt` — never extended; `demo-*` dirs print SKIP).
- **Hinge is scripted, not spliced:** the narration segment BEFORE it ends on a tease (an open
  loop planted in the words — "...that gap was about to close, on the most experienced observers
  alive"), the segment AFTER opens with the payoff in its first sentence. The script's loop table
  carries the pair as `cta-hinge` (references/script-scaling.md). No natural tease at 30–40% =
  rewrite the script, not move the CTA.
- **Dips:** 1.0s black in, 1.0s black out (dramatic-punctuation tier). Hard cut into the payoff
  clip after the out-dip; the payoff clip is REAL footage, never a graphic.
- **Audio:** the CTA carries its own VO (`data-volume="1"`); narration is silent under it (lint
  overlap rule); score/SFX bed ducked ≥12 dB or out. Never within 60s of another audio-carrying
  insert (the "never two inserts back-to-back" rule).
- **Not a chapter boundary:** the CTA sits inside the preceding chapter; the next chapter starts
  on the payoff sentence, so chapter-scrubbing lands on the payoff, not the ad.
- **Deliverables:** SRT cue from `data-srt-label`; `metadata.md` description puts
  `channel.cta.first_link` as the FIRST URL (above socials) and carries the ep2-style line
  "📘 The book mentioned at mm:ss — Storm-Ready Home ... https://paulraymond.online".
- **Never** skipped, shortened, moved to the outro, muted, or replaced by a text card. A re-cut of
  the clip is a NEW versioned file + config bump (old file stays: shipped episodes reproduce).
- Wiring (staged episode-relative — `render.cmd` cds into the episode dir, no `../` srcs):
  copy the asset to `media/cta/<file>` (gitignored; sweep md5-checks it against `assets/cta/`), then
  `<video id="ins-cta-paul" src="media/cta/paul-storm-ready-v4c.mp4" data-start="<T>"
  data-duration="15.104" data-track-index="1" data-volume="1" data-srt-label="<channel.cta.srt_label>">`
  with a 1.0s blackout element before and after on the picture track.

### Broadcast-clip rehook cadence
Core audience is 40–70+ — they watched these events on live TV; real broadcast/news/PD/survivor
clips are the nostalgia rehook, stock footage only fills between them. **A real clip lands every
45–60s (or as the beat needs), never long stretches of pure stock.** Network news: transcribe
first, cut at the best moment; up to ~12-15s per pull when narrated over (commentary audio may
be featured, audio mix is a per-cut editor decision), courtesy credit in
description — credit manages goodwill, it does NOT remove
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
  accumulate in `assets/styles/`. **Library-first:** before hand-authoring any graphic, search
  `library/catalog-index.json` (in-house exemplars + triaged official HyperFrames catalog;
  browse: `python3 -m http.server 8765` from `library/` → `/gallery/`) and
  `npx hyperframes catalog --query "<intent>"`. COPY the closest exemplar/snippet/official
  block into the episode and HAND-RETUNE it per beat — the ep2 `g-*.html` method. Building
  from scratch stays allowed with a one-line reason in `edit_script.md`. What remains BANNED
  is unchanged: scripts/generators that emit or alter episode HTML (the tripwire in
  CLAUDE.md). A template is a starting point an agent edits with per-cut judgment, never a
  builder that outputs a finished scene.
- **Exit animations end fully gone:** every panel/graphic exit tween
  finishes at `autoAlpha:0` AND overshoots any slide (a 660px slide on an 820px panel left a
  stuck sliver for ~1s). Verify each sub-comp with a snapshot at host-window-end − 0.5s.
- Text-over-media always sits on the `.glasscard` panel (rgba(10,16,24,.55) + blur 18px +
  1px white@.14 border, radius 28 — see "On-screen text rules" below; `quotecard.glasscard`
  drops the box-shadow); panel gradients use `box-sizing:border-box` with text inside the
  solid zone. Dates/figures use the Abril `popfig` popup (red, text-shadow, ≤3 words, mid-screen)
  — never a colour-block date card.
- **AI-first, code-second (from 6-channel experience):** scripts
  exist for deterministic checks (lint) ONLY. Pacing, grading, clip choice, placement, SFX are
  per-case editor judgment — never encode editorial baselines as enforcement, never constrain
  the editor with code before it has seen the specific problem.
- **Render QC density:** eyeball ≈ 1 frame / 15-20s of runtime on every render (dense sweep or
  `hyperframes check` + snapshot grid), plus targeted frames at every region changed since the
  last render. 18 frames on a 28-min cut is not a review.

### On-screen text rules
- **Zone occupancy.** Screen zones: title (top-left), centre popup, lower-third, RHS panel,
  source credit (a corner). ONE text element per zone per time window. Before placing any text,
  list what occupies every zone during its window — INCLUDING where animated elements travel
  (a chip that pans under a moving ring collides mid-tween). Intentional layering (a label ON a
  map feature) carries `data-overlap-ok="reason"`. `scripts/overlap_check.mjs` enforces it:
  0.5s steps, post-transform bboxes, comp-internal AND comp-vs-card pairs.
- **One fact, one instance.** A date / percentage / number appears ONCE per frame. If the
  graphic already prints "AUG 30", no popup says it again. (Dup-fact check in overlap_check.)
- **No decorative eyebrows.** Kill "AUGUST 2005"-style eyebrows over a big "AUG 25". Functional
  context only — the italic date line inside a glass panel (g-circle pattern) is the approved
  form.
- **Narration order, narration words.** Text reveals land in the order the voice says them and
  use the voice's wording ("SOME HAD NO MONEY", not a rewritten paraphrase). Sync to
  `audio/<seg>.words.json`; never "Yoda" (card-layout order).
- **Any text over footage sits on glass.** `.glasscard` (rgba(10,16,24,.55), blur 18px, 1px
  white@.14 border, radius 28) is the ONE treatment — no bare text on moving footage, no
  mid-beat swap from footage to a dark card for readability.
- **Small text never carries a moment alone (BFMG).** A quote card, a cost list, a headline
  pair = glass card OVER footage. Dark-gradient `c-*dark` fillers are for ≤5s bridges only.

## Content ID / claims protocol

Content ID cannot be scanned offline — the protocol is layered:
1. **Structural immunity**: PD / stock / self-made / AI assets are un-claimable by construction.
   Only `insert` segments carry any risk.
2. **Provenance ledger**: every sourced file gets a row in `episodes/<slug>/media/provenance.csv`
   (file, source_url, license, fetched date) — claims become instantly traceable/disputable.
3. **Pre-publish check**: upload **private/unlisted** first; YouTube's Studio "Checks" step runs
   Content ID before publish. Wait for Checks to pass (+ a few hours soak — matches can lag),
   swap any claimed segment while still private, THEN flip public. Never publish blind.

## Look: grain layer

Every clip renders under a unified film layer: animated grain (SVG turbulence or canvas noise,
JS-driven — never CSS @keyframes), subtle vignette, occasional drifting dust specks. Purpose:
one filmic look that also hides stock/archive/AI seams. Reusable snippet `assets/styles/grain.js`
— a snippet, not a scene template.

## Music

Tense/curious instrumental bed per episode — generate via DeAPI ACE music when available
(keys in ./.env), else PD/CC0 fallback (attribution logged in provenance). Ducked under
narration (~-14dB), rises during holds. Bed choice is an editorial call, owner ear-checks at
preview.

## Character sub-arcs

The hit videos' vignettes about real people ARE the banked emotional payoff + net-info-gain.
**Memorial portrait dwell: a real person's face stays on screen briefly —
~4-5s max, once — then cut to symbolic/context imagery. Never linger on a victim's face.**
Rules: real, named, publicly documented people only; verified quotes/facts (NWS service
assessments, news archives, memorials); respectful framing — narrate the record, never
dramatize beyond it; NO fabricated composites; no real-person likeness in generated imagery.

## Beat bands (measured from teardowns; editor agent decides each rotation)

hook cuts 2-3s · body 4-8s · holds 3-10s · inserts 5-15s. The editing agent picks every cut
point from that segment's words.json (cut on the word being spoken). Lint enforces only hard
floors/ceilings; taste stays with the model.

## Cadence + sync rules

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
- **Burned-in radar/satellite timestamps: map to the narration or
  crop/cut them out of frame** — cropping is a legitimate alternative to honest-labeling when
  the clock itself isn't the story. Watch UTC-vs-local (NEXRAD burns UTC). Grain filter over
  archive graphics as needed to unify the look.
- **Graphics never idle — graphics are SEQUENCES, not posters.**
  The clock is INFORMATION, not motion: something the viewer didn't know yet must land every
  2-3s (a label, a number, the polygon, an annotation, a state change). Motion without new
  information is an animated still. Reveal every element ON its spoken word; text cards build
  line-by-line, never all-at-once; a finished graphic exits, it does not sit.
- **Mandatory self-audit before render: after authoring, re-walk every
  graphic/text/quote element as a viewer** — for each one ask: landing, idling, or minor fix?
  Table the verdicts (the "is it sitting for the egg to hatch" pass). Same pass re-checks clip
  pacing. This is an AI-judgment step — never enforced by script.
- **Cut-pacing baselines (guidance for the editor's reasoning; the still cap IS code-enforced
  in sweep):** stills 3-6s MAX with motion, never longer · video clips up to
  12-15s when the clip matches the narration (motion earns time) · hooks 2-4s · graphics for as
  long as they keep delivering new information, PLUS ~1s of land time after the last beat —
  never cut ON motion. Deviate whenever the beat demands it — reason per shot.
- **Naming: one asset = one exact filename, cited by filename always** — never prose aliases
  ("cupcake renamed fruit-cake" ban). Different stock files of similar subjects are legitimate
  different shots; the sin is re-showing ONE file under different references. Edit script
  carries a shot ledger: filename → subject-family → uses.
- **Numbers**: no eyebrow pre-reveal; counters roll fast then slow dramatically into the final
  figure; secondary stats appear after the landing.
- **Lower-third sub-lines**: high contrast or backing bar — no dark italic on busy ground.
- **Outro**: match-cut the channel title to the closing line; card does not sit.

## Editing grammar (seed — grows via LEARNINGS.md)

- Hook: the narrator's payoff line over motion from 0:00; no archive audio in the hook (see "Cold-open hook contract").
- After an emotional payoff: hold 2-4s, ambience up, then cut hard to the next act. Declare each hold with an
  empty marker `<section class="clip hold" id="hold-N" data-start="X" data-duration="3.0" data-track-index="8"></section>`;
  `lint_timeline.py` sanctions a narration gap only inside a blackout, a declared hold, or the CTA (ep-1974, 21 Sep 26).
- **Chapter blackout (documentary breath — ep1/ep2 device, MANDATORY ep4+):** between acts,
  and on a key beat, cut to a full BLACK. It resets the eye and is what makes ep1/ep2 read like
  a documentary. **Duration table: 0.6–0.9s = chapter break · 1.0–1.3s = dramatic punctuation ·
  1.5s+ = dead air.**
  A seamless butt-cut (e.g. a panel's timed slide-out straight into the next shot) needs NO
  blackout — only where a blackout exists does the table apply. Place a plain black section
  on the picture track:
  `<section class="clip blackout" data-start="X" data-duration="0.7"–"1.2" data-track-index="1"></section>`
  with `.blackout { position:absolute; inset:0; background:#000; }`. Cut TO black hard (no fade),
  hold in silence or low ambience, cut OUT to the next act. (ep1/ep2 shipped 2.4–3.0s; ep6 is
  the first cut on the table.) **ep3 kept only the cold-open
  VOID (h1-s3) and dropped the recurring act-boundary blackouts** — its (now-deleted)
  `build_ep3.py` generator never emitted them between acts. A regression, not a style choice:
  the next episode's editor MUST hand-place act-boundary blackouts. ep3 stays as shipped; do
  not re-render it for this. (Generators were purged 2026-08-02 — see CLAUDE.md TRIPWIRE;
  episode HTML is hand-authored — there are no "shot table" workflows.)
- Never two inserts back-to-back; narration re-anchors between them.
- Stats mid-video, emotion banked at the end (teardown-verified pattern).
- Micro-loops every 30-45s, phrasing varied; no recap; CTA short.
- **Signature closing footnote (channel = The Warning Hour):** every
  episode ends on a short, punchy, WARM and positive beat — preparedness, never fearmongering —
  landing on the channel name. Canonical shape (tweak per episode, keep the cadence):
  "Disasters don't ask permission. But they do send warnings. Learn what yours sounds like —
  so when it comes, you already know what to do. This was The Warning Hour." It plays over the
  title card; it IS the outro (still no recap, no content summary).

---
# GRAPHICS CONTRACT (binding, from ep2)
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
- **Un-positioned `tl.set()`/`tl.to()` land at the END of the timeline as built so far** — a late tween inserted above them
  silently shifts them (g-slope 2026-09-12: the panel vanished at 5.5 s). Every set/to carries an explicit position.
- **Panel exit TIMING:** the slide-right exit above is REQUIRED —
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
**A diagram is a claim (owner 2026-09-12).** Every bespoke diagram is briefed on `references/mg-brief-template.md`
BEFORE anyone draws: SOURCE figure it traces, DATUM / SCALE / ORIENTATION, geometry in px, and a MUST-BE-TRUE list with
ratios, all numbers confirmed. Review order is fixed: meaning (the truths) → layout → motion → code gate; a truths failure
ends the review. The orchestrator reads one final frame itself against the truths; vision-agent verdicts get that
spot-check every time (g-slope: a reader passed a diagram with the island drawn under water).
ep2 built real widgets: a CAPE gauge with gradient fill, a layered lid cross-section, staggered
shear arrows + rotating column, a conic-gradient supercell. A cone captioned "tornado" or a line
captioned "warm air" conveys nothing — build the mechanism, animate it, let the label name it.

## 8. Hard gate — code QC, not frame QC
`node scripts/graphics_qc.mjs .` (from the episode dir) must exit 0 before any render. Frame renders
CONFIRM; they never DISCOVER. Sampling 105 frames of a 35-min cut inspects 0.3% of the runtime and
cannot see text collision, empty containers, or crop errors — those are `getBoundingClientRect`
assertions in the DOM. (ep3 v2 root cause.)
