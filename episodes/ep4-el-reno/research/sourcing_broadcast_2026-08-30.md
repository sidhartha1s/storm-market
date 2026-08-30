# Broadcast sourcing pass — 2026-08-30

Gap-fill for GAP A (2013 OKC interstate gridlock) and GAP B (May 31–June 1 2013 OKC flash-flood
night), plus a 30–40% extra-cut pass over the 23 existing raw broadcast files. All sources are
official station/network YouTube channels, `channel_id` verified before download. No
storm-chaser/streamer/private footage used; two chaser-credited shots (`StormChasingVideo.com`,
`TVNWeather.com`) were found embedded inside otherwise-official broadcasts and deliberately
avoided (see "Not found / avoided" below). `kfor-10yr-recap.mp4` (banned, provenance-laundering
flag) was not touched.

## Sources downloaded (4 new raw files)

| File | Channel | channel_id | Title | Uploaded | Duration |
|---|---|---|---|---|---|
| `broadcast/abc-families-fleeing-highways.mp4` | ABC News | `UCBi2mrWuNuyYy4gbM6fU18Q` | Families Fleeing Storm Trapped on Okla. Highways | 2013-06-02 | 164.4s |
| `broadcast/abc-tornadoes-rush-hour-trucks.mp4` | ABC News | `UCBi2mrWuNuyYy4gbM6fU18Q` | Tornadoes Strike During Rush Hour, Overturn Trucks | 2013-06-01 | 168.6s |
| `broadcast/kfor-chopper4-flooding-aerials.mp4` | KFOR Oklahoma's News 4 | `UCEUYiWFyzpEBMZ3aG7ud7xg` | Raw: Chopper 4 aerials flooding in OKC | 2013-06-02 | 38.6s |
| `broadcast/kfor-flooded-streets-metro.mp4` | KFOR Oklahoma's News 4 | `UCEUYiWFyzpEBMZ3aG7ud7xg` | Power lines down and flooded streets throughout the metro | 2013-06-02 (desc: "May 31") | 170.2s |

Downloaded at 640x360 (source ceiling — only format 18 available via yt-dlp `android` client;
`-f "bv*[height<=1080]+ba/b[height<=1080]"` returned 403s on all four until switching to
`--extractor-args "youtube:player_client=android" -f 18`). Matches the resolution profile of the
existing 23 raw files, which are also mostly 640x360 pre-grade.

## GAP A — 2013 OKC interstate gridlock (3 cuts)

| File | Parent | Window | Dur | Beat | On screen | Audio |
|---|---|---|---|---|---|---|
| `abc-families-fleeing-highways__0008.60-0013.10.mp4` | abc-families-fleeing-highways | 8.60–13.10 | 4.50s | A4 exodus | Aerial night highway, light-trail traffic | "...traffic at a standstill on major highways...gridlock proving deadly" |
| `abc-families-fleeing-highways__0024.20-0030.28.mp4` | abc-families-fleeing-highways | 24.20–30.28 | 6.11s | A4 exodus | Storm-chopper aerial over metro (green sky) → night overpass traffic, headlights | "...deadly tornado looming above...complete gridlock" |
| `abc-tornadoes-rush-hour-trucks__0050.04-0056.40.mp4` | abc-tornadoes-rush-hour-trucks | 50.04–56.40 | 6.37s | A4 exodus (best candidate) | Night highway light-trail (KWTV/KOTV credit) → close bumper-to-bumper gridlock, ambulance lights among stopped cars | "Thousands of central Oklahomans...clogged Interstate 40" |

Best candidate: the third row — tightest match of narration to a real, dynamic gridlock shot,
sourced via ABC re-airing KWTV/News9-credited (official, allow-listed) footage.

## GAP B — May 31–June 1 2013 OKC flash-flood night (4 cuts)

| File | Parent | Window | Dur | Beat | On screen | Audio |
|---|---|---|---|---|---|---|
| `kfor-chopper4-flooding-aerials__0008.00-0014.00.mp4` | kfor-chopper4-flooding-aerials | 8.00–14.00 | 6.01s | A4 flood | Aerial: muddy floodwater over a residential neighborhood, houses/trees submerged | silent (chopper b-roll) |
| `kfor-chopper4-flooding-aerials__0022.00-0028.00.mp4` | kfor-chopper4-flooding-aerials | 22.00–28.00 | 6.01s | A4 flood | Same aerial pass, different framing, for cutaway variety | silent |
| `kfor-flooded-streets-metro__0120.10-0125.32.mp4` | kfor-flooded-streets-metro | 120.10–125.32 | 5.24s | A4 flood | Flooded street at night, headlights reflecting off standing water | "...the road out here...was completely flooded" |
| `kfor-flooded-streets-metro__0125.32-0130.58.mp4` | kfor-flooded-streets-metro | 125.32–130.58 | 5.27s | A4 flood | Same flooded street, continues | "...several inches, almost a foot...full of water" |

Best candidate: the first aerial cut (`kfor-chopper4-flooding-aerials__0008.00-0014.00.mp4`) —
the single strongest flood visual in the whole pool, a KFOR chopper shot of an entire
neighborhood underwater.

## EXTRA — 12 new cuts from the existing 23 raw files (30–40% pool growth)

Compared every candidate window against filenames already in `media/broadcast/cuts/graded/`
before cutting; all 12 below are previously-unused moments.

