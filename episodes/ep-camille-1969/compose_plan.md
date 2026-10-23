# ep-camille-1969 · compose_plan.md (22 Oct 26, written while TTS runs)

Plan only. No HTML here. The builder of `index.html` is the orchestrator; each graphic goes to the builder named in Part 3.
Inputs read: `edit_script.md` draft 5 (H1 to Z1), `DESIGN.md`, `references/mg-quickref.md`, `references/mg-brief-template.md`
(+ `mg-brief-example-g-slope.md`), `library/inhouse/index.json`, `config.yaml` (cta, end_ask, tempo 0.94), `media/src/provenance.csv`
(153 rows), `omni_shots.md`, `scripts/render_preflight.py` LAYERS, and Joplin's shipped `index.html` (git `64330f03`; the
Joplin folder is not in this worktree, so read it with `git show 64330f03:episodes/ep-joplin-2011/index.html`).

Owner decisions honoured (his file `C:\Users\Sidhartha\.claude\scratch\devq-retention\answers-eps-acts.json`, saved_at "22 Oct 26 11:37:27"):
- `camille_lva` = "use", comment "ENSURE THAT this aint missed on your metadata while shipping please. please note such descrepancies carefully."
  So: every LVA still is used with credit, and `metadata.md` carries the credit line (Part 1.8).
- `camille_ins_harvey` = "yes", comment "make it trasnformative. an overlay/karaoke captions or soemthign tranformative and keep clip with audio".
  So: the WDBJ clip plays with its own audio inside a designed treatment with a word-timed karaoke caption (g-a2-harvey, Part 4 O12).

Timing figures below are ESTIMATES from word counts at the measured pace (5 wavs on disk: 3.3 to 4.3 words/s, about 201 wpm at
tempo 0.94) plus 0.3 s per segment gap. Every real cue comes from `audio/<seg>.words.json` once it lands. Never time a graphic from this file.

---

## Part 1 · Composition skeleton

### 1.1 Structure (Joplin model: one flat `index.html`, act markers on track 0)
Joplin ships ONE `index.html` with `<section class="clip act" id="act-*">` markers on track 0 and every graphic as its own
`compositions/g-*.html` host. "One sub-composition per act" is done the same way here: one act marker per act, every element of
that act inside the marker's window, graphic ids prefixed by act (`g-t1-*`, `g-i1-*`, `g-a1-*` ... `g-z1-*`).

| Track | What sits there | id pattern (Joplin) |
|---|---|---|
| 0 | act markers: `act-hook` (H1+T1), `act-intro` (I1), `act-a1`, `act-a2`, `act-a3`, `act-a4`, `act-z1` | `act-*` |
| 1 | picture: stills (`<section class="clip still-wrap" id="c-*">` around `<img id="kb-*">`), muted videos `v-*`, blackouts `bo-*`, Paul clips `ins-paul-*`, CTA `ins-cta-paul`, end ask `ins-paul-e1/e2`, Harvey insert `ins-a2-harvey`, bridges `br-*` | |
| 2 | graphic hosts `host-*` → `compositions/g-*.html` (incl. the Harvey caption host with `data-caption-for`) | `host-*` |
| 3 | card zone (only where a card must sit over a comp; avoid: occlusion gate) | |
| 4 | index overlays: popfigs, glance chips, source lines, name chips; each wrapped in a timed `<section|div id=... data-start data-duration data-track-index="4">` (overlap_check ignores unwrapped overlays) | `pf-*`, `chip-*`, `src-*` |
| 7 | presenter circle videos `class="pip"` | `pip-w<n>` |
| 8 | declared holds `<section class="clip hold">` | `hold-*` |
| 9 | circle rings | |
| audio | narration `nx-<seg>` (`audio/<seg>.wav`, volume 1), beds and swells `sx-*` | |

Popfig rule applied to every Picture line: red Abril popfig = 3 words or fewer, big line 16 characters or fewer, mid-screen, NEVER
over a card or a map comp. Where the script puts a date stamp over our map ("Tuesday · Aug 19, 1969 · 7 PM · Massies Mill"),
the stamp lives INSIDE the map comp's rail (the briefs below carry it), not as an index popfig. Over footage: big "AUG 19, 1969",
sub line "Tuesday · 7 PM".

Quote-card rule applied to every Picture line: a quote that sits OVER a photograph is a `.glasscard` (mg-quickref "Text over footage",
the one treatment). A quote on its own is the library `quote-card` (beige cite card on dark ground, full frame). Where the script
says "beige cite card" over an LVA photo, the plan uses a glass card over that photo, or cuts the photo (≤ 6 s) and then the
full-frame beige card. Reason: mg-quickref is the one home of MG rules.

Still rule: every `<img>` window ≤ 6 s (sweep check 9), punch zoom or pop on its narration beat, no slow Ken Burns (DESIGN.md
"Footage motion"). A segment longer than about 6 s alternates two stills of DIFFERENT subjects, or hands over to a comp.
Photos placed INSIDE a comp are figures the comp traces or measures (A1-S13, A2-S8, A4 eight-map insets), never a dodge of the cap.

### 1.2 Act windows (estimate) and chapter blackouts (hand-placed, track 1, cut to black hard, no fade)
| Act | Segments | Est. start | Est. length | Blackout after |
|---|---|---|---|---|
| hook | H1-S1, T1-S1, T1-S2 | 0:00 | about 20 s | none (no void before 1:00; hard cut T1-S2 → I1-S1) |
| intro | I1-S1 … I1-S10 | 0:20 | about 75 s | `bo-1` 0.7 s after I1-S10 |
| A1 | A1-S1 … A1-S19 | about 1:37 | about 4:25 | `bo-2` 0.8 s after the A1-S19 card hold |
| A2 | A2-S1 … A2-S21 + Harvey insert | about 6:03 | about 4:20 | `bo-3` 0.9 s after the A2-S21 fade |
| A3 | A3-S1 … A3-S14, CTA inside | about 10:25 | about 4:55 (incl. 26 s CTA block) | `bo-4` 0.8 s after the A3-S14 hold |
| A4 | A4-S1 … A4-S16 | about 15:20 | about 4:00 | none: A4-S16 fades straight into Z1-S1 (seamless; DESIGN.md allows a butt-cut) |
| Z1 | Z1-S1, Z1-S2, END-ASK, Z1-S3, close card | about 19:05 | about 55 s | ends on the close card |
Estimated total: about 19:25 (1,163 s). Target 20 min (owner `camille_len`). `word_budget.py` must run on the real wavs.

### 1.3 CTA mount (A3-S6 → CTA → A3-S7)
- `ins-paul-4` (A3-S6, Paul full frame, chip "110+ MISSING · AUG 23 · AP" + source line over him) → `bo-cta-in` 1.0 s →
  `<video id="ins-cta-paul" src="media/cta/paul-storm-ready-v9-oct20.mp4" data-start=T data-duration="24.042" data-track-index="1"
  data-volume="1" data-has-audio="true" data-srt-label="[PAUL RAYMOND — STORM-READY HOME · paulraymond.online]">` → `bo-cta-out` 1.0 s
  → A3-S7. Stage `assets/cta/paul-storm-ready-v9-oct20.mp4` unchanged into `media/cta/` (sweep md5 `bba0b9f3289d0de3797dbfbd1017e3d8`).
- Window `channel.cta.window` = [0.40, 0.60] of runtime. ESTIMATE: CTA start about 701 s of 1,163 s = 0.603. **Over the window
  by the estimate.** Pre-CTA narration is 2,228 of 3,581 words (62 %). Keep every optional hold AFTER the CTA; blackouts before it
  at their 0.7 s floor. Measure after TTS; if still above 0.60, it is the owner's call (`window_by_slug`) or a pre-CTA trim. Risk 1.
- After `bo-cta-out` the payoff opens on REAL footage, never a graphic (DESIGN.md CTA contract): A3-S7 opens on
  `media/src/V10/Rescue_Mission_Briefing_(7797539862).jpg` for about 2.5 s, then the counter comp `g-a3-missing-b` lands on "a hundred and nine".
- Narration silent under the CTA; bed ducked ≥ 12 dB or out; circle off. CTA is not a chapter boundary (no blackout of its own beyond the dips).
- The `sweep_episode.py` WARN "another insert within 60s of the CTA" from `ins-paul-4` is expected (DESIGN.md exception).
- metadata.md: `channel.cta.first_link` first URL, plus "📘 The book mentioned at mm:ss" line from the real CTA start.

