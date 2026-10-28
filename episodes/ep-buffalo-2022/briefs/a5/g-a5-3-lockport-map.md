# g-a5-3-lockport-map · A5-S2 (7.90 s to end) · deep · Opus 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: the built `compositions/g-intro-4-morning-map.html` (same data sources, land/water/line styling, pin and ring; read its header comment for the data pipeline) at a new, closer scale, and `library/inhouse/master-map-us-canada.html`. Route/marker fit: `references/editing-patterns/ep3-map-route-fit.html`.

## 0. What this graphic claims
Outside Erie County, in Lockport (Niagara County, north-northeast of Buffalo), a 27-year-old man lost his life to carbon monoxide after snow buried his furnace. That death is the "+1" that turns 46 into 47 in the next segment.

## 1. SOURCE
- WIVB final-count page: "his furnace was buried in snow and sent carbon monoxide into his Lockport home"; 27-year-old man, Niagara County: `research/deaths.md` sections 2 and 4 (SECONDARY; name UNCONFIRMED, never shown); `factcheck/a5-r1.md` row 10 and the "New evidence" block.
- Geography (positioning data, not on-screen numbers): Census `cb_2022_us_county_500k` Erie County NY (GEOID 36029) and Niagara County NY (36063); City of Buffalo `cb_2022_36_place_500k` GEOID 3611000; City of Lockport `cb_2022_36_place_500k` (Lockport city, NY). Interior points expected: Buffalo 42.8925 N, 78.8597 W (same value `briefs/a4/g-a4-10-ems-pins.md` uses); Lockport about 43.1698 N, 78.6956 W. Lakes and Ontario land: Natural Earth 10m `ne_10m_lakes`, `ne_10m_admin_1_states_provinces` (as g-intro-4). Report the values you used.
- Measured: Lockport is 33.6 km from Buffalo at a bearing of about 23° (north-northeast). Narration's "Northeast of Buffalo" is accepted wording (`factcheck/a5-r1.md` row 10); the map draws true geography.

## 2. DATUM, SCALE, ORIENTATION
- Full-frame designed ground (radial gradient as tokens.md) under the map from frame 0, layer `lk-ground`. North up.
- Projection: equirectangular, cos 42.6 N (same ratio as g-a4-10). Scale 900 px per degree of latitude, 662.5 px per degree of longitude. Anchor: Buffalo interior point at (860, 640).
  x = 860 + (lon + 78.8597) * 662.5 ; y = 640 - (lat - 42.8925) * 900.
- Expected (±10 px): Buffalo pin (860.0, 640.0); Lockport pin (968.7, 390.4); Niagara County north shore near y 210; Erie County south edge near y 1056; county band x about 680 to 1125. Lake Erie fills the lower left, Lake Ontario the top, Ontario (Canada) land west of the Niagara River.
- Corner x >= 1600, y >= 680: only empty land/ground there (no label, pin or icon).

## 3. GEOMETRY (px)
- Land `#0b1016`, water `#04070a` with a 1.5 px `#2a3644` shoreline (as g-intro-4). Erie County outline 2 px `#5a768f` at 60 %; Niagara County outline 2 px `#5a768f` at 60 %, fill `rgba(127,178,229,0)` that lights to `rgba(127,178,229,0.18)` on its cue. US-Canada border dashed 6/6 `#2a3644`.
- Buffalo pin: 9 px `#93a3b2` dot + label "BUFFALO" Arial 700 26 px `#93a3b2` tracking 4, placed LEFT of the pin, right edge x 836, centre y 640 (over Lake Erie/Ontario side: 0.6-opacity `#0b1016` backing if the shoreline crosses it).
- Travel line: dashed 3 px `#dfe7ee`, dash 10 8, from Buffalo pin to Lockport pin (straight segment, length = distance between the two computed points, about 273 px; dash length `ceil(len)+1`). A marker dot 12 px `#f2f5f8` with a 2 px ring rides the line head (per-leg `attr` tween, no MotionPathPlugin); assert it sits on the line head at three times.
- Lockport pin: 11 px `#e74c3c` dot + 2 px ring pulsing (scale 1 -> 2.2, opacity 0.6 -> 0, 1.2 s, finite repeats).
- Place chip (glass as `g-intro-2-toll-chips`: `rgba(10,16,24,.55)`, blur 18 px saturate 1.15, 1 px `rgba(255,255,255,.14)`, radius 28, padding 18 px 30 px), left edge x 1010, centre y 390 (to the right of the Lockport pin, 30 px clear of its ring): "LOCKPORT" Arial Black `font-weight:900` 52 px `#f2f5f8` + " · NIAGARA COUNTY" Arial 700 30 px `#93a3b2` tracking 4. About x 1010 to 1650, y 345 to 435.
- Furnace icon panel (self-drawn SVG, no stock icon), box x 1180 to 1560, y 480 to 760 (it ends at x 1560, left of the presenter corner, so reaching y 760 is allowed): a house wall section in `#2a3644` with a furnace vent pipe `#93a3b2` exiting low on the wall at about (1260, 690); a snow mass (`#dfe7ee` at 90 %, soft top edge, a bezier path) whose top edge rises from y 760 to y 650, burying the vent; a thin grey wisp (CO) curling back from the buried vent into the wall, `#93a3b2` at 50 %, drawn by stroke-dashoffset.
- CO chip (same glass), left x 1180, top 790: "CARBON MONOXIDE" Arial Black 900 38 px `#e8c56a`. About x 1180 to 1600, y 790 to 862. Keep its right edge < 1600 (if the measured width runs past 1600, set 34 px and state the box).
- Source, Arial 400 19 px `#c8d3e0`, `left:96px; bottom:54px`: "Erie County Executive Mark Poloncarz, via WIVB".
- Type tiers: 52 big, 38/30/26 mid, 19 small.

