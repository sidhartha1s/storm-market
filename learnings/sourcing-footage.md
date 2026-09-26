# learnings/sourcing-footage.md: sourcing and footage: clip picks, provenance, licensing, geometry, repeats

Newest first. New entries go at the top, under this line. Superseded lines point at their current home.

## 2026-09-11 · Krakatau #4 mistake ledger: which gate should have caught what
- Not catchable by code: what a clip shows. provenance.csv now carries a `shot` column (what is visible, including
  burned-in chyrons) for every broadcast cutter, written from one labelled contact grid read by a subagent; the
  builder refuses a cutter without one. Pick pictures from `shot`, never from a file name.
- Quote cards: the attribution era must match the cut underneath (Ulrich 1958 sat on an 1883 print); `shot`
  starts with an era/category token so the check is a glance.

## 2026-09-11 · Krakatau #4 slice QC: text that runs off the frame, and blind clip picks
- Picking broadcast cutters by file name ("f24_005 = 2026 plume") put an airport departure board under "same
  mountain, same mechanism, then where?" and a terminal corridor under the siren explainer. Rule: every clip is
  eyeballed (labelled contact grid, one subagent read) before it is wired; provenance.csv carries the source,
  not the picture.

## 2026-09-08 — breaking lane v1 (br-elnino-california, /mini-storms first run)
- **Scene-cut broadcast pulls:** ffmpeg `select='gt(scene,0.35)'` on 6 news reels gave 51
  usable 3–7 s cuts in one pass; windows must be clamped to the cut's real length (several
  were 1–2 s short → sweep "frame extraction failed" is the symptom).
- **Long map holds:** a 12 s NOAA outlook still fails the 6 s still rule; render it as a 13 s
  zoompan mp4 (`ffmpeg -loop 1 ... zoompan`) — passes as video and still moves.
- **Pexels API key in ~/.claude/.env returns 403 (dead); Pixabay key works.** Wikimedia Commons
  API rate-limits after ~10 file fetches (429) — batch with a pause.
- Reuse pool for the whole El Niño series: `library/mini-storms/el-nino-2026/` (+ provenance.csv).

## 2026-09-08 — breaking lane, first video (br-elnino-california): owner corrections + measured facts
- **Pixabay "mudslide" search returned an Amalfi-coast town clip.** Every stock pick gets a contact-sheet
  eyeball before wiring; the owner spotted it in the preview. Pexels API keys (all 3) are dead (403).
- **Instagram via `yt-dlp --cookies-from-browser chrome` fails while Chrome is open** (cookie DB locked).
  Use a cookies.txt export or close Chrome first. No social clips in this cut.
- **Gemini (nanobanana) free tier is exhausted** → thumbnail candidates come from real render frames
  (`thumbs/frame-cand-*.png`) until a paid key exists.
- **A worktree's clip pool dies with the worktree (2026-09-11, Krakatau #4):** `library/mini-storms/<event>/` media
  is gitignored, so `git worktree remove` deleted the 72-asset Krakatau pool the moment #3 shipped; only the clips
  already staged into `episodes/ms-krakatoa-1883/media/` (bc + _orig + stills) survived, and the #4 builder had to
  fall back to them. Rule: before removing an episode worktree, copy `library/mini-storms/<event>/` into the main
  checkout (`robocopy /E`), then remove. Pools are cross-angle assets; the worktree is not their home.

## ep6 ship (2026-08-23) — hyperframes 0.8.x, the hidden-console chain, and a preflight bug
- **Credits need provenance rows for EVERY still.** The seven owner-supplied Wikimedia stills
  (charity-web-c*, hsdrrs-web-c*) had no provenance row; licence/author were pulled from the
  Commons API and the files matched to the Commons thumbnails by a subagent before writing the
  CC-BY attribution block (`media/provenance-wikimedia-stills.csv`). Four of the six used are
  CC BY / CC BY-SA — attribution is mandatory, not courtesy.

## ep6 draft v2 review — text collisions were a CHECKER false negative (owner 2026-08-22)
- **"Source ends early" — check what the SOURCE is before saying so (corrected 2026-08-23):**
  ins-hodges "cut before finishing" was first answered "the C-SPAN pull ends at 7.44s, nothing to
  extend". Wrong: the 7.44s file was OUR pull; the source is the local 39-minute C-SPAN hearing
  (`media/audio-assert/ins06_house_testimony.mp4`, transcript alongside). Re-cut to the sentence
  end (8.85s) and retimed everything after it by +1.55s. Never call a pull "the source".

