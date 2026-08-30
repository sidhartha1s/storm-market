# Footage Source Inventory — El Reno, OK Tornado (May 31, 2013)

Claim-safe sourcing pass only. **No bulk downloads yet.** Spot-checked a handful of URLs
for a 200/resolves — noted per entry. Channel rule reminder: storm-chaser/streamer footage
(Dan Robinson, Reed Timmer, Basehunters, TWISTEX/Tim Samaras tapes, and unofficial re-uploads
of unclear provenance) is **BANNED without license** — this event is chaser-footage-heavy, so
treat anything not from a govt/official-station/stock source as suspect by default.

---

## 1. archive.org — PD reels / news / audio

- **URL:** `https://archive.org/advancedsearch.php?q=(el+reno+tornado)+OR+(oklahoma+tornado+2013)&output=json`
  **What:** Search API confirmed 107 hits. Mixed bag — mostly unrelated podcasts/radio call-in shows
  matched on keyword noise ("2013" + "tornado" + "Oklahoma" separately). Two items worth a manual look:
  - `inside-the-mega-twister-hd` — "Inside The Mega Twister" (National Geographic, HD) — **NOT PD**,
    it's a Nat Geo production; someone uploaded it to archive.org but that doesn't launder the
    license. Do not use without checking archive.org's own rights notice on the item page.
  - `Darkest_Lost_Media_Vol2` / `localnewsarchive_others` — grab-bag lost-media compilations of
    unknown provenance (likely unlicensed broadcast rips). **Avoid.**
  **License:** Mixed/unclear per item — verify individually before use, don't blanket-trust an
  archive.org upload as PD just because it's hosted there.
  **Claim risk:** Medium-high (most items are re-uploads of copyrighted broadcast/doc content).
  **Use:** Skip unless a specific item's rights page confirms PD/CC — none confirmed yet.
  **Spot-check:** `archive.org/details/inside-the-mega-twister-hd` → 200 OK (page resolves, item exists).