## 4. MUST BE TRUE IN THE PICTURE
1. Buffalo and Lockport pins at the projected Census points (±10 px of §2), Lockport up and slightly right of Buffalo (bearing about 23°, never drawn due east).
2. Lockport sits inside the Niagara County outline; Buffalo inside Erie County; the Erie/Niagara county line (Tonawanda Creek) passes between them, from the Census outlines, never drawn by eye.
3. The marker moves Buffalo to Lockport along the dashed line only, and arrives as "Niagara County" is spoken.
4. No age, name or number on screen (27 is spoken, not shown); no "47" here (S3 owns it).
5. Furnace icon: the reveal follows the voice's order (CO chip and wisp on "carbon monoxide" @14.14, then the snow buries the vent on "snow buried his furnace" @15.50-16.48). At the settled frame (S2 +16.6) the vent is fully under the snow and the wisp curls from the buried vent into the wall, so the picture reads as one cause chain.
6. No label under a line, ring, dot or another label; nothing in x >= 1600, y >= 680; all text 96 px from the edges.

## 5. PANEL TEXT (exact) and CUES
Seconds from A5-S2 start (`audio/a5-s2.words.json`); comp-local = segment time - 7.90 (second column).
Strings: `BUFFALO` · `LOCKPORT` · ` · NIAGARA COUNTY` · `CARBON MONOXIDE` · `Erie County Executive Mark Poloncarz, via WIVB`

| seg t | comp t | spoken word | action |
|---|---|---|---|
| 7.90 | 0.00 | (cut from g-a5-2) | ground, land, lakes, county outlines on frame 0 (no fade from black); camera layer `lk-cam` starts a slow push scale 1 -> 1.06 about (915, 515), linear, whole window |
| 8.04 | 0.14 | "Northeast of Buffalo," @8.04-9.10 | Buffalo pin + label in `fromTo(autoAlpha 0, scale 0.6 -> 1, 0.35, back.out)` at 0.14; travel line draws from Buffalo at 0.60 (`stroke-dashoffset`, 1.6 s, power2.inOut) with the marker riding its head |
| 9.62 | 1.72 | "Niagara County," @9.62-10.46 | marker reaches Lockport at 2.20; Niagara County fill lights to 0.18 (0.6 s); Lockport pin in at 2.20, ring pulse starts |
| 12.62 | 4.72 | "Lockport" @12.62 | place chip in `fromTo(x:-40 -> 0, autoAlpha 0 -> 1, 0.45, power3.out)`; source in `fromTo(autoAlpha 0, 0.4)` |
| 14.14 | 6.24 | "carbon monoxide" @14.14-14.98 | icon panel in `fromTo(autoAlpha 0, y:20 -> 0, 0.4, power3.out)` at 6.10; CO chip in `fromTo(scale 1.15 -> 1, autoAlpha 0 -> 1, 0.4, power4.out)` at 6.24; CO wisp draws 6.30 to 7.30 |
| 15.50 | 7.60 | "snow buried his furnace." @15.50-16.48 | snow mass top edge rises y 760 -> 650 over the vent, 0.9 s, power2.out, done by 8.50 |
| whole window | | | camera push; pin ring pulse (finite repeats); marker idles with a 1 px float after arrival; no 4 s gap without a tween |
| 16.80 | 8.90 | after "furnace." @16.48 | labels and chips out `to(autoAlpha 0, y:-10, 0.5, power2.in)` stagger 0.04; map layer fades to 0 by 9.50 (fade-through to ground) |

Comp duration 9.50 s (host S2 +7.90 to S2 +17.40, 0.66 s past the wav end; trim to the real gap before S3; if the gap is shorter, end the fade at host end - 0.08).

## 6. CONTRACT
One file `compositions/g-a5-3-lockport-map.html`, root `id="g-a5-3-lockport-map-root"`, `data-composition-id="g-a5-3-lockport-map"`, PAUSED timeline `window.__timelines["g-a5-3-lockport-map"]`. Prefix `lk-`. Paths precomputed by a one-shot in-memory script (not committed; state the source files and simplification tolerance in the comp's header comment, as g-intro-4 does). Labels live outside the camera layer only if they would ride the push: here the push is 6 %, so labels may sit inside it; if `out-of-frame` or a cut word shows, move them out. Rest: `references/mg-quickref.md`. Footage: none.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a5-3-lockport-map`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a5-3-lockport-map`.

## 7a. DONE LINE
All seven items of the template 7a. Item 6: projection constants, the two interior points used and their computed px, the line length and the county boxes, printed by the script and stated in the receipt. Full-frame: no footage under it.

## 8. RECEIPT
As the template.
