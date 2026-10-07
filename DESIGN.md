# DESIGN.md — storm-market editing architecture

Every motion-graphics rule (file contract, safe zones, the presenter circle, type, palette, glass card, motion, exits, on-screen text,
what the gates parse) lives in `references/mg-quickref.md`. This file is the editorial architecture only.

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
carries the **fact-QC layer** (revised 27 Sep 26: writer tags `[verify]` only, a parallel
fact-check fan-out resolves it, "Section lock — the ONE definition" gates TTS — read it there,
not here) and the **insert-transcription rule** (transcribe every insert in full BEFORE cut
selection; cut at the transcript's action/emotion peak).

## Audio rules (hard)

- Every sourced clip is **muted by default**, and "muted" means the `muted` attribute on the `<video>`:
  hyperframes plays any video's track unless the element says otherwise, and `sweep_episode.py` fails a
  `<video>` with neither `muted` nor `data-volume` (El Reno v3 shipped audible stock footage that way).
  Exactly one exception: `insert` segments, where the clip's audio IS the content.
- **Every `insert` goes to the owner before it enters any render**: frames + ~10-word transcript
  + source link, one message, wait for yes/no. No exceptions, no batching-through.
- Narration is TTS'd **per segment** (separate wavs). Tempo is per lane (`config.yaml channel.tempo`,
  applied by `scripts/tts_episode.py`); the editor slows a key reveal with `(tempo 1.0)` on its heading (CLAUDE.md "Voice"). Owner ear-check before ship covers it.
- Ambience/music beds: PD/licensed only, ducked under narration, audible in holds.
- One-shot SFX hits (a stamp/boom/impact, not a riser or a bed): before hand-setting `data-start`,
  run `python3 scripts/sfx_peak.py episodes/<slug>` — it reports each hit's true peak offset
  inside its source file and the corrected `data-start` (cue - peak) so the transient lands on
  the cut, not the file's raw sample zero. Risers keep the existing rule (a riser ends where the
  line ends); beds are unaffected.

## Placement — LLM judgment, native hyperframes timing, no engine

1. TTS per narration segment -> wav + duration; faster-whisper -> per-segment words.json.
2. The editing agent reads words.json + the clip inventory and authors the composition directly:
   `<video>/<img>/<audio>` elements with `data-start`/`data-duration` in `index.html`.
   Cut points = word timestamps read by the model, chosen editorially. No placement.mjs port.
3. Deterministic checks stay small: `scripts/lint_timeline.py` checks that every referenced file exists, every
   window sits inside the composition, narration does not overlap inserts, no banned audio hash, and the repeat
   rule. Everything judgment-shaped stays with the model.

## Sourcing — agent-executed, owner never downloads

Per beat: agent pulls 2-3 candidates, extracts frames, vision-checks, picks. Tools on box:
- archive.org advancedsearch API + direct download (curl/spider) — news reels, local TV, PD film
- FEMA/NOAA/NWS/USGS media pages — direct or playwright-cli
- yt-dlp — government YouTube channels (NWS briefings, FEMA), 911/broadcast audio compilations
- stock-fetch CLI (keys in ~/.claude/.env; the Pexels keys return 403 since 2026-09-08, Pixabay works) — generic storm/sky/town b-roll
- NEXRAD Level-II archive (AWS open data, free) — data for OUR radar animations
- DeAPI stills + LTX clips (keys in ./.env) — AI dramatization gaps
License check per item; storm-chaser footage NEVER without license; news-network footage
sparingly/short/narrated-over (claims budgeted, segments must survive being claimed).

### Cold-open hook contract
The first 25-30s decide the video. Owner rated ep2's first hook 0.6/10 and the rebuilt one
shipped; these are the standing requirements for every episode's cold open:
- **NO black start: frame one is MID-ACTION** — the episode's
  defining shot already moving. High curiosity, high impact from the first frame.
- **The highest-intent real clips open the video, never only the end.** The footage the title promises (the slide, the
  collapse, the impact) is in the hook. A later act may return to it, but the best shot is never saved for the end (ep-nepal: the hook missed the slide).
- **The NARRATOR's first line starts at 0:00. No broadcast, radio or archive audio anywhere in
  the hook** (owner 22 Sep 26, replaces the old "anchor line by 2.5 s" rule): archive audio is
  low quality, and a 10/10 narrated hook is worthless if viewers leave before it starts.
  Archive audio belongs inside the acts, as `insert` segments.
- **Date/place popup (popfig) inside the first second** (viewer must know where/when instantly),
  sized to clear before the first designed graphic arrives.
- **Every cut lands ON an audio event** (a line ends, a roar starts, a siren swells) — never
  cut mid-sentence, never let commentary "just start" and get cut off.
