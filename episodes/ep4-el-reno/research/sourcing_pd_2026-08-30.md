# PD sourcing pass — 2026-08-30

Goal: +30-40% real PD video over what the wire needs, target ≥15 new usable clips. Result:
**7 genuinely new REAL VIDEO clips** (DVIDS, fills the "Moore Guard video, only stills salvaged"
gap named in edit_script.md) + **8 supplementary STATIC-GRAPHIC clips** (NWS outlook slides —
not real video, see caveat below) + 2 provenance/quality findings the team should act on.

## New REAL VIDEO — DVIDS (all US-govt/DoD PD, no cap)

| file | source | duration | on screen | beat |
|---|---|---|---|---|
| `dvids/dvids-291199-flashlight-search-a.mp4` | [DVIDS 291199](https://www.dvidshub.net/video/291199/146th-asos-moore-tornado-search-and-rescue-package) | 8.0s | 146th ASOS guardsmen w/ flashlights searching a flattened home, night, radio chatter audible | A1 Moore |
| `dvids/dvids-291199-flashlight-search-b.mp4` | same | 8.0s | soldier w/ helmet light walking a debris field with search team, night | A1 Moore |
| `dvids/dvids-291199-flashlight-search-c.mp4` | same | 8.0s | flashlight beam sweeping debris close-up, dramatic night search | A1 Moore |
| `dvids/dvids-291199-daylight-frame-search.mp4` | same | 8.0s | guardsmen climbing/searching a collapsed house frame, night (filename says "daylight", it isn't — kept as-cut) | A1 Moore |
| `dvids/dvids-291529-tarmac-loading.mp4` | [DVIDS 291529](https://www.dvidshub.net/video/291529/oklahoma-tornado-recovery) | 8.0s | USAF E-3 on tarmac, stairs deployed, airmen walking to aircraft | A1 Moore (mobilization) |
| `dvids/dvids-291529-bag-toss.mp4` | same | 8.0s | airmen tossing donated duffel bags off the aircraft, dynamic | A1 Moore |
| `dvids/dvids-291529-warehouse-unload.mp4` | same | 8.0s | airmen inside cargo bay tossing/catching bags (not a warehouse despite filename) | A1 Moore |

All 7: 1920x1080, h264 crf18, 30fps, audio kept, individually frame-checked clean of burned-in
captions. `dvids-883792-137th-response-may20.mp4` (the "Air Observer" 137th SOW package,
1920x1080 native, the best-quality raw source found) was **NOT cut** — see caveat below.

## Supplementary STATIC-GRAPHIC — NWS Norman outlook slides (PD, not real video)

**Caveat, read before using:** the 5 long "briefing" files handed to me as candidates for
"on-camera forecaster / office b-roll" turned out to be 100% narrated PowerPoint-style outlook
decks — a fixed slide held for the full narration beat, camera never on a person, no office
footage anywhere in any of them. Cutting an mp4 from a frozen slide is equivalent to a still;
it needs the same Ken Burns pan/zoom treatment at wire time and should not be counted as "real
video." Offered as optional pool variety only:

| file | source (long briefing) | on screen |
|---|---|---|
| `nwsnorman/cuts/nwsnorman-briefing-may17-18-c__182.00-188.00.mp4` | May 17 2013 10PM briefing | "Sunday Afternoon-Evening" outlook map, wide risk area |
| `nwsnorman/cuts/nwsnorman-briefing-may17-18-c__222.00-228.00.mp4` | same | "Monday Afternoon-Evening" outlook map |
| `nwsnorman/cuts/nwsnorman-briefing-may29-a__63.00-69.00.mp4` | May 29 2013 1230pm briefing | "Tornado Potential Today" map, surface low + dryline |
| `nwsnorman/cuts/nwsnorman-briefing-may29-a__263.00-269.00.mp4` | same | "2:00-6:00 PM CDT" estimated-timing map |
| `nwsnorman/cuts/nwsnorman-briefing-may29-b__103.00-109.00.mp4` | May 28 2013 11pm briefing | SPC Day-2 Categorical Outlook, **national CONUS map** (distinct wide view) |
| `nwsnorman/cuts/nwsnorman-briefing-may29-b__163.00-169.00.mp4` | same | "Severe Weather Timing Wednesday" 3-color time-band map |
| `nwsnorman/cuts/nwsnorman-moore-may20-briefing-b__83.00-89.00.mp4` | May 19 2013 830am briefing (day before Moore EF5) | "This Afternoon-Evening" map, risk centered on OKC/Moore — date-relevant A1 lead-in |
| `nwsnorman/cuts/nwsnorman-moore-may20-briefing-b__223.00-229.00.mp4` | same | "Monday Afternoon-Evening" map |

All 8: 1920x1080, h264 crf18, 30fps, no audio, 6s each, static single frame throughout.

## Findings the team should act on

1. **`nwsnorman/nwsnorman-elreno-radar-loop-c.mp4` appears MISLABELED.** Eyeballed the full
   130s file (contact sheet, 10s samples): every frame is dated **"April 9, 2013"** on screen —
   not May 31, 2013. This is not El Reno tornado radar. Left untouched (no cuts made from it).
   Recommend the team re-verify/rename/pull this file before it gets wired into anything.
2. **`nwsnorman-lessons-most-dangerous-tornado-full.mp4` is already fully mined** — confirmed by
   both eyeballing it (contact sheet, 60s samples across all 25:47) and cross-checking
   `provenance.csv`'s existing docmine rows (27 clips, dated 2026-08-03, from the same file).
   The only unmined content left is (a) storm-intercept photos individually credited to named
   researchers/chasers (Talbot, Garfield, Farrar/Demko, Robinson, Sullivan, Gullickson/Tempest
   Tours — same credit-risk class as the already-flagged "Dick McGowan" shot) — banned per house
   rule, credit is not a license — and (b) diagram slides (buoyancy balloon, skew-T, CAPE,
   inflow-winds notch, TWISTEX path map) that duplicate what docmine already pulled. No new safe
   cuts made from this file.
3. **`dvids-883792-137th-response-may20.mp4`** (the highest native-res DVIDS find, 1920x1080,
   "Air Observer" 137th SOW package) has an aerial flyover of the Moore damage path and a
   wreckage/blue-flag close shot that looked clean on a coarse 1s contact sheet, but a precision
   re-check showed the produced package has near-continuous burned-in stat captions and
   crossfade wipes throughout its 62s runtime — no clean 5+s window exists. Two attempted cuts
   were made, verified captioned, and are **NOT usable as-is** — left on disk renamed
   `media/dvids/CAUTION-captioned-DO-NOT-USE-dvids-883792-aerial-flyover.mp4` and
   `...-wreckage-flag.mp4` (no provenance row, do not wire) so they don't get mistaken for
   cleared assets. Not recommended for reuse without a full manual scrub-through if the team
   wants that aerial shot. Raw source is at `media/dvids/_raw/dvids-883792-137th-response-may20.mp4`.

## Searched, not found (confirms existing gaps in footage_sources.md)

- No El Reno/Canadian County-specific DVIDS asset (video or image) — DVIDS coverage of this
  disaster period is Moore-only, as previously documented.
- No OKC flash-flood-night (May 31-Jun 1) DVIDS or FEMA video.
- No FEMA-hosted video (FEMA's own multimedia library did not surface distinct video beyond the
  already-catalogued Booher stills).
- DVIDS's own search UI/API is Cloudflare/WAF-blocked to non-browser clients; all finds above
  came via targeted web search for known asset pages, then direct cloudfront mp4 pulls
  (`https://d34w7g4gy10iej.cloudfront.net/video/<catalog>/<DOD_id>/<DOD_id>.mp4` — the
  *unsuffixed* filename is the full-res original; suffixed variants like `-720x406-800k` are
  lower-res transcodes).

## Counts

- Real video: 7 new clips (target was "≥15 usable clips" combined with existing pool additions —
  fell short on real video alone; the static-graphic set brings the combined new-asset count to 15).
- Provenance rows added: 15 (`media/provenance.csv`, dated 2026-08-30).
- Raw DVIDS downloads kept at `media/dvids/_raw/` (3 files, ~250MB combined) for future re-cutting
  if more windows are wanted later.
