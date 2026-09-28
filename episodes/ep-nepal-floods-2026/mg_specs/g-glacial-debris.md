# BRIEF — g-glacial-debris · A2 · valley-wall cutaway, bedrock vs loose glacial gravel, fast seepage

## 0. Claim
The Kali Gandaki's walls are steep and much of them is old glacial debris (loose rock/gravel dragged and
dropped by ancient glaciers, never cemented), so water moves through it fast and it gives way fast.

## 1. SOURCE
factcheck-B row 8 (CONFIRMED): GeoJournal, "Geomorphological and pedological investigations on the
glacial history of the Kali Gandaki" — documents moraine/talus/outwash-gravel ("paraglacial sediment")
draped on the valley walls, mobilized by rain. No published cross-section traced; layer thicknesses and
angle are SCHEMATIC, NOT TO SCALE.

## 2. DATUM, SCALE, ORIENTATION
- Stage 1920x1080. Cutaway occupies x 96-1180, y 200-980. Grey bedrock forms the core wedge; a tan loose
  layer drapes over its outer (upper-left) face.
- SCHEMATIC, NOT TO SCALE label at (110, 1000).

## 3. GEOMETRY (px)
- Bedrock wedge: polygon (260,220) - (1100,980) - (200,980), fill grey gradient #2a3644 -> #15202b, stroke #4a5560.
- Glacial debris layer: a band 60-110px thick draped along the wedge's upper-left edge, polygon
  (260,220)-(360,220)-(1050,900)-(1000,980)-(1100,980)-(1150,900)... (a ribbon following the bedrock face,
  offset outward ~80px), fill tan gradient #8a6a3f -> #6b4f2c, stroke #a8825a.
- Water seep dots: 10 small circles (#7fb2e5, r4-6) that travel down through the tan layer only (clipped
  to the debris polygon), fast (0.9s per pass), looping — visually much faster than any equivalent seep in
  the bedrock (bedrock gets none).
- Label "GLACIAL DEBRIS" (diagram label tier) at (760,300), leader line to the tan band.
- Label "BEDROCK" at (340,880), leader line to the grey wedge.

## 4. MUST BE TRUE
1. The tan "glacial debris" band sits entirely draped OVER the grey bedrock's outer face — never appears as a separate freestanding shape, never sits inside/under the bedrock.
2. Seep dots are visible ONLY inside the tan layer's clip path, never inside the grey bedrock.
3. Seep dots complete a full pass (top to bottom of the tan band) in under 1.2 s each — visibly "fast" motion, matching "water moves through it fast."
4. "GLACIAL DEBRIS" label points at the tan band; "BEDROCK" label points at the grey wedge; neither leader line crosses the other layer.
5. "SCHEMATIC, NOT TO SCALE" is present and legible.

## 5. PANEL TEXT (exact) and CUES
Headline (x96,y70): "Old Ice Left This Wall Loose".
Labels: "GLACIAL DEBRIS", "BEDROCK".
Cues (s, local @175wpm):
- headline + bedrock wedge draw in @0.4
- tan debris layer drapes on @3.0
- "BEDROCK" label @4.0, "GLACIAL DEBRIS" label @5.5 (`/* CUE "covered in old glacial debris" @est 5.5 */`)
- seep dots start fast-looping through the tan layer only @12.34 (`/* CUE "water moves through it fast" @est 12.34 */`)
- exit @18.0 (slide out power3.in)
Declared duration 20.0 s (narration ~18.51 s + ~1.4 s tail).
