# g-a3-8-sky · A3-S7 · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplar: `references/editing-patterns/ep6-glasscard-popfig-bfmg.html` (chips over footage).

## 0. Claim
On Friday, September 7, cirrus clouds moved in from the southeast in the morning; by noon only alto-stratus from the northeast. The brick-dust sky, a warning sign seen in other storms on this coast, was watched for that evening and the next morning and never showed.

## 1. Source
MWR Sept 1900 p. 372, Cline's report (factcheck/a3-r1.md rows 27, 28): "There were cirrus clouds moving from the southeast during the forenoon of the 7th, but by noon only alto-stratus from the northeast were observed"; "The brick-dust sky was not in evidence in the smallest degree ... was carefully watched for, both on the evening of the 7th and the morning of the 8th."

## 2. Datum, scale, orientation
Overlay, transparent root, over beach footage. Zones: top-centre sky inset, centre-left chips, source line top-left.
- Sky inset: one glass card 560 x 300 at left 680, top 140. Inside: a compass rose (N up) 120 px at the card's left, and a strip of sky to its right where cloud streaks move. Direction arrows point FROM the stated direction (SE first, then NE).

## 3. Geometry
- Chip C1 "FRI · SEPT 7" (popfig is not used: it would sit over the inset card) centred x 960, top 520.
- Inset layer 1 (morning): five thin white streaks `#f2f5f8` opacity 0.6, 2 px, 120 to 200 px long, drifting from the lower right to the upper left of the strip (from the SE); label "CIRRUS · FROM SE · MORNING" Arial 700 22 px `#93a3b2` tracking 3 under the strip. Compass arrow `#f2f5f8` from SE toward centre.
- Inset layer 2 (noon): three grey bands `#5a768f` opacity 0.7, 18 px tall, drifting from the upper right (from the NE); label swaps to "ALTO-STRATUS · FROM NE · NOON"; compass arrow swaps to NE.
- Chip C2 "NO BRICK-DUST SKY" centred x 960, top 520 after C1 leaves; tag "watched for, evening and next morning" Arial 700 22 px `#93a3b2`.
- Source line top-left: "Isaac Cline, Monthly Weather Review, Sept. 1900, p. 372".

## 4. Must be true in the picture
1. Directions: morning streaks come from the SE, noon bands from the NE (compass arrows agree with the labels).
2. No red or brick-coloured sky tint anywhere in the comp (it never showed).
3. The footage is not called Galveston on screen (stock, not a Galveston shot).
4. Nothing in x >= 1600, y >= 680.

## 5. Text and cues (a3-s7.words.json, segment 20.18 s; whisper "Klein's" = Cline's)
- 0.00: source line in.
- 1.14 ("Friday") /* FRI @1.14 */: C1 in.
- 3.28 ("you"): C1 out by 3.88.
- 3.96 ("Thin") /* CIRRUS @3.96 */: inset in, layer 1 streaks drift.
- 7.62 ("by noon") /* NOON @7.62 */: layer 1 fades, layer 2 slides in from the NE, label swaps 7.76 to 8.24.
- 10.92 ("Klein's"): inset dims to 0.6.
- 15.56 ("brick") /* BRICK-DUST @15.56 */: inset out; C2 in.
- 19.62 ("never") /* NEVER @19.62 */: C2's main line gets a 2 px rule under it.
- Host 0.00 to 20.18 plus land time (cap 21.2).

## Motion for the whole window
Clouds drift continuously inside the inset; chips drift; footage moves under all of it.

## Exit
C2 slides out `x:980` in the last 0.6 s; A3-S8 opens on g-a3-9-swell (cut).

## Footage under it
Flat beach under broken high cloud, slow push at eye height: candidates `media/candidates/a3/A3-S7_c1_pexels-39562256_calm-beach-cloudy-sky.mp4` (c2, c3 backups; none viewed yet). Modern people, buildings or piers in shot disqualify a take. The orchestrator names the pick.