| File | Parent | Window | Dur | Beat | Quote / content |
|---|---|---|---|---|---|
| `cnn-ethics-of-chasing__0055.72-0059.88.mp4` | cnn-ethics-of-chasing | 55.72–59.88 | 4.17s | chasers/ethics | "...a hundred yards away from debris flying...pretty grave danger" |
| `cnn-ethics-of-chasing__0062.14-0069.88.mp4` | cnn-ethics-of-chasing | 62.14–69.88 | 7.77s | chasers/ethics | Mike Eilts (Twister research team): "storm chasing has gone too far" |
| `cnn-ethics-of-chasing__0096.50-0101.02.mp4` | cnn-ethics-of-chasing | 96.50–101.02 | 4.53s | chasers/science | "...we still don't know everything about tornadoes" (opens on KOCO-credited funnel shot) |
| `kfor-sutton-studio-interview__0079.04-0084.96.mp4` | kfor-sutton-studio-interview | 79.04–84.96 | 5.94s | storm on air | Emily Sutton narrates over KFOR's own "Live 4" chase footage: "...bird fall from the sky...wind progressed even higher" |
| `kfor-sutton-studio-interview__0084.96-0091.12.mp4` | kfor-sutton-studio-interview | 84.96–91.12 | 6.17s | storm on air | Continuation: "...you'll actually start to see chunks of trees..." |
| `koco-one-year-ago__0058.56-0063.28.mp4` | koco-one-year-ago | 58.56–63.28 | 4.73s | El Reno aftermath | "The mayor of El Reno says the loss of lives forever changed..." |
| `koco-one-year-ago__0094.58-0100.90.mp4` | koco-one-year-ago | 94.58–100.90 | 6.33s | recovery | Health Center reopening ceremony: "...celebrating reopening" |
| `kfor-2019-survivor-testimony__0068.16-0073.32.mp4` | kfor-2019-survivor-testimony | 68.16–73.32 | 5.17s | survivor testimony | J.C. Gillig: "...my whole body, I was in pain...gasping for air" |
| `kfor-2019-survivor-testimony__0117.32-0120.40.mp4` | kfor-2019-survivor-testimony | 117.32–120.40 | 3.10s | survivor testimony | "I feel God had his hand on us for sure." |
| `koco-survivor-testimony-b__0037.38-0041.38.mp4` | koco-survivor-testimony-b | 37.38–41.38 | 4.00s | survivor testimony | "I know we lost everything. Everything's gone." |
| `koco-survivor-testimony-c__0027.80-0034.46.mp4` | koco-survivor-testimony-c | 27.80–34.46 | 6.67s | survivor testimony | "...put your shoes on, tie your shoes...tornado blew our shoes off our feet" |
| `koco-survivor-testimony-c__0054.10-0056.94.mp4` | koco-survivor-testimony-c | 54.10–56.94 | 2.87s | survivor testimony | "I didn't know if my mom was alive because she wasn't moving." |

Beats covered: chasers/TWISTEX reaction (3), storm on air (2), Moore/El Reno aftermath +
recovery (2), survivor testimony (5). "Retrospectives" beat (`kfor-retrospective-2026.mp4`) was
deliberately NOT mined further — the entire ~27-minute file is a studio "What's Up With This
Weather?" talk-show format (two hosts split-screen + a small radar-graphic replay), not dynamic
archival footage; the 3 cuts already wired from it are the only visually distinct windows, and
adding more from the same repetitive visual would hurt variety rather than help it. Flagged in
"Not found" below rather than force-cut.

## Not found / avoided

- **Third KWTV/KOTV or KFOR-native gridlock source**: searched `KFOR I-40 traffic stopped
  tornado warning May 2013`, `KOCO Oklahoma City interstate stopped tornado 2013`, `News9
  highways gridlocked tornado warning May 2013` — no additional correctly-dated (May 31–June 2
  2013) official gridlock upload found beyond the two ABC packages used. KWTV's own channel
  (`Oklahoma's Own`, `UCSGeXKPLsXkSCIwaG2cCjLA`) has no standalone 2013 gridlock upload; its
  gridlock b-roll only surfaces re-aired inside the ABC package.
- **Third KOCO/News9 flood source**: searched `KOCO flood water rescue Oklahoma City 2013`,
  `News9 flooding OKC 2013 rescue water`, `13 dead flooding Oklahoma City 2013 news` — all
  KOCO/News9 flood-titled hits found (`Busy Oklahoma City interstate flooded with water`,
  `SkyNEWS 9 HD Gives Bird's-Eye View of Flooding`, `Families rescued from flooded homes in El
  Reno`, etc.) date to 2010, 2019, or 2022, not May–June 2013. Two KFOR sources covered the gap
  instead.
- **`StormChasingVideo.com`-credited dashcam segment** (first 0–13s of
  `abc-tornadoes-rush-hour-trucks.mp4`): frame-checked, confirmed third-party chaser-video-vendor
  credit burned in — excluded from every cut window in that file.
- **`TVNWeather.com`-credited funnel shot** (~79–84s of `cnn-ethics-of-chasing.mp4`, "Thrill
  seekers hoping to capture chaos" line): frame-checked, confirmed third-party credit — the
  narration window was moved to 96.50–101.02s instead (opens on a KOCO-credited, official-station
  shot).
- **`kfor-tenth-victim.mp4`**: silent (no audio track), and `BEST_CUTS.md` already flags its
  "tenth victim" claim as unresolvable against the fact ledger (8 tornado deaths / 13 flood
  deaths). Left untouched, no new cut made.
- **DVIDS Moore Guard video**: not part of this pass's scope (owner ask was GAP A/B + extras from
  the 23 broadcast files); `edit_script.md` still lists this as a separate must-find with only
  stills salvaged.

## Provenance

23 new rows appended to `media/provenance.csv` (4 raw sources + 3 GAP A cuts + 4 GAP B cuts + 12
EXTRA cuts), each with `file`, `source_url`, `license` (Content-ID-claims-budgeted broadcast,
`channel_id` cited), `fetched` = 2026-08-30, and `notes` (parent file, quote/description, beat).
