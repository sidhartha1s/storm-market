# A4 · Stores, churches, restaurants · motion-graphics list (briefs written 17 Oct 26)

Source of every Picture line: `episodes/ep-joplin-2011/edit_script.md` A4-S1 to A4-S14 (there is no A4-S2 or A4-S8; no wav exists for either).
Numbers: `research/facts.md` rows only. Cues: `audio/<seg>.words.json`.

## Conventions (every brief in this folder uses them)
- **Cue notation** `a4-s3 "pushed" 12.62` = that word's `start` in `audio/a4-s3.words.json`, seconds from the start of that
  segment's wav. Words are written as whisper spelled them ("Rangeline", "layway", "538"). Comp-local time = (`nx-a4-s3`
  data-start − host data-start) + 12.62; the data-starts come from the narration mounts in `index.html`. Put the spoken
  cue in a comment beside each tween (`/* PUSHED a4-s3 12.62 */`).
- **Spoken text drift:** the voice differs from the script in two places, and the cue words follow the voice: a4-s4 says
  "ended up, but it came to rest"; a4-s5 says "The store's manager said" (script: "managers").
- **Shared bases, never redrawn** (each is owned by the brief of its first use; copy the base file, retune, do not rebuild):
  - MASTER MAP: the Joplin case-board map, first built for T1-S2 (intro briefs). It owns all geography (streets, store and
    church outlines, the tornado path and centre line, St. John's). A4 map comps add layers to a copy of it and add no geography.
  - BELOW-GROUND LINE: the thin "below ground" line under the master map, first drawn for T1-S3. The stair and cellar
    cross-sections use its stroke, colour and label style for their ground line.
  - COUNTER CARD: "INSIDE A BUILDING n of 135" over "BELOW GROUND, NONE FOUND", glass card top right, first visit A3-S11.
  - COMMENT CARD: the viewer-comment card, first use A1-S3 (the RODALCO2007 comment). Card only, never a frame of the chase video.
- **Approximate counts keep their "about"** on screen where the source says approximately (B9 "approximately 200", B11
  "approximately 35"): the chips read "ABOUT 200 INSIDE" and "ABOUT 35 IN THE TRAINING ROOM", where the Picture lines
  wrote "200 INSIDE" and "35 IN THE TRAINING ROOM". The orchestrator may restore the Picture-line text; it is a writer's line, not the owner's.
- **Sums are computed, not printed by NIST** (run 17 Oct 26, `python3` inline): B45's eight buildings 1+4+4+3+8+5+3+3 = 31;
  H26 homes 59 + apartments 12 = 71; counter visit 2 = 71 + 31 = 102; B34 6 + 6 = 12; B39 3 + 4 = 7; B13 73 − 63 = 10.
- **Source lines** inside comps sit bottom-left (x 96, baseline ≤ 1026), never in the presenter corner (x ≥ 1600, y ≥ 680).
- **Photo credit lines** under the NIST and NOAA stills are not comps: the orchestrator mounts them as index `.srclab`
  overlays (house class, `library/inhouse/snippets/cards.css`) with the text from the file's `provenance.csv` row, moved
  bottom-left when the presenter circle is on. Listed below so nothing is missed.

## Open numbers and open claims (left out of every drawing until a facts.md row carries them)
1. **"likely near the center"** (Walmart, A4-S4 Picture line and narration "most likely near the middle of the store"): no
   facts.md row says it. B7 says only "It is uncertain exactly where inside the store these victims were located." The
   script cites factcheck-A4-Z1, which is not in `research/`. The three Walmart markers sit inside the "3 LOST" chip, not on the plan.
2. **Comment like count "1,500"** (A4-S5): lives in `research/comment-beats.json` (vid CburjPYmSdo, likes 1500, "10 years
   ago"), not facts.md. The card keeps the likes slot; the orchestrator fills it if the comment bank counts as the source.
3. **Store, church and hospital positions and the tornado centre line**: no coordinates in facts.md. They belong to the
   MASTER MAP base and its traced source. A4 map briefs state only relations (B17: the centre line runs just north of 20th
   Street, between Walmart and Home Depot, very near the Pizza Hut).
4. **Building dimensions** (Walmart, Home Depot, Stained Glass Theater stair, Macadoodles store height): none in facts.md.
   Those drawings carry "SCHEMATIC · NOT TO SCALE". The one real dimension drawn is the cellar's depth, about 20 ft (B35).

## Graphics
| comp id | segments | what it shows | DEEP/STANDARD | exemplar | cue span (s) |
|---|---|---|---|---|---|
| `g-a4-strip` | A4-S1 | MASTER MAP copy: push into the 20th St / Range Line commercial strip, refuge-area markers in Walmart and Home Depot | DEEP (Opus 5.5 high) | MASTER MAP base; `references/editing-patterns/ep3-map-route-fit.html` | a4-s1 0.00 → "basement," 5.24 (+0.6 exit) |
| `g-a4-walmart` | A4-S3, A4-S4 | Walmart plan: 200 dots, 55 gather at the back refuge band, back wall falls in; section A–A: wall on cabinets, the pocket; 3 LOST chip | DEEP (Opus 5.5 high) | `references/editing-patterns/ep2-met-explainer.html`; official `svg-stroke-trace` | a4-s3 0.00 → a4-s4 "Depot?" 16.68 (+1.0), photo cutaway inside it |
| `g-a4-comment` | A4-S5 | COMMENT CARD over the NIST Home Depot photo: "what about that Home Depot? Think that'd be a bad spot?" | STANDARD (Sonnet 5.5 high) | COMMENT CARD base (A1-S3); official `testimonial-proof-card` | a4-s5 0.00 → "standing." 3.54 (+0.6) |
| `g-a4-hd-panels` | A4-S5 | glass label "63 of 73 wall panels collapsed" with a 73-tick strip, over the DVIDS Home Depot site aerial | STANDARD (Sonnet 5.5 high) | `references/editing-patterns/ep6-glasscard-popfig-bfmg.html` | a4-s5 "tornado" 22.24 → "What" 26.64 (+0.6) |
| `g-a4-homedepot` | A4-S5 | Home Depot plan: training room at the back lit, its panels fall outward; ABOUT 35 IN THE TRAINING ROOM; front wall falls in, lumber entrance; 8 LOST; source line | DEEP (Opus 5.5 high) | `g-a4-walmart` (same plan family: build it after the Walmart base read); `library/inhouse/stat-panel.html` rail rows | a4-s5 "About" 4.56 → "down." 20.42 (+1.0) |
| `g-a4-20th` | A4-S6, A4-S7 | MASTER MAP copy: centre line just north of 20th St between the two stores, near the Pizza Hut; cooler-door inset, 5 LOST; pan to 20th and Connecticut, Dillon's produce-cooler inset, 35 figures, 35 IN THE COOLER · ALL SURVIVED | DEEP (Opus 5.5 high) | MASTER MAP base; `ep3-map-route-fit.html` | a4-s6 0.00 → a4-s7 "basement?" 14.12 (+0.8) |
| `g-a4-theater-quote` | A4-S9 | full-frame beige cite card: 56 INSIDE, the director's first announcement verbatim, then "ABOUT 25 MINUTES LATER" and the second | STANDARD (Sonnet 5.5 high) | `library/inhouse/quote-card.html` | a4-s9 0.00 → "there?" 23.96 (+0.6) |
| `g-a4-stairs` | A4-S10 | cross-section: stair one person wide down through the BELOW-GROUND LINE, about 15 figures below, 3 markers above, a figure at the stair head | STANDARD (Sonnet 5.5 high) | BELOW-GROUND LINE (T1-S3); `library/inhouse/radar-beam.html` (full-frame SVG diagram) | a4-s10 0.00 → "moment." 13.18 (+1.0) |
| `g-a4-churches` | A4-S11 | two glass chips over the church-site stills: "3 LOST", then "4 LOST", source line with "7 IN CHURCHES" | STANDARD (Sonnet 5.5 high) | `references/editing-patterns/ep5-glass-stat-panel.html` | a4-s11 "Three" 13.44 → "it?" 21.64 (+0.6) |
| `g-a4-above` | A4-S12 | glass text card over the Range Line corridor aerial: "In all of the demolished buildings, those lost or badly hurt were above ground", chip ALL ABOVE GROUND · THE 8 BUSINESSES AND CHURCHES STUDIED | STANDARD (Sonnet 5.5 high) | `references/editing-patterns/ep6-glasscard-popfig-bfmg.html` | a4-s12 "The" 3.90 → "ground?" 11.18 (+0.6) |
| `g-a4-cellar` | A4-S13 | cross-section: store above the BELOW-GROUND LINE, concrete cellar about 20 ft down, 12 figures led down, store demolished above, 12 BELOW GROUND · ALL OK | DEEP (Opus 5.5 high) | BELOW-GROUND LINE (T1-S3); `library/inhouse/moves/demo.html` (measure-draw, debris) | a4-s13 "Macadoodles" 0.00 → "hurt." 11.84 (+1.0) |
| `g-a4-counter` | A4-S14 | COUNTER CARD visit 2: INSIDE A BUILDING 102 of 135 over BELOW GROUND, NONE FOUND, about 5 s | STANDARD (Sonnet 5.5 high) | COUNTER CARD base (A3-S11) | a4-s14 0.00 → "Their" 4.66 |
| `g-a4-handoff` | A4-S14 | MASTER MAP copy under the counter card, then St. John's outline lights | STANDARD (Sonnet 5.5 high; back to Opus if the base needs a retune) | MASTER MAP base | a4-s14 0.00 → "sirens." 6.88 (+0.5 to segment end) |

## Not comps (index overlays the orchestrator mounts; text from `media/candidates/a4/provenance.csv` once the pick is final)
| what | segment | text |
|---|---|---|
| credit, Walmart wall photo (pick c2) | A4-S3 | "NIST NCSTAR 3, Fig. 3-40" |
| credit, Home Depot photo (pick c1) | A4-S5 | "NIST NCSTAR 3, Fig. 4-10" |
| credit, church-site and Macadoodles-site aerials (stand-ins) | A4-S11, A4-S13 | "NOAA aerial, 24 May 2011" (see the stand-in note in `g-a4-churches.md`) |

## What the Picture lines leave open (the orchestrator decides; each brief follows the reading stated in it)
- **A4-S1 clip window:** the map holds to "basement," 5.24, then the Range Line corridor clip has "and" 5.88 to the wav end
  7.32 plus the gap before A4-S3: under 2 s unless that gap is long.
- **A4-S5 order:** comment card, photo, plan, then the Home Depot aerial clip on "The tornado center passed" 21.80 to the end.
  The centre line itself waits for A4-S6 as the Picture lines place it. Alternative: start `g-a4-20th` at a4-s5 "The" 21.80
  so the line draws on "passed" 22.88, and cut the clip to the plan's tail.
- **A4-S4 markers:** the Picture line asks for three markers "near the middle of the store"; held back (Open 1).
- **A4-S7, S9, S11, S13 photos:** no lawful ground photo exists of Dillon's, the theater, either church or Macadoodles
  (`media/candidates/a4/candidates.md`); the NOAA aerials are centred on a geocoded address and the building is not
  confirmed. `g-a4-20th` and `g-a4-theater-quote` are designed full frame so they need no photo; `g-a4-churches` and
  `g-a4-cellar`'s opening still need the owner's call on the stand-ins.
- **A4-S10 director:** B30 and B46 suggest the director is one of the theater's three, but no row says so; the stair head
  figure is drawn neutral, not as a loss marker.
- **A4-S12 "the 8 businesses and churches":** B31 says "the eight buildings discussed in this section"; the chip names them
  businesses and churches, which matches the eight in B45 only if the Elks Lodge and the theater count as businesses (B47 counts the Elks Lodge as one).