## 2026-08-15 — ep6 owner rules + broadcast-geometry gotchas (later same day)
C. **Video-range black is Y=16, not 0.** A pillarbox/blanking detector thresholded at
   "luma < 4" passes limited-range black bars. This exact miss made two sessions measure the
   same WWL reels and reach opposite conclusions (pillarboxed vs clean). Threshold ≤17, or
   use cropdetect.
D. **Broadcast compilation reels have PER-SEGMENT geometry — run cropdetect per cut window,
   never one blanket crop per reel.** The WWL aug28-31 reels are 1280x720 progressive
   carriers with 4:3 content whose active rect varies segment to segment (w 938-974,
   x 152-174, some with top blanking). One measured crop applied reel-wide leaves 10-20px
   black slivers on other segments. Recipe: cropdetect on the exact source window → inset
   ~6px → crop to 16:9 inside the active rect (house style, matches the DVIDS recipe) →
   scale 1920x1080. Then verify numerically with 12px edge strips (Y>17) AND one eyeball
   frame.

## 2026-08-15 — ep6 TTS + sourcing (measured surprises)
5. **DVIDS image IDs are a single global sequential counter** — numerically adjacent IDs are
   unrelated uploads; always verify each image's title page. DVIDS search/NARA REST are
   JS/auth-gated for scripts; the direct CDN pattern
   `d1ldvf68ux039x.cloudfront.net/thumbs/photos/{bucket}/{id}/2000w_q95.jpg` works headless.
7. **Scene picking from long reels: contact sheets FIRST, never per-frame agent probing (owner
   correction 2026-08-15).** An agent "watching" a reel by extracting one frame at a time is a
   blind person borrowing eyes one glance at a time. The pipeline is: PySceneDetect CSV (already
   the standing rule) → deterministic script renders labeled contact-sheet grids (~30 scene
   thumbnails per image, scene number + timestamp burned in) → judgment reads the SHEETS and
   tags scene numbers per beat → one ffmpeg batch extracts the tags. Code does everything
   deterministic; eyes only choose.

## Sourcing doctrine for future episodes (owner, ep5 review, 2026-08-13)
ep5 mounted 142 cuts that traced to only ~30 real source acquisitions — 5-6 reels re-sliced.
Owner: "30 sources should be 60. The clips are there." Count SOURCES, not cuts; and count
ASSERTION assets specifically (broadcast pulls, day-after newspapers, official audio, presser
clips, survivor clips, before/after stills) — third-party proof that the thing happened beats
another angle of the same b-roll. Re-slicing a reel is editing, not sourcing.

## Owner pivot 2026-08-12 — cadence, sourcing, SFX, durable references

- **Cadence anxiety retired:** video beats up to 12-15s when genuinely matched; stills 3-6s MAX
  with motion (sweep now enforces 6s, was 12s); prefer video everywhere. Claim-risk pulls >12-15s
  need narration over them; transcribe news clips before cutting.
- **PySceneDetect** (scenedetect.com) approved for splitting long sources into scene cuts —
  validate on this box before first use; cheaper than agent OCR passes.

## 2026-08-05 — ep5 kickoff: the retention lattice + script fact-QC layer (owner orders, all standing from ep5 on)
6. **Real human portraits (owner):** show the real faces briefly — per-person licensing verdicts
   first; ≤4–5s dwell, once, then symbolic; never a child victim's likeness.
