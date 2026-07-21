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

## Composition authoring rules

- Animations JS/WAAPI only — CSS @keyframes disables fast-capture (measured 2026-07-21).
- Render: `npx hyperframes@<pin> render . --gpu --browser-gpu --experimental-fast-capture=true
  --quality standard --crf 16 --fps 30`.
- Each episode's index.html is authored fresh (agent-as-editor). Reusable CSS snippets may
  accumulate in `assets/styles/` but NO scene templates — template-ification is the failure mode
  this design exists to avoid.

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
Rules: real, named, publicly documented people only; verified quotes/facts (NWS service
assessments, news archives, memorials); respectful framing — narrate the record, never
dramatize beyond it; NO fabricated composites; no real-person likeness in generated imagery.

## Beat bands (measured from teardowns; editor agent decides each rotation)

hook cuts 2-3s · body 4-8s · holds 3-10s · inserts 5-15s. The editing agent picks every cut
point from that segment's words.json (cut on the word being spoken). Lint enforces only hard
floors/ceilings; taste stays with the model.

## Editing grammar (seed — grows via LEARNINGS.md)

- Hook: cold-open insert (911 audio / broadcast) or present-tense stat over motion. ≤15s to thesis.
- After an emotional payoff: hold 2-4s, ambience up, then cut hard to the next act.
- Never two inserts back-to-back; narration re-anchors between them.
- Stats mid-video, emotion banked at the end (teardown-verified pattern).
- Micro-loops every 30-45s, phrasing varied; no recap, no outro; CTA short.
