# BRIEF · g-a1-gutter · "what people in Joplin said afterward" · STANDARD (Sonnet 5.5, high)

Episode ep-joplin-2011, act A1, segment A1-S1, the act's first picture after the I1→A1 blackout. The host runs from a1-s1 0.00 to
the wav end 14.04. It is full-frame: the page sits on the channel ground. The NIST ground photograph of a street in the path follows
(a clip in index.html, not this comp; see `_list.md` "Picture-line readings", A1-S1 photo).
Base: PAGE UNDERLINE (the intro's I1-S5 base, if built; copy its card, shadow and bar style). Exemplar `library/official/vox-annotate.html`.
Open numbers: none.

## 0. What this graphic claims
After the storm, residents told the NWS the sirens went off even for thunderstorms, meant only "a little more water in the
gutter", and came so often they stopped paying attention (S18, S17). These are the residents' words, shown on the record's own page.

## 1. SOURCE
- S18 "\"sirens are sounded even for thunderstorms,\" and \"all sirens mean is there is a little more water in the gutter\"". NWS Assessment, Finding #2b.
- S17 "they are \"bombarded with [sirens] so often that we don't pay attention\"". NWS Assessment, Finding #2b.
- Page image: `media/candidates/a1/a1-s1_c1_nws-p13-finding2b-quotes.jpg` (NWS PDF p13, printed p7, public domain). All three quotes are in one paragraph.

## 2. DATUM, SCALE, ORIENTATION
- Ground `radial-gradient(ellipse at 50% 45%, #0b1016, #030507 78%)` from frame 0.
- Page box x 300 to 1560, y 200 to 940. Crop the image to the Finding 2b paragraph and fit it inside the box. Choose the crop so the quoted
  phrases' capital letters are at least 28 px tall on screen.
- Chip zone: none (the Picture line has no chip). Source line x 96, baseline 1010.
- Presenter circle: nothing enters x ≥ 1600, y ≥ 680, so the circle may stay on.

## 3. GEOMETRY
- Page: a 1 px `rgba(255,255,255,.14)` edge and a soft shadow (0 20px 60px rgba(0,0,0,.5)).
- Underlines: 6 px Amber 1 `#d8a13a` bars, 6 px below each phrase's baseline, from the first glyph to the last glyph ±4 px
  (measured on the image at its final size), one bar per line of a wrapped phrase, drawn left to right (`scaleX 0 → 1`, `transformOrigin:"left center"`):
  - U1 "sirens are sounded even for thunderstorms"
  - U2 "all sirens mean is there is a little more water in the gutter"
  - U3 "bombarded with [sirens] so often that we don't pay attention"
- Each finished bar stays on, so three bars show by the end.
- Source line: "NWS Central Region Service Assessment, Joplin, 2011 · Finding 2b", Arial 700 20 `#c8d3e0`.

## 4. MUST BE TRUE IN THE PICTURE
1. Each bar sits under its own phrase only and is drawn while that phrase is spoken.
2. No bar crosses a line of text (6 px gap, measured on the frame).
3. The page stays inside the text-safe frame during the push.

## 5. PANEL TEXT (exact) and CUES (a1-s1)
| element | text | cue |
|---|---|---|
| ground + page (already in place, settling from scale 1.02 to 1.00 over 0.8 s with a plain `to()`) + source line | "NWS Central Region Service Assessment, Joplin, 2011 · Finding 2b" | frame 0. The source line rises on "said" 1.34 |
| slow drift toward U1 (page y −20 px over 3 s) | | "They" 2.86 |
| U1 draws | | "even" 4.56 to "thunderstorms." 5.04 + 0.5 s |
| drift toward U2 | | "Some" 6.48 |
| U2 draws | | "all" 6.86 to "gutter." 9.04 + 0.3 s (spans the phrase) |
| drift toward U3 | | "Others" 10.16 |
| U3 draws | | "bombarded" 10.86 to "attention." 13.04 + 0.3 s |
| exit: page fades through to the ground (cut to the photo at host end) | | 13.44 ("attention." end) to 14.04 |

The drifts are camera moves on the page group (text printed on the page moves with it, which is fine: it is the page, not HUD text).
None exceeds 1.5× scale. Known gate issue: page crops may flag flat-type or undesigned (`learnings/mg.md` 12 Oct 26). Report it, do not pad.

## 6 to 8
`references/mg-brief-template.md` §6, §7, §7a (all seven), §8.
