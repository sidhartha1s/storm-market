# g-a5-7-ride · A5-S5 6.04 to 12.52 · DEEP · Opus 5.5 high
Shared rules: `_list.md` "Shared rules". Base: `g-a5-3-island-map` (copy its basemap, projection, island polygon and city tone; build only after g-a5-3 passes its full-size read). Route-draw technique: `library/inhouse/master-map-us-canada.html`.

## 0. Claim
The later story has Cline driving a cart through the city's low parts, and other tellings put him on horseback along the beach. Neither has a route on record: these are tellings, drawn as sketches.

## 1. Source
- Cart through low areas: TSHA (sources-cline.md §4; fact-check a5-r1 row 20).
- Horseback along the beach: Wikipedia 1900 hurricane, "reportedly rode along the beach on horseback to warn residents" (sources-cline.md §4, SECONDARY; fact-check row 21).
- No route, no streets, no distance exists in any research row. Low areas are not mapped in the research either.

## 2. Datum, scale, orientation
Same projection, fit and scale bar as g-a5-3, but framed on the city end: camera starts at g-a5-3's end framing and pushes in to the amber city area so it fills x 300 to 1620 (state the zoom factor; use `logZoom` if over 1.5x). North up; the Gulf beach is the island's south (bottom) shore.

## 3. Geometry (px, at the final framing)
- Island and water as g-a5-3; only the city end lit amber at 0.6; the rest of the island blue at 0.4.
- Cart line: a hand-drawn-looking stroke (`#f2f5f8`, 4 px, round caps, slight jitter baked into the path, dash none) that wanders through the INTERIOR of the amber area, about 900 px long, never touching the shore. Drawn with stroke-dashoffset. A small cart glyph (28 px, `#f2f5f8`) rides its head.
- Beach line: a dashed stroke (`#7fb2e5`, 4 px, dash 14 8) running along the city's Gulf shoreline, offset 14 px inland from the coast stroke, about the amber area's full shore length. A small horse-and-rider glyph (32 px) rides its head.
- Chip "LATER TELLINGS: ON HORSEBACK", glass, left edge 96, top 140.
- Note "SCHEMATIC · NO ROUTE ON RECORD" Arial 700 22 px `#93a3b2` tracking 3, left 96, top 990, on from frame 0.
- Labels: "Low parts of town" (diagram label, Arial 700 24 px `#f2f5f8`) beside the cart line's start; "Gulf beach" beside the beach line's mid-point, below it over the water.
- Source line top-left top 54 (above the chip at 140; chip height ~100, check no overlap): "Texas State Historical Association · Wikipedia summary of later accounts".

## 4. Must be true in the picture
1. Neither line has a start or end pin, street name, time or distance: nothing implies a known route.
2. The cart line stays inside the city (amber) area; the beach line follows the Gulf (south) shore of the city only.
3. The SCHEMATIC note is on screen for the whole host.
4. The cart line and its glyph are on before "Other tellings"; the beach line and chip only from "horseback".
5. No label sits on a line (template 7a item 5), including the first 0.5 s of each draw.
6. Corner x >= 1600, y >= 680: island land there turns the circle off for this window; report it.

## 5. Text and cues (a5-s5.words.json; host starts at "through" 6.04)
Comp-local = word time − 6.04.
- 6.04 ("through" 6.04): frame 0 = g-a5-3's final map state with the city lit (no tally, no chips); push to the city 6.04 to 7.20, power2.inOut.
- 6.54 ("low" 6.54) /* LOW @6.54 */: "Low parts of town" label in; 6.78 ("parts"): cart line draws 6.78 to 8.60, `ease:none` with the glyph at its head.
- 9.46 ("Other" 9.46): cart line dims to 0.45.
- 10.52 ("horseback," 10.52) /* HORSEBACK @10.52 */: chip in.
- 11.26 ("riding" 11.26) /* BEACH @11.68 */: beach line draws 11.26 to 12.40, "Gulf beach" label at 11.68.
- Host: 6.04 to 12.52 (g-a5-8 cuts at "The" 12.52).

## Motion for the whole window
The push, then the two line draws; between draws the glyph at the cart line's end bobs (y ±3, 0.8 s yoyo) and the Gulf shimmer from g-a5-3 continues.

## Exit
Cut at 12.52 to the book-spine card: root to 0 over the last 0.3 s.

## Footage under it
None: full-frame map.