8. **Licensing (Carr/Camp):** CAL FIRE firenado heli clip = USE-WITH-CREDIT (CA state-works PD
   doctrine; AB 2880 died 2016; source Storyful's CAL FIRE-credited copy, not network versions).
   911/dispatch recordings CPRA-released = CLEAR-TO-USE from the original holder. Raw
   Broadcastify scanner rips = HELD (no license path). Camp Fire bystander evacuation clips +
   sheriff bodycam = strike-class (chaser-equivalent), network-aired re-cuts only.

## ep3 v3 — stop rendering to find things a script can find (2026-07-29)
- **A blanket `fit="contain"` pillarboxes photos that were already the right shape.** Four
  stills at 1.58-1.75 aspect were running inside blurred bars for nothing. Letterbox on the
  IMAGE's aspect, not the segment's hint — with papers exempt, since cropping a front page
  cuts the text.
- **A substitution pool with no geography will contradict the narration.** Past the reuse
  ceiling, `pick()` drew from a flat spare list and put the Heinz plant in Princeton,
  Indiana under a sentence about Annapolis, Missouri — the far end of the track, three hours
  later. Act-scoped pools first, global spares second. The narration/picture gate found it;
  no human review had.
- **Word-level timings turn "does the picture contradict the voice" into a script.**
  `narration_picture_check.py` reads `audio/<seg>.words.json` and tests what is on screen at
  the instant a year or a town is spoken. Build the place vocabulary from the archive's
  filename convention (`1925_-_<Town>_-_`), not from every capitalised token — the loose
  version called "Where", "Morning" and "Building" towns and buried three real findings in
  thirteen false ones.

## ep3 v3 - second audit round (2026-07-29)
- **Cut rate is an asset-budget decision, not just a taste one.** ep2 (shipped, 7.5/10) holds an
  11.0s median across 136 windows in 28 min. Driving ep3 to a 5.5s median needed ~260 windows in
  35 min - roughly double the assets per minute - and the photo library could not feed it, so
  frames silently repeated 5-12 times. Pick the median from `distinct_assets * 3 / minutes`, then
  design the rhythm inside that budget. Landing at a 6.5s median with 216 windows fit 106 assets
  with zero over the 3-use ceiling.
- **Identify assets by content hash, never by path.** Six newspaper front pages existed
  byte-identical under `media/newspapers/` and `media/photos/`; the reuse lint counted each path
  separately, so one page reached nine on-screen uses under a ceiling of three.
- **Count uses per WINDOW, not per `<img>` tag.** The letterbox treatment emits the same src twice
  (blurred backdrop + foreground), which inflates a naive `grep src=` count by 2x and produces
  false reuse findings. Two of my own audit agents were fooled by exactly this.
- **A "credited" archival face is still a misattribution if no credit renders.** The Signal Corps
  commander who shut Finley down sat under a panel headlined JOHN PARK FINLEY for 32 seconds; the
  edit script said "credited" but no attribution element existed anywhere in the window. If a real
  person's face is on screen under someone else's name, that is a factual error, not a design nit.

## 2026-07-26 — ep2 v1 owner review (9/10; every item below is a standing rule now)

**Editorial (owner corrections):**
- **Broadcast variety:** TV/broadcast pulls stay short and MEANINGFUL — never a 12-24s single
  pull; length itself is editor judgment ("4,4,4" was an owner example, not a formula — don't
  hardwire it). Different sources, different cuts, different chapters; never reuse the same
  broadcast cut twice. Grade every broadcast/private-rec clip (unified grade = transformational
  + look-glue); stock/PD exempt.
- **Bare static stills >10s = retention risk.** Motion video tolerates 12-15s; a bare still
  doesn't. Split with another visual or overlay an info beat — but never force filler.
- **Insert/AV cuts on sentence boundaries via transcript, always.** 8-14s, complete meaningful
  statement (emotional or informational), never mid-sentence. "80% is the cut; the last 20% is
  knowing what to leave out."
**Process:**
- **Verify each CUT, not just the source video.** An official CBS upload titled for the April 2011
  Alabama outbreak contained Henryville, IN (March 2012) footage inside its montage — caught only
  because a chyron was legible in a snapshot frame. Rule: before wiring any broadcast cut, extract
  a frame FROM THE CUT and check chyrons/landmarks against the event; title + official channel are
  not provenance for individual shots.

- **Provenance notes are load-bearing at COMPOSE time.** cullman-aftermath.mp4 carried a
  "2017-era footage" warning in provenance.csv and still got wired into a 2011 documentary
  (twice). Rule: before wiring any clip, re-read its provenance row; a "backup only"/era
  mismatch note disqualifies it.

## 2026-07-26 — ep2 overnight build (tooling gotchas, all reproduced)
- yt-dlp `--print` implies `--simulate` — subtitle downloads silently skip; run without `--print`.

## 2026-07-26 — ep2 design review (owner corrections, all wired into CLAUDE.md/DESIGN.md same session)

1. **Broadcast-clip rehook cadence**: core audience 40–70+ watched these disasters on live TV —
   real broadcast/news/PD/survivor clips every 45–60s as rehooks; stock fills BETWEEN real clips,
   never the reverse. Network clips 3–4s, narrated-over, credited (credit ≠ license, ≠ claim immunity).
2. **Claims-vs-strikes ruling (Oldshue)**: network material = revenue claims (budgeted OK);
   independent chaser/streamer footage = manual strikes (channel-fatal) → NEVER-without-license
   covers streamers too. Disguising a source (grain/crops/short cuts) to dodge Content ID is
   prohibited — structural immunity, not obfuscation. The story can be narrated over our radar
   re-plots + network tower-cam instead of the streamer's frames.
3. **Burned-in radar timestamps: map to narration OR crop out of frame** — cropping now an
   approved alternative to honest-labeling when the clock isn't the story. UTC-vs-local trap stands.
4. **Cold-open montage grammar**: clips enter MID-ACTION (the hit, not wind-up/aftermath), cuts
   land ON the audio event (scream/crash/dispatch line), 911 audio as one scene in the chain.
   Never re-rip clips from competitor videos — trace to original sources (their edit carries
   their Content ID fingerprint + VO bleed); refs are a shot list only.

## 2026-07-23 — v3 pre-render multi-agent QC sweep (owner-ordered; caught what 2 shipped versions missed)
1. **`rain-wall-parked-cars.mp4` showed a MALAYSIAN license plate** — shipped in v1 AND v2
   unnoticed. Lesson: vision-verify every inherited/act-dir clip too, not just newly sourced
   ones; foreign tells (plates, signage, architecture) are the #1 stock hazard. Replaced with
   `rain-wall-downpour-generic.mp4` (anonymous pavement closeup). Tainted file kept on disk for
   v2 provenance but must never be re-used.
4. Honest-label rule reconfirmed: watch-beat popup must narrate the radar's burned-in clocks
   ("watch 1:30 PM → by 5 PM this appears"), never caption footage with a time it contradicts.

## 2026-07-22 — owner review of ep1 v1 (9/10, "best one till date"; ~80% of issues = cadence + repetition)

1. **Cadence is REASONED per clip, never defaulted**: the editor-agent must justify each hold —
   "1.5s stinger or 12s land-the-beat" is an editorial decision per beat; anything >8s needs a
   reason written in the edit script. Overlong offenders in v1: hook porch-swing, cloud shots,
   siren still at 11:05 (14.6s), outro title dwell.
2. **No visual repeats within an episode** (owner caught all three: lamp-post rain ×2,
   rain-window ×2 within 2 min, St John's facade ×2). One reuse allowed ONLY as an intentional
   callback: different crop/grade, >5 min apart, flagged in the edit script.
3. **Sync rule — the frame must not contradict the narration**: "died in the dark" over a
   daylight photo; "Walmart" over a Walgreens aerial; "1:30 PM watch" over a 22:43 UTC radar
   stamp. Named entity / time-of-day / timestamp in VO ⇒ matching visual or a neutral one.

## 2026-07-22 — ep1-joplin full-episode build (overnight ship-it)
- **Real-radar frames carry burned-in scan times (UTC)** — any popup naming a different clock
  time contradicts the frame. Label honestly (fine-print provenance line) or match the scan.
- **NASA ASTER false-color reads as alarming red** — always add a one-line false-color
  explainer popup; the gray scar IS the story.
- **NEXRAD via GCP mirror, not AWS**: `gcp-public-data-nexrad-l2` allows anonymous listing
  (AWS bucket is GetObject-only); pyart `plot_ppi_map` creates a NEW GeoAxes (style
  `fig.axes[-1]`); velocity lives on sweep 1 (split-cut VCP), not sweep 0.
  Render script kept at `C:/nexrad-t/render_radar.py`.

## 2026-07-22 — owner feedback on demo-joplin-90 (overall: "incredible")

1. **Memorial/character beats: prefer a REAL photo where one publicly exists** (news/memorial
   coverage — an editorial-respect judgment per case); else make the STAT carry the emotion —
   e.g. the death toll as a rising red counter (Joplin = 161, NWS-verified; owner recalled 178 —
   always verify the number). Symbolic stock (grad cap) reads weakest of the three options.
2. **Radar/graphic beats: REAL data beats stylized animation.** Owner loved the sweep but wants
   the actual storm: render real NEXRAD Level-II archive data (AWS open data, free) for the event,
   or use NWS archived radar imagery (PD) — stylized radar only when no real data exists.

## 2026-07-22 — demo-joplin-90 (first E2E, owner: "incredible")
**Editorial/pipeline:**
- Word-timestamp cuts work exactly as designed: transcribe each TTS segment, cut on the word.
- Stock tonal mismatch is real: sunny clips need a static CSS `filter` grade (brightness/saturate)
  to sit in a documentary cut — grade at composition, not ffmpeg.
- Sourcing workflow pattern (5 parallel download agents + vision-verify stage) delivered 100%
  usable assets in ~14 min — keep for episodes; scale agents per act.
- Owner delegation note: insert selection was owner-delegated for the demo; REAL episodes keep
  the owner gate (frames + transcript + source, yes/no).
