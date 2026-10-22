# Brief: g-path-map (BASE only) · ep-moore-1999 · builder Opus 5.5 high

The base map family for the episode (`mg_plan.md` "Deep"). This round builds the BASE alone, for a full-size read before
any act variant is copied from it (mg-brief-template 7a, last line). Act variants (I1, A1, A2, A3, A4, A5) come later,
cued to their act's words.json; do not build them now.

## 0. What this graphic claims
The 3 May 1999 tornado (survey ID A9) ran on the ground from about 2 mi SSW of Amber (Grady County) to Midwest City
(Oklahoma County), about 37 miles, up to 1 mile wide, through Bridge Creek, Newcastle, south Oklahoma City, Moore and Del City.

## 1. SOURCE
- Track: `media/stills/oun-19990503_overview_filled.kml` (NWS Norman damage-path KML, public domain; 60 geometries for the
  whole outbreak: find A9 as the long SW-to-NE track that starts near 34.98 N -97.9 W (Amber) and ends in Midwest City near
  35.45 N -97.38 W; check it against the towns below and say which geometry index you used).
- Facts (research/fact-sheet.md, all CONFIRMED): touchdown 6:26 pm about 2 mi SSW of Amber; Bridge Creek 6:47 pm; Newcastle
  (I-44 at SH-76) 7:02 pm; Moore city limit 7:22 pm; Del City limits (SE 44th) 7:38 pm; Midwest City limits 7:41 pm;
  dissipates about 7:48 pm in Midwest City north of Reno Ave. Path 37 mi; max width 1,760 yd (1 mile).
- Counties: Grady, McClain, Cleveland, Oklahoma (the four on the path; lead times 65 / 18 / 31 / 13 min, SA p9); Comanche
  and Caddo also take a warning in A1-S1 (4:47 pm), so the frame must be able to show them.
- County outlines: US Census cartographic boundary file (cb_2018_us_county_500k or 20m, public domain), Oklahoma (FIPS 40)
  only. Roads: I-44, I-35, I-40, I-240 from Census TIGER primary roads (public domain), only where the map shows them.
  Download into `episodes/ep-moore-1999/media/geo/` (gitignored) and convert to a projected SVG path set by a script you run
  once and do not commit (state the projection and scale in the receipt). Never trace by eye.

## 2. DATUM, SCALE, ORIENTATION
- North up. Projection: equirectangular with cos(35.2 deg) x-scale (or Albers; state it). One px-per-mile figure for the
  whole family, computed and stated.
- Base frame: the six counties above in view with 96 px left/right and 54 px top/bottom margins. A second named camera
  state, "metro": Bridge Creek to Midwest City filling the frame. The variants push between these with `logZoom`
  (`library/inhouse/snippets/helpers.js`).

## 3. GEOMETRY
- County fills: dark ground per tokens.md canvas; county lines 1.5 px, low contrast; county names in the small tier, inside
  their county, never under the track.
- Track: drawn as the KML polygon/line, stroke in the channel red, widened to read at 1080p; a "draw-on" tween reveals it
  from Amber to Midwest City (strokeDashoffset, dash = ceil(len)+1); a head dot rides the draw head by GSAP (assert it
  sits on the head at three times).
- Town dots + labels: Amber, Bridge Creek, Newcastle, Moore, Del City, Midwest City, and Oklahoma City (downtown, as a
  reference, off the track). Labels beside their dot, never on the track.
- Leave the bottom-right corner (x >= 1600, y >= 680) free of labels: the presenter circle sits there.

## 4. MUST BE TRUE IN THE PICTURE
1. The track starts SSW of Amber and ends inside Midwest City; Bridge Creek, Newcastle, Moore and Del City sit on it in that order.
2. Its length on screen equals 37 mi at the stated px-per-mile, within 5 %.
3. Moore is south of downtown Oklahoma City; the track passes south and east of downtown, never through it.
4. Grady is the first county the track crosses; the track crosses McClain, Cleveland, then Oklahoma County.
5. Nothing is labelled that the sources above do not name.

## 5. PANEL TEXT and CUES
Base demo only: a 20 s timeline that frames all six counties, draws the track over 8 s, pops the town labels as the head
passes each, then pushes to "metro". No narration cues yet. Text: county names, town names, nothing else (chips come per act).

## 6. CONTRACT / 7. TOOLS / 7a. DONE LINE / 8. RECEIPT
As `references/mg-brief-template.md` sections 6 to 8, plus `references/mg-quickref.md` (read it before building).
File: `episodes/ep-moore-1999/compositions/g-path-map.html`, composition id `g-path-map`. Do not touch index.html; the
orchestrator mounts it. Palette and type: `library/inhouse/snippets/tokens.md`. Start from
`library/inhouse/master-map-us-canada.html` (basemap pattern) and say what you kept.
