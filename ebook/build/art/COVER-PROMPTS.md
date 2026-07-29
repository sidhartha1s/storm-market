# Cover art prompts — The Storm-Ready Home

> **Current prompt is Prompt 3.** Prompts 1 and 2 produced the superseded hazard-map covers and are
> kept for reproducibility only. Dominant headline locked 2026-07-27:
> **WHAT THE SURVIVORS DID DIFFERENTLY**.

---

## Prompt 3 — portrait cover, Yoder mechanics (CURRENT)

```
Front cover of a serious American natural-disaster preparedness manual. Photographic,
cinematic, high production value. Vertical portrait, 2:3 aspect ratio.

COMPOSITION: the upper 45% is the scene. The lower 55% is a deep near-black field for
typography — keep it clean and empty of detail.

SCENE, upper area: a plain two-storey American farmhouse with warm golden light in
every window, standing calm beneath a violent dark sky. A tornado descends in the far
distance behind it. Rain streaks and debris in the air. A faint, subtle protective
glow outlines the house and yard — understated, like warm light, NOT a science-fiction
force field, no hexagons, no visible energy dome.

SUBJECT, right side, from the chest up, overlapping the scene: a plain, weathered,
ordinary-looking American man in his early fifties. Sun-lined face, slightly
asymmetric features, thick greying moustache, short practical haircut. He looks like a
county emergency-management volunteer or a contractor, NOT a fashion model and NOT
conventionally handsome. Arms crossed, calm, direct eye contact with the viewer. Dark
navy work jacket over a faded blue work shirt. Naturally lit, sober expression.

FRAME: a thin double border rule in muted antique gold inset from the trim edge,
running around the entire cover. Deep near-black ground.

TYPOGRAPHY, classical high-contrast serif, cream white, flush left with generous
margins, spelled exactly as written:

Very top, small, letter-spaced, muted gold all-caps:
PAUL REYNOLDS · VOLUME I

Directly below it, smaller italic cream:
First Edition · MMXXVI

DOMINANT HEADLINE, the largest type on the cover, three lines, all-caps, filling the
upper part of the black field — this must be visibly LARGER than the title:
WHAT THE SURVIVORS
DID DIFFERENTLY

Below it, clearly SECONDARY and smaller, the title in two lines:
THE STORM-READY HOME

Below the title, small italic cream:
The 130 things you can do before the next one.

Below a thin gold horizontal rule, small grey letter-spaced all-caps:
130 PROTECTIONS · 23 HAZARDS · 60 DAYS · 5 REGIONS

At the very bottom, inside its own thin-ruled band, small muted gold all-caps:
TORNADO · HURRICANE · FLOOD · WILDFIRE · ICE · HEAT · QUAKE · BLACKOUT

All text sharp and perfectly legible. No other text anywhere. No logos, no seals, no
government emblems, no watermarks, no page curl, no 3D book mockup.
```

### Notes on Prompt 3

- **The headline must out-size the title.** That is the single mechanic carried over from the Yoder
  cover, and it is the thing most likely to come back wrong. Check it on delivery.
- **The energy dome was deliberately toned down** to a warm glow. A hexagonal force field reads as
  a video game and undercuts a sourced reference manual.
- **The face brief is deliberately anti-handsome.** The v2 portrait read as a fashion model; Yoder's
  subject reads as a real practitioner, which is why it converts.
- This is a lot of text over a full scene, where Yoder's text sits on flat colour. If v3 comes back
  crowded, the fix is a smaller house and a simpler sky — not smaller type.

---

Byline locked: **Paul Reynolds** (collision-checked 2026-07-27 — several Paul Reynolds exist,
none in weather, disaster, or preparedness).

Generate both. Save as:
- `cover-us-clean.png` — no text, type composited in HTML
- `cover-us-typed.png` — text baked by the generator, for comparison

Target: vertical portrait 2:3, largest available size. 6×9in at 300dpi = 1800×2700 ideal.

---

## Prompt 1 — clean plate (primary)

```
Book cover art for a serious American natural-disaster preparedness manual for
families — a reference book about surviving tornadoes, hurricanes, floods, wildfires,
blizzards and long power outages. Editorial, authoritative, not sensational, not
apocalyptic.

Illustration: the continental United States seen from above at night as a dark
textured relief map. Each region glows with its own hazard energy — amber and red
spiral storm systems curling off the Gulf and southeast coast, an electric orange
corridor running north through the central plains, deep red-orange wildfire glow
across the mountain west and California, cold blue-white ice haze over the upper
midwest and northeast, pale dust ochre across the southwest desert. The hazards read
as luminous weather data painted onto the land, not literal fire or clouds.

Near-black background with faint atmospheric haze. Cinematic, high contrast,
painterly but precise, fine film grain. Palette: deep navy-black, amber, burnt
orange, cold steel blue.

CRITICAL: the bottom 40% must fade to near-solid black and stay visually empty —
that space is reserved for typography added later. Vertical portrait, 2:3 aspect.
No text, no letters, no numbers, no labels, no logos, no watermarks, no borders,
no state lines, no legend.
```

---

## Prompt 2 — baked type (comparison)

```
Book cover art for a serious American natural-disaster preparedness manual for
families — a reference book about surviving tornadoes, hurricanes, floods, wildfires,
blizzards and long power outages. Editorial, authoritative, not sensational, not
apocalyptic.

Illustration: the continental United States seen from above at night as a dark
textured relief map. Each region glows with its own hazard energy — amber and red
spiral storm systems curling off the Gulf and southeast coast, an electric orange
corridor running north through the central plains, deep red-orange wildfire glow
across the mountain west and California, cold blue-white ice haze over the upper
midwest and northeast, pale dust ochre across the southwest desert. The hazards read
as luminous weather data painted onto the land, not literal fire or clouds.

Near-black background with faint atmospheric haze. Cinematic, high contrast,
painterly but precise, fine film grain. Palette: deep navy-black, amber, burnt
orange, cold steel blue. The bottom 45% fades to near-solid black to carry text.

Typography set into the composition, in a classical high-contrast serif, cream white
on the black lower area, generously spaced and precisely kerned, flush left with a
wide left margin:

Small amber all-caps line at the very top: STORM MARKET FIELD MANUAL
Large two-line title in the lower area: THE STORM-READY HOME
Below it, smaller and lighter: What the survivors did differently — and the 130
things you can do before the next one.
Below a thin horizontal rule, small grey all-caps: 130 PROTECTIONS · 23 HAZARDS ·
60 DAYS · 5 REGIONS
At the bottom, small white: PAUL REYNOLDS

Text must be spelled exactly as written, sharp, and perfectly legible. No other text
anywhere. No logos, no watermarks. Vertical portrait, 2:3 aspect.
```

---

## Hard constraints (why they are in the prompt)

- **No agency logo, seal, or "official" styling.** The legal section of the design spec forbids
  anything implying US government endorsement. The cover is the most visible surface.
- **No baked text in Prompt 1.** Title, count, and byline are all still moveable — the count drops
  if the outline audit merges chapters, and the landing page will A/B the title.
- **Bottom 40% empty and near-black.** That is the type well. Most covers die on poor contrast
  behind the title, not on bad art.
