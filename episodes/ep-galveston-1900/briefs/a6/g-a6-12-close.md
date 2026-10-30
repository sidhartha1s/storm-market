# g-a6-12-close · A6-S9 · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplars: `library/inhouse/title-card.html`, `library/inhouse/outro-brand.html`, `episodes/ep6-katrina-2005/compositions/g-close.html`. DESIGN.md "Signature closing footnote": the line plays over the title card and IS the outro (no recap).

## 0. Claim
None (no fact). The episode's two motifs (the 1891 page, the telegraph line) fade out under the channel's title card while the signature line plays.

## 1. Source
- 1891 page: `media/candidates/a1/A1-S1_c1_galveston-daily-news-1891-07-16.jpg` (read its `provenance.csv` row; the intro brief lists the scan's human check as open: if it is still open, use the telegraph line alone).
- Telegraph line: wire layer of `g-intro-4-wire-map`.
- Title: channel name "The Warning Hour" (DESIGN.md, `assets/brand/` logo).

## 2. Datum, scale, orientation
No axis. Title centred on (960, 500).

## 3. Geometry (px)
- Ground: tokens.md radial gradient.
- Page: the 1891 page as a still, 900 px wide, centred, opacity 0.35, slight sepia kept, blurred 2 px; whole lines only (mg-quickref "document page" rule).
- Wire: a single lit line `#7fb2e5` 3 px across the frame at y 760 from x 96 to 1824, with a slow pulse; a dark dashed second line (`#5a768f` 0.35) under it at y 790 (Havana's, as in the hook).
- Logo: `assets/brand/warning-hour-logo.png`, 160 px, centred x 960, top 300.
- Title: "The Warning Hour" Abril `AbrilFig` 110 px `#f2f5f8`, centred, top 480.
- Line under the title: 2 px `#d0121f`, 420 px, centred at y 620, scaleX 0 to 1 from the centre.
- No subtitle, no URL, no recap text. Footnote words are voice only (no captions burned in).
- No source line (no fact).

## 4. Must be true in the picture
1. Proper case "The Warning Hour" (never all caps or lowercase).
2. Page and wire fade out completely before the end; the title stays to the last frame.
3. Presenter circle OFF (close card).
4. One text node (the title) plus the logo image: `flat-type` needs 4+ text nodes, so it does not apply; state the graphics_qc result in the receipt.

## 5. Text and cues (a6-s9.words.json, 11.176 s; host 0.00 to 11.176 + tail)
- 0.00: frame 0 = page and wire on (page opacity 0.35, wire lit), ground on.
- 0.00 to 2.64 ("Disasters ... warnings."): wire pulse runs twice (0.40, 2.40 "send").
- 3.82 ("Learn") : page fades 0.35 to 0, 3.82 to 6.12.
- 5.58 ("who is sending it") : the Havana dashed line fades first (5.58 to 6.12), then the lit line (6.76 "So" to 8.42).
- 9.76 ("This") /* TITLE @9.76 */: logo in (scale 0.9 to 1, 0.5 s); title in at 10.02 ("was") (fromTo y 24, autoAlpha, 0.6, power3.out); red line grows at 10.46 ("warning").
- Hold the title to the end of the episode (host end = 11.176 + the end tail the editor sets; DESIGN.md end ask/CTA rules decide what follows).

## Motion for the whole window
Wire pulse until it fades; page drifts y −10 px over 6 s; after 10.46 the title floats ±3 px and the red line shimmers (opacity 0.8 to 1) so the hold is not idle.

## Exit
Episode end: fade to black over the last 0.8 s of the host.

## Footage under it
None: full-frame designed card.
