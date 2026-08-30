# Insert Gate Packet — ep4 El Reno — Broadcast Clip Approvals

Owner: mark each shortlisted clip APPROVE or REJECT. House rule applied throughout: **network/
station-sourced cuts are hard-capped at ≤4 seconds**, narrated over, never reused twice, and
budgeted as **Content ID revenue claims (survivable, expected)** — never a strike risk, per
clip_hunt.md §6 fair-use reality. All 21 candidate clips live in `media/broadcast/`; 3 review
frames each in `media/_gate/<basename>/frame[1-3].jpg`. NWS Norman "Lessons" PD pull for A6-S3
is handled separately and is NOT one of these 21 — no action needed on it here.

The 9 SHORTLIST clips below now carry **verbatim faster-whisper (small.en) transcripts** of
their proposed cut windows, generated 2026-08-01 by extracting each window (+ a few seconds of
padding for sentence-boundary context) from `media/broadcast/` and transcribing locally — see
each entry's "Transcript (VERBATIM, faster-whisper small.en)" line.

**EDITOR RULINGS (main session, 2026-08-01):**
- `abc-3-storm-chasers-killed`: audio says "13 people killed in the Oklahoma Twister" — early-reporting
  conflation that contradicts our verified figure (8 tornado deaths). Cut is approved-candidate for
  MUTED visual use only; its audio never plays.
- `kfor-sutton-very-close-call` ("please do not ride this out in any interior closet or bathroom"):
  promoted to COLD-OPEN ANCHOR candidate — intelligible, high-stakes, ep2-Spann-class. If approved,
  it opens the episode at ~2.5s under the siren spine. Several proposed-cut windows
were nudged by 1-3s where the original ≤4s window landed on a mid-word chop or mostly dead air;
each change is called out in that clip's entry. The **BENCH** section (12 clips, below) and
**PROVENANCE FLAGS** section remain **inferred from the 3 review frames + filename + clip_hunt.md
description only — not re-transcribed**; do not treat any quoted-looking text there as verified
dialogue unless it appears as an on-screen caption in a frame (noted where it does).

---

## 1. SHORTLIST — 9 clips, one YES/NO each