- **The hook's sound is reasoned per episode, never a template** (owner 26 Sep 26). Pick it from
  the story and write the reason in `edit_script.md`: a siren only when the story is a warning; otherwise
  wind, a 911 line tone, silence into an impact, or a music sting. ep2's siren spine (fade in from black,
  duck under the narrator, swell at impact, die into the void) is one worked example, not the default.
  No silent clips and no dead air unless the silence is the chosen effect.
- **Inserts end on their complete emotional statement** — trim orphan tails ruthlessly
  ("we knew something was coming." — stop. Nothing after).
- **No void or black between the hook and the intro** (channel post-mortem 27 Sep 26: docs lost 22-35 points at
  20-40 s on black holds, title cards and disclaimers). Nothing black before 1:00; the first chapter blackout comes after the intro.
- Few clips, each earning its slot (ep2: warning → impact → dispatch → void). More clips ≠
  more captivating; undifferentiated montage is what scored 0.6.

### CTA contract (must-keep, every episode from ep4 on)
The ebook CTA (Paul on camera, QR + "first link in the description") is a fixed element of
every episode from ep4 on. File, duration, window and labels live in `config.yaml channel.cta`
(current file and README in `assets/cta/`) — never a
per-episode copy of the rule, never a hand-edited path. Shape: **hook > story > CTA > close**.
- **Window: the CTA starts inside 85–95% of total runtime** (owner 23 Sep 26: the 30–40% placement
  was not converting and annoyed viewers). Place it late, at a seam where it does not interrupt a reveal. `sweep_episode.py` fails outside the window (episodes shipped
  before the contract are listed in `channel.cta.exempt` — never extended; `demo-*` dirs print SKIP).
