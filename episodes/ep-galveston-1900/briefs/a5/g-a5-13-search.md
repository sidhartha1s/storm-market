# g-a5-13-search · A5-S8 9.26 to end · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplars: `library/inhouse/stat-timeline.html` (row of dated tiles), official `split-flap-board` (a value ticking to its result).

## 0. Claim
In every 1900 Monthly Weather Review issue that could be opened (February to October), the word Belen never appears. Three issues could not be opened.

## 1. Source
sources-cuba.md header: "Belen"/"Belén", "Gangoiti" appear nowhere in any 1900 MWR issue grepped (Feb-Aug, Sep, Oct; Jan, Nov, Dec not retrievable). Fact-check a5-r1 rows 32 to 33.

## 2. Datum, scale, orientation
Full-frame designed card (tokens radial background). Twelve month tiles in calendar order, left to right.

## 3. Geometry (px)
- Search box: glass card, `left:460px; top:180px; width:1000px; height:110px`, radius 16; magnifier glyph 44 px `#93a3b2` at left; typed text "BELEN" Arial Black 900 56 px `#f2f5f8` with a 3 px caret blinking (0.5 s).
- Tiles: 12 tiles, each 120 x 200, gap 16, row width 12 x 120 + 11 x 16 = 1616, left 152, top 400. Tile face `#15202b`, border 1 px `rgba(255,255,255,.14)`, radius 10. Month label top "JAN" ... "DEC" Arial 700 22 px `#93a3b2`; "MWR 1900" under it Arial 700 19 px `#93a3b2`.
- Result in each tile's lower half: Feb to Oct "0" Arial Black 900 64 px `#f2f5f8`; Jan, Nov, Dec greyed tile (opacity 0.45) with "NOT OPENED" Arial 700 19 px `#93a3b2` in two lines.
- Chip "BELEN: 0 · ISSUES READ", glass, centred x 960, top 690 (bottom ~ 790); its right edge < 1600 (card ~ 700 wide).
- Source line top-left: "Monthly Weather Review, 1900 (issues Feb. to Oct.)".

## 4. Must be true in the picture
1. Exactly 9 tiles show 0 (FEB to OCT) and exactly 3 show NOT OPENED (JAN, NOV, DEC). Never a 0 on a greyed tile.
2. The chip says "ISSUES READ": it never claims all twelve.
3. Tiles' results land left to right in calendar order, after "Belen" is typed.
4. Row spans x 152 to 1768, y 400 to 600: clear of the corner.
5. The "0" on nine tiles is one label on several things: declare `data-repeat-ok="one result per issue tile"` on each "0" leaf only after a frame read.

## 5. Text and cues (a5-s8.words.json; host starts at "I" 9.26)
Comp-local = word time − 9.26.
- 9.26: frame 0 shows the empty box with the caret and the twelve tiles blank (month labels on); source line on.
- 9.36 ("searched" 9.36): caret blinks.
- 10.44 ("for" 10.44) /* BELEN @10.72 */: "BELEN" types one letter per 0.06 s from 10.60, done 10.90.
- 11.56 ("In" 11.56): results tick across: each tile 0.12 s apart from 11.56, the 0 tiles flip in (split-flap style, 0.25 s), the three greyed tiles dim with NOT OPENED in their turn; last tile at 12.88.
- 13.52 ("never" 13.52) /* NEVER @13.52 */: chip in.
- Host: 9.26 to 14.32 + gap to A5-S9 (land time 1.0 s).

## Motion for the whole window
Caret blink; tiles' tick sequence; chip and box drift after.

## Exit
Tiles drop out (y +40, autoAlpha 0, 0.4 s, 0.03 stagger), chip slides right, last 0.6 s.

## Footage under it
None (full-frame card).
