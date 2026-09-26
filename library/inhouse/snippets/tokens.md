# Overlay chrome design tokens (The Warning Hour)

De-facto tokens as they actually settled across shipped episodes (ep2, ep5, ep6; ep1/ep3 for
`.dim`/`.archgrade`/`.stockgrade`). Not aspirational — these are the values in the CSS today.

**This is the one home for the channel palette, fonts and type tiers** (owner ask 27 Sep 26: "keep
one palette and type file"). Every other file (`DESIGN.md`, `references/mg-quickref.md`,
`cards.css`) points here instead of restating hex codes, font stacks or px tiers. Swatch preview:
`library/inhouse/snippets/brand-swatch.html`.

## TV first
About 40 % of this channel's viewers watch on TV, 35-38 % on mobile, the rest desktop/tablet
(owner-supplied split, 27 Sep 26). Design for the TV viewer first: large type (52 px+ headline
tier, viewed from a couch on a 42-65" screen) and high background/text contrast (`#f2f5f8` on
`#04070c`-family darks, never mid-grey on mid-grey). What reads clearly on a TV at distance —
big bold type, strong contrast, few colours per frame — also reads cleanly on a 6" phone up close;
the reverse is not true, so TV is the binding constraint, not an afterthought for the minority.

## Canvas
- Composition: 1920×1080, `#root { position: relative; overflow: hidden; background: #04070c; }`
- Panel/text-block width convention: 820px-ish content column (`.quotecard` typically
  `left/right: 140-260px` on a 1920 canvas ≈ 1400-1640px wide; narrower `.quotecard.glasscard`
  variant uses `left/right: 260px`).
- Lower-third anchor: `left: 110px; bottom: 110px` (`.lt`, `.stamp` mirrors it at `top: 110px`).

## Z-index map
| Layer | z-index |
|---|---|
| cards (`.lt`, `.popup`, `.namecard`, `.dispatchlab`, `.quotecard`, `.stamp`) | 4–8 |
| `#grade` (color grade overlay) | 89 |
| `#vignette` | 90 |
| `#grain` | 91 |
| `.dust` | 92 |

## Palette
Palette and surfaces (glass card, beige cite card, popfig red) live in `references/mg-quickref.md` "Palette and surfaces".
`cards.css` chips use the glass-card surface (the `rgba(5,8,12,…)` dark chips were retired 26 Sep 26).

## Type stacks
- **Emotive / italic:** Georgia, 'Times New Roman', serif — quotes (`.quotecard .q`), namecard
  subs, polaroid captions.
- **Data / names / headlines:** Arial, 'Arial Black', sans-serif — location labels (`.lt-loc`),
  namecard names, popfig subs, popups.
- **Counters / dispatch / radio:** 'Courier New', monospace — `.dispatchlab .d1`.
- **Display headline (dates/figures):** 'AbrilFig' (`AbrilFatface-Regular.ttf`, `@font-face`),
  falls back to Georgia, serif — `.popfig .pf-big`.

## Grade tints (per-episode color story, applied via `#grade`)
- Warm / fire: `rgba(255,150,90,0.24)` (ep5, wildfire) — spec calls out `rgba(255,200,140,.30)`
  as the fire family; ep5's shipped value is close but not identical, use ep5's as the proven
  baseline and treat `.30`/lighter amber as an acceptable variant.
- Cold / flood: `rgba(96,138,178,0.22)` (ep6, flood) — matches spec exactly.
- Both use `mix-blend-mode: soft-light`, `#grade { position: absolute; inset: 0; z-index: 89;
  pointer-events: none; }`.

## Archival/stock filters (ep1, ep3 — not a `#grade` overlay, applied per-clip)
- `.archgrade { filter: sepia(0.28) contrast(1.08) brightness(0.96) saturate(0.8); }`
- `.stockgrade { filter: saturate(0.55) contrast(1.12) brightness(0.82) sepia(0.12); }`

## Scrim / dim overlays (ep1)
- `.dim { position: absolute; inset: 0; background: rgba(3,5,8,0.45); pointer-events: none; }`
- `.dim-heavy { position: absolute; inset: 0; background: rgba(2,4,6,0.68); pointer-events: none; }`

## Structural rules (don't violate)
- GSAP timelines only — no CSS `@keyframes` (breaks fast-capture render).
- Overlay exits slide out and end at `autoAlpha:0` (`references/mg-quickref.md` "Motion and exits");
  a hard unmount at the end of the card's track-3 window is not an exit.
- Any positioned card class placed with `left/right/top/bottom` needs `inset: auto` to
  neutralize `.clip`'s `inset: 0` (see ep3's `.lt`, `.quotecard`, `.srclab` — ep2/ep5/ep6
  predate this fix and rely on more specific rules; carry `inset: auto` forward as the
  current best practice).
- Every text-over-media element sits on the glass card (`references/mg-quickref.md`), not a dark chip.
- Namecard/dispatch lines use `display: table; margin: 0 auto` (or `N auto 0` for stacked
  lines) per line — never `text-align: center` alone, so the background chip hugs the text.
