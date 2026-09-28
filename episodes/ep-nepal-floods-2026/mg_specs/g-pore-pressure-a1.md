# BRIEF — g-pore-pressure-a1 · A1 teaser · slope cross-section, rising water line, USGS card

## 0. Claim
Landslides build for days and finish in seconds: rain raises water pressure inside a slope until the
last friction holding it gives way. This teaser plants the mechanism before A2 (`g-pore-pressure`) explains it in full.

## 1. SOURCE
factcheck-A row 11 (CONFIRMED): USGS Landslide Hazards Program — rainfall infiltration raises pore-water
pressure, the standard triggering mechanism for rainfall-induced landslides. No published cross-section
figure for Kali Gandaki exists; geometry is SCHEMATIC, NOT TO SCALE (no real slope angle/depth numbers
are claimed on screen).

## 2. DATUM, SCALE, ORIENTATION
- Stage: full 1920x1080. Slope occupies left two-thirds (x 96-1180); glass card sits right (x 1220-1824).
- Ground/sky line y = 300 (sky above, hillside below). Slope face runs from apex (280,300) down to
  toe (1000,880) — a single schematic hillside, not a measured profile.
- SCHEMATIC, NOT TO SCALE label at (110, 940).

## 3. GEOMETRY (px)
- Hillside fill: polygon apex(280,300) - (1000,880) - (96,880) - (96,300), soil gradient #5b4a3f -> #2a221d.
- A thin blue line (#7fb2e5, 4px) inside the slope body, horizontal-ish, starts at y 820 (near the toe)
  and creeps upward to y 560 over the comp's run — this is the "water line" the picture line names.
- Sky: rect (0,0)-(1920,300), gradient #0b1016 -> #030507.
- Glass card (right, 604x260 at x1220,y410): eyebrow "SOURCE", headline "U.S. Geological Survey",
  sub "Landslide Hazards Program".

## 4. MUST BE TRUE
1. The blue line sits INSIDE the hillside polygon at every frame, never above the ground/sky line (y<300) or below the toe.
2. The blue line's y decreases (rises) monotonically across the comp — never resets or jumps down.
3. The glass card names USGS and Landslide Hazards Program exactly, legible, inside the safe margin (x<=1824).
4. "SCHEMATIC, NOT TO SCALE" is present and legible.
5. Something moves for the whole window (the rising line itself, plus an ambient drift on the hillside gradient).

## 5. PANEL TEXT (exact) and CUES
Card: eyebrow "SOURCE" · headline "U.S. Geological Survey" · sub "Landslide Hazards Program".
Cues (s, local, @est 175 wpm from beat start `/* CUE "..." @est N */`):
- hillside draws in @0.3
- water line begins creep @3.43 (`/* CUE "Rain soaks in slowly" @est 3.43 */` — rain starts wetting the slope)
- card reveals @7.20 (`/* CUE "the water pressure inside the slope climbs" @est 7.20 */`)
- water line nears the top, subtle shudder on the hillside @15.77 (`/* CUE "The three seconds on camera" @est 15.77 */`)
- card exits, comp exits @21.0 (x:660->0 slide out reversed, power3.in)
Declared duration 23.5 s (narration ~22.29 s + ~1.2 s tail).