- **Hinge is scripted, not spliced:** the narration segment BEFORE it ends on a tease (an open
  loop planted in the words — "...that gap was about to close, on the most experienced observers
  alive"), the segment AFTER opens with the payoff in its first sentence. The script's loop table
  carries the pair as `cta-hinge` (references/script-scaling.md). No natural tease inside the window =
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
  "📘 The book mentioned at mm:ss — Storm-Ready Home ... <channel.cta.first_link>" (that same URL, never the bare home page).
- **Never** skipped, shortened, moved to the outro, muted, or replaced by a text card. A re-cut of
  the clip is a NEW versioned file + config bump; the old file leaves the tree in the same PR.
- Wiring (staged episode-relative — `render.cmd` cds into the episode dir, no `../` srcs):
  copy the asset to `media/cta/<file>` (gitignored; sweep md5-checks it against `assets/cta/`), then
  `<video id="ins-cta-paul" src="media/cta/<channel.cta.file name>" data-start="<T>"
  data-duration="<channel.cta.duration>" data-track-index="1" data-volume="1" data-srt-label="<channel.cta.srt_label>">`
  with a 1.0s blackout element before and after on the picture track.

### Broadcast-clip rehook cadence
Core audience is 40–70+ — they watched these events on live TV; real broadcast/news/PD/survivor
clips are the nostalgia rehook, stock footage only fills between them. **A real clip lands as the beat needs
(cadence aim: CLAUDE.md "REAL clip", not a hard gate), never long stretches of pure stock.** Network news: transcribe
first, cut at the best moment; up to ~12-15s per pull when narrated over (commentary audio may
be featured, audio mix is a per-cut editor decision), courtesy credit in
description — credit manages goodwill, it does NOT remove
claim risk, and it never substitutes for a license. **Claims-vs-strikes distinction (Oldshue
ruling): network/TV material draws Content ID revenue claims (budgeted, survivable); independent
chaser/streamer footage draws manual copyright strikes (channel-fatal) — the NEVER-without-license
rule covers streamers, not just "storm chasers" by job title. Disguising a source (grain, crops,
short cuts) to dodge detection is prohibited — safety comes from structural immunity, not
obfuscation.**

## Composition and review
- Each episode's index.html is authored fresh (agent-as-editor); graphics are library-first and hand-retuned
  (`references/mg-quickref.md`). Building from scratch stays allowed with a one-line reason in `edit_script.md`.
  A template is a starting point an agent edits with per-cut judgment, never a builder that outputs a finished scene
  (the TRIPWIRE in CLAUDE.md).
- **Footage review density:** eyeball ≈ 1 frame / 15-20s of runtime on every render (dense sweep or
  `hyperframes check` + snapshot grid), plus targeted frames at every region changed since the
  last render. 18 frames on a 28-min cut is not a review. Compositions are verified per the quick-ref "Verify".

## Content ID / claims protocol

Content ID cannot be scanned offline — the protocol is layered:
1. **Structural immunity**: PD / stock / self-made / AI assets are un-claimable by construction.
   Only `insert` segments carry any risk.
2. **Provenance ledger**: every sourced file gets a row in `episodes/<slug>/media/provenance.csv`
   (file, source_url, license, fetched date) — claims become instantly traceable/disputable.
3. **Pre-publish check**: upload **private/unlisted** first; YouTube's Studio "Checks" step runs
   Content ID before publish. Wait for Checks to pass (+ a few hours soak — matches can lag),
   swap any claimed segment while still private, THEN flip public. Never publish blind.

## Look: palette and type
One palette and type file for the whole channel (colours, fonts, px tiers, TV-readability floor,
CSS custom properties): `library/inhouse/snippets/tokens.md`. Swatch preview:
`library/inhouse/snippets/brand-swatch.html`.

## Look: grain layer

Every clip renders under a unified film layer: animated grain (SVG turbulence or canvas noise,
JS-driven — never CSS @keyframes), subtle vignette, occasional drifting dust specks. Purpose:
one filmic look that also hides stock/archive/AI seams. Reusable snippet `assets/styles/grain.js`
— a snippet, not a scene template.

## Music

Tense/curious instrumental bed per episode — generate via DeAPI ACE music when available
(keys in ./.env), else PD/CC0 fallback (attribution logged in provenance). Level under
narration: CLAUDE.md "Narration sits above every bed" (Two lanes section). Rises during holds. Bed choice is an editorial call, owner ear-checks at
preview.

## Character sub-arcs

The hit videos' vignettes about real people ARE the emotional payoff + net-info-gain.
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
- **No visual repeats** in an episode. Reuse only as intentional callback:
  different crop/grade, >5 min apart, flagged with `data-callback="reason"` on the element
  (lint-enforced; max 3 uses, each reuse flagged; last 90s = summary zone, exempt — owner OK'd recap reuse).
- **No SUBJECT repeats either (ep1 v2 RCA)**: two different files of the same visual subject
  (two night-lamp-rain shots, two town aerials of the same look) read as a repeat to the
  viewer. Dedup by what the FRAME shows, not the filename. When authoring, group the shot
  list by subject family (night-rain, town-aerial, siren, rubble...) and use each family
  ≤2 non-adjacent times per act stretch.
- **Sync rule**: the frame must not contradict the narration — named store, time-of-day,
  burned-in timestamps. Match the visual or use a neutral one. No asset means an honest designed card, never fabricated footage.
- **Burned-in radar/satellite timestamps: map to the narration or
  crop/cut them out of frame** — cropping is a legitimate alternative to honest-labeling when
  the clock itself isn't the story. Watch UTC-vs-local (NEXRAD burns UTC). Grain filter over
  archive graphics as needed to unify the look.
- **Mandatory self-audit before render: after authoring, re-walk every
  graphic/text/quote element as a viewer** — for each one ask: landing, idling, or minor fix?
  Table the verdicts (the "is it sitting for the egg to hatch" pass). Same pass re-checks clip
  pacing. This is an AI-judgment step — never enforced by script.
- **Cut-pacing baselines (guidance for the editor's reasoning; the still cap IS code-enforced
  in sweep):** stills 3-6s MAX with zoom or pan, never longer · video clips up to
  12-15s when the clip matches the narration (motion earns time); prefer video everywhere · hooks 2-4s · graphics for as
  long as they keep delivering new information (land time: quick-ref) — never cut ON motion. Deviate whenever the beat demands it — reason per shot.
  Floor from shipped cuts: ep2 had 187 windows, 10.0 s median, 2 picture gaps; uncovered picture gaps in the dozens is a bug.
- **Naming: one asset = one exact filename, cited by filename always** — never prose aliases
  ("cupcake renamed fruit-cake" ban). Different stock files of similar subjects are legitimate
  different shots; the sin is re-showing ONE file under different references. Edit script
  carries a shot ledger: filename → subject-family → uses.
- **Outro**: match-cut the channel title to the closing line; card does not sit.

## Editing grammar (seed — grows via learnings/)

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
  the first cut on the table.) ep3 dropped the act-boundary blackouts because its deleted generator never
  emitted them: a regression, not a style choice, so every editor hand-places them. ep3 stays as shipped.
- Never two inserts back-to-back; narration re-anchors between them.
- Stats mid-video; where human moments go: script-scaling.md "Emotion".
- Micro-loops every 30-45s, phrasing varied; no recap; CTA short.
- **Signature closing footnote (channel = The Warning Hour):** every
  episode ends on a short, punchy, WARM and positive beat — preparedness, never fearmongering —
  landing on the channel name. Canonical shape (tweak per episode, keep the cadence):
  "Disasters don't ask permission. But they do send warnings. Learn what yours sounds like, so when it comes, you already know what to do. This was The Warning Hour." It plays over the
  title card; it IS the outro (still no recap, no content summary).
