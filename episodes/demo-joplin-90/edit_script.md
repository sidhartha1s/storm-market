# The Sirens of Joplin — 90s demo (prod-grade E2E proof)

Owner-approved 2026-07-22 as the grammar-validation demo. Every segment type exercised.
Target ~92s. Voice: pocket-TTS Pharaoh (config external.voice_ref). Music: tense/curious
instrumental bed, ducked −14dB under narration, up during hold.

## Segments

### S1 — insert (cold open) — 6s
Broadcast/siren audio WITH its own sound. Candidate needed: Joplin EAS tone / local TV
severe-weather cut-in / NWS warning audio, May 22 2011. **OWNER GATE before render.**
Visual: the clip itself, grain overlay, no text.

### S2 — narration — 24s (~52 words)
> May twenty-second, two thousand eleven. Joplin, Missouri. The sirens sounded at five
> eleven that evening, and most people did what people always do. They waited. Because
> in Joplin, the sirens had cried wolf so many times before, and the sky did not yet
> look like a killer.
Visuals: archive stills/footage — quiet Joplin street, sky, people. Cuts 4-6s on word
timestamps ("sirens", "waited", "cried wolf", "sky").

### S3 — graphic — 12s (VO continues)
> At five forty-one, a rain-wrapped wedge nearly a mile wide dropped onto the west side
> of town. Seventeen minutes. That was the warning Joplin got.
Visual: self-made radar-style sweep (JS/canvas) + big counter "17:00" counting down +
text popup "5:41 PM — EF5". No claim risk — drawn, not sourced.

### S4 — narration — 18s (~39 words)
> The winds passed two hundred miles per hour. Faster than a Formula One car at full
> speed, grinding through neighborhoods for thirty-eight minutes. It did not skip like
> tornadoes usually do. It stayed down, and it stayed wide.
Visuals: damage footage/aerials (NOAA/FEMA PD), cuts on "two hundred", "grinding",
"stayed down".

### S5 — hold — 4s
One aerial damage shot just SITS. No voice. Ambience + music up. Grain heavy.

### S6 — narration (character beat) — 18s (~38 words)
> A hundred and sixty-one people never saw the morning. One of them was a young man
> named Will Norton, driving home from his own high school graduation, minutes from
> his front door when the wind took him.
Visuals: single slow-push still (graduation-adjacent archival or AI-still dramatization,
no real-person likeness), then black. [Will Norton: publicly documented Joplin victim —
verified fact, respectful framing.]

### S7 — narration (thesis close) — 10s (~21 words)
> Joplin was not a failure of forecasting. The warning was there. This is the story of
> the seventeen minutes nobody believed.
Visual: title card "THE SIRENS OF JOPLIN" over grain, hard cut to black.

## Assets needed
- S1 insert candidates (2-3, owner picks/rejects)
- Archive/PD: quiet-street or 2011-era Joplin stills, storm sky, damage aerials (FEMA/NOAA)
- Radar graphic: canvas/JS, authored in comp
- Music: ~95s tense-curious instrumental (DeAPI ACE; fallback PD bed)
- TTS: S2, S3, S4, S6, S7 as separate wavs