### 1. `twc-bettes-suv-toss-marquee.mp4`
- **Station / rights holder:** The Weather Channel (network-official, channel_id `UCGTUbwceCMibvpbd2NaIP7A` per clip_hunt.md §3)
- **Proposed cut:** 0:08–0:12 (~4s, unchanged — verified clean) — the truck-in-frame-with-funnel moment visible at frame2 (duration 87.5s total; this is the marquee "SUV tossed" segment itself)
- **Transcript (VERBATIM, faster-whisper small.en):** "...wide and is heading right at Bettes [whisper heard "Betis"] and his team." (mid-narration fragment — this is TWC's own narration over the funnel/truck shot, not dialogue tied to the SUV toss itself). Window ends cleanly right after "team." into a brief pause before the next sentence starts — no mid-word chop.
- **Beat served:** A3-S3b (Mike Bettes SUV-toss visual)
- **Frames:** `C:/Users/Sidhartha/Automation Projects/storm-market/.worktrees/ep4-el-reno/episodes/ep4-el-reno/media/_gate/twc-bettes-suv-toss-marquee/frame1.jpg`, `frame2.jpg`, `frame3.jpg`
- **Source URL:** `youtube.com/watch?v=35xCZqdc5u4` — "Tornado Hits The Weather Channel Crew" (2013-10-02) per clip_hunt.md §3
- **Claim expectation:** Content ID revenue claim, budgeted
- **Note:** frame3 is near-black (impact/dark moment) — verify the exact 4s window lands on legible footage before final wiring, not just this dark frame.
- [ ] APPROVE
- [ ] REJECT

### 2. `kfor-sutton-josefy-up-close.mp4`
- **Station / rights holder:** KFOR Oklahoma's News 4 (station-official, channel_id `UCEUYiWFyzpEBMZ3aG7ud7xg`)
- **Proposed cut:** 0:02.4–0:06.4 (~4s — NUDGED from 0:00–0:04) — wide funnel shot from the chase vehicle (frame1/frame2 both show clear tornado-in-frame, windshield-mount POV)
- **Transcript (VERBATIM, faster-whisper small.en):** "it has multiple vortices, I see the vortices swirling" — the original 0:00-0:04 window was ~2.4s of dead air before speech starts, then chopped mid-word on "multiple"; nudged +2.4s to land on-speech immediately and end cleanly right at the end of "swirling."
- **Beat served:** A2-S4 (storm-coverage pull — rain-wrapped/multi-vortex visual)
- **Frames:** `.../media/_gate/kfor-sutton-josefy-up-close/frame1.jpg`, `frame2.jpg`, `frame3.jpg`
- **Source URL:** `youtube.com/watch?v=UjZDY142Y-Q` (2013-06-02) per clip_hunt.md §3
- **Claim expectation:** Content ID revenue claim, budgeted
- **Note:** this is KFOR's OWN on-air chase vehicle (Sutton is KFOR staff, not a third party) — the windshield/wiper framing looks dashcam-like but the rights holder is confirmed station-official, not a re-upload.
- [ ] APPROVE
- [ ] REJECT

### 3. `kfor-sutton-very-close-call.mp4`
- **Station / rights holder:** KFOR Oklahoma's News 4 (channel_id `UCEUYiWFyzpEBMZ3aG7ud7xg`)
- **Proposed cut:** 0:00–0:04 (~4s, unchanged — verified clean) — trees whipping, tornado visible close behind the KFOR chase vehicle, "Live 4" bug on screen
- **Transcript (VERBATIM, faster-whisper small.en):** "please do not ride this out in any interior closet or bathroom." A complete sentence, followed by a clean pause before the next line — no chop, no dead air within the window.
- **Beat served:** A3-S1/A3-S1b (the trap tightening / escape margin beat) — near-miss tension
- **Frames:** `.../media/_gate/kfor-sutton-very-close-call/frame1.jpg`, `frame2.jpg`, `frame3.jpg`
- **Source URL:** `youtube.com/watch?v=t8dKk86Oa-o` — "LIVE: Emily Sutton Has Very Close Call" (2013-06-02) per clip_hunt.md §3
- **Claim expectation:** Content ID revenue claim, budgeted
- [ ] APPROVE
- [ ] REJECT

### 4. `abc-3-storm-chasers-killed.mp4`
- **Station / rights holder:** ABC News (network-official, channel_id `UCBi2mrWuNuyYy4gbM6fU18Q`)
- **Proposed cut:** 0:03.2–0:06.9 (~3.7s — NUDGED from 0:00–0:04) — rural field damage shot (snapped trees, downed line, EF0/EF1-level debris; frame1)
- **Transcript (VERBATIM, faster-whisper small.en):** "Among the 13 people killed in the Oklahoma Twister were three men" — original 0:00-0:04 window was ~3.2s of dead air/other audio before this narration starts, then chopped mid-word on "deeply"; nudged to start on-speech and end cleanly after "men," before "deeply involved in tornado research" continues.
- **Beat served:** A3-S2/A3-S4 (TWISTEX death beat — establishing damage context)
- **Frames:** `.../media/_gate/abc-3-storm-chasers-killed/frame1.jpg`, `frame2.jpg`, `frame3.jpg`
- **Source URL:** `youtube.com/watch?v=O_LXG2aYfE4` — "3 Storm Chasers Killed in Oklahoma Tornadoes" (2013-06-03) per clip_hunt.md §3
- **Claim expectation:** Content ID revenue claim, budgeted
- [ ] APPROVE
- [ ] REJECT

### 5. `cnn-samaras-family-interview.mp4`
- **Station / rights holder:** CNN (network-official, channel_id `UCupvZG-5ko_eiXAupbDfxWw`)
- **Proposed cut:** 0:03.0–0:07.0 (~4s — NUDGED from 0:00–0:04) — Sal Lucido (Carl Young's stepfather) speaking to camera, lower-third names him (frame2)
- **Transcript (VERBATIM, faster-whisper small.en):** "Car[l] was killed Friday afternoon and I didn't hear about it" (whisper transcribed the name as "Car," almost certainly "Carl" — consistent with Carl Young). Original 0:00-0:04 window was ~3s of dead air before speech, then chopped mid-word on "killed"; nudged to start on-speech and end cleanly right before "until Sunday morning" continues.
- **Beat served:** A7-S2 (TWISTEX legacy/humanizing beat)
- **Frames:** `.../media/_gate/cnn-samaras-family-interview/frame1.jpg`, `frame2.jpg`, `frame3.jpg`
- **Source URL:** `youtube.com/watch?v=GsCP83vwWCE` (2013-06-04) per clip_hunt.md §3
- **Claim expectation:** Content ID revenue claim, budgeted
- [ ] APPROVE
- [ ] REJECT

### 6. `koco-reshaped-storm-chasing.mp4`
- **Station / rights holder:** KOCO 5 News (station-official, channel_id `UCoIhMkbeDRBImkGiA5mZp5A`)
- **Proposed cut:** 0:00–0:03.8 (~3.8s — NUDGED end from 0:04) — remote interview subject in front of a radar display on a home monitor (frame2/3)
- **Transcript (VERBATIM, faster-whisper small.en):** "the 2013 El Reno tornado and Oklahoma County flash flooding" — original 0:04 end point chopped mid-word on "left"; trimmed ~0.2s earlier to end cleanly right after "flooding," still under the 4s cap.
- **Beat served:** A6-S3 (chase-culture reckoning, "what changed after")
- **Frames:** `.../media/_gate/koco-reshaped-storm-chasing/frame1.jpg`, `frame2.jpg`, `frame3.jpg`
- **Source URL:** `youtube.com/watch?v=aRdeq_MEOaM` — "A storm that reshaped storm chasing" (2:04) per clip_hunt.md §3
- **Claim expectation:** Content ID revenue claim, budgeted
- [ ] APPROVE
- [ ] REJECT

### 7. `cnn-ethics-of-chasing.mp4`
- **Station / rights holder:** CNN (network-official, channel_id `UCupvZG-5ko_eiXAupbDfxWw`)
- **Proposed cut:** 0:00–0:04 (~4s, unchanged — verified clean) — CNN reporter on-scene at wreckage/debris pile, hand gesturing toward a crushed vehicle (frame1/2)
- **Transcript (VERBATIM, faster-whisper small.en):** "Because you're watching Mother Nature at work and all the associated dynamics," — a complete clause ending on a natural pause (the next line, "it's fantastic," starts after the window). No chop, no dead air. Note: this line is someone (a chaser, before Tim Samaras is named later in the package) explaining the draw of chasing, not the reporter's own risk/ethics framing — confirms the clip does touch the "why do people do this" angle the title promises, though the specific 4s window is scene-setting rather than the explicit ethics debate.
- **Beat served:** A3-S3/A6 (chasing-risk framing)
- **Frames:** `.../media/_gate/cnn-ethics-of-chasing/frame1.jpg`, `frame2.jpg`, `frame3.jpg`
- **Source URL:** `youtube.com/watch?v=OzNfXo8Sm-I` — "Are storm chasers taking too much risk?" (2013-06-04) per clip_hunt.md §3
- **Claim expectation:** Content ID revenue claim, budgeted
- **Note:** the 3 sampled frames show wreckage/breaking-news chyrons rather than an explicit "ethics" framing shot — confirm the actual 0:00-0:04 window lands on the risk-discussion portion, not the breaking-news recap, before final wiring.
- [ ] APPROVE
- [ ] REJECT

### 8. `kfor-tenth-victim.mp4`
- **Station / rights holder:** KFOR Oklahoma's News 4 (channel_id `UCEUYiWFyzpEBMZ3aG7ud7xg`)
- **Proposed cut:** 0:00–0:03.8 (~3.8s — NUDGED end from 0:04) — daytime road scene, fire/rescue vehicles staged (frame1)
- **Transcript (VERBATIM, faster-whisper small.en):** "Oklahoma's woke up once again this morning to tragedy" — original 0:04 end point chopped mid-word on "after"; trimmed ~0.2s earlier to end cleanly right after "tragedy." (~0.7s lead-in silence before speech starts is negligible, left as-is.)
- **Beat served:** A4-S4/A7-S3 (death-toll / named-categories beat)
- **Frames:** `.../media/_gate/kfor-tenth-victim/frame1.jpg`, `frame2.jpg`, `frame3.jpg`
- **Source URL:** `youtube.com/watch?v=y65DPajL0wI` (2013-06-02) per clip_hunt.md §3
- **Claim expectation:** Content ID revenue claim, budgeted
- **Note:** "tenth victim" language in the original KFOR package reflects a broader 2013-outbreak count (tornado + flood combined, contemporaneous reporting) — do NOT let the on-screen "10th" number contradict our locked FACT LEDGER figures (8 tornado deaths / 13 flood deaths); use only as neutral b-roll, mute any conflicting on-screen text if present in the actual cut.
- [ ] APPROVE
- [ ] REJECT

### 9. `koco-survivor-testimony-a.mp4`
- **Station / rights holder:** KOCO 5 News (channel_id `UCoIhMkbeDRBImkGiA5mZp5A`)
- **Proposed cut:** ⚠️ UNVERIFIED — see flag below. Do NOT wire until owner confirms.
- **FLAG (2026-08-01):** The claimed caption **"Never thought it would happen to us, and it did."**
  does **not** appear anywhere in this file. Checked exhaustively: (1) faster-whisper small.en
  transcribed the ENTIRE 120.4s clip verbatim (not just the proposed window) and that phrase is
  not in it; (2) both sampled review frames (`frame1.jpg`, `frame2.jpg`) show the interview
  subject with a station mic and no caption/lower-third text burned in at all. Either this quote
  belongs to one of the other two unmapped KOCO 2019 survivor-testimony source URLs
  (`opEZ8hVGyB4` / `R_iM34O7Cs0` / `pMsfPk-FxxI` — one is likely `-b` or `-c`, not `-a`) and was
  mis-assigned to this filename, or the caption claim in the original packet entry was itself
  unverified. **Recommend re-checking which of `koco-survivor-testimony-a/b/c.mp4` actually
  contains that caption before approving this beat on the strength of that quote.**
- **Full verbatim transcript of this file (faster-whisper small.en, entire 120.4s, for reference/re-triage):**
  interview covers: hearing screaming, thinking they'd get out because she "could see holes,"
  knowing her father was on the way, what she saw stepping outside ("a lot of destruction... I
  saw some blood on the floor... just bodies everywhere... limbs, legs, arms"), whether it was a
  "war zone or disaster zone," checking on friends/neighbors with trailers gone, and closing:
  *"...because you never know when something's gonna happen and how quick it can happen. Yeah,
  you don't think about it. That's right."* (~1:40–1:49) — this closing exchange is the closest
  actual sentiment match to the packet's claimed quote ("never thought it would happen"), but it
  is NOT the same wording and should not be presented as the verbatim caption.
- **Description:** pending owner re-triage of the caption/filename mismatch above — do not treat
  any quoted text for this clip as a verified caption until resolved.
- **Beat served:** A7-S3 (human-cost close, restraint beat)
- **Frames:** `.../media/_gate/koco-survivor-testimony-a/frame1.jpg`, `frame2.jpg`
- **Source URL:** not recorded in clip_hunt.md (one of the 3 KOCO 2019 survivor-testimony shorts, `opEZ8hVGyB4` / `R_iM34O7Cs0` / `pMsfPk-FxxI` — not individually mapped to filenames in the hunt doc)
- **Claim expectation:** Content ID revenue claim, budgeted
- [ ] APPROVE
- [ ] REJECT

---

## 2. BENCH — 12 clips not shortlisted

- `cnn-damage-done.mp4` — same reporter-at-wreckage setup as the shortlisted ethics clip; redundant angle, would duplicate the visual grammar within one act.
- `cnn-storm-reporting-dangerous.mp4` — 6-minute studio panel (Reliable Sources); no single 4s window stands out over the shortlisted family-interview/ethics clips; duration also the longest of the 21, hardest to isolate a clean cut from.
- `kfor-10yr-recap.mp4` — **see PROVENANCE FLAGS below; recommend exclusion.**
- `kfor-2019-survivor-testimony.mp4` — solid but redundant with koco-survivor-testimony-a/b/c and kfor-tenth-victim's daytime reporter stand-up; weaker frames (night ambulance b-roll, less distinctive than the shortlisted captioned quotes).
- `kfor-retrospective-2026.mp4` — 26-minute in-house podcast wrapper; no clean ≤4s cut identified from 3 frames alone (frame1/2 are two hosts talking, frame3 is a useful TWISTEX-location map graphic but is a re-created graphic, not raw footage — better sourced as our own graphic if needed).
- `kfor-sutton-studio-interview.mp4` — good content (Sutton post-storm reflection) but the beat it'd serve (aftermath/reflection) is already covered by koco-reshaped-storm-chasing; avoid doubling up on the same reflective-interview beat.
- `koco-10yr-anniversary.mp4` — vertical/Shorts aspect ratio, awkward fit for a 16:9 documentary composition; anniversary framing already covered by the shortlist's forward-looking beats.
- `koco-one-year-ago.mp4` — frame2 shows the wrecked Cobalt exterior; **sensitivity note, not excluded for provenance** — edit_script.md's existing house guidance already plans the NWS crash-scene PD photo for this exact beat (A3-S4) as the "static historical document" version; this broadcast alternative would duplicate that plan and raises the same TWISTEX-vehicle sensitivity the script flags. Bench in favor of the already-planned PD photo.
- `koco-survivor-testimony-b.mp4` — same beat as survivor-testimony-a with a weaker/no visible caption in the sampled frames; redundant.
- `koco-survivor-testimony-c.mp4` — same beat again; captioned quote is good ("tornado blew our shoes off our feet") but a third survivor-testimony clip would be one too many for a single beat per the no-repeat-obvious rule.
- `twc-bettes-describes-direct-hit.mp4` — good storm-wall footage but visually near-identical to the marquee clip's wide shots; would read as an obvious repeat of the same funnel footage within one act.
- `twc-bettes-returns.mp4` — reflection/return-to-scene piece; redundant with koco-reshaped-storm-chasing's "what changed after" beat; also has one dark/unusable-looking frame (frame2, blue-black).

---

## 3. PROVENANCE FLAGS

- **`kfor-10yr-recap.mp4` — FLAGGED, recommend exclusion.** Frames 1 and 2 show unbranded,
  windshield-mount, in-vehicle POV tornado footage (visible wiper-blade/dashboard edge, rain
  streaking, shaky handheld motion) with only a small "4 WARN / STORM REPORT" bug and a
  "MAY 31, 2013" chyron overlaid — no visible KFOR reporter, no confirmed KFOR-owned chase
  vehicle context (unlike the Sutton clips, where Emily Sutton is on record as KFOR's own
  meteorologist in the vehicle). This is the exact pattern clip_hunt.md warns about: dashcam/
  chaser-style raw footage re-packaged inside a station-branded upload. The rights holder
  shown on the upload is KFOR, but nothing in these 3 frames establishes the footage was shot
  by KFOR staff rather than licensed/sourced from a third-party chaser and re-aired under a
  station wrapper — a provenance-laundering risk that could complicate rights clearance if the
  original videographer was an unlicensed independent chaser. **Recommend exclusion even though
  the "historic 2-mile wide tornado" framing would otherwise be a strong storm-coverage pull.**

- **`kfor-sutton-josefy-up-close.mp4` and `kfor-sutton-very-close-call.mp4` — reviewed, NOT
  flagged.** Both are also windshield/dashcam-style POV, but clip_hunt.md and the on-screen
  "LIVE 4" bug independently confirm these are KFOR's own on-air chase vehicle with named KFOR
  staff (Emily Sutton, Kevin Josefy) — provenance is established, not laundered. Kept in the
  shortlist.

No other clips among the 21 showed unbranded raw/chaser-style footage inside a station wrapper.

---

**Summary for owner:** 9 shortlisted, 12 benched, 1 provenance flag (`kfor-10yr-recap.mp4`,
recommend exclusion). Mark each shortlisted clip's checkbox above.
