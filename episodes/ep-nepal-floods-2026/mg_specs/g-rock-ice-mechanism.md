# BRIEF — g-rock-ice-mechanism · A3 · hanging slab falls, ice melts to water, tongue runs far; ESB stack

## 0. Claim
The Langtang collapse was a rock-and-ice avalanche: a hanging slab breaks off, friction-melts some of its
ice into water in the fall, and the resulting slurry runs much farther than dry rock would. It was about
2,000 ft wide and fell almost 4,000 ft — about three Empire State Buildings stacked, drawn at the SAME
vertical scale as the drop so the comparison is honest.

## 1. SOURCE
factcheck-B rows 17-18 (CONFIRMED): EOS/AGU Landslide Blog + ICIMOD, "26 August 2026, Nepal and Tibet" —
rock and glacier ice fall together, friction-melt turns part of the ice to water, the slurry runs far
past a dry rockfall's reach; slab ~600 m wide, fell ~1,200 m. Converted (python-checked): 600 m = 1,968.5
ft -> "about 2,000 ft wide"; 1,200 m = 3,937.0 ft -> "almost 4,000 ft" (not quite 4,000, matches "almost").
Empire State Building height to tip = 1,454 ft (public record); 3 x 1,454 = 4,362 ft.

## 2. DATUM, SCALE, ORIENTATION
- Stage 1920x1080. Mountain face + drop occupies x 96-1180 (left/centre). ESB stack occupies x 1280-1560 (right).
- SAME vertical scale both sides: drop of 3,937 ft is drawn as 700 px -> scale = 0.17782 px/ft (700/3937).
- Drop baseline (valley floor, where the tongue runs out) at y = 980. Slab starting ledge at y = 980 - 700 = 280.
- ESB stack baseline also y = 980 (same floor line, drawn once, full width, so both scales visibly share it).
- Width check: 2,000 ft slab at the same 0.17782 px/ft horizontal scale = 355 px (used for the slab's width on the face).

## 3. GEOMETRY (px)
- Steep rock face: polygon (300,280)-(700,280)-(900,980)-(96,980), grey-brown gradient #4a5560 -> #2a221d.
- Hanging slab (rock+ice) at the ledge: rect-ish polygon 355px wide x ~90px tall at (330,240)-(685,240)-(685,330)-(330,330),
  rock #5a768f base with an ice cap #cfe6f5 stripe along the top 25px.
- Crack line: dashed red (#d0121f) zigzag along the slab's base edge (330,330)-(685,330), appears before the fall.
- Fall path: slab travels from (500,280) down to (500,980) along the face, rotating -12deg, duration ~1.4 s (fast, "fell almost 4,000 ft" in seconds).
- Ice-to-water: 8 small ice-blue fragments (#cfe6f5) detach from the slab mid-fall and turn into 8 blue droplet
  dots (#7fb2e5) by the time the slab lands (colour-morph via two overlaid elements crossfading).
- Tongue: once landed, a wide flow shape (fill #6b4f2c gradient, semi-translucent blue overlay #7fb2e5 at 35%
  opacity for "slurry") spreads from the landing point (500,980) out to x 900, well past a thin dashed grey
  "plain rockfall" reference line that stops at x 640 (labelled "DRY ROCKFALL" small, #93a3b2).
- Number ticks: "ABOUT 2,000 FT WIDE" leader from the slab (330-685,240) at (330,200). "FELL ALMOST 4,000 FT"
  vertical tick beside the fall path, from y280 to y980 at x 950, label at (960,600).
- ESB stack (right, x1280-1560): 3 stacked simple building silhouettes, EACH exactly 1454*0.17782 = 258.5 px
  tall (so 3 stacked = 775.5 px, from y 980 up to y 204.5), width 180px, fill #15202b stroke #93a3b2, a spire
  notch on the top building. Dashed horizontal guide at y 280 (the drop-top level, 3,937 ft mark) so the
  viewer sees the stack (4,362 ft) sits slightly ABOVE the drop-top line -- the honest "about three" gap.
  Label "3 X EMPIRE STATE BUILDING · 1,454 FT EACH" at (1280,150). Small note "SAME SCALE AS THE DROP AT LEFT" at (1280,1000).

## 4. MUST BE TRUE
1. The slab detaches only after the crack line is fully drawn, never before.
2. The slab's fall covers y 280->980 (700 px) in under 1.6 s — a fast, sudden drop, not a slow drift.
3. Ice-fragment dots visibly appear DURING the fall and are gone (fully "melted"/replaced by droplets) by landing — never present before the slab starts moving, never still solid ice after landing.
4. The post-landing tongue (with the blue slurry tint) extends visibly PAST the dashed "DRY ROCKFALL" reference line's endpoint (x 640) — the tongue's rightmost edge must exceed x 640.
5. The ESB stack's total height (3 buildings) is visibly taller than the "700 px = 3,937 ft" drop-top guide line at y280 — the stack's top sits above y280 (i.e., y < 280), matching 4,362 > 3,937.
6. Both number labels ("ABOUT 2,000 FT WIDE", "FELL ALMOST 4,000 FT") and the ESB label are legible, numerals on screen, words in the voice only.
7. "SAME SCALE AS THE DROP AT LEFT" note is present — this is the one honesty check a reviewer must find first.

## 5. PANEL TEXT (exact) and CUES
Headline (x96,y70): "Rock, Ice and a Fast Slurry".
Labels: "ABOUT 2,000 FT WIDE", "FELL ALMOST 4,000 FT", "DRY ROCKFALL" (small, comparison line),
"3 X EMPIRE STATE BUILDING · 1,454 FT EACH", "SAME SCALE AS THE DROP AT LEFT".
Cues (s, local @175wpm):
- headline + rock face draw in @0.4
- hanging slab + crack line reveal @3.77 (`/* CUE "rock and ice avalanche" @est 3.77 */`)
- slab falls, ice-to-water morph @7.54-8.94 (`/* CUE "friction melts some of the ice" @est 7.54 */`)
- tongue spreads past the dry-rockfall line @10.63 (`/* CUE "runs much farther than dry rock" @est 10.63 */`)
- "ABOUT 2,000 FT WIDE" + "FELL ALMOST 4,000 FT" labels @15.77 (`/* CUE "about two thousand feet wide...fell almost four thousand feet" @est 15.77 */`)
- ESB stack builds in (3 buildings staggered) + labels @21.26 (`/* CUE "three Empire State Buildings stacked up" @est 21.26 */`)
- exit @24.3 (slide out power3.in)
Declared duration 26.0 s (narration ~24.00 s + ~2.0 s tail for the number/ESB beat to land).

## QC fix log (self-audit, headless screenshot at t=22s + computed-style debug pass)
1. ESB buildings were `fill="#15202b"` (panel-dark token) against the page's own near-black radial-gradient
   background — computed styles confirmed opacity:1 and correct bounding boxes, but the buildings were
   effectively invisible (dark-on-dark). Fix: `fill="#2a3644"` (diagram grey 2) `stroke="#c8d3e0"` 3px —
   both tokens.md colours, now legible against the dark canvas.
2. "ABOUT 2,000 FT WIDE" (tick + label, originally y120-170) collided with the headline "Rock, Ice and a
   Fast Slurry" (y70-132) both vertically and horizontally. Fix: moved the tick to y=350 and the label to
   y=296 — below the slab's original ledge position, which is empty by the time this cue fires (15.77s,
   well after the slab has fallen at 7.54-8.94s).
