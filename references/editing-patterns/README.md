# editing-patterns — durable reference comps (owner order 2026-08-12)

Episode folders get DELETED after publishing. Docs must never point at
`episodes/<slug>/...` for a pattern — they point HERE. When an episode ships a
pattern worth copying, copy the comp into this folder the same session.

| File | Pattern it carries | Origin |
|---|---|---|
| `ep2-stat-panel-anatomy.html` | RHS fact panel over moving footage: slide-in, beats revealed one at a time to narration, timed slide-out exit (`x:980, autoAlpha:0`) riding the hard cut | ep2 (shipped, 9/10) |
| `ep2-met-explainer.html` | Meteorology explainer layer — diagram builds while the voice explains | ep2 |
| `ep2-numbers-card.html` | Big-number stat card, counter animation | ep2 |
| `ep3-map-route-fit.html` | Any spatial claim gets a MAP: route fitted onto a real map plate, anchored on measurable landmarks, fit on the mileage column | ep3 (owner-praised piece of a 2/10 cut) |
| `ep5-glass-stat-panel.html` | Glassmorphism panel (blur backdrop, 1px light border, no colored strip) over aftermath footage; no eyebrow kicker | ep5 (owner: "i really love the glassmorphic cards") |
| `ep5-grid-rightrail.html` | Pictogram grid left + clean right rail (1/4-1/3 width): big number, legend, stat rows landing one at a time | ep5 22:29-22:40 (owner: "epic") |
| `ep5-terrain-map.html` | Designed terrain map: irregular canyon walls + contour hints + canyon labels so geography reads as geography | ep5 |
| `ep6-glasscard-popfig-bfmg.html` | The three ep6 text devices: `.glasscard` (the ONE treatment for text over footage; quote variant drops the halo), `.popfig` Abril date/figure popup (red, shadow, mid-screen, ≤3 words, no colour block — replaces the red stamp cards; font in `fonts/`), and a BFMG block (three graded clips under a glass card that lands WITH the narration line) | ep6 (owner-approved v3 2026-08-23) |
| `ep6-glass-panel-camera-clamp.html` | Track-dots map + RHS glass panel on a camera that zooms/pans but is CLAMPED so the subject (the red circle) stays fully in frame and the panel never covers the dots | ep6 4:55 (owner: "great potential" → fixed) |

ep6 also ships the checker the text rules depend on: `scripts/overlap_check.mjs` v2 stages every
comp template into a bare gsap page, steps 0.5s through each host window, and intersects the
post-transform bboxes of all visible leaf text (cards AND comp-internal, mid-tween included);
>25% overlap of the smaller box or the same fact string twice on screen = FAIL. Run it before
every render; `data-overlap-ok="reason"` marks intentional layering.

Rules the patterns encode (the full MG rules: `references/mg-quickref.md`; editorial doctrine: DESIGN.md):
- Panels slide out, never vanish; exits get ~1s of land time after the last beat — never cut ON motion.
- One reveal at a time; minimal text (facts/numbers, no prose paragraphs, no eyebrow kickers).
- Stills 3-6s MAX and always in motion (punch zoom, pop or overlay on the beat; slow Ken Burns retired, DESIGN.md "Footage motion"); video is the default medium.
