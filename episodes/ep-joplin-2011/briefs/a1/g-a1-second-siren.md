# BRIEF · g-a1-second-siren · "the second time the sirens went off" · DEEP (Opus 5.5, high)

Episode ep-joplin-2011, act A1, segment A1-S11, the exit hook. The host runs from a1-s11 0.00 to the wav end 5.88. It is a full-frame map, entered
on a cut from `g-a1-ring`. The bed drops out on "meant." (audio, index.html). The A1→A2 chapter blackout follows.
Base: MASTER MAP (T1-S2) + SIREN RING (style and radius from `briefs/a2` `g-a2-countdown`, the 5:11 ring). Copy both and
add no geography. Same builder as `g-a1-theater-map` and the a2 map comps, built after `g-a2-countdown`'s ring has passed its frame read.
Open numbers: none. The siren times (5:11 and 5:38 p.m., S27) are **not** drawn here: A2's countdown reveals them.

## 0. What this graphic claims
That evening the sirens sounded twice (S27), and the second sounding left people unsure what it meant (S25, S26). The
picture plants the question only. The split into "a worse warning" against "all clear" is A2's payoff (`g-a2-map-close`), so it is not shown here.

## 1. SOURCE
- S27 "the rare occurrence of two siren activations (at 5:11 p.m. and 5:38 p.m.) during the same evening." NIST Sec. 4.7.3.
- S26 "Their interpretations of the second siren ranged from it being a warning for a situation that was more dangerous than before to an 'all clear' from danger." NIST Sec. 4.7.1.2.
- S2 the 25-siren system (the icons come from the base's I1-S2 layer).

## 2. DATUM, SCALE, ORIENTATION
- The base's projection and city framing, north up, no camera move beyond a ≤ 2 % drift.
- Both rings are centred where `g-a2-countdown` centres its ring. Ring 1 radius = the base ring radius r. Ring 2 radius = r + 24 px.
  The 24 px is visual separation only: both rings stand for the same 25-siren system, not a wider reach (§4.2).
- Presenter circle: graphics-only scene. It stays on if the rings and labels keep out of x ≥ 1600, y ≥ 680. If r + 24
  enters that corner, the circle goes off for this comp. Say which in the receipt.

## 3. GEOMETRY
- **25 siren icons:** the base's I1-S2 layer, unchanged, at 70 %.
- **Ring 1 (first sounding):** stroke 3 px, the SIREN RING colour at 40 %, dashed 12/10, static. Label "First siren" in
  Arial 700 26 `#93a3b2`, outside the ring at 200° (left), 20 px clear of the stroke.
- **Ring 2 (second sounding):** stroke 4 px, the SIREN RING colour at 100 %, solid. The pulse is three expanding copies of
  ring 2, each going from scale 1.00 to 1.18 and from opacity 0.8 to 0 over 1.2 s, staggered 0.4 s, `repeat` finite (4 cycles, no `repeat:-1`), `svgOrigin`
  at the ring centre in both from and to vars. Label "Second siren" in Arial 700 26 `#f2f5f8`, outside the ring at 340° (right),
  20 px clear of the pulse's largest radius (r + 24) × 1.18.
- No chip, no source line (the Picture line asks for none). Rows S26 and S27 are paid in A2, which carries their source lines.

## 4. MUST BE TRUE IN THE PICTURE
1. There are two rings: the first dim and still, the second bright and pulsing. Nothing else pulses.
2. The rings differ in radius by 24 px ±2 only. Neither reads as covering a different area of the city.
3. No time, number or "all clear" text appears anywhere.
4. Neither label sits under a ring stroke or a pulse copy at any point of the pulse cycle. Check it at the pulse's maximum.

## 5. PANEL TEXT (exact) and CUES (a1-s11)
| element | text | cue |
|---|---|---|
| base map + siren icons | base text | frame 0 |
| ring 1 draws (strokeDashoffset, 0.5 s) + label | "First siren" | "The" 0.50 |
| ring 2 draws + label; pulse begins | "Second siren" | "second" 0.94 (draw 0.4 s), pulse from "time" 1.16 |
| ring 2 brightens once (stroke to 6 px and back, 0.4 s) | (none) | "agree" 4.52 |
| hold to the blackout | | to 5.88. The pulse keeps running (4 cycles of 1.2 s = 4.8 s from 1.16, ending 5.96, so trim the last cycle to end at 5.88). The final 0.3 s fades to black into the chapter blackout |

## 6 to 8
`references/mg-brief-template.md` §6, §7, §7a (all seven; item 4: `svgOrigin` in both vars), §8.