- **Gap:** Did not find a dedicated PD "newsreel" or C-SPAN/govt-hearing item specific to El Reno on
  archive.org (unlike some other episodes' newsreel-rich events). If a NOAA Service Assessment public
  hearing or Congressional testimony on this event exists, it'd likely be on archive.org/C-SPAN — worth
  a follow-up pass but not found in this scan.

---

## 2. NOAA / NWS / NSSL media

- **URL:** `https://www.weather.gov/oun/events-20130531`
  **What:** NWS Norman's full event writeup — embeds: Jeff Snyder storm photos (6), Brennan Joseph &
  Tom Magnuson supercell photos, **10 damage-survey photos** (EF-2/EF-3 home/building destruction near
  El Reno), a photo of the destroyed chase vehicle where 3 TWISTEX chasers died (use only as a static
  historical document photo w/ attribution, not chaser b-roll), damage path maps, warning-polygon
  maps, rainfall maps, and KMZ path files for El Reno-Union City-Yukon and West OKC tracks.
  **License:** US-govt work product = public domain.
  **Claim risk:** None (PD).
  **Use:** Spine — damage stills, path-map overlays, meteorology-explainer graphics.
  **Spot-check:** page fetched successfully this session (content extracted via WebFetch).

- **URL:** `https://www.youtube.com/watch?v=xvVkj90pxko` — "El Reno: Lessons From the Most Dangerous
  Tornado in Storm Observing History"
  **What:** Uploaded by channel **NWSNorman** (confirmed via yt-dlp: `channel=NWSNorman`,
  `channel_id=UCacncsbh_AhMe-CUmEMzmTg`). Official NWS content — likely covers RaXPol/DOW research
  findings and the "why the warning process changed" angle.
  **License:** US-govt, PD.
  **Claim risk:** None.
  **Use:** Spine — pull narration-worthy clips, meteorology-explainer B-roll, quotable NWS analysis.

- **URL:** `https://repository.library.noaa.gov/view/noaa/32144` — "Aerial Damage Survey of the 2013
  El Reno Tornado Combined with Mobile Radar Data" (NOAA repository PDF/report).
  **What:** Aerial survey imagery + mobile radar (RaXPol/DOW) analysis, NOAA Technical Memorandum.
  **License:** PD (NOAA repository).
  **Claim risk:** None.
  **Use:** Still frames from aerial survey imagery for damage-path graphics; cite as source text on-screen.

- **URL:** `https://repository.library.noaa.gov/view/noaa/32227` — "The Multiple-Vortex Structure of the
  El Reno, Oklahoma, Tornado on 31 May 2013" (NOAA Tech Memo).
  **What:** Scientific paper w/ RaXPol-derived figures (multi-vortex structure images).
  **License:** PD.
  **Use:** Static diagram/figure inserts for the meteorology-explainer beat.

- **URL:** `https://www.spc.noaa.gov/publications/edwards/st-anim.htm` — El Reno satellite + tornado
  animated GIF (9-frame), SPC/NWS.
  **License:** PD (NOAA SPC).
  **Claim risk:** None.
  **Use:** Low-res animated radar/satellite reference — good for a quick cutaway, not hero shot.

- **RaXPol / DOW raw footage:** RaXPol is OU/ARRC's mobile radar (`arrc.ou.edu/radar_raxpol.html`),
  DOWs belong to CSWR (`cswr.org`) — **both university/nonprofit research entities, not US-govt**.
  Their raw video (if any exists beyond derived radar-image figures already cited above) is NOT
  confirmed public domain — treat as a licensing unknown, not spine-safe by default. The NOAA Tech
  Memo figures (already PD, above) are the safe way to use RaXPol's *data*; do not pull raw RaXPol
  chase-vehicle video without confirming a license.

---

## 3. FEMA / National Guard / USGS (DR-4117, incident period May 18–Jun 2 2013)

- **FEMA Photo/Media Library:** Confirmed DR-4117-OK exists (declared 2013-05-20, "Oklahoma Severe
  Storms, Tornadoes, and Flooding"). Found one confirmed FEMA-credited photo via secondary source
  (Alamy licensing a "Andrea Booher/FEMA" photo, "El Reno, Okla., June 14, 2013 — Tornado damage to a
  business in El Reno") — confirms FEMA had a photographer (Andrea Booher) on the ground shooting
  El-Reno-specific damage. **Action needed:** pull directly from FEMA's own media library
  (fema.gov/multimedia or the FEMA Photo Library / disaster/4117 page), not the Alamy resale listing —
  Alamy's own license is not the PD one FEMA's original grant carries. Not yet directly browsed this
  session; treat as a **confirmed-exists, not-yet-catalogued** lead.
  **License:** PD (FEMA work product).
  **Claim risk:** None once pulled from the FEMA original.

- **DVIDS (dvidshub.net):** Search returned strong results, but almost all indexed hits are for the
  **Moore, OK EF5 (May 20, 2013)**, not El Reno (May 31) specifically:
  - `dvidshub.net/video/883792/137th-response-may-20-2013-tornado` — 137th unit response, Moore.
  - `dvidshub.net/image/938053/moore-may-20-2013-tornado` — National Guard image set, Moore.
    Spot-check: **200 OK**, page resolves.
  - `dvidshub.net/image/937230/...aids-search-and-rescue-moore` — Guard search & rescue, Moore.
  - `dvidshub.net/news/508149/us-northcom-aids-oklahoma-tornado-disaster-relief-efforts` — NORTHCOM
    coordination article, general OK response (covers the whole May 18–Jun 2 window, so plausibly
    touches El Reno relief too, but the specific assets shown are Moore-dated).
  **License:** PD (DoD/National Guard work product).
  **Claim risk:** None.
  **Use:** These are legitimate for the episode's **Moore context beat** (item 7 below) but are NOT
  El-Reno-specific b-roll — don't caption them as El Reno damage. No DVIDS asset found yet that is
  explicitly dated/tagged to the El Reno/Canadian County tornado itself — flagged as a gap (item 8).

- **USGS:** No tornado-specific USGS media surfaced (USGS's remit here would be things like flood
  gauge data / post-event terrain change, not tornado-strike imagery) — not pursued further; low
  expected yield for this event type.

---

## 4. Government YouTube channels (yt-dlp checked)

Confirmed `yt-dlp` (2026.07.04) works on this box; channel/uploader metadata pulled per URL below.

- **NWSNorman** — `youtube.com/NWSNorman`, channel_id `UCacncsbh_AhMe-CUmEMzmTg`. Confirmed official
  (see item 2 above, `xvVkj90pxko`). Best single government video source found for this episode.
- **FEMA** official channel — not directly queried this pass; FEMA's YouTube (`youtube.com/fema`) is
  a known-good official channel per prior episodes' pattern — recommend the same follow-up pull
  (search "El Reno" / "Oklahoma tornado 2013" filtered to that channel) before sourcing.
- **Oklahoma Dept of Emergency Management (OEM)** — not directly queried this pass; flagged as a
  follow-up (their channel would carry state-level briefing/PIO footage, PD as a state-govt work,
  though state PD status should be confirmed — Oklahoma state works are generally not copyrighted
  under state statute, but verify before treating identically to federal PD).

---

## 5. Broadcast candidates (short 3–4s pulls only, narrated over)

**Critical finding: none of the highest-relevance YouTube results are on the stations' own official
channels.** Checked uploader via `yt-dlp --print channel`:

| URL | Title | Uploader/channel | Official? |
|---|---|---|---|
| `youtube.com/watch?v=h4EGJV-7HX8` | "May 31st 2013 El Reno Tornado Coverage - KFOR" | **SRRadar** | No — third-party reupload |
| `youtube.com/watch?v=6gbgqM0JfW0` | "KFOR tornado coverage May 31, 2013 - Part 2" | **tom terry** | No — private channel (not KFOR's branded channel) |
| `youtube.com/watch?v=dX7uzdfktB4` | "KFOR tornado coverage May 31, 2013 - Part 1" | **tom terry** | No, same as above |
| `youtube.com/watch?v=0LaZ1XWCwpk` | "5-31-2013 El Reno Tornado Coverage (KWTV) Pt.1" | **StormSpotterMike** | No — third-party reupload |

**Per-cut verification rule (apply before ANY broadcast pull is wired into the edit):** confirm the
upload is on the station's own verified/branded channel (KFOR4, News9/KWTV) before treating it as a
"broadcast pull, short 3-4s, narrated, Content-ID-budgeted" clip. A third-party re-upload of station
footage does NOT change the underlying rights holder (still KFOR/Griffin Media or Griffin's News9
equivalent — Content-ID claim risk is identical), but it DOES add a provenance-laundering risk: some
of these "re-uploads" may in fact be storm-chaser or private-citizen footage mislabeled with a station
name in the title (e.g., a chaser's dash-cam clip captioned "KFOR coverage"). **Do not use any of the
four rows above until the actual station's own channel is found and the same segment located there**,
or until the specific clip is frame-matched against a verified KFOR/News9 broadcast to rule out
chaser-footage mislabeling.

- **Action item:** search `youtube.com/@KFOR4` and `youtube.com/@News9` (or their current handles)
  directly for their own "El Reno 2013" anniversary/archive re-airs — stations often re-post their own
  historical coverage on anniversary dates (News9's site shows 2019/2024 "remembering El Reno" anniversary
  pieces, e.g. `news9.com/story/5e6fd4b908ef1d09b20df98b`, which may embed the station's own original
  video player rather than YouTube — check page-embedded video source directly).
- **Mike Morgan / KFOR:** confirmed he anchored the May 31 coverage per multiple secondary sources, but
  no verified-official upload of his segment located yet — same caution applies.

**Shortlist status: BLOCKED pending official-channel confirmation.** Do not source any broadcast clip
for this episode from the four URLs above as-is.

---

## 6. NEXRAD KTLX Level-II archive (self-made radar plots)

**Confirmed via GCS public-bucket listing (`gs://gcp-public-data-nexrad-l2`, HTTP JSON API, no auth
needed):**

- `2013/05/31/KTLX/NWS_NEXRAD_NXL2DP_KTLX_20130531220000_20130531225959.tar` (22:00–22:59 UTC)
- `2013/05/31/KTLX/NWS_NEXRAD_NXL2DP_KTLX_20130531230000_20130531235959.tar` (23:00–23:59 UTC) ← tornado window
- `2013/06/01/KTLX/NWS_NEXRAD_NXL2DP_KTLX_20130601000000_20130601005959.tar` (00:00–00:59 UTC Jun 1)

All three hourly tars exist and are reachable. **Spot-check:** HEAD request on the 23:00 UTC tar
returned `200 OK`, `Content-Type: application/x-tar`, ~size confirmed present (matches the pattern of
the other hourly files, each ~90–110MB). The requested 23:00–00:30 UTC window is fully covered by the
23:00 and 00:00 (Jun 1) hourly tars — good, no gap.

**Caveat:** `C:/nexrad-t/render_radar.py` (referenced in the task) is currently hardcoded to **ep1-joplin**
paths (`KSGF20110522...`, `RAW_DIR`/`OUT_DIR` pointing at `episodes/ep1-joplin/...`) — it is NOT yet
adapted for El Reno/KTLX. Treat it as a reusable *pattern* (pyart read → NWSRef/NWSVel cmap → dark-bg
render), not a ready-to-run script for this episode. A new El Reno-specific script (KTLX site, new
bounding box around El Reno/Union City/Yukon/I-40, new file list from the 23:00/00:00 tars above) will
need to be written when sourcing begins — flagging now so it's not assumed done.

---

## 7. Moore EF5 (May 20, 2013) context footage — FEMA/DVIDS, PD

Same DR-4117 disaster declaration covers both Moore (May 20) and El Reno (May 31), 12 days apart — the
episode's context/lead-in beat can legitimately use Moore footage as scene-setting for "the same brutal
May" without re-licensing:

- `dvidshub.net/video/883792/137th-response-may-20-2013-tornado` — National Guard 137th unit response.
- `dvidshub.net/image/938053/moore-may-20-2013-tornado` — image set (spot-checked, resolves).
- `dvidshub.net/image/937230/oklahoma-national-guard-aids-search-and-rescue-moore-okla-tornado`.
- `dvidshub.net/news/508149/us-northcom-aids-oklahoma-tornado-disaster-relief-efforts` — NORTHCOM/DCO
  coordination writeup, useful as narration source text too.

**License:** PD (DoD/National Guard). **Claim risk:** none. **Use:** cold-open or context beat only —
label on-screen as Moore, May 20, to avoid misattributing it as El Reno footage.

---

## 8. GAPS — nothing claim-safe found; route to AI-generated stills / own graphics

1. **Ground-level tornado-in-progress b-roll (the money shot).** Every wide, close, or dramatic shot of
   the actual 2.6-mile wedge on the ground that exists publicly is chaser/streamer-sourced (Dan
   Robinson, Reed Timmer, Basehunters, TWISTEX, Jeff Piotrowski, Vortex2/mobile-mesonet teams) or
   unverified-provenance station re-uploads (item 5). **No PD or stock equivalent exists for this
   specific storm's silhouette/multi-vortex look.** → AI-generated stills/b-roll (owner to generate)
   is the only claim-safe route for the tornado-on-the-ground hero shots.
2. **Verified official broadcast pulls (KFOR/News9).** Blocked per item 5 until official-channel
   uploads are located and frame-matched. If none surface, this becomes an AI-broll gap too, or the
   episode leans harder on the NWSNorman video + NOAA damage-survey stills instead of broadcast pulls.
3. **RaXPol/DOW raw chase video.** University/nonprofit-owned, not confirmed PD — gap unless a license
   is obtained; NOAA Tech Memo figures (item 2) are the safe substitute for the *data*, not the raw video.
4. **Day-after front pages (Daily Oklahoman, June 1 2013).** The Oklahoman's digital archive is on
   Olive Software / accessible via GenealogyBank / Newspapers.com — **all paywalled/subscription**, no
   free-to-use front-page scan located. Chronicling America (LOC, PD) only covers historical papers
   through the 1960s-70s window generally, so it doesn't reach 2013. → Gap: either budget a
   newspapers.com day-pass to screenshot the front page (then treat as fair-use brief historical
   document, on-screen only, not the whole page lingering) or have the owner AI-generate a
   period-accurate mockup front-page graphic instead of sourcing the real one.
5. **911/dispatch audio specific to El Reno/Canadian County.** Not located in this pass (archive.org
   search surfaced no matching item; NWS event page doesn't embed dispatch audio). Follow-up needed —
   check Canadian County Sheriff/OK 911 records requests, or drop this beat if unavailable in time.
6. **El Reno-specific (not Moore) DVIDS/National-Guard assets.** DVIDS indexing this session skewed
   entirely to Moore May 20; nothing found explicitly tagged El Reno/Canadian County May 31. Possible
   the Guard's May 31 response was smaller-scale/less documented than Moore's. Follow-up search with
   DVIDS's own site search (this session's WebFetch on dvidshub.net's search page returned empty —
   likely JS-rendered results; retry with a direct API/query-string search or browser automation).

---

## Summary (≤300 words)

**Strongest PD finds:** NWS Norman's event page (`weather.gov/oun/events-20130531`) is the backbone —
damage-survey photos, chase-vehicle-crash-scene photo, path/warning maps, and KMZ track files, all US-govt
PD. The **NWSNorman YouTube channel** video "El Reno: Lessons From the Most Dangerous Tornado in Storm
Observing History" (confirmed official via yt-dlp channel metadata) is the single best moving-footage
PD asset. Two NOAA technical-memo repository items (aerial damage survey + multi-vortex-structure paper)
give citable diagrams/figures for the meteorology-explainer beat. **NEXRAD KTLX archive is fully
confirmed**: hourly Level-II tars for 22:00–23:59 UTC (May 31) and 00:00 UTC (Jun 1) all exist and
resolve on the public GCS mirror — the 23:00–00:30 UTC ask is fully covered; `render_radar.py` will need
a new El Reno-specific config (it's currently ep1-Joplin/KSGF-hardcoded). DVIDS has solid PD National
Guard imagery/video, but it's dated to the **Moore EF5 (May 20)**, not El Reno itself — usable only as a
labeled context/lead-in beat under the shared DR-4117 declaration.

**Broadcast shortlist: currently blocked.** Every KFOR/KWTV-titled clip found is uploaded by a
third-party account (SRRadar, tom terry, StormSpotterMike), not the stations' own branded channels —
per-cut verification failed for all four candidates checked. Must locate the stations' own uploads (or
their embedded-player anniversary pieces on kfor.com/news9.com) before any broadcast pull is wired in.

**Biggest gaps:** (1) actual tornado-on-the-ground hero shots — this storm's public footage record is
almost entirely chaser/streamer-owned (Robinson, Timmer, Basehunters, TWISTEX) and therefore banned;
route to AI-generated b-roll. (2) verified broadcast pulls, pending official-channel confirmation.
(3) day-after front pages — paywalled, no free PD equivalent; consider an AI-generated period mockup.
(4) El Reno-specific 911 audio and DVIDS assets — not located this pass, follow-up needed.