### 1.4 End ask
`ins-paul-e1` = `media/end-ask/paul-end-ask-v1-oct19-a.mp4` (9.083 s) then `ins-paul-e2` = `...-b.mp4` (6.417 s), back to back,
track 1, `data-volume="1" data-has-audio="true"`, srt labels with their words (copy Joplin's). Place: after Z1-S2, before Z1-S3.
Must start inside the last 30 s: Z1-S3 is about 9 s and the close card tail ≤ 3 s, so e1 starts about 27.5 s before the end. Tight:
the close card may not run longer than 3 s past Z1-S3's last word. Narration and circle off under both; close bed runs on under them.

### 1.5 Paul full-frame clips (5 of a 6 ceiling; `omni_shots.md`)
| id | Segment | Words | Est. length | File state now |
|---|---|---|---|---|
| ins-paul-1 | H1-S1, frame one | 26 | about 8.5 s | `media/paul/ins-paul-1/raw-01.mp4` exists; no logo step, not whisper-checked, not named `ins-paul-1.mp4` |
| ins-paul-2 | A1-S9 | 25 | about 8 s | not generated |
| ins-paul-3 | A2-S4 | 25 | about 8 s | not generated |
| ins-paul-4 | A3-S6 (CTA hinge) | 23 | about 7.5 s | not generated |
| ins-paul-5 | A4-S14 (peak) | 26 | about 8.5 s | not generated |
Mount as placeholders until the files exist: `<section class="clip placeholder" id="ph-paul-<n>" data-start data-duration="<est>"
data-track-index="1">` (black), no narration under it, circle off. Swap to `<video id="ins-paul-<n>" src="media/paul/ins-paul-<n>/ins-paul-<n>.mp4"
... data-track-index="1" data-volume="1" data-has-audio="true" data-srt-label="<his exact line>">` once the logo step (mg-quickref
"Logo on every full-frame clip") is done; duration = his last word + about 0.3 s from a whisper of the clip, never padded to 10 s.
Every later `data-start` shifts by (real − estimate): place everything after a placeholder relative to the placeholder's end.
`render_preflight.py` LAYERS refuses a render without Paul's clips, the circle and the bed.

### 1.6 Presenter circle (FlashHead, made on the ZBook)
On through all narration wherever the corner (x ≥ 1600, y ≥ 680) is free. Off: H1 and T1 (Paul opens full frame; circle first appears
with the first card, I1-S1), Paul clips, CTA + dips, end ask, blackouts, the Harvey insert, close card, Z1-S3. Two passes of
`scripts/circle_audio.py` (I1-S1 → A3-S6 start; A3-S7 → Z1-S2 end), `scripts\circle_face.py` on the ZBook, `scripts/circle_cut.py`.
A window ends with its last line (lint fails > 4.0 s with no voice). Corner turned off per scene where a label, number, marker or a
broadcaster's mark sits under it: the briefs keep x ≥ 1600, y ≥ 680 EMPTY in every comp so the circle can stay on.

### 1.7 Audio layers
Levels: narration 1.0; score bed 0.13; ambience ≤ 0.20; swells/hits near 0.4 under speech; checked with ebur128 per 15 s window.
- **Hook sound (script's reasoned pick):** heavy rain on a tin roof under ins-paul-1 from 0:00, cut dead on his last word. No file
  on disk is tin-roof rain (GAP 4). Nearest on disk: `assets/sfx/rain-loop.mp3` (street rain). Not a substitute without the editor's
  ear: source a Pixabay tin-roof rain (free, licence row in `assets/sfx/provenance.md`).
- **Bed (one family across the episode, act-sectioned as Joplin did; all on disk, claim-free DeAPI):**
  | id | Window | Source | Note |
  |---|---|---|---|
  | sx-bed-intro | T1-S1 → I1-S10 | `assets/sfx/deapi/score-act1-darkambient.mp3` (168 s) | dread, sub-bass |
  | sx-bed-a1 | A1 | `assets/sfx/deapi/test-dark-ambient-60s.mp3` self-crossfaded to the act length | a different file from intro, same colour |
  | sx-bed-a2 | A2 (out under the Harvey insert to 0.05, gone in the A2-S19 hold, creek ambience only) | `assets/sfx/deapi/score-act2-unease.mp3` (170 s) crossfaded to length | |
  | sx-bed-a3a / a3b | A3 before / after the CTA (out under the CTA) | `assets/sfx/deapi/score-act3-somber.mp3` (115 s) crossfaded | |
  | sx-bed-a4 | A4 → Z1-S2 (drops out under A4-S10 last sentence; room tone only under A4-S14) | `assets/sfx/deapi/score-act6-close.mp3` (300 s) | grief and quiet hope |
  | sx-bed-close | END-ASK → close card | tail of `score-act6-close.mp3` from a different offset | |
  Copy each used file into `media/beds/` (Joplin pattern). Volumedetect each source and compensate gain before mixing
  (`score-act5-tension.mp3` is loud; not used). Owner ear-check at preview.
- **Ambience (≤ 0.20):** `assets/sfx/rain-loop.mp3` under A1-S1 → A1-S16 (the rain night), thins on A1-S17 "thinned to a mist", out on the
  last word of the A1-S19 card read; ducks under ins-paul-2. Creek ambience under the A2-S19 → S21 hold: GAP 6 (no creek file; Pixabay or
  ffmpeg-made filtered noise, labelled). Low rumble rising for A2-S5: `assets/sfx/sfx-rumble-bed-long.mp3`.
- **Hits and swells (`assets/sfx/sfx-swell.wav` at 0.4; `sfx_peak.py` for hits):** about one per 45 to 60 s, landing ON the line.
  T1-S1 "thirty-three" · I1-S7 "let go" · I1-S9 "name" · A1-S4 lightning flash (`assets/sfx/04_distant_storm_rumble.mp3` thunder, not a swell)
  · A1-S8 "eleven people" · A1-S10 "engine flooded" · A1-S14 "eight times" · A2-S3 "fast" · A2-S8 "ten feet across" · A2-S9 "five feet in
  twenty minutes" · A2-S13 "two" · A3-S1 "cut off" · A3-S7 "eighty-nine" · A3-S9 "twenty miles away" · A3-S11 "don't agree" · A3-S13
  "never found" · A4-S1 "eight people" (card slam, `assets/sfx/sfx-boom.wav` at 0.4) · A4-S5 "red beans" (none: let it sit; editor) ·
  A4-S11 "DNA testing isn't possible" · Z1-S1 "until about four". NO swell under A1-S19 (script: "no music swell"), A4-S10 last
  sentence (score drops out), A4-S14 (room tone only). Risers end where the line ends.
- **Phone ring A1-S7** (one ring): GAP 5 (no file; ffmpeg-made two-tone bell is acceptable, labelled self-made).
- **Non-narration audio budget:** on disk and planned = Paul clips about 40 s + CTA 24 s + end ask 15.5 s + Harvey bite about 6 s + rain,
  thunder, rumble. Outside VOICES = about 6 s (Harvey only). CLAUDE.md calls about 30 s in 32 min failure-thin; this is thinner.
  Candidates in GAP 16 (each an `insert`: owner yes, word-timed running caption, `data-caption-for`).

### 1.8 Credits (metadata.md, owner's "ENSURE THAT this aint missed")
"Photographs: Library of Virginia, Virginia Governor's Negative Collection (Flickr Commons, No known copyright restrictions)" with the
negative numbers used; "USGS Professional Paper 804 and Open-File Reports 70-51, 99-518"; "NOAA/NWS WPC"; "ATS-III, UW-Madison SSEC";
"NARA (111-LC-55088)"; "WDBJ7, Aug 19, 2019 (Deborah Harvey)"; VCU Libraries if a reel is used. Build the line from the final
`index.html` src list, never from this plan.

---

## Part 2 · Per segment: picture, graphic, overlays

Paths are under `episodes/ep-camille-1969/`. `LVA/x` = `media/src/V13/x` unless a Vnn folder is named. Mount the downscaled copy
(`optimize_clips.py <episode> --apply`; LVA scans are 5550 x 4350, far over the composition size; `media_budget.py` refuses them raw).
"→" = cut order inside the segment. Every still ≤ 6 s.

| Seg | Est. | Picture (track 1) | Graphic (track 2) | Index overlays (track 4) / audio |
|---|---|---|---|---|
| H1-S1 | 0:00 | ins-paul-1 (placeholder until logo'd) | none | popfig in first second, top left: big "AUG 1969", sub "Nelson County, Virginia"; chip "IDENTIFIED BY NOW?" on "identified by now"; chip "8 STILL UNNAMED" on "eight of them" + src "Virginia Department of Health · August 2026". Tin-roof rain (GAP 4) cut dead on his last word |
| T1-S1 | 0:08 | `media/src/V13/Massies_Mill_Flooding_(7797529874).jpg` punch-in from frame one (never black) | g-t1-33 (Sonnet) | swell on "thirty-three" (words.json 0.16 s); bed-intro starts |
| T1-S2 | 0:12 | (comp full frame) | g-t1-track (Opus O2) | none (rail inside comp) |
| I1-S1 | 0:20 | `media/src/S05/ats3-camille-1969-08-17-loop-1080.mp4` (muted, scale to cover 1920 wide) → g-i1-track landfall beat → `media/src/M01/111-lc-55088.mp4` (NARA Gulfport/Biloxi, muted; pick a wreckage shot, no bodies, read frames) | g-i1-track (Opus O2, Waveland + stamp in rail) · g-i1-gulf (Sonnet, glass bar over M01) | circle first appears here |
| I1-S2 | 0:30 | (comp) | g-i1-track continues: inland crawl, symbol loses its eye | chip "TWO NIGHTS LATER" lives in the comp rail (no popfig over a map) |
| I1-S3 | 0:40 | `media/src/V24/camille1969varainblk.gif` as dimmed ground (NOAA VA storm-total rain, real document) | g-i1-rain (Sonnet) counter | |
| I1-S4 | 0:48 | (comp continues) page crop of OFR 70-51 Table 1 p. 11 rendered from `media/src/V22/ofr70-51.pdf` (prep: pdftoppm, whole lines) | g-i1-rain tail: freeze + table-row card | chip "A TRASH BARREL" inside comp |
| I1-S5 | 0:55 | (comp full frame) | g-i1-pmp (Sonnet) | |
| I1-S6 | 1:02 | `LVA/West_of_Rockfish_(7797546944).jpg` (homes hit by mudslides) | g-i1-blunt (Sonnet, glass quote) | |
| I1-S7 | 1:07 | (comp) → last 2.5 s `media/src/V23/pp804-p26-fig12.jpg` crop of one scar panel | g-i1-slope (Opus O6) | swell on "let go" |
| I1-S8 | 1:14 | (comp) | g-i1-hundred (Sonnet, on the base map) | cue "one in every hundred" = words.json 2.48 to 3.44 s |
| I1-S9 | 1:20 | (comp) | g-i1-eight (Sonnet, on the base map) | cue "eight" 0.14 s; swell on "name" 3.12 s |
| I1-S10 | 1:24 | g-i1-tye (map push west) → `LVA/View_of_Massies_Mill_(7797543848).jpg` | g-i1-tye (Opus O1) | stamp "Aug 19, 1969 · night" in comp rail; popfig "AUG 19, 1969" only over the photo if it does not collide. `bo-1` |
| A1-S1 | 1:37 | (comp) | g-a1-river (Opus O1): Tye + Route 56 through Massies Mill, rain texture, stamp | rain ambience in |
| A1-S2 | 1:46 | (comp) | g-a1-home (Sonnet, base copy) | |
| A1-S3 | 2:02 | (comp, full-frame beige ×2) | g-a1-forecast (Sonnet) | |
| A1-S4 | 2:13 | (comp) | g-a1-hardrain (Sonnet) | thunder hit on the flash |
| A1-S5 | 2:39 | (comp) | g-a1-synoptic (Opus O3) | |
| A1-S6 | 3:10 | (comp) | g-a1-gauges (Opus O4) | |
| A1-S7 | 3:40 | (comp) | g-a1-phone (Sonnet, base copy) | phone ring (GAP 5) |
| A1-S8 | 3:54 | (comp) | g-a1-wagon (Sonnet, base copy) | swell "eleven people" |
| A1-S9 | 4:10 | ins-paul-2 (placeholder) | none | rain ducks under him |
| A1-S10 | 4:18 | g-a1-flee-a (car stops) → `media/src/V03/Aerial_View_of_Tyro_(7797534024).jpg` (6 s) | g-a1-flee-a (Opus O5) · g-a1-cattle (Sonnet, glass quote over V03) | swell "engine flooded" |
| A1-S11 | 4:32 | (comp) | g-a1-flee-b (Opus O5) | |
| A1-S12 | 4:46 | (comp) | g-a1-davis (Opus O1, pull-out, Davis Creek glows) | stamp "2:50 AM" + chip "POWER AND PHONES OUT" in rail |
| A1-S13 | 4:59 | photo inside comp: `LVA/Massies_Mill_Bridge,_II_(7797542906).jpg` (aerial, Rt. 56 bridge over the Tye) | g-a1-peak (Sonnet) channel trace + chip | |
| A1-S14 | 5:12 | (comp) | g-a1-hydro (Sonnet) | swell "eight times" |
| A1-S15 | 5:21 | (comp) | g-a1-staff (Sonnet) | |
| A1-S16 | 5:27 | (comp) | g-a1-eight (Sonnet, base copy: Rockfish + James drawn, 8 markers; a different frame from g-i1-eight) | |
| A1-S17 | 5:32 | `media/src/V01/Massies_Mill_(7797544864).jpg` (6 s) → `media/src/V02/Church_in_Massies_Mill_(7797536534).jpg` (6 s) | none | popfig "AUG 20, 1969" sub "daybreak"; src "USGS Open-File Report 70-51"; rain thins |
| A1-S18 | 5:45 | `LVA/Rt._56_over_Tye_River_(7797538158).jpg` (1 mi east of Massies Mill) | none | name chips "Warren Raines, 14" then "Carl Raines, 16" |
| A1-S19 | 5:53 | `media/src/V04/Tye_River_at_Norwood_(7797540690).jpg` darkened (≤ 5 s) → full-frame card | g-a1-letgo (Sonnet, beige quote, held about 5 s after the line) | `hold-a1-s19` on track 8 for the card read; rain out on the card's last word; NO swell. `bo-2` |
| A2-S1 | 6:03 | g-a2-davis (first sentence) → `media/src/V06/Mudslides_in_Nelson_(7797546600).jpg` on "That night, the ground" | g-a2-davis (Opus O1) | bed-a2 in |
| A2-S2 | 6:16 | (comp) | g-a2-hollows (Opus O1, base copy: dark house icons, "Huffman's Hollow" text label only, no pin) | |
| A2-S3 | 6:20 | (comp) | g-a2-mawyer (Opus O6) | swell "fast" |
| A2-S4 | 6:38 | ins-paul-3 (placeholder) | none | |
| A2-S5 | 6:46 | (comp; starts on black) | g-a2-roar (Sonnet) | rumble bed rising |
| A2-S6 | 7:01 | (comp) | g-a2-clock (Sonnet) | |
| A2-S7 | 7:16 | (comp) | g-a2-anatomy (Opus O6) incl. PP 804 title card | |
| A2-S8 | 7:42 | photo inside comp: `media/src/V23/pp804-p26-fig12.jpg` | g-a2-scar (Opus O7) | swell "ten feet across" |
| A2-S9 | 8:06 | (comp) | g-a2-surge (Opus O6) | swell "five feet in twenty minutes" |
| A2-S10 | 8:21 | (comp continues) | g-a2-surge tail: Camp and Miller beige card over the slowed surge | |
| A2-S11 | 8:31 | `media/src/V05/Lovingston_Damages_(7797544338).jpg` (≤ 6 s) → `LVA/Home_Collapsed_in_Howardsville_(7797528336).jpg` | g-a2-gamble (Sonnet, glass quote + chip spanning both) | no place label over the second still |
| A2-S12 | 8:42 | `LVA/Debris_and_Damages_in_Nelson_(7797538826).jpg` → `LVA/Damaged_Belongings_in_Howardsville_(7797528010).jpg` | g-a2-raynor (Sonnet, glass quote) | no faces, no bodies |
| A2-S13 | 8:58 | (comp) | g-a2-houses (Sonnet) spans S13 to S15 | swell "two" |
| A2-S14 | 9:04 | (comp) | g-a2-houses | |
| A2-S15 | 9:09 | (comp) | g-a2-houses | |
| A2-S16 | 9:15 | WDBJ clip b-roll of the Davis Creek road (outside the bite, muted) | g-a2-harvey (Opus O12) lower third starts here | GAP 2: clip not on disk |
| Harvey | 9:21 | `ins-a2-harvey` = WDBJ bite about 103 to 109 s of source, own audio (`data-volume="1" data-has-audio="true"`), cut on her last word | g-a2-harvey (Opus O12) caption host `data-caption-for="ins-a2-harvey"` | narration silent; bed to 0.05; circle off |
| A2-S17 | 9:28 | WDBJ b-roll of the road (same file, other range, muted) | g-a2-harvey tail (lower third out) | |
| A2-S18 | 9:34 | (comp) | g-a2-sissy (Sonnet) | |
| A2-S19 | 9:46 | hold stills: `LVA/Along_Rt._29_(7797534372).jpg` (6 s) → `LVA/West_of_Rockfish,_II_(7797547244).jpg` (6 s) → `LVA/Overturned_Home_in_Nelson_(7797538480).jpg` (≤ 6 s) | g-a2-oakhill (Sonnet: cite card S19, chip S20) | bed out; creek ambience (GAP 6). No place label on any still (captions: north Lovingston, west of Rockfish, Rt. 655) |
| A2-S20 | 10:02 | `media/src/V23/pp804-p42-fig22.jpg` (eroded mountain channels) | g-a2-oakhill chip | |
| A2-S21 | 10:11 | `LVA/Damaged_Homes_along_the_Rockfish_River_(7797551880).jpg` slow fade toward black | none (no text) | fade; `bo-3` |
| A3-S1 | 10:25 | `LVA/Debris_along_Rt._29_(7797546164).jpg` (5 s, hard in) → comp | g-a3-cutoff (Opus O8) | popfig "AUG 20, 1969" over the still only; swell "cut off" |
| A3-S2 | 10:49 | `LVA/Bridge_Out_in_Amherst_(7797517316).jpg` (Amherst, Rt. 29 over the Buffalo: Tinsley's county) → `LVA/Black_Creek_Washed_Out_Bridge_(7797535922).jpg` | g-a3-tinsley (Sonnet, glass quote lands after "check which roads were open") | |
| A3-S3 | 11:05 | `LVA/Bridge_Out_to_Rural_Home_(7797551428).jpg` → `LVA/Rescue_Mission_Planning_(7797540124).jpg` | g-a3-whitehead (Sonnet, glass quote on "not a rescue") | |
| A3-S4 | 11:20 | `media/src/V01/Massies_Mill_(7797544864).jpg` with `data-callback="return to Massies Mill, first shown A1-S17, about 5.5 min apart"`, different crop → comp | g-a3-ginger-a (Opus O9: map, Tye drawn, unlabelled marker at Massies Mill) | |
| A3-S5 | 11:31 | (comp) | g-a3-missing-a (Sonnet) | |
| A3-S6 | 11:40 | ins-paul-4 (placeholder) | none | chip "110+ MISSING · AUG 23 · AP" + src "Associated Press, Aug 23, 1969 (The Pontiac Press, p. 1)" over Paul (allowed: text over him) |
| CTA | 11:48 | `bo-cta-in` 1.0 → `ins-cta-paul` 24.042 → `bo-cta-out` 1.0 | none | narration silent, bed out, circle off |
| A3-S7 | 12:14 | `media/src/V10/Rescue_Mission_Briefing_(7797539862).jpg` (real, about 2.5 s, hard cut after `bo-cta-out`) → comp | g-a3-missing-b (Sonnet) | swell "eighty-nine" |
| A3-S8 | 12:29 | `LVA/Flood_Damage_East_of_Schuyler_(7797526964).jpg` → comp | g-a3-heli (Sonnet, cutoff base copy: helicopter over the Blue Ridge + AP beige card) | GAP 14: no helicopter photo |
| A3-S9 | 12:49 | comp → `media/src/V12/Raging_Waters_of_the_James_(7797523300).jpg` (Richmond: no place label) | g-a3-ginger-b (Opus O9) | swell "twenty miles away". GAP 3: VCU reel V16 (moving water) preferred over V12 |
| A3-S10 | 13:08 | (comp) | g-a3-nov13 (Sonnet) | |
| A3-S11 | 13:19 | (comp) | g-a3-counts (Sonnet) | swell "don't agree" |
| A3-S12 | 13:48 | (comp) | g-a3-list (Opus O10) spans S12 to S14 | |
| A3-S13 | 14:05 | (comp) | g-a3-list | swell "never found" |
| A3-S14 | 14:27 | (comp) | g-a3-list | `hold-a3-s14` 2 to 3 s after "names?", then `bo-4` |
| A4-S1 | 15:20 | (comp) | g-a4-vdh (Sonnet) | boom on "eight people" |
| A4-S2 | 15:41 | (comp) | g-a4-screens (Sonnet) | GAP 7: screenshots |
| A4-S3 | 16:07 | (comp) | g-a4-stacks (Sonnet) | |
| A4-S4 | 16:20 | (comp) | g-a4-list (Sonnet, list card over the base map with the 8 markers) | |
| A4-S5 | 16:38 | (comp) | g-a4-eight (Opus O11) spans S5 to S10, LVA photos as figure insets | |
| A4-S6 | 16:51 | (comp) | g-a4-eight (Newell lower third inside the comp) | |
| A4-S7 | 17:03 | inset in comp: `media/src/V08/Rockfish_River_Flood_Plain_(7797531654).jpg` | g-a4-eight | |
| A4-S8 | 17:14 | inset: `media/src/V09/Howardsville_Bridge_Out_(7797526062).jpg` | g-a4-eight | |
| A4-S9 | 17:26 | inset: `media/src/V07/Schuyler_Dam_and_Bridge_(7797545198).jpg` | g-a4-eight | |
| A4-S10 | 17:37 | (comp) | g-a4-eight | bed drops out under the last sentence |
| A4-S11 | 17:47 | (comp) | g-a4-files (Sonnet, eight-map base copy) | |
| A4-S12 | 18:18 | `media/src/V11/Scottsville_Aerial_View_(7797532376).jpg` (6 s) → `LVA/Rt._603_Flooding_(7797532996).jpg` (Goochland, James) → `LVA/Traffic_on_I-95_after_Camille_(7797524116).jpg` | g-a4-newell (Sonnet, quote lower third spanning the stills) | no place label over the stills |
| A4-S13 | 18:33 | `LVA/Woods_Mill_Aerial_View_(7797532016).jpg` (Rt. 29 at Woods Mill) → `LVA/Debris_on_Rockfish_River_(7797550188).jpg` | none | chip "62 TO 74 TODAY" |
| A4-S14 | 18:45 | ins-paul-5 (placeholder) | none | room tone only, no swell |
| A4-S15 | 18:54 | (comp) | g-a4-contact (Sonnet) | |
| A4-S16 | 19:02 | (comp) | g-a4-open (Sonnet, base copy: 8 unlabelled markers, stamp "October 2026" in rail) | score fades toward the close |
| Z1-S1 | 19:08 | (comp) | g-z1-night (Opus O6) | swell "until about four" |
| Z1-S2 | 19:30 | `LVA/The_James_and_Rockfish_Rivers_(7797547848).jpg` (the confluence; ≤ 4 s) → comp | g-z1-headings (Sonnet, eight-map base copy + the three headings card) | |
| END-ASK | 19:39 | ins-paul-e1 → ins-paul-e2 | none | close bed; circle off |
| Z1-S3 | 19:55 | (comp) | g-z1-close (Sonnet) | narration only, circle off; card ≤ 3 s past the last word |

Segments mapped: 86 script segments (H1 1, T1 2, I1 10, A1 19, A2 21, A3 14, A4 16, Z1 3) + the Harvey insert + CTA + END-ASK = 89 rows.

### 2.1 Shot ledger (files used more than once, or same-subject pairs)
| File | Uses | Rule |
|---|---|---|
| V01 Massies_Mill | A1-S17, A3-S4 | callback, about 5.5 min apart, `data-callback` |
| V10 Rescue_Mission_Briefing / V13 Rescue_Mission_Planning | A3-S7 / A3-S3 | same subject family, non-adjacent (CTA between) |
| West_of_Rockfish / West_of_Rockfish,_II | I1-S6 / A2-S19 | same family, different acts |
| WDBJ clip | A2-S16, Harvey, A2-S17 | one source, three ranges, never the same frames |
No other file repeats. The Picture lines' own repeats (V01 at I1-S10, A1-S13, A1-S17, A3-S4; V05 at A2-S11, A2-S12, A3-S1; V03 at
A1-S10 and A2-S19) are resolved by the substitutions above. The Picture line for A2-S19 calls V03 "fatal mudslides in Nelson": that
caption belongs to `LVA/Along_Rt._626_(7797531010).jpg`, not V03 (Tyro, Rt. 56): read the provenance row, not the alias.

---

## Part 3 · Graphic list

Chain of command (CLAUDE.md): deep graphics by Opus 5.5 at high effort or above; the rest by Sonnet 5.5 at high effort with the brief
below. The builder never verifies its own work; the orchestrator reads a settled frame of every graphic over its real footage before any
render. A Sonnet graphic that fails the read twice goes to Opus. Every builder's brief carries `references/mg-quickref.md` and
`library/inhouse/snippets/tokens.md`.

### 3.1 Opus (12 lanes, 24 comps incl. the unmounted base)
| Lane | Comp(s) | Purpose (one line) | Start from |
|---|---|---|---|
| O1 | g-base-nelson (base, never mounted) → g-i1-tye, g-a1-river, g-a1-davis, g-a2-davis, g-a2-hollows | the episode's one Nelson County map: real county outline, Tye/Rockfish/James/Davis Creek, Rt. 56 and U.S. 29, camera pushes and pull-outs | `library/inhouse/master-map-us-canada.html` (projection, camera rig), `references/editing-patterns/ep3-map-route-fit.html`, `ep5-terrain-map.html` |
| O2 | g-t1-track, g-i1-track | Camille's track from the Gulf to Virginia, push in to Nelson; landfall at Waveland; inland crawl losing its eye | `library/inhouse/master-map-us-canada.html` |
| O3 | g-a1-synoptic | why it rained there: remnant over Kentucky at 8 PM, storm band from N/NW already over Virginia, center crosses near midnight, SE moist inflow | `master-map-us-canada.html` + `references/editing-patterns/ep2-met-explainer.html` |
| O4 | g-a1-gauges | the gauge that overflowed at 11+, the bucket before 2 AM, the trash containers, two nearby readings 4× apart | `library/inhouse/numbers-rollup.html` + `quote-card.html` |
| O5 | g-a1-flee-a (A1-S10 part), g-a1-flee-b (A1-S11) | the station wagon stops past the house as the Tye floods the road; on foot along Rt. 56; two dots by two trees | g-base-nelson + `library/inhouse/moves/demo.html` (camera rig) |
| O6 | g-i1-slope, g-a2-mawyer, g-a2-anatomy, g-a2-surge, g-z1-night | the debris-avalanche cross-section family: a strip of soaked soil lets go, how it starts, where, what it does in the creek, the night it kept happening | `library/inhouse/radar-beam.html` (full-frame SVG physics diagram) |
| O7 | g-a2-scar | a real PP 804 scar measured: width, length (football fields), depth, boulder vs pickup, the 40 sq mi zone south of Horseshoe Mountain | g-base-nelson + `library/inhouse/split-shared-scale.html` (scale objects) |
| O8 | g-a3-cutoff | Nelson cut off: roads grey out, radio arc over the Blue Ridge to Augusta County, relayed to Richmond | g-base-nelson (pull-out) |
| O9 | g-a3-ginger-a, g-a3-ginger-b | an unlabelled marker waits at Massies Mill (A3-S4), then runs 20 river-miles down the Tye (A3-S9) | g-base-nelson |
| O10 | g-a3-list | the 2019 list of 125: The dead (84), The missing (33, Wood rows amber, 19 Davis Creek rows), The unidentified (8, text softened) | `library/inhouse/bulletin-typewriter.html` (document reconstruction) + `event-timeline.html` (scroll rail) |
| O11 | g-a4-eight | the eight found and never named: U.S. 29, each find place on its river with a photo inset, down the James into Fluvanna, 4 of 8 children | g-base-nelson |
| O12 | g-a2-harvey | the WDBJ Harvey bite made transformative: framed clip with her own audio, karaoke running caption, locator map, lower third | `git show 64330f03:episodes/ep-joplin-2011/compositions/g-a6-radio-cap.html` and `g-a1-ksn-cap.html` |

### 3.2 Sonnet (42 comps)
| id | Seg | Purpose | Start from |
|---|---|---|---|
| g-t1-33 | T1-S1 | "33 never found" lands over the Massies Mill aerial | `references/editing-patterns/ep6-glasscard-popfig-bfmg.html` |
| g-i1-gulf | I1-S1 | glass bar "Gulf Coast · 143 · NWS" over M01 footage | `library/inhouse/ranked-bars.html` (one rail) |
| g-i1-rain | I1-S3, I1-S4 | rain counter 0 → 27 in with "about 8 hours" clock, freezes, the trash-barrel table row | `library/inhouse/numbers-rollup.html` + `quote-card.html` |
| g-i1-pmp | I1-S5 | probable-maximum cite card, then one gauge filled to about four-fifths | `quote-card.html` + `stat-timeline.html` (progress rail) |
| g-i1-blunt | I1-S6 | glass quote: PP 804 blunt-force finding over the mudslide photo | `ep6-glasscard-popfig-bfmg.html` |
| g-i1-hundred | I1-S8 | 100 small figures, one turns amber, beside Nelson's outline | g-base-nelson copy |
| g-i1-eight | I1-S9 | Nelson outline, eight unlabelled markers | g-base-nelson copy |
| g-a1-home | A1-S2 | two small squares beside the Tye: the Raines house, the Wood family; name chips | g-base-nelson copy |
| g-a1-forecast | A1-S3 | two beige quote cards in sequence (Halverson; McGinnis) | `quote-card.html` (this is the quote-card FAMILY BASE: build first, full-size read, then copy) |
| g-a1-hardrain | A1-S4 | white flash, map goes dark and wet, rain counter climbs with no numbers, "Hard rain" chip, Evans quote | g-base-nelson copy + family base |
| g-a1-phone | A1-S7 | phone icon rings once at the Raines square; stamp "2 AM · Aug 20"; chip | g-base-nelson copy |
| g-a1-wagon | A1-S8 | figures cross from the Wood square; chip "11 IN ONE STATION WAGON"; Warren quote | g-base-nelson copy |
| g-a1-cattle | A1-S10 | glass quote over the Tyro aerial | family base, glass |
| g-a1-peak | A1-S13 | trace the Tye channel on the Massies Mill aerial; chip "≈ 70,000 CU FT / SECOND" | `ep6-glasscard-popfig-bfmg.html` |
| g-a1-hydro | A1-S14 | old 31-year record vs the 1969 peak, to scale (8×); "gage destroyed by flood" card; stamp "4 AM" | `ranked-bars.html` (vertical) |
| g-a1-staff | A1-S15 | gauge staff: 13.7 ft (1944) vs 29.0 ft (Aug 20, 1969), to scale | `then-now-scale.html` |
| g-a1-eight | A1-S16 | county map with the Rockfish and James drawn, eight unlabelled markers | g-base-nelson copy |
| g-a1-letgo | A1-S19 | full-frame beige quote, Warren Raines, WTKR, held 5 s | family base |
| g-a2-roar | A2-S5 | black, then beige quote "squadron of airplanes", then a ring spreading over the hollows map | family base + g-base-nelson copy |
| g-a2-clock | A2-S6 | slim timeline under the map, slide marks closer together, two after "about 4 AM"; chip "ABOUT 3 MINUTES" | `stat-timeline.html` |
| g-a2-gamble | A2-S11 | glass quote (PP 804 on Gamble) + chip "MULTIPLE FRACTURES" | family base, glass |
| g-a2-raynor | A2-S12 | glass quote, Dr. Robert Raynor (rings) | family base, glass |
| g-a2-houses | A2-S13 to S15 | 25 house icons, 23 fade, "2 OF 25"; counters 27 and 22 missing; then 52 line and "Huffman · 18" | `numbers-rollup.html` |
| g-a2-sissy | A2-S18 | one list row on a beige card, heading "The missing"; chip "Davis Creek · 19 never found" | family base |
| g-a2-oakhill | A2-S19, S20 | OFR 99-518 cite card over the hold stills; then the chip | family base, glass |
| g-a3-tinsley | A3-S2 | glass quote, Ed Tinsley | family base, glass |
| g-a3-whitehead | A3-S3 | glass quote, Dick Whitehead | family base, glass |
| g-a3-missing-a / -b | A3-S5 / A3-S7 | two-column counter KNOWN LOST / MISSING: 100+ (Aug 22); then 110+ → 109 → 89, KNOWN LOST arrow only | `numbers-rollup.html` (build -a, then copy to -b) |
| g-a3-heli | A3-S8 | helicopter icon crosses the Blue Ridge into the cut-off county; chip; AP beige card | g-a3-cutoff copy (after O8's base read) |
| g-a3-nov13 | A3-S10 | Virginia outline, two bars 113 and "39 still missing", Encyclopedia Virginia card | `ranked-bars.html` |
| g-a3-counts | A3-S11 | four number cards, each with what it counts; 125-in-Nelson inset; ghost tag | `split-shared-scale.html` (cards never merged) |
| g-a4-vdh | A4-S1 | typeset VDH media-update card, "generate new leads" highlight, chip "NO AGES · NO NAMES" | family base |
| g-a4-screens | A4-S2 | three captured screens (VDH post as in CBS19, NamUs case page), Newell quote lower third | `ep6-glass-panel-camera-clamp.html` |
| g-a4-stacks | A4-S3 | two stacks never merged: 33 never found / 8 found, never named; date strip | `split-shared-scale.html` |
| g-a4-list | A4-S4 | beige list card "The unidentified" over the base map, eight markers return | family base + g-base-nelson copy |
| g-a4-files | A4-S11 | chips beside the eight markers: autopsy 1969, dental charts, cremated, no DNA test | g-a4-eight copy |
| g-a4-newell | A4-S12 | small verbatim quote lower third, Newell, 29News | family base, lower third |
| g-a4-contact | A4-S15 | clean contact card, OCME Central District email, held ≥ 4 s | `title-card.html` |
| g-a4-open | A4-S16 | map, 8 unlabelled markers, stamp "October 2026" | g-a4-eight copy |
| g-z1-headings | Z1-S2 | Rockfish into the James, 8 markers (6 Rockfish, 2 James), then the three headings 84 · 33 · 8, chip | g-a4-eight copy |
| g-z1-close | Z1-S3 | close card, THE WARNING HOUR, match-cut on the closing line | `library/inhouse/outro-brand.html` |
(Count: 41 rows, 42 comps: g-a3-missing-a and -b share a row. The quote-card family base is g-a1-forecast.)

### 3.3 Build order and parallel lanes
- **Wave 1, now (geometry needs no audio):** O1 base `g-base-nelson`; O2; O3; O6 family base (g-i1-slope); O10 (typeset the 125 rows);
  Sonnet quote-card family base `g-a1-forecast`; Sonnet stand-alones with no map: g-t1-33, g-i1-gulf, g-i1-rain, g-i1-pmp, g-a1-hydro,
  g-a1-staff, g-a2-houses, g-a3-missing-a, g-a3-nov13, g-a3-counts, g-a4-stacks, g-a4-contact, g-z1-close. All parallel; each builder
  edits only its own `compositions/` file(s); the orchestrator mounts hosts in `index.html` before dispatch.
- **Gate between waves:** the orchestrator reads `g-base-nelson` at full size (a family built on one base: base read first), and the
  quote-card family base. Cues get filled the moment each segment's `words.json` lands.
- **Wave 2:** O1 instances, O4, O5, O7, O8, O9, O11 (all need the base); O6 variants; every Sonnet base copy (g-i1-hundred, g-i1-eight,
  g-a1-home, g-a1-hardrain, g-a1-phone, g-a1-wagon, g-a1-eight, g-a2-roar), every glass/beige quote copy.
- **Wave 3 (after their parents):** g-a3-heli (after O8), g-a4-files / g-a4-open / g-z1-headings / g-a4-list (after O11).
- **Blocked by files:** O12 g-a2-harvey (WDBJ clip, GAP 2); g-a4-screens (GAP 7).
- Heavy jobs (snapshots, gates) on the ZBook; no gates or browsers beside a render.

---

## Part 4 · Briefs

### 4.0 Shared contract for every brief (template §6 to §8, not restated per brief)
- **MAP SCALE CHANGED (O1 built, 22 Oct 26 13:36, orchestrator-read):** k = 1480 px/deg lat, kx = 1170.1 px/deg lon, 1 mi = 21.45 px, 5 MI bar = 107.25 px. Formula below with these numbers wins. Place px for every map comp: `media/geo/nelson-px.json` (never re-project by hand). Base file: `compositions/g-base-nelson.html`, camera group `#g-base-nelson-cam`.
- §6 CONTRACT: `references/mg-brief-template.md` §6 verbatim. File `compositions/<id>.html`, root `id="<id>-root"` (never `#root`),
  `data-composition-id="<id>"`, paused timeline at `window.__timelines["<id>"]`, ids prefixed with the comp suffix, root transparent
  unless the brief says full-frame ground. Type and motion: `references/mg-quickref.md` "Type tiers", "Motion and exits"; colours by
  name from `library/inhouse/snippets/tokens.md` "Palette" (river lines = Cold blue 2, highlight = Amber 1, danger = Danger red 1,
  ground = BG gradient, cite card = Beige cite card). Text-safe margin 96 px left/right, 54 px top/bottom. **Corner x ≥ 1600, y ≥ 680
  stays empty in every comp** (the presenter circle sits there). Every cue is written as `/* WORD @<s> */` from `audio/<seg>.words.json`
  (Whisper writes digits: cue on "33", not "thirty-three"). Comp time 0 = host `data-start` = the segment's first word unless the brief says otherwise.
- §7 TOOLS and §7a DONE LINE: template §7, §7a verbatim (graphics_qc 0 errors, sweep/blank_scan/overlap/occlusion not naming your comp,
  fill figure, frame 0, seek order, no label under a line, shared numbers computed by script and stated, overlay frame over the real picture).
- §8 RECEIPT: template §8 (≤ 15 lines).
- Source lines are small-tier text in the source-credit corner (bottom-left, x ≥ 96, y ≤ 1026), one per window.
- Map geometry (used by every map comp, O1 owns it): stage 1920 x 1080, equirectangular, origin lon −78.85, lat 37.76, k = 1900 px per
  degree latitude, 1502 px per degree longitude (k · cos 37.76°): `x = 960 + (lon + 78.85) · 1502`, `y = 540 − (lat − 37.76) · 1900`.
  At this zoom 1 mile ≈ 27.5 px (1900 / 69.0). Data: Nelson County outline from Census TIGER/Line 2020 counties (FIPS 51125) and
  its neighbours Albemarle 51003, Amherst 51009, Augusta 51015, Buckingham 51029, Fluvanna 51065; rivers from USGS NHD flowlines
  (Tye River, Rockfish River incl. South and North Forks, James River, Davis Creek, Piney River); roads from TIGER primary/secondary
  roads (U.S. 29, VA 56, Rt. 151); place points from USGS GNIS: Massies Mill, Tyro, Lovingston, Woods Mill, Schuyler, Rockfish,
  Howardsville, Wingina, Norwood, Arrington, Horseshoe Mountain, Bremo Bluff. Downloads are free federal data; save them under
  `episodes/ep-camille-1969/media/geo/` with a provenance row each. Coordinates are converted to px by a script (template §7a item 6),
  printed in the receipt, never placed by eye. If the Nelson outline does not fit inside x 400 to 1440, y 110 to 980, change k once
  and report the new k to the orchestrator before any copy is made.

### O1 · g-base-nelson (+ instances g-i1-tye, g-a1-river, g-a1-davis, g-a2-davis, g-a2-hollows) · Opus 5.5, high
- **0. Claim.** The story happened in one small mountain county: the Tye on its west side (Massies Mill), the Rockfish on its north
  and east (Davis Creek, Woods Mill, Schuyler), both draining to the James on its southeast edge. The map is honest geography the
  rest of the episode builds on.
- **1. Source.** TIGER/Line 2020 counties and roads, USGS NHD flowlines, USGS GNIS points (Shared contract). Cross-check against
  `media/src/V21/ofr99-518-nel_map-72dpi.png` (USGS map, Lovingston and Horseshoe Mtn quadrangles) and OFR 70-51 Fig. 4 caption
  "Davis Creek, 5 miles north of Lovingston" (`media/src/V22/ofr70-51.pdf`).
- **2. Datum, scale, orientation.** The Shared contract projection. North up. A 5-mile scale bar, 137.5 px, bottom-left at
  (96 to 233.5, 1000), label "5 MI". Base ground = BG gradient; neighbour counties drawn at 25 % stroke, no fill.
- **3. Geometry.** Nelson outline stroke 2 px Label grey; rivers 3 px Cold blue 2 (James 5 px); Davis Creek 2 px; roads 1.5 px Diagram
  grey 1 (U.S. 29 labelled "U.S. 29", VA 56 "RT. 56"). Labels beside their feature, never on a line. Camera = one `<g>` with
  transform; pushes over 1.5× use `logZoom` (`library/inhouse/snippets/helpers.js`). Rail (top-left, x 96 to 700, y 54 to 200) holds the
  date/time stamp for every instance (Abril-style figure in the comp, since no index popfig may sit over a map).
  Instances (each its own file, copied from the base after the orchestrator's base read):
  - g-i1-tye (I1-S10, about 9.9 s): from the county view push west to the Tye at Massies Mill (zoom about 3×, logZoom), Tye line
    brightens, rail stamp "Aug 19, 1969 · night", place label "Massies Mill". The comp ends on "With them that night" with a camera settle (never a hard
    vanish); the LVA still takes over there.
  - g-a1-river (A1-S1, about 8.8 s): Massies Mill close view (same zoom as g-i1-tye's end), Tye and Rt. 56 side by side, rail stamp
    big "Aug 19, 1969" sub "Tuesday · 7 PM · Massies Mill", rain texture (thin diagonal strokes, GSAP-driven, finite repeats) over the
    map, label "Tye River", "Rt. 56" land on their words.
  - g-a1-davis (A1-S12, about 13.2 s): rail stamp "2:50 AM" + chip "POWER AND PHONES OUT" on "ten to three"; pull out from the Tye to
    the whole county (logZoom); the Rockfish draws in (north), then Davis Creek glows Amber 1 with label "Davis Creek" on "Davis Creek".
    Davis Creek is drawn on the Rockfish side, never as a Tye tributary.
  - g-a2-davis (A2-S1 first sentence): county view pushes east to Davis Creek and Woods Mill; creek in thin blue with small hollows
    branching off (the NHD first-order tributaries of Davis Creek); stamp "Davis Creek · Woods Mill" + "night of Aug 19, 1969".
  - g-a2-hollows (A2-S2): same view; small house icons in the hollows, dark (no lit windows); text label "Huffman's Hollow" beside
    the Davis Creek label, text only, no pin.
- **4. Must be true.** (1) Davis Creek joins the Rockfish system, never the Tye. (2) Massies Mill sits on the Tye; Woods Mill and
  Schuyler on the Rockfish; Howardsville at the Rockfish mouth on the James. (3) Davis Creek's mouth area lies about 5 miles (137 px
  ±15 %) north of Lovingston. (4) The James runs along the southeast edge. (5) Scale bar = 137.5 px = 5 mi. (6) Corner x ≥ 1600,
  y ≥ 680 empty. (7) No label sits on a river or road line.
- **5. Text and cues.** Exact labels above. Cues: g-i1-tye "Tye River" and "Massies Mill" in I1-S10; g-a1-river "seven" (stamp),
  "Tye River", "Route 56"; g-a1-davis "three" (stamp), "Davis Creek"; g-a2-davis "Davis Creek", "Woods Mill"; g-a2-hollows "Huffman's".

### O2 · g-t1-track, g-i1-track · Opus 5.5, high
- **0. Claim.** Camille came ashore on the Mississippi coast late on 17 Aug 1969, crossed Mississippi, Tennessee, Kentucky and West
  Virginia, and two nights later its remnant crossed into Virginia, no longer a hurricane, over the mountains of Nelson County.
- **1. Source.** HURDAT2 Atlantic best track, storm AL091969 (NOAA NHC, free): every 6-hourly point and intensity flag. Landfall
  Waveland MS, 11 PM CDT 17 Aug (N1); tropical depression from 19 Aug 0600 UTC (factcheck-B). Cross-check
  `media/src/V24/camille1969trk.gif` (WPC track map).
- **2. Datum, scale, orientation.** Projection and states from `library/inhouse/master-map-us-canada.html` (Natural Earth admin-1).
  North up. Wide view frames the Gulf coast to Virginia; end view = Nelson County at the base-map framing so g-i1-tye can continue it.
- **3. Geometry.** Track line 4 px, drawn by strokeDashoffset over the real points; storm symbol (hurricane glyph) rides the path
  head, asserted on the path at three times. Symbol style follows HURDAT2 status: hurricane glyph with an eye while status = HU,
  shrinks and loses the eye at the TS point, a plain low circle at TD. Waveland marker + label "Waveland, Miss.". Nelson County
  outline from O1 data; rivers thin blue; label "Nelson County, Virginia".
  - g-t1-track (T1-S2, 7.73 s): track draws Gulf → Virginia, then push in to Nelson County (logZoom), rivers draw, label; on "how"
    a small rain-gauge glyph at "0.0 in" appears (not running).
  - g-i1-track (I1-S1 second clause + I1-S2): Waveland marked with rail stamp big "AUG 17, 1969" sub "11 PM"; then the crawl inland
    across MS, TN, KY, WV with the symbol shrinking and losing its eye; rail chip "TWO NIGHTS LATER" on "Two nights later". No
    Virginia number anywhere in this comp.
- **4. Must be true.** (1) Every track vertex is a HURDAT2 point (script-converted, listed in the receipt). (2) The eye disappears
  where HURDAT2 drops below hurricane status, never earlier or later. (3) Waveland marker is on the coast of Hancock County MS.
  (4) The track reaches Virginia south of Roanoke and Lynchburg (OFR 70-51 p. 5). (5) No number for Virginia appears.
- **5. Cues (T1-S2 words.json on disk).** "Hurricane" @0.58 track starts drawing; "Nelson" @2.52 push-in starts; "Virginia" @4.06 rivers
  + label; "how" @5.52 gauge glyph; comp ends 7.73 (hold settles ≥ 1 s before cut, never cut on motion). I1 cues from i1-s1/i1-s2 words.json.

### O3 · g-a1-synoptic · Opus 5.5, high (A1-S5, about 31.6 s)
- **0. Claim.** At 8 PM Camille's remnant was still over Kentucky; the rain over Nelson County was already falling from a band of
  storms that had come in from the north and northwest; near midnight the center crossed into Virginia south of Roanoke and
  Lynchburg and intensified, drawing moist air from the southeast, and rain along the Blue Ridge's western slopes increased fast.
- **1. Source.** OFR 70-51 p. 5 (V14, quoted in the script Rows); PP 804 p. 4 (V15); HURDAT2 20 Aug 0000 UTC 84.0W (factcheck-B 1).
- **2. Datum, scale.** master-map-us-canada projection, frame Kentucky to the Virginia coast; Blue Ridge drawn as a thin ridge line
  from Natural Earth or a USGS physiographic boundary (cite in receipt).
- **3. Geometry.** Remnant swirl (spiral glyph, slowly rotating) at the HURDAT2 20 Aug 00Z point; rail stamp "8 PM". Amber band of storm
  cells already over Virginia entering from N/NW (schematic band, label "storms from the north"). Stamp "near midnight": the swirl moves
  along HURDAT2 into Virginia on a line south of Roanoke and Lynchburg (both labelled) and tightens (scale 0.85). Soft Cold-blue shading
  southeast of Nelson drifting northwest toward it, label "moist air from the southeast". Nelson outline + Tye; a small marker "Raines
  house" fades in on "the Tye ran right past the Raines house". Source line "USGS Open-File Report 70-51 · USGS Professional Paper 804,
  after Schwarz 1970".
- **4. Must be true.** (1) At "8 PM" the swirl is west of Virginia (Kentucky). (2) The storm band is over Virginia BEFORE the swirl
  arrives. (3) The swirl's path into Virginia passes south of both Roanoke and Lynchburg. (4) The inflow arrow points from SE toward
  Nelson. (5) No label says the Blue Ridge "caused" the rain (V16). (6) **The script's label "about 3,000 ft deep" has no quoted row:
  do NOT draw it unless the orchestrator confirms the figure in PP 804 p. 4; use "moist air from the southeast".**
- **5. Cues.** "eight that evening" stamp + swirl; "band of heavy storms" band; "Near midnight" stamp + move; "southeast" shading;
  "Raines house" marker; "rain gauge" ends (exit = settle, then cut).

### O4 · g-a1-gauges · Opus 5.5, high (A1-S6, about 29.4 s)
- **0. Claim.** The one recording gauge stopped at 11 inches because it overflowed; a bucket overflowed before 2 AM; most readings came
  from containers; and four times the survey found over 20 inches with under 6 inches less than 5 miles away.
- **1. Source.** OFR 70-51 Table 1 rows (render the rows from `media/src/V22/ofr70-51.pdf` p. 11; text verbatim from the script Rows):
  "WB Recorder · 11+ · Gage overflowed"; "11" bucket · Bucket overflowed before 2 a.m."; "Barrel", "Street trash container", "Plastic
  garbage container". PP 804 reporting Schwarz 1970: "for each of four observations of over 20 inches total rainfall, less than 6
  inches was measured at a location less than 5 miles away".
- **2. Datum.** Left 60 %: the counter and table rows; right 40 % (x 1150 to 1560, never past y 680 into the corner): a schematic
  terrain strip with a 5-mile scale bar of 137.5 px (base-map scale), label "SCHEMATIC".
- **3. Geometry.** Gauge glyph (the episode's rain-gauge from g-i1-rain, same drawing) climbs with NO numbers, then jams at "11+" and
  blinks (3 finite blinks). Beige row card 1 slides in; row card 2 below; then three short rows "Barrel" · "Street trash container" ·
  "Plastic garbage container" pop in 0.4 s apart. Then two dots on the strip, 110 px apart (= 4 mi, under 5), labels "20+ in" and
  "under 6 in" beside (not under) the dots; chip "4 TIMES". Source line "Weather Bureau survey team, reported in USGS Professional Paper 804".
- **4. Must be true.** (1) No hourly or intermediate number ever shows on the gauge. (2) The two dots are < 137.5 px apart with the
  scale bar visible. (3) The dots are not placed on the real county map (no real coordinates exist). (4) Row text is character-exact.
- **5. Cues.** "eleven inches" jam; "overflowed" row 1; "before two" row 2; "sitting outside" three rows; "more than twenty" dot 1; "less
  than six" dot 2; "four separate times" chip; exit after "next hollow's".

### O5 · g-a1-flee-a (A1-S10 part), g-a1-flee-b (A1-S11) · Opus 5.5, high
- **0. Claim.** The station wagon backed out, passed the house and flooded out; eleven people went on foot along Rt. 56 in the dark;
  somewhere on that road Warren grabbed a limb and Carl found a tree of his own.
- **1. Source.** factcheck-A1 marker 5 and S10/S11 (WDBJ, WTKR, C-VILLE RAW quotes in the script Rows).
- **2. Datum.** Base-map close view of Massies Mill (g-a1-river's end framing). The house squares are the same positions as g-a1-home
  (shared numbers: copy them, never re-place). Label "approx." on the house squares is NOT used; positions stay schematic-small (12 px).
- **3. Geometry.** g-a1-flee-a (A1-S10, first sentence only, about 4 s): car icon leaves the Raines square, passes the house by ≤ 1 square
  width and stops dead as the Tye line widens over Rt. 56 (blue widens 3 → 14 px along a 120 px stretch). g-a1-flee-b (A1-S11, copy of -a's end state): eleven small
  figures move along Rt. 56 (GSAP per-leg attr tweens, no MotionPath), the Tye widening toward them; chip "ON FOOT · RT. 56"; figures
  thin to two dots, each beside its own tree symbol; neither tree labelled.
- **4. Must be true.** (1) Car stops just past the house, on Rt. 56. (2) Figures stay on the road line. (3) Two trees, two dots,
  no names on trees. (4) No depth number for the water.
- **5. Cues.** Host 1: "backed out", "engine flooded"; Host 2: "Route", "didn't last", "limb", "tree of his own".

### O6 · slope family: g-i1-slope, g-a2-mawyer, g-a2-anatomy, g-a2-surge, g-z1-night · Opus 5.5, high
- **0. Claim.** On a steep wooded slope above a hollow, a thin strip of soaked soil lets go and comes down into the creek, which then
  surges down the channel with water, mud and rock; people in the hollow were struck by that load. Strips, never whole hillsides.
- **1. Source.** PP 804 (`media/src/V23/pp804.pdf`) pp. 14 to 17 and abstract: slopes > 35 % ; pre-existing depressions; scar top at
  the steepest part; N, NE, E aspects several times as many; surges; "rose about 5 feet in 20 minutes" (p. 5). OFR 70-51 p. 41: typical
  scar 1 to 3 ft deep, 25 to 75 ft wide, 300 to 600 ft long. Photo for the look: `media/src/V23/pp804-p26-fig12.jpg`.
- **2. Datum, scale.** SCHEMATIC, NOT TO SCALE (soil depth exaggerated). Stage full frame. Hollow floor y = 640. Profile (px):
  ridge (300, 220) → (500, 280) [30 %] → (900, 480) [50 %, the steepest] → (1300, 620) [35 %] → floor (1300 to 1700, 640). Creek notch
  x 1330 to 1400, 30 px deep. House x 1450 to 1560 on the floor, 90 px tall. Soil band 24 px thick parallel to the surface. A dip:
  concave notch 8 px deep along x 560 to 860. Small tag "NOT TO SCALE" bottom-left above the source line.
- **3. Geometry.** Strip = soil polygon from x 520 to x 860 along the surface (top at x 520, inside the steepest segment, inside the dip).
  On release it slides down-slope (down-right) along the surface to the creek (per-leg attr tweens), thinning and lengthening.
  Trees: 10 to 14 simple trunks on the strip ride it down and tilt.
  - g-i1-slope (I1-S7): soil darkens with water (colour tween), strip lets go on "let go", runs into the hollow; label "debris avalanche ·
    USGS Professional Paper 804". Ends on a settle; the last 2.5 s of the segment cut to the fig12 photo crop (index).
  - g-a2-mawyer (A2-S3): Mawyer beige card (exact text in the script) top-left; the soil creeps 6 px over 0.4 s ("oozing ... a fraction of a
    second"), holds 0.3 s, then the strip breaks loose on "fast"; a bush glyph just past the strip's edge (his bush), unlabelled.
  - g-a2-anatomy (A2-S7): opens on a title card "Professional Paper 804 · Garnett P. Williams and Harold P. Guy · U.S. Geological
    Survey · 1973" (about 3 s), then the profile with labels landing on their words: "steeper than 35 %" with a rise/run triangle "1 ft up
    for every 3 ft across" drawn on the 35 % segment; the dip glows; "top of the scar: steepest part" pointer at x 520; compass rose at
    (1420, 240) r 90 lights N, NE, E on "north, northeast and east".
  - g-a2-surge (A2-S9 + A2-S10): camera pulls back to the hollow floor; the strip hits the creek and a brown surge with timber runs down
    the channel (rightward, off the floor end x 1700 → frame edge, fading before the margin); then a back-yard gauge staff at (1180 to
    1260, 300 to 600) climbs "about 5 ft in 20 min · Woods Mill"; source line "USGS Professional Paper 804". On A2-S10 the surge slows
    (timeScale 0.4) under a beige card: "the streams rose higher and faster than anyone would have predicted, and left no time for those
    caught in their path to reach safety · Camp and Miller, USGS Open-File Report 70-51 (1970)".
  - g-z1-night (Z1-S1, about 21 s): first the county map at night (O1 base copy): rain gauge glyph near its top, rail clock "about 2:50 AM";
    on "lights" the house dots go dark one by one. Then the cross-section returns dark (BG darker 30 %): strip 1 lets go, then a second
    strip (x 980 to 1180), then a third (x 620 to 820, smaller), while the rail clock runs to "about 4 AM". Label "debris avalanches · USGS
    Professional Paper 804"; source line "USGS Professional Paper 804, pp. 4 to 5, 15 to 16".
- **4. Must be true.** (1) The strip is ≤ 45 % of the slope length (no whole hillside). (2) The strip's top sits on the 50 % segment.
  (3) The rise/run triangle drawn on screen measures 1:3 within 5 %. (4) Debris moves DOWN the slope and then DOWNSTREAM. (5) The house stays
  on the floor; nothing says "asleep". (6) Gauge: 5 ft marked as 5 equal ticks; "20 min" on the label, no clock drawn. (7) Three strips in
  g-z1-night, released one after another, never together.
- **5. Cues.** I1-S7 "soaked slope" darken, "let go" release, "down the creek" run; A2-S3 per its words; A2-S7 "Garnett" title, "thirty-five"
  label, "dips" glow, "steepest" pointer, "north" compass; A2-S9 "creek at the bottom" surge, "five feet" gauge; Z1-S1 "ten to three"
  clock, "lights" houses dark, "letting go" strips, "four" clock.

### O7 · g-a2-scar · Opus 5.5, high (A2-S8, about 24.4 s)
- **0. Claim.** A typical scar is a long thin strip: 25 to 75 ft wide, 300 to 600 ft long (one or two football fields), 1 to 3 ft
  deep; boulders up to 10 ft across came down; the scars are mostly confined to about 40 square miles in the middle of Nelson County,
  just south of Horseshoe Mountain.
- **1. Source.** OFR 70-51 p. 41 (numbers as quoted); PP 804 p. 14 boulders "up to 10 feet"; `media/src/V23/pp804-p26-fig12.jpg` (Fig. 12
  A to C, typical scars, headwaters of Wills Cove); `media/src/V21/ofr99-518-nel_map-72dpi.png` to place the 40 sq mi zone.
- **2. Datum.** Photo panel left (x 120 to 1000, crop ONE of the three Fig. 12 photos, whole, no figure caption cut mid-line). Comparison
  panel right (x 1060 to 1560, y 120 to 640). Football field = 300 ft (field of play) = 160 px in the comparison panel, so 600 ft = 320 px.
- **3. Geometry.** Outline the scar in the photo (Amber 1, 3 px, traced from the visible bare strip). Three measure labels beside the
  outline: "25 to 75 ft wide", "300 to 600 ft long · USGS OFR 70-51", "1 to 3 ft deep"; the labels say "typical", no claim that this scar
  was measured. Football field glyph slides beside a 300-to-600 ft bar (160 to 320 px). Boulder silhouette 10 ft beside a pickup 6 ft tall
  (boulder height = 1.67 × truck height). Then cut to the base map: a shaded patch of 40 sq mi (area 30,250 px² ± 15 % at 27.5 px/mi),
  placed in the middle of the county just south of Horseshoe Mountain per the OFR 99-518 map, label "about 40 sq mi".
- **4. Must be true.** (1) Width : length ratio drawn on the comparison bar is consistent (75 ft ≪ 300 ft). (2) Boulder : truck = 10 : 6.
  (3) Patch area within ±15 % of 30,250 px². (4) Patch lies south of the Horseshoe Mountain label. (5) No "whole hillside" wording;
  PP 804's 200 to 800 ft is not used.
- **5. Cues.** "long strip" outline; "twenty-five" width; "three to six hundred" length + field; "one to three feet" depth; "boulders"
  silhouettes; "forty square miles" map.

### O8 · g-a3-cutoff · Opus 5.5, high (A3-S1, about 19 s after the still)
- **0. Claim.** By morning Nelson was cut off: phones down, roads and bridges gone; the sheriff, trapped in the west of the county, got
  a radio distress call out; Augusta County's sheriff's department, over the Blue Ridge, heard it and passed it to civil defense in Richmond.
- **1. Source.** C-VILLE 14 Aug 2019 RAW; WHSV Part 2 RAW (script Rows). Augusta lies across the Blue Ridge to the northwest (factcheck-A3 S1).
- **2. Datum.** Base map county view, then a pull-out (logZoom) far enough to show Augusta County (NW) and Richmond (E, about 100 mi;
  ≈ 2,750 px at base zoom, so final zoom ≈ 0.45).
- **3. Geometry.** Roads leaving the county grey out one by one (TIGER roads crossing the outline, about 8 to 12), then the county
  sits alone; Blue Ridge crest line on the NW edge (label "Blue Ridge"). A thin radio arc (dashed, animated dash) from the west of the
  county (between Massies Mill and Tyro, unlabelled origin) over the Blue Ridge to an "Augusta County" label; then a straight relay line
  to "Richmond". Chip "CUT OFF" on "cut off".
- **4. Must be true.** (1) Arc crosses the Blue Ridge line. (2) Augusta is NW of Nelson, Richmond E. (3) After the grey-out no road
  crossing the county line stays coloured. (4) No count of missing anywhere.
- **5. Cues.** "cut off" chip; "roads and bridges" grey-out; "radio" arc; "Augusta" label; "Richmond" relay; "missing" settle and exit.
- Wave 3: g-a3-heli (Sonnet) copies this comp's end framing; hand over the camera numbers in the receipt.

### O9 · g-a3-ginger-a, g-a3-ginger-b · Opus 5.5, high
- **0. Claim.** A week after the flood Ginger Raines, seven, had not been found (A3-S4); she was found two weeks after it, twenty miles away (A3-S9).
- **1. Source.** WTKR 2 Sep 2019 RAW "discovered two weeks later. 20 miles away"; C-VILLE RAW (script Rows). No find place is given.
- **2. Datum.** Base map; the Tye's NHD polyline from Massies Mill downstream toward the James.
- **3. Geometry.** -a: county view, Tye drawn from Massies Mill toward the James, a small unlabelled marker at Massies Mill, waiting (slow
  pulse). -b: the marker slides down the Tye polyline 20 river-miles (550 px of path length ± 10 %, computed by script), label "20 miles"
  on arrival; no place name at the end point. If the Tye from Massies Mill to the James is shorter than 20 river-miles, stop at the
  measured length and report it to the orchestrator before drawing (the source does not say the route was the river).
- **4. Must be true.** (1) Marker stays on the river line. (2) Path length = 20 mi ± 10 % at 27.5 px/mi, or the conflict is reported.
  (3) No name, age or place label on the end point.
- **5. Cues.** -a: "Massies Mill" marker; -b: "two weeks" slide starts, "twenty miles away" label; then cut to V12 still (index).

### O10 · g-a3-list · Opus 5.5, high (A3-S12 to S14, about 56 s)
- **0. Claim.** The closest thing to a final answer for Nelson County is the 2019 list of 125 names: 84 under "The dead", 33 under "The
  missing" (Donna Fay and Gary Wood among them; 19 from Davis Creek), 8 under "The unidentified".
- **1. Source.** News & Advance 10 Aug 2019 list, Wayback
  `https://web.archive.org/web/20210807224023id_/https://newsadvance.com/news/local/article_fab7a328-62a9-5a8d-8ea9-4c6eb62939a6.html`
  ("Information courtesy of Oakland-Nelson County Museum of History"). Text verbatim, every row: name, age, place, as printed.
  factcheck-A3 S11 to S13 counts. C-VILLE 14 Aug 2019 card text (script A3-S13).
- **2. Datum.** A typeset page column 900 px wide centred-left (x 200 to 1100), Georgia rows at mid tier, heading in Arial; the page
  scrolls upward (y) continuously at ≥ 6 px/s; counter in the top-right rail (x 1200 to 1560, y 54 to 200) counts rows reached → 125.
  Source line "Nelson County · News & Advance, 2019 (Oakland Museum list)".
- **3. Geometry.** S12: heading "The dead", slow scroll, counter climbs as the scroll passes rows, landing "125" on "a hundred twenty-five".
  S13: scroll stops on heading "The missing"; rows "Wood, Donna Fay, 18, Massies Mill" and "Wood, Gary, 4, Massies Mill" turn Amber 1 on
  their names; C-VILLE beige card "Two of the Wood children—Donna Fay and Gary—were among the 33 people whose bodies were never recovered.
  · C-VILLE Weekly, 2019" slides in on "Neither of them was ever found" (right side, x 1150 to 1560, y ≤ 640); then the 19 Davis Creek
  rows light together; source line swaps to "19 never found + 33 named under The dead = 52 · News & Advance 2019 list; C-VILLE, WHSV 2019".
  S14: scroll moves to "The unidentified": 8 rows with text blurred (no age or place readable), one small amber marker per row; hold.
- **4. Must be true.** (1) Row counts per heading = 84 / 33 / 8 (script count, in the receipt). (2) Exactly 19 rows lit as Davis Creek
  (18 "Davis Creek" + 1 "Davis Creek area"). (3) The Wood rows are under "The missing". (4) No unidentified row is legible. (5) Whole
  lines only: no row cut at the box edge in any frame of the scroll (mg-quickref document rule). (6) The words "bodies" appear only
  inside the quoted C-VILLE card.
- **5. Cues.** S12 "list of names" scroll; "hundred twenty-five" counter; "Eighty-four" pulse on the dead heading. S13 "the missing"
  stop; "Donna Fay" row; "Gary" row; "Neither" card; "Nineteen" rows. S14 "one more heading" scroll; "Eight people" rows; hold to `bo-4`.

### O11 · g-a4-eight · Opus 5.5, high (A4-S5 to A4-S10, about 68 s)
- **0. Claim.** The eight were found along the Rockfish and the James, from Woods Mill down to above Bremo in Fluvanna County; the
  list says the adults may have been travelling on U.S. 29 and the children together; four of the eight were children or teenagers.
- **1. Source.** N&A 2019 list RAW (factcheck-A4 S6 to S8 lines in the script Rows); WHRO 13 Oct 2026 (Newell; "four children possibly
  between 6 and 19"); factcheck-A item 3 (six from the Rockfish, two from the James).
- **2. Datum.** Base map; pull-out to include the James down to Bremo Bluff (lon about −78.29: x ≈ 1800 at base zoom, so zoom ≈ 0.75
  centred east). U.S. 29 from TIGER.
- **3. Geometry.** S5: the list card's two closing lines highlight (from g-a4-list's card, rebuilt here top-left) and U.S. 29 draws as one
  thin line running N–S out of frame. S6: the line pulses once N and S; lower third (inside the comp, bottom-left, x 96 to 1100):
  "potentially a family or families on vacation ... traveling through Virginia · Lara Newell, WHRO, October 13, 2026". S7: photo inset
  card (V08, 420 x 280, slides in beside its marker, ≤ 6 s), two markers slide onto the Rockfish: chips "Woods Mill", "1 mile below".
  S8: inset V09; a marker at the Rockfish mouth on the Albemarle bank, chip "Howardsville · Albemarle shore"; map widens; a marker on
  the James at Buford Island (between Howardsville and Wingina, i.e. UPSTREAM of the Rockfish mouth), chip "Buford Island". S9: inset V07;
  three SMALLER markers on the Rockfish: "below Schuyler", "below the railroad bridge" (Southern Railroad crossing of the Rockfish from
  TIGER rail lines), "2 miles above Howardsville". S10: map widens down the James past the Nelson line into Fluvanna; small marker
  "above Bremo · Fluvanna County"; four markers (the four children/teens: below Schuyler, below the railroad bridge, 2 mi above
  Howardsville, above Bremo) turn Amber 1 one by one; chip "4 OF THE 8: CHILDREN OR TEENS", source "WHRO, October 13, 2026".
- **4. Must be true.** (1) Final tally on the map: 6 markers on the Rockfish, 2 on the James (Buford Island upstream of the mouth, Bremo
  downstream). If the Albemarle shore at Howardsville is not on the Rockfish in the TIGER/NHD data, STOP and report: the tally is a
  fact-checked claim. (2) No age on screen; place chips only. (3) Child markers smaller than adult markers. (4) Every marker on its
  river polyline. (5) Photo insets never cover a marker or chip; no inset is labelled with a place other than its provenance row's.
- **5. Cues.** S5 "U.S. Twenty-Nine" line, "red beans" highlight; S6 "Lara Newell" lower third; S7 "Woods Mill", "A mile below"; S8
  "Albemarle shore", "Buford Island"; S9 "Below Schuyler", "railroad bridge", "Two miles above"; S10 "Bremo", "Four of the eight".

### O12 · g-a2-harvey (insert treatment + karaoke caption) · Opus 5.5, high
- **0. Claim.** Deborah Harvey, eight in 1969, tells WDBJ in 2019 what came after: "You started realizing that all of these people
  who rode the school bus with you, went to church with you, were gone." Her own voice, her own words, made transformative (owner).
- **1. Source.** WDBJ, Tim Saunders, 19 Aug 2019, "Hurricane Camille: Davis Creek", Anvato 554865782, 175 s, 852 x 480,
  `https://d2pvyxdw30n8fd.cloudfront.net/WDBJ/v5d5b203acaa0a/SD.mp4` (factcheck-A2). Download into `media/src/W01/` with a provenance
  row (licence: broadcast, Content ID claim expected, owner yes 22 Oct 26). Transcribe the WHOLE clip with faster-whisper into
  `media/src/W01/wdbj-davis.words.json` before choosing cuts; the bite is near 103 to 109 s; open frames to confirm she is on camera.
- **2. Datum.** Full-frame designed ground (BG gradient). Clip panel at x 120 to 1240, y 140 to 770 (1120 x 630, 16:9; source upscaled
  1.31×, lanczos, prepped by ffmpeg into `media/clips/`). Right column x 1300 to 1560, y 140 to 640: a mini locator of Nelson County
  (base copy) with Davis Creek lit. Running caption band INSIDE the panel bottom, opaque, 1120 x 140 at y 630 to 770, covering the
  broadcast's own lower-third captions. WDBJ's bug stays visible: read its position on frames and keep the band and every card off it
  (a broadcaster's mark is never covered; if the bug sits in the bottom band area, move the band below the panel instead, y 790 to 930).
- **3. Geometry.** A2-S16 (narration over WDBJ b-roll, muted): lower third "Deborah Harvey · 8 years old in 1969" bottom-left, source
  "WDBJ, Aug 19, 2019". Harvey host: panel scales in (0.92 → 1, 0.5 s) at the bite start; the clip's `<video id="ins-a2-harvey">` is
  mounted on track 1 in index with `data-volume="1" data-has-audio="true"`, and is positioned/cropped to sit exactly in the panel (the comp
  draws the frame, ground, caption and locator around it; the comp leaves the panel rectangle transparent). Caption: the whole chunk
  dim, each word turns white as spoken, from the clip's words.json, verbatim. Host carries `data-caption-for="ins-a2-harvey"`,
  root `data-type-ok="running caption"`. A2-S17: panel narrows back out to full-frame b-roll (muted range of the same file) as the
  lower third slides out.
- **4. Must be true.** (1) Caption words = her words, verbatim, timed to the clip (≤ 0.1 s). (2) Cut on her last word, nothing after.
  (3) WDBJ bug visible in every frame of the bite. (4) No narration under the bite. (5) Lower third never overlaps the caption band.
- **5. Cues.** A2-S16 "Deborah Harvey" lower third; bite start/end from the clip's words.json; A2-S17 "It took her father" exit.

### 4.1 Sonnet briefs (each one is the builder's whole brief together with 4.0; text is exact; cue = the spoken word in that segment's words.json)
Full-frame ground for every non-overlay comp = BG gradient. Overlay comps (glass) = transparent root, footage beneath named.
Exits: cards slide out (x:980, autoAlpha 0, 0.6 s, power3.in) in the last 0.6 s; nothing cuts on motion.

- **g-t1-33** (T1-S1, 3.31 s, overlay on `V13/Massies_Mill_Flooding_(7797529874).jpg`). Glass card centre-left: big "33" (Danger red 1),
  mid "never found". Source line "Nelson County · News & Advance, 2019 (Oakland Museum list)". Cue "33" @0.16 card pops (scale 0.8→1,
  back.out), "never found" @2.36 label. Exit on comp end with the cut.
- **g-i1-gulf** (I1-S1 second sentence, overlay on M01). Glass bar bottom-left: label "Gulf Coast", bar scaleX 0→1 to a fixed 600 px,
  value "143", source "NWS". Cue "hundred forty-three". Only this one bar (no Virginia bar).
- **g-i1-rain** (I1-S3 + I1-S4, over dimmed `V24/camille1969varainblk.gif`, ground opacity 35 %). The episode's rain-gauge glyph
  (cylinder 140 x 420 px at x 300, y 300 to 720; draw it once, other comps reuse the drawing). Rail stamp "7 PM · Aug 19" on "seven".
  Counter leaf counts 0 → 27 (power3.out) with a clock ring "about 8 hours" filling beside it; lands "27 in" on "twenty-seven inches".
  Source line "ESSA-Weather Bureau survey · USGS Open-File Report 70-51". I1-S4: counter freezes (1 pulse), the OFR page crop slides in
  right (whole lines), then the beige row card over it: "Nelson County · 27 · Trash barrel · accuracy: Good · emptied afternoon before rain
  began" on "trash barrel"; chip "A TRASH BARREL". Must be true: no number between 0 and 27 is held; the card text is exact.
- **g-i1-pmp** (I1-S5). Beige cite card: "probable maximum rainfall · Weather Bureau study for the Corps of Engineers, 1956 · USGS OFR
  70-51 p. 7" on "worked out". Then one gauge (the shared glyph) fills to 82.5 % on "four-fifths", label "about 80 to 85 % of the maximum
  possible · Schwarz 1970, via USGS PP 804". Must be true: one gauge only; no 27 in vs 28 in comparison; fill 80 to 85 %.
- **g-i1-blunt** (I1-S6, 4.33 s, overlay on `V13/West_of_Rockfish_(7797546944).jpg`). Glass card: "died from broken bones and other
  blunt-force injuries, rather than by drowning" / "USGS Professional Paper 804, 1973"; chip "BLUNT-FORCE INJURIES". Cues: card on
  "broken" @1.84, chip on "blunt" @3.02. Comp ≥ 4.4 s.
- **g-i1-hundred** (I1-S8, 4.84 s, base copy). Nelson outlined left; right a 10 x 10 grid of small figures (each 22 px, 12 px gap, x 1000
  to 1340, y 300 to 640). Cues: "Nelson County" @0.14 outline glows; "one" @2.48 one figure turns Amber 1; "hundred" @3.44 label "about
  1 in 100 · Nelson County, 1970 census 11,702". Source line "Nelson County · NWS: 123 and 126 · 125 on the 2019 list".
- **g-i1-eight** (I1-S9, 3.49 s, base copy). Nelson outline; "eight" @0.14 eight unlabelled markers pop in 0.15 s apart inside the county;
  source "Virginia Department of Health · August 2026". No ages, no names, no rivers labelled.
- **g-a1-home** (A1-S2, base copy at g-a1-river's framing). A 14 px square beside the Tye on Rt. 56 labelled "the Raines house" on
  "Warren Raines"; name chips one at a time beside it: "Warren Raines, 14" on "fourteen", "Carl Raines, 16" on "sixteen"; a second square
  next door "the Wood family" on "Wood family"; on "station wagon" a small wagon icon by the Raines square. Square positions recorded
  in the receipt (O5 reuses them).
- **g-a1-forecast** (A1-S3, quote-card FAMILY BASE, full frame). Card 1 on "showers": "The weather bureau at the time simply stated there
  will be showers tonight, clearing in the morning." · Jeff Halverson, meteorology professor, UMBC · Radio IQ (WVTF), 23 Aug 2019. Card 2
  on "Bernard McGinnis": "11 o'clock news that night, weather report said rainy and cloudy. Just go to bed, yeah." · Bernard McGinnis,
  recalled · interviewed 2009 · Radio IQ (WVTF), published 2019. Phrase-by-phrase reveal on the voice; card 1 exits left as card 2 enters.
- **g-a1-hardrain** (A1-S4, about 25.6 s, base copy). One white frame (0.08 s) on the flash at comp start, then the map dark and wet
  (rain strokes, finite repeats); the rain-gauge glyph bottom-right OUTSIDE the corner (x 1300 to 1440, y 400 to 640) climbs slowly, no
  numbers; chip "Hard rain from 8 p.m. to 4 a.m." on "By eight"; then glass quote "if you were out in it it was almost like you couldn't
  breathe" · Audrey Diane Evans · interviewed 2009 · Radio IQ (WVTF), published 2019 on "One woman"; hold drifts until "Virginia".
- **g-a1-phone** (A1-S7). Raines square (from g-a1-home); phone icon rings once (rotation shake 0.6 s) on "phone rang"; rail stamp "2 AM ·
  Aug 20"; chip "PHONES STILL WORKING" on "still worked".
- **g-a1-wagon** (A1-S8). Wood square lights on "Next door"; eleven small figures (4 from the Wood square join 7 at the Raines square)
  on "eleven people"; chip "11 IN ONE STATION WAGON"; glass quote "Next door neighbor asked if four of their kids could come with us." ·
  Warren Raines · interviewed 2009 · Radio IQ (WVTF), published 2019 on "Mr. Wood".
- **g-a1-cattle** (A1-S10 after g-a1-flee-a, overlay on `V03/Aerial_View_of_Tyro_(7797534024).jpg`). Glass quote "There was cattle
  floating by, logs, automobiles. Even had an entire house float by." · Warren Raines · WDBJ7, 12 Aug 2019, on "carrying"; a faint
  lightning flicker (opacity pulses on a full-frame white layer at ≤ 0.15, 3 finite pulses).
- **g-a1-peak** (A1-S13, full frame, photo `V13/Massies_Mill_Bridge,_II_(7797542906).jpg` inside the comp, punch-in). Trace the Tye's
  visible channel in thin Cold blue 2 over the photo (stroke draw) on "Tye's peak"; chip "≈ 70,000 CU FT / SECOND" on "seventy
  thousand"; label "drains about 66 sq mi" on "sixty-six". Source line "USGS Open-File Report 70-51 · Tye River at Massies Mill,
  slope-area measurement".
- **g-a1-hydro** (A1-S14). Vertical scale, base y 900: a bar "old record (31 years)" 100 px tall; the 1969 bar rises to 800 px (8×) on
  "eight times", label "Aug 20, 1969 · 4 AM"; beige card "gage destroyed by flood · Tye River near Lovingston · USGS OFR 70-51" on "tore";
  chip "8× THE 31-YEAR RECORD". Must be true: bar ratio 8.0 ± 0.1; no hourly curve (no hourly record exists).
- **g-a1-staff** (A1-S15). Gauge staff at x 700, 30 px per ft from y 960: mark "13.7 ft · 1944" at y 549; water mark climbs past it to
  "29.0 ft · Aug 20, 1969" at y 90 (stays ≥ 54 px from top). Cues "twenty-nine feet", "1944". Source line "USGS Open-File Report 70-51 ·
  Tye River near Lovingston, from floodmarks".
- **g-a1-eight** (A1-S16, base copy, county view): Rockfish and James draw in first, then the eight unlabelled markers fade in and hold;
  source "Virginia Department of Health · August 2026". Different framing from g-i1-eight (rivers drawn, wider).
- **g-a1-letgo** (A1-S19, full-frame beige, family copy). After the line, card: "My mother said, 'Let go. We'll catch you.' I let go of
  it. And I got there, and they were gone." · Warren Raines · WTKR News 3, 2019. Phrase-by-phrase reveal; host = line start + read time
  + 5 s hold (`hold-a1-s19` covers it); gentle drift, no exit animation before the blackout cut.
- **g-a2-roar** (A2-S5). Black 0.6 s; beige quote "like a squadron of airplanes warming up for takeoff · residents, as reported in USGS
  Professional Paper 804" on "squadron"; then the Davis Creek hollows map (g-a2-hollows copy) trembles (x ±3 px, finite) and a ring
  spreads from the hollows to r = 165 px (6 mi) on "several miles", label "ground shook for several miles".
- **g-a2-clock** (A2-S6). Under a dim hollows map: a slim timeline (x 200 to 1400, y 820) with marks dropping as slides go, spacing
  shrinking toward the right; chip "ABOUT 3 MINUTES" on "three minutes"; rail stamp "about 4 AM · rain down to a mist" on "four in the
  morning"; two more marks after it.
- **g-a2-gamble** (A2-S11, overlay spanning `V05/Lovingston_Damages` → `V13/Home_Collapsed_in_Howardsville`). Glass quote "almost none of
  the dead showed evidence of drowning" / "USGS Professional Paper 804 (1973), on the findings of Dr. J. H. Gamble of Lovingston" on
  "Gamble"; chip "MULTIPLE FRACTURES" on "multiple fractures".
- **g-a2-raynor** (A2-S12, overlay spanning its two stills). Glass quote "The current they had been in was so strong that it had even taken
  off their rings, high school rings and wedding rings." / "Dr. Robert Raynor, quoted by The News & Advance in 2009; reprinted Aug 11,
  2019" on "Robert Raynor".
- **g-a2-houses** (A2-S13 to S15, about 16.3 s, over a dim hollows map). Row of 25 house icons (each 36 px, 12 px gap, centred, y 520);
  23 fade one by one ending on "two"; chip "2 OF 25". S14: counter "27" lands on "twenty-seven" with source "Davis Creek community · USGS
  Open-File Report 70-51"; second counter "22 missing" on "Twenty-two". S15: counters clear; a single line along the creek; text "Davis
  Creek · 52" with source "News & Advance list, 2019 (Oakland Museum), counted; WDBJ and C-VILLE 2019" on "about fifty"; then card
  "Huffman · 18" on "Eighteen". No first names, no faces. Must be true: 52 shows only here; 23 fade, 2 remain.
- **g-a2-sissy** (A2-S18). Beige card set like the page: heading "The missing", one row "Martin, Mary Ann "Sissy," 10, Davis Creek", source
  "News & Advance, 2019 · names from the Oakland-Nelson County Museum of History", on "Mary Ann Martin"; chip "Davis Creek · 19 never found"
  on "Nineteen". No photo.
- **g-a2-oakhill** (A2-S19 + S20, overlay over the hold stills). Glass cite card (long; set in 3 lines max per screen, two screens):
  "If both evacuation plans and a warning system had been in place ... the citizens along Davis Creek would have been advised just before
  midnight of August 19 to seek refuge at a nearby structure not in the path of streams draining steep slopes, such as the Oak Hill
  Church." · USGS Open-File Report 99-518, 1999, on "Thirty years later"; S20 chip "IF ALL HAD HEARD AND GONE: MOST OR ALL OF 50 COULD
  HAVE BEEN AVOIDED · USGS OFR 99-518" on "If everyone", fades before S21. No church marker.
- **g-a3-tinsley** (A3-S2, overlay over `V13/Black_Creek_Washed_Out_Bridge`). Glass quote "It took me about 8 hours to do that and there
  were no main, secondary roads in to Nelson County." · Ed Tinsley, State Police, Amherst County · WHSV, 2019; lands AFTER "check which
  roads were open".
- **g-a3-whitehead** (A3-S3, overlay over its stills). Glass quote "By the first night, it was obvious it was not a rescue." · Dick
  Whitehead, the sheriff's son · C-VILLE, 2019, on "wasn't a rescue".
- **g-a3-missing-a** (A3-S5). Two columns "KNOWN LOST" and "MISSING"; rail stamp "Aug 22, 1969"; MISSING counts to "100+" on "a hundred";
  KNOWN LOST stays blank. Source "Associated Press, Aug 22, 1969 (The Pontiac Press, p. 1)".
- **g-a3-missing-b** (A3-S7, copy of -a). Opens at "110+"; ticks to "109" on "a hundred and nine" (rail "Aug 24 · AP", source "Associated
  Press, via The Pontiac Press, Aug 25, 1969, p. 7"), then "89" on "eighty-nine" (rail "Aug 25 · UPI", source "United Press International,
  via The Pontiac Press, Aug 25, 1969, p. 62 · AP and UPI counts differ"); KNOWN LOST arrow climbs on "kept climbing", no number.
- **g-a3-heli** (A3-S8, copy of g-a3-cutoff's end framing). County still cut off; one helicopter icon crosses in over the Blue Ridge on
  "helicopter"; chip "IN BY HELICOPTER"; beige card "Hit hardest was Nelson County" · Associated Press, Aug 23, 1969 (The Pontiac Press,
  p. 1) on "hit hardest".
- **g-a3-nov13** (A3-S10). Virginia outline (Natural Earth from the master map) small top-left; rail stamp "Nov 13, 1969"; bar "113" on "a
  hundred thirteen", then bar "39 still missing" on "Thirty-nine"; source "USGS Open-File Report 70-51, p. 1"; beige card "thirty-nine
  missing and presumed dead" · Encyclopedia Virginia, timeline on "Encyclopedia Virginia".
- **g-a3-counts** (A3-S11, about 28.6 s). Four cards in a row, never merged, each landing on its number: "113 · Virginia, found, Nov 1969 ·
  USGS" · "150 · Virginia, later count · USGS 1973, 1999" (inset under it on "a hundred fifty": "125 in Nelson · USGS PP 804") · "153 ·
  Virginia, later count · National Weather Service" · "124 · Nelson County · Virginia Dept. of Health" (ghost tag under it on "Nelson
  County alone": "124 · Virginia? · Encyclopedia Virginia", flickers 3 times then stays dim). Spoken order is 113, 150, 153, 124: build in
  that order. No arithmetic between cards. Final 6 s: the four tags (state/county, found/missing, 1969/later) pulse in turn on "the whole
  state or one county, the found or the missing, 1969 or years later".
- **g-a4-vdh** (A4-S1, about 21 s). Rail stamp "Late August 2026". Typeset beige card, heading "OCME Missing Persons Program", source
  "Virginia Department of Health · media update, August 28, 2026"; card slams in on "eight people" (scale 1.15 → 1, 0.25 s); the
  words "generate new leads" highlight on "new leads"; line "In total, 124 people died in Nelson County and eight fatalities are still
  unidentified" shown on "a hundred twenty-four" (source "Virginia Department of Health, 2026"); chip "NO AGES · NO NAMES" on "no name".
  A real page capture replaces the typeset card if GAP 8 is filled.
- **g-a4-screens** (A4-S2). Three captures (GAP 7), each a slow-pushed card about 2 s with a different tilt: VDH social post as shown in
  CBS19's story; NamUs case page; then lower third "Public awareness is often the key that unlocks cases like this." · Lara Newell ·
  Virginia Department of Health, August 2026 on "public awareness". Blocked until the captures exist; no mock-ups.
- **g-a4-stacks** (A4-S3). Two stacks side by side, never merged: left "33 never found", right "8 found, never named"; source "Nelson County
  list · News & Advance, 2019"; then date strip "found Aug 24 to Sept 6, 1969", source "NamUs, via CBS19, August 2026" on "five and
  eighteen days".
- **g-a4-list** (A4-S4, over a dim base map with the eight markers returning from g-i1-eight's positions). Beige card heading "The
  unidentified", source "News & Advance, August 10, 2019 · information from the Oakland-Nelson County Museum of History" on "the list".
- **g-a4-files** (A4-S11, copy of g-a4-eight's final state). The eight markers lit; chips pop beside them one at a time: "autopsy, 1969"
  on "autopsies", "dental charts" on "dental", "cremated" on "cremated", "no DNA test" on "DNA"; source "WHRO, October 13, 2026 · WSET,
  August 27, 2026"; markers dim on the last line. Chips never sit on a marker or river line.
- **g-a4-newell** (A4-S12, overlay lower third spanning the stills). Small verbatim: "We just want to make sure that some of these older
  cases are highlighted, especially as time goes on, we start losing the people who had historical knowledge of events." · Lara Newell,
  long-term unidentified coordinator, Office of the Chief Medical Examiner · 29News/WVIR, August 31, 2026. Two lines max per screen;
  phrase reveal on the voice.
- **g-a4-contact** (A4-S15). Clean centred card: "Office of the Chief Medical Examiner, Central District" / "OCME_CENT@vdh.virginia.gov",
  lifts in over the eight markers (dim) on "If you remember"; held ≥ 4 s; gentle float.
- **g-a4-open** (A4-S16, copy of g-a4-eight's end). Eight unlabelled markers; rail stamp "October 2026" on "October"; slow pull-out.
- **g-z1-headings** (Z1-S2, copy of g-a4-eight). The Rockfish draws into the James; eight unlabelled markers (6 on the Rockfish, 2 on
  the James, one of the James markers above the Rockfish mouth) — same positions as O11; on the list cue the three headings type on as a
  beige card "The dead 84 · The missing 33 · The unidentified 8", source "News & Advance, Aug 10, 2019 (Oakland-Nelson County Museum of
  History)"; chip "8 STILL UNNAMED" on "waiting for a name", source "Virginia Department of Health · August 2026 · WHRO, 13 Oct 2026".
  Note: the spoken Z1-S2 line does not say "three headings"; the card lands on "carried people" and the chip on "name".
- **g-z1-close** (Z1-S3). `outro-brand.html` retuned: THE WARNING HOUR wordmark builds on "This was The Warning Hour" (match-cut on
  the line); before it, the signature lines are NOT typed on screen (narration carries them; one reading target). Ends ≤ 3 s after the last word.

---

## Part 5 · Gaps (Picture lines or required layers with no file on disk)

| # | What | Needed at | State | Fix (owner bin?) |
|---|---|---|---|---|
| 1 | Paul clips ins-paul-2..5 | A1-S9, A2-S4, A3-S6, A4-S14 | not generated (75 credits total approved by the coordinator's go per omni_shots.md) | coordinator's Omni run; placeholders meanwhile |
| 1b | ins-paul-1 final | H1-S1 | only `media/paul/ins-paul-1/raw-01.mp4`; no logo step, not whisper-checked | logo step + whisper, then mount `ins-paul-1.mp4` |
| 2 | WDBJ Harvey clip | A2-S16, insert, A2-S17 | not downloaded; URL in factcheck-A2 | download + transcribe (free; owner yes on record) |
| 3 | VCU Richmond Police reel V16 (moving James water) | A3-S9 (V12 still is the stand-in) | not on disk; V15, V17 also listed in footage-inventory.tsv | free PD download from scholarscompass.vcu.edu/rpd_films/70 |
| 4 | Rain on a tin roof (hook sound) | H1-S1 | none in `assets/sfx/` | Pixabay free, licence row |
| 5 | Phone ring | A1-S7 | none | ffmpeg-made bell, or Pixabay |
| 6 | Creek ambience | A2-S19..S21 hold | none | Pixabay free, or ffmpeg-made |
| 7 | VDH social post (as in CBS19) and NamUs case page screenshots | A4-S2 | none | capture pages (free) |
| 8 | VDH media-update page capture | A4-S1 | none (typeset card is the planned fallback) | capture (optional) |
| 9 | OFR 70-51 Table 1 page renders | I1-S4, A1-S6 | PDF on disk (`V22/ofr70-51.pdf`), no render | pdftoppm prep, crop whole lines |
| 10 | Geo data (TIGER counties/roads/rail, NHD flowlines, GNIS points, HURDAT2) | every map comp | none on disk | free federal downloads into `media/geo/` with provenance rows |
| 11 | Real moving footage of Nelson County | hook rule "mid-action shot after Paul"; REAL-clip cadence | none; T1-S1 opens on a still | check `media/src/M02/LadyCalledCamille.mp4` (1971 PD civil-defence film, 28:53) for Virginia scenes before compose |
| 12 | Helicopter photo | A3-S8 | none in the LVA set (V13 "Army Assists" is Richmond, wrong place) | map icon only (planned) |
| 13 | AP/UPI 1969 newspaper clippings (Pontiac Press pp. 1, 7, 62) | A3-S5, S7, S8 | images were checked by fact-check, not saved | optional: save page crops for real-document texture |
| 14 | V13 "Army or rescue still" | A3-S3 | resolved with Bridge_Out_to_Rural_Home + Rescue_Mission_Planning | none |
| 15 | "moist air · about 3,000 ft deep" label | A1-S5 | no quoted row supports the number | confirm in PP 804 p. 4 or drop |
| 16 | Outside voices (non-narration audio budget about 6 s) | acts 1 to 3 | none | candidates, each an insert needing the owner's yes + running caption: WTKR 2 Sep 2019 Warren Raines video ("Let go. We'll catch you", A1-S19); WDBJ7 12 Aug 2019 Raines video (A1-S10 quote); Radio IQ 2009 interview audio (Warren Raines A1-S8, McGinnis A1-S3, Evans A1-S4); WHSV 2019 Tinsley (A3-S2) |
| 17 | WDBJ b-roll for A2-S17 | A2-S17 | same file as gap 2 | fallback in the script: our map with the road drawn up the hollow |
| 18 | Tin-roof hook, circle face videos | H1, all narration | circle not made (needs all narration wavs) | `circle_audio.py` + ZBook FlashHead after TTS |

Picture lines resolved from disk (not gaps): A1-S18 Tye still (`V13/Rt._56_over_Tye_River`), A2-S8 scar photo
(`V23/pp804-p26-fig12.jpg`), A4-S13 Rt. 29 still (`V13/Woods_Mill_Aerial_View`), the "LVA scarred hollow" of I1-S6 (`V13/West_of_Rockfish`).

## Risks (top 3)
1. **CTA window:** estimate puts the CTA at 0.603 of runtime, over the 0.40 to 0.60 window (62 % of narration words sit before the hinge). Measure after TTS and placeholders; if over, owner call (`window_by_slug`) or a pre-CTA trim; holds go after the CTA.
2. **Thin real footage and outside sound:** no moving picture of Nelson County on disk, only stills (+ M01 Gulf film, ATS loop); outside voices about 6 s (Harvey). The hook's mid-action rule and the REAL-clip cadence lean on GAP 11 and GAP 16, and every voice insert needs his yes.
3. **Map truth carries many claims:** the eight-map's 6 Rockfish / 2 James tally depends on the Albemarle shore at Howardsville being the Rockfish bank; Ginger's 20 miles may exceed the Tye's length; Davis Creek must stay on the Rockfish side. One base map (O1) feeds 20+ comps, so a base error multiplies: base read before any copy.
