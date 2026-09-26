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
The full palette to pick from; an episode uses 10 of these or fewer (unchanged rule, values now
listed once, here).

| Name | Hex / value | Role |
|---|---|---|
| BG deep space | `#04070c` | `#root` flat background |
| BG gradient center | `#0b1016` | canvas radial-gradient inner stop |
| BG gradient edge | `#030507` | canvas radial-gradient outer stop (78 %) — never a flat `#000`/`#0a1017` fill |
| Panel dark (RHS stat panel) | `#15202b` | panel gradient solid zone |
| Panel dark 2 | `#0b1016` | secondary panel fill |
| Panel dark 3 | `#04070a` | tertiary panel fill |
| Headline white | `#f2f5f8` | headlines, lower-third location, namecard name |
| Body light | `#dfe7ee` | body copy, row values |
| Label grey | `#93a3b2` | eyebrow, label, section header, counter label, diagram label |
| Source credit grey | `#c8d3e0` | source label chip, counter-label alt |
| Popfig red | `#d0121f` | date/figure Abril reveal (`.popfig .pf-big`) |
| Danger red 1 | `#c0392b` | death/danger accents |
| Danger red 2 | `#e74c3c` | stat-panel counter |
| Crimson | `#8e2020` | `.stamp` background, debris/blocks |
| Amber 1 | `#d8a13a` | serif subs, quote attribution, `.stamp-amber` text, warm-air diagrams |
| Amber 2 | `#e8c56a` | dispatch counter (`.d1`), namecard sub |
| Amber time | `#f5d98b` | `.stamp .st-time` |
| Amber cool time | `#c8b98a` | `.stamp-amber .st-time` |
| Cold blue 1 | `#5a768f` | cold-air / cool-part diagrams |
| Cold blue 2 | `#7fb2e5` | cold-air highlight |
| Beige cite card | `rgba(232,222,200,.90)` | quoted-source card over dark maps, dark text on top |
| Beige polaroid | `#f4f0e6` | `.polaroid` card stock |
| Beige stamp text | `#f4f0e8` | `.stamp` text colour on crimson |
| Caption dark | `#2a2622` | `.pol-cap` text |
| Caption dark sub | `#6b6257` | `.pol-cap span` |

Surfaces: glass card `rgba(10,16,24,.55)` + `backdrop-filter: blur(18px) saturate(1.15)` + 1px
`rgba(255,255,255,.14)` border, radius 28 — the ONE treatment for text over footage, no bare text
on moving footage, no dark chip (the old `rgba(5,8,12,…)` dark chips were retired 26 Sep 26;
`cards.css` chips now all use this glass surface). Beige cite card above is the only exception,
for quoted sources over dark maps.

## Fonts
| Family (CSS stack) | Source | Role |
|---|---|---|
| Georgia, 'Times New Roman', serif | system | quotes (`.quotecard .q`), namecard subs, polaroid captions |
| Arial, 'Arial Black', sans-serif | system | location labels, headlines, namecard names, popfig subs, popups |
| 'Courier New', monospace | system | dispatch/radio counters (`.dispatchlab .d1`) |
| 'AbrilFig' (Abril Fatface), falls back Georgia, serif | `episodes/<slug>/fonts/AbrilFatface-Regular.ttf`, vendored per episode via `@font-face { src: url('fonts/AbrilFatface-Regular.ttf'); }`; canonical copy at `references/editing-patterns/fonts/AbrilFatface-Regular.ttf` | display headline for date/figure popfigs (`.popfig .pf-big`) |

## Type tiers (px)
Three tiers minimum in every designed card (unchanged gate rule: `graphics_qc` flags flat-type
below 3 tiers with 4+ text nodes).

| Tier | px range | Shipped floor | Example |
|---|---|---|---|
| Small | < 26 px | 19 px (`.srclab`) is the smallest shipped size — do not go smaller; a TV viewer at couch distance loses text under this | source label, stamp eyebrow (20 px), counter label (20 px) |
| Mid | 26-51 px | — | serif sub (26-32 px), row value (30 px), quote (44 px) |
| Big | >= 52 px | — | headline (52-66 px), lower-third location (52 px), stat-panel counter (84 px) |
| Display | 150 px | fixed | Abril popfig date/figure |

**TV-readability minimum: nothing under 19 px ships on a full-frame card, and headline-weight
text stays at 52 px or above** — both are the values already shipping (ep-1974-super-outbreak:
22, 36, 38, 58, 118, 120, 150 px), kept here as the floor so a builder never guesses smaller for a
"cleaner" look. Large type and high contrast that read on a TV from the couch also read on a phone
held at arm's length; the inverse fails on TV.

## CSS custom properties
Paste into an episode's `<style>` block (or a shared `:root` if the composition already has one):
```css
:root {
  /* palette */
  --bg-deep: #04070c;
  --bg-grad-center: #0b1016;
  --bg-grad-edge: #030507;
  --panel-1: #15202b;
  --panel-2: #0b1016;
  --panel-3: #04070a;
  --headline: #f2f5f8;
  --body: #dfe7ee;
  --label: #93a3b2;
  --source-credit: #c8d3e0;
  --popfig-red: #d0121f;
  --danger-1: #c0392b;
  --danger-2: #e74c3c;
  --crimson: #8e2020;
  --amber-1: #d8a13a;
  --amber-2: #e8c56a;
  --amber-time: #f5d98b;
  --amber-cool-time: #c8b98a;
  --cold-1: #5a768f;
  --cold-2: #7fb2e5;
  --beige-cite: rgba(232, 222, 200, 0.90);
  --beige-polaroid: #f4f0e6;
  --beige-stamp: #f4f0e8;
  --caption-dark: #2a2622;
  --caption-dark-sub: #6b6257;
  --glass-bg: rgba(10, 16, 24, 0.55);
  --glass-border: rgba(255, 255, 255, 0.14);

  /* fonts */
  --font-serif: Georgia, 'Times New Roman', serif;
  --font-sans: Arial, sans-serif;
  --font-sans-black: 'Arial Black', Arial, sans-serif;
  --font-mono: 'Courier New', monospace;
  --font-display: 'AbrilFig', Georgia, serif; /* @font-face per episode: fonts/AbrilFatface-Regular.ttf */

  /* type tiers (px) */
  --type-small: 20px;   /* < 26px tier; never below 19px */
  --type-mid: 30px;     /* 26-51px tier */
  --type-big: 58px;     /* >= 52px tier */
  --type-display: 150px;
}
```

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
