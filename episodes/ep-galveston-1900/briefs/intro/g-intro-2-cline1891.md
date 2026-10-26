# g-intro-2-cline1891 · H1-S2 · standard · Sonnet 5.5 high
Shared rules: `_shared.md`. Exemplars: `library/official` `lt-dark-card` for the lower-third shape (restyle to the glass card), `episodes/ep-1974-super-outbreak/compositions/g-cite-paper.html` (single-word marker tag over a page).

## 0. Claim
The man who wrote part of the 1891 page was Isaac Cline, Galveston's weatherman, and he called the fear an "absurd delusion".

## 1. Source
- sources-cline.md §1: Commons transcription of the 16 July 1891 page, "is simply an absurd delusion and can only have it's origin in the imagination". CONFIRMED-secondary; edit_script.md "Open before anything goes on screen": one human look at the 1891 page scan before this quote is shown. Do not ship until the orchestrator records that look.
- sources-cline.md §2 / factcheck-E.md H1-S2: in Galveston by 1889 (NOAA VLab), "its own weatherman" CONFIRMED SECONDARY.

## 2. Datum, scale, orientation
Overlay comp, transparent root, over the 1891 page still with a slow push to the column (editor's clip, track 1). No map, no scale. Zones used: lower-third (bottom-left), centre chip, source line (top-left).

## 3. Geometry (px)
- Lower-third card: `left:110px; bottom:110px`, padding 18px 28px. Line 1 "ISAAC CLINE" Arial Black 900 52 px; line 2 "Galveston Weather Office" Arial 700 27 px `#f5d98b` letter-spacing 1 px. Card width hugs text (`display:table`), about 620 x 130 px.
- Chip "ABSURD DELUSION": centred, `left:50%; top:600px; transform:translateX(-50%)` set in `tl.set` at 0 (never in CSS), Arial Black 900 64 px `#f2f5f8` (this one is the beat's headline, so big tier), letter-spacing 2 px, padding 22px 40px. Under it, inside the card, tag "Isaac Cline, 1891" Georgia italic 26 px `#d8a13a`.
- A thin red rule 4 px `#d0121f`, width 0 to the chip's text width, 30 px under the main line, `scaleX 0 -> 1`, `transformOrigin:"left center"`, 0.5 s: the strike-under that lands with the telegraph click.
- Source line top-left: "Galveston Daily News, July 16, 1891 · text: Wikimedia Commons transcription".

## 4. Must be true in the picture
1. The lower-third has left the frame before the chip enters (never two cards on screen).
2. The chip sits over the page, not over the column words being pushed to: the orchestrator picks the push so the quoted column sits in the top half (y < 520); if the push ends lower, move the chip to top 180 and report.
3. The words on the chip are exactly ABSURD DELUSION (the transcription's words), no quote marks needed because the tag names the speaker and year.
4. Nothing in x >= 1600, y >= 680 (circle corner; the circle is hidden in the hook, kept clear anyway for one rule across the section).

## 5. Text and cues (h1-s2.words.json, segment 6.632 s)
- Source line in at 0.00, holds the whole segment.
- Lower-third in at 1.24 ("Isaac" 1.24): /* ISAAC @1.24 */ line 1 then line 2 at 1.60 ("Klein" = Cline 1.60); line 2 rises in after line 1 by 0.36 s.
- Lower-third out 4.28 to 4.88 ("He" 4.28).
- Chip in at 5.50 ("absurd" 5.50), /* ABSURD @5.50 */ red rule draws 5.92 to 6.42 ("delusion" 5.92, the telegraph-key click).
- Host 0.00 to 7.40 (the chip holds through the cut into H1-S3's first 0.0 to 0.75 s is NOT allowed: H1-S3 is a hard cut to the ruins photo). So chip exits 6.70 to 7.30 only if the editor leaves a pause after the segment; else the chip's exit is anchored to the segment end: exit 6.03 to 6.63, host 0.00 to 6.63. The orchestrator states which from index.html; the default is the second.

## Motion for the whole window
Source line static is not enough: the chip and lower-third drift +-4 px; between 4.88 and 5.50 (0.62 s with only the source line) nothing else is needed (gap under 4 s), but the source-line card drifts too.

## Exit
Chip and tag slide out `x:980, autoAlpha 0, 0.6, power3.in`; source line fades with it.

## Footage under it
The 1891 Galveston Daily News page scan (Commons `File:Galveston_Daily_News_-_July_16,_1891.jpg`, CC0 per sources-cline.md; footage-inventory.md says no scan was found, so the orchestrator confirms the file and downloads it before this comp is read). No other footage.
