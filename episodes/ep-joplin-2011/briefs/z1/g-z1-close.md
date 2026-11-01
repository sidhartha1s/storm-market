# BRIEF · g-z1-close · the close card after Paul's signature line · STANDARD (Sonnet 5.5, high)

Episode ep-joplin-2011, the 4.0 s tail after the last voice (index.html header: "4.0 s tail after the last voice for the close card").
Full-frame MG. Host `host-z1-close`: data-start = the end of `ins-paul-6` (Paul on camera says the signature line, ending "This was
The Warning Hour."), data-duration 4.0. Read both from the mounted host in `index.html`. It comes in on a cut from Paul; it is the last
picture of the episode. No audio in this file.
Base, hand-copied and retuned (never redrawn): the `.twh` wordmark of `library/inhouse/outro-brand.html` (Arial Black 900, 120 px,
tracking 6, `#f2f5f8`, the word WARNING in amber `#d8a13a`, its 0.45 s settle from scale 1.14 to 1). The black cover is a plain
full-frame #000 div on top (section 3). Not copied: the episode line, the tag line, its flat ground, any `#root` id.

## 0. What this graphic claims
Nothing new: the channel's name, once, as the picture ends. No episode fact, no recap, no call to action (CLAUDE.md: the script never
refers to its own structure; DESIGN.md "Signature closing footnote": it IS the outro).

## 1. SOURCE
DESIGN.md "Signature closing footnote" (the line lands on the channel name); `library/inhouse/snippets/tokens.md` for the palette.

## 2. DATUM, SCALE, ORIENTATION
1920 x 1080. Ground: `radial-gradient(ellipse at 50% 45%, #0b1016, #030507 78%)` (the channel's closing ground).

## 3. GEOMETRY
- Wordmark "THE WARNING HOUR" on one line, centred x 960, line box top 468, line-height 144 (centre y 540).
- 0.00: ground on, wordmark at opacity 0. 0.00 to 0.45: wordmark opacity 0 → 1 and scale 1.14 → 1 about its own centre (960, 540).
- 0.45 to 3.00: breathing hold, scale 1 → 1.015, ease sine.inOut (the hold moves, nothing idles).
- 3.00 to 4.00: a black cover (#000, full frame, on top) fades 0 → 1; the comp root itself is never faded and stays opaque to its last frame.

## 4. MUST BE TRUE IN THE PICTURE
1. The only text in any frame is "THE WARNING HOUR"; WARNING alone is amber.
2. The wordmark fits inside x 96 to 1824 at scale 1.14 (measure the box; shrink the font, never the tracking, if it does not).
3. The last frame (3.97 s) is black.
4. Nothing in x ≥ 1600, y ≥ 680 besides the black cover (the logo bug zone).

## 5. PANEL TEXT (exact) and CUES (host-local seconds)
| element | text | cue |
|---|---|---|
| wordmark in, settle | THE WARNING HOUR | 0.00 to 0.45 |
| breathing hold | | 0.45 to 3.00 |
| black cover in | | 3.00 to 4.00 |

## 6 to 8
`references/mg-brief-template.md` §6, §7, §7a, §8. COMPID `g-z1-close`. Add `data-type-ok="close card: the channel name only, no small print"` on the comp root.
