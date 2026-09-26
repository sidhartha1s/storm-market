# Overlay chrome design tokens (The Warning Hour)

De-facto tokens as they actually settled across shipped episodes (ep2, ep5, ep6; ep1/ep3 for
`.dim`/`.archgrade`/`.stockgrade`). Not aspirational — these are the values in the CSS today.

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
The `rgba(5,8,12,…)` backing chips still in `cards.css` are the pre-26 Sep 26 treatment; new work uses the glass card.

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
- Every text-over-media element sits on a dark backing chip `rgba(5,8,12,0.78)`.
- Namecard/dispatch lines use `display: table; margin: 0 auto` (or `N auto 0` for stacked
  lines) per line — never `text-align: center` alone, so the background chip hugs the text.
