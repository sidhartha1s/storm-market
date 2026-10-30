# g-a4-5-homes: a million homes dark, "the costliest storm on record" (A4-S10)
Builder: Sonnet 5.5, high effort. Depth: standard (illustrated street, counter, quote card). Read `references/mg-quickref.md`, `learnings/mg.md`, `briefs/a4/_list.md`, then this brief.
Start from: `library/inhouse/numbers-rollup.html` (count-up on a leaf span) and `library/inhouse/quote-card.html` (beige cite card; tokens.md "Beige cite card"). The street is drawn fresh in SVG. File `compositions/g-a4-5-homes.html`, prefix `a45-`.
Sits over: nothing. Full-frame designed scene on track 2. Corner circle on: nothing at x ≥ 1600, y ≥ 680 except night ground and falling snow.

## 0. Claim
More than a million homes lost power, many for days; the weather service calls it the costliest storm on record up until that time.

## 1. Source
- Homes: Smith, Monthly Weather Review, Nov 1950, via https://usdeadlyevents.com/?p=3507 (SECONDARY): "in more than 1,000,000 homes being without power for many days". `research/nws-facts.md` §5 "Homes without power"; `factcheck/a4-r1.md` row 31.
- Costliest: §5 JKL "made the Great Appalachian Storm of 1950 the costliest storm on record up until that time" (a4-r1 row 33). No dollar figure anywhere (conflict 2; the $100M chip was cut, grade r1 fix 5).
- The quote card shows the source's own words; the voice says "up to that time", the card "up until that time" (the quote must be verbatim to its source).

## 2. Datum, scale, orientation
Illustration, not to scale. Horizon: snow ground from y 900 to 1080.

## 3. Geometry (px, 1920 x 1080)
- Sky: linear gradient top `#04070c` to y 900 `#0b1016`.
- Ground: rect y 900 to 1080, `#15202b`, top edge a 2 px `#dfe7ee` line at 0.35 (snow line).
- Houses: 7 outlines in a row, each 180 px wide, gap 22 px, x 150 to 1542 (nothing past x 1560: corner rule). Body 180 x 150 (y 750 to 900), gable roof apex 70 px above (y 680), stroke 3 px `#93a3b2`, fill `#0b1016`. Vary roof pitch and a chimney on houses 2, 5 (fixed values, no randomness at runtime). Snow caps: 6 px `#dfe7ee` strokes along each roof edge.
- Windows: 2 per house, 36 x 40 px, at y 790, centred at house x + 50 and house x + 130. Lit: fill `#e8c56a` at 0.9 with a 14 px glow `#e8c56a` at 0.4. Dark: fill `#15202b`, glow 0.
- Snow: 60 flakes, 2 to 4 px `#dfe7ee` at 0.4 to 0.8, falling 40 to 70 px/s with a slight drift, whole comp (finite repeats sized to the host, positions from a fixed seed).
- Counter block (centred x 960): "1,000,000+" Arial Black 900 110 px `#f2f5f8`, block y 170 to 290; "HOMES WITHOUT POWER" Arial 700 30 px `#93a3b2` tracking 6, baseline y 340. The count-up writes the digits with commas into one leaf span; the "+" is its own span. Glass card behind (tokens.md glass, radius 28), about x 520 to 1400, y 140 to 370.
- Quote card (beige cite card `rgba(232,222,200,.90)`, radius 18, dark text), x 300 to 1500, y 230 to 560: eyebrow "NATIONAL WEATHER SERVICE · JACKSON, KY" Arial 700 22 px `#6b6257` tracking 6 at top-left padding 44 px; quote "“The costliest storm on record" line 1 and "up until that time”" line 2, Georgia italic 56 px `#2a2622`, left aligned, line height 1.2.
- Source line (left 110, bottom 60) for the whole comp: "Source: NWS Jackson KY; NOAA NCEI; Monthly Weather Review, Nov 1950 (secondary via usdeadlyevents.com)" Arial 700 20 px `#c8d3e0` tracking 1. It sits on the ground band; its right end must be ≤ 1560.
- Three tiers: 110/56 big, 30 mid, 22/20 small.

## 4. Must be true in the picture
1. Windows go dark in blocks, left to right, and every window is dark by 5.20 ("days"); none relights.
2. The counter never shows a value before "more" (1.98) and lands exactly on "1,000,000" with "+", never above it.
3. The quote text is verbatim JKL ("The costliest storm on record up until that time"), with the attribution on the card; no dollar figure, no "one of".
4. One reading target: the counter block is gone before the quote card lands.
5. Houses and text stay clear of x ≥ 1600, y ≥ 680; text inside 96 / 54 px margins.

## 5. Panel text (exact) and cues
Text: `1,000,000` · `+` · `HOMES WITHOUT POWER` · `NATIONAL WEATHER SERVICE · JACKSON, KY` · `“The costliest storm on record` · `up until that time”` · the source line above.
Cues from `audio/a4-s10.words.json` (segment time = comp time):
- 0.00 "and": street on with every window lit, snow falling, source line on. Slow 2 % push on the street layer (scale 1 to 1.02, ease none, whole comp). `/* AND FOR THE PEOPLE @0.00 */`
- 1.98 "more": glass card in; count-up 1 to 1,000,000 starts (power3.out, 0.6 s). `/* MORE THAN @1.98 */`
- 2.36 "million": first block dark (houses 1 and 2: window fill and glow to dark, 0.25 s). `/* MILLION @2.36 */`
- 2.58 "homes": count lands; "+" pops in (`fromTo` scale 0.6 to 1, autoAlpha, 0.3 s, back.out(2)); "HOMES WITHOUT POWER" in (`fromTo` y 14 to 0, autoAlpha, 0.35 s). `/* HOMES @2.58 */`
- 3.06 "lost": block 2 dark (houses 3, 4). `/* LOST @3.06 */`
- 3.38 "power,": block 3 dark (houses 5, 6). `/* POWER @3.38 */`
- 4.40 "many": house 7 left window dark; 5.20 "days": its right window dark. `/* MANY / DAYS @4.40 / 5.20 */`
- 5.70: counter card out (`to` y -30, autoAlpha 0, 0.45 s, power3.in), done by 6.15; street dims to 0.5.
- 6.16 "The Weather Service": quote card in (`fromTo` y 30 to 0, autoAlpha, 0.5 s, power3.out) with its eyebrow. `/* WEATHER SERVICE @6.16 */`
- 7.64 "costliest": quote line 1 in (`fromTo` autoAlpha 0, y 12 to 0, 0.4 s, power3.out). `/* COSTLIEST @7.64 */`
- 9.12 "up": quote line 2 in. `/* UP TO THAT TIME @9.12 */`
- To end: card floats y 0 to -6 px (sine.inOut, yoyo, finite repeats); snow keeps falling.
- Exit: card slides out (`to` x 980, autoAlpha 0, 0.6 s, power3.in) in the host's last 0.6 s.
Host: data-start = A4-S10 audio start, duration = 10.093 + 0.40 = 10.493 s (assumed gap). The quote holds about 1.0 s after line 2 before the exit begins; if the real gap is shorter, start the exit no earlier than 10.0.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8. Done line item 4: capture 2.58 and 5.20 twice each and confirm counter value and window states match.
