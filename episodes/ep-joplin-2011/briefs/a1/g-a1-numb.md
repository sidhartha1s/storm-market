# BRIEF · g-a1-numb · "a viewer said it, and the survey found it" · STANDARD (Sonnet 5.5, high)

Episode ep-joplin-2011, act A1, segment A1-S3. The host runs from a1-s3 0.00 to the wav end 17.92 (the first word is "You've" 0.64).
It is a full-frame MG on the channel ground, entered on a cut from `g-a1-theater-map`. `g-a1-strip-sirens` follows on a cut.
This brief **defines the COMMENT CARD base** (`_list.md` "Shared bases"). a1 (`g-a1-quote-58`), a2, a4 and a5 copy it, so
build the card first and send it alone for a full-size read before the rest of this comp (template 7a).
The page half is a PAGE UNDERLINE copy (the intro's I1-S5 base, if built). Exemplar `library/official/vox-annotate.html`.
Open numbers: the 3,000 likes (`_list.md` Open 1) is not drawn, and its row is reserved but empty.

## 0. What this graphic claims
A viewer's comment ("no one is paying any attention to the sirens going off") matches what the NWS survey found: the
perceived frequency of the sirens left most participants "desensitized or complacent" (S16), and the first siren had lost a
degree of credibility (S19). The comment is a viewer's words, and the page is the record. Both are on screen, and neither is spoken as fact.

## 1. SOURCE
- The comment, verbatim excerpt (`angle.md` "The opening comment"): RODALCO2007, under "JOPLIN, MO, Tornado, 22 May 2011":
  "… no one is paying any attention to the sirens going off. …" The ellipses mark the excerpt from the longer comment.
- S16 "the perceived frequency of siren activation in Joplin led the majority of survey participants to become desensitized or complacent to this method of warning." NWS Assessment, Preface.
- S19 "initial siren activation has lost a degree of credibility for many residents." NWS Assessment, Finding #2c.
- Page image: `media/candidates/a1/a1-s3_c1_nws-p4-preface-desensitized.jpg` (NWS PDF p4, public domain).

## 2. DATUM, SCALE, ORIENTATION
- Ground: `radial-gradient(ellipse at 50% 45%, #0b1016, #030507 78%)` from frame 0.
- Left half: the comment card, left edge x 120, width 760, vertically centred on y 500.
- Right half: the page box x 960 to 1560, y 200 to 900. Crop the page image to the paragraph holding "desensitized or complacent"
  and fit it inside the box (no stretch). Choose the crop so that the phrase's capital letters are at least 28 px tall on screen.
- Chip zone: top centre, x 960, y 96 to 166. Source line: x 96, baseline 1010.
- Presenter circle: nothing enters x ≥ 1600, y ≥ 680, so the circle may stay on.

## 3. GEOMETRY
**COMMENT CARD (the base; copies change only the text):**
- Panel: width 760, height from its content (min 240), fill Panel dark `#15202b` at 92 %, 1 px `rgba(255,255,255,.14)` border,
  radius 28, padding 36 px top and bottom, 44 px left and right. No avatar and no monogram (no real photo, `mg-quickref` "Text doctrine").
- Row 1: "YouTube comment · RODALCO2007" in Arial 700 22 `#93a3b2`, tracking 3. A copy whose commenter has no name on record
  prints "YouTube comment" only.
- Row 2: the comment text in Arial 700 40 `#f2f5f8`, line height 1.25, at most 3 lines.
- Row 3: "under “JOPLIN, MO, Tornado, 22 May 2011”" in Arial 700 22 `#93a3b2`.
- Row 4 (likes): 30 px of reserved height, empty. It is drawn only when the orchestrator confirms the count.
- Entrance: panel `fromTo(x:-60, autoAlpha:0 → x:0, autoAlpha:1, 0.6, power3.out)`, then rows 1 to 3 `fromTo(autoAlpha 0, y 24 → 0, 0.4)`
  0.25 s apart. The panel is hidden in CSS as well (`mg-quickref` "Motion and exits").

**Page half:**
- The page image has a 1 px `rgba(255,255,255,.14)` edge and a soft shadow (0 20px 60px rgba(0,0,0,.5)).
- Underline: a 6 px Amber 1 `#d8a13a` bar, 6 px below the phrase's baseline, from the first glyph to the last glyph of
  "desensitized or complacent" ±4 px (measure on the image at its final size). If the phrase wraps, use one bar per line, drawn in reading order.
  The bar draws left to right with `scaleX 0 → 1`, `transformOrigin:"left center"`.
- Chip: glass chip, "NUMB TO SIRENS" in Arial Black 900 52 `#f2f5f8`, tracking 2.
- Source line: "NWS Assessment, Preface and Finding 2c", Arial 700 20 `#c8d3e0`.

## 4. MUST BE TRUE IN THE PICTURE
1. The comment text on screen is the verbatim excerpt with its ellipses, and no word is changed.
2. No like count, and no frame of the chase video.
3. The underline sits under "desensitized or complacent" and under nothing else (frame read at full size).
4. The card, page, chip and source line do not overlap one another.

## 5. PANEL TEXT (exact) and CUES (a1-s3)
| element | text | cue |
|---|---|---|
| ground | | frame 0 |
| comment card in, rows 1 to 3 | "YouTube comment · RODALCO2007" · "“… no one is paying any attention to the sirens going off. …”" · "under “JOPLIN, MO, Tornado, 22 May 2011”" | panel 0.00 to 0.60, rows from "You've" 0.64 |
| page in (x 60 → 0, autoAlpha, 0.6 s) + source line | "NWS Assessment, Preface and Finding 2c" | "A" 4.80 |
| underline draws | (none) | "gone" 8.90 to "sirens." 10.04 (1.14 s, power1.inOut) |
| chip | "NUMB TO SIRENS" (S16) | "sirens." 10.04 |
| page slow push (scale 1.00 to 1.03, plain `to()`) | | 4.80 to 17.92, continuous |
| card float (y ±4 px, 4 s sine, finite repeats) | | 0.60 to 17.92 |
| exit: card and page slide out (`to x:∓980, autoAlpha:0, 0.6, power3.in`) | | 17.32 to 17.92 (the last 0.6 s) |

"For many of them, the first siren just wasn't as believable anymore" (12.06 to 13.84) is S19. The source line already names Finding 2c, so nothing new lands there.
Known gate issue: `graphics_qc` may flag page-crop comps as flat-type or undesigned (`learnings/mg.md` 12 Oct 26, open). Report it. Do not pad the design to pass.

## 6 to 8
`references/mg-brief-template.md` §6, §7, §7a (all seven), §8. Send the COMMENT CARD alone first, then the comp.
