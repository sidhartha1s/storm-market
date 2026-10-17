# Joplin graphics: orchestrator frame reads

One row per read of a settled frame. A Sonnet graphic that fails twice moves to Opus (CLAUDE.md chain of command).
Footage is not mounted yet, so these reads check each graphic on its own; the read over footage comes after the picks.

| graphic | frame read | verdict | defect, fix |
|---|---|---|---|
| g-a2-quote-108 | sheets-pre/g-a2-quote-108-frames/over-photo_4.3s.png | PASS | glass card per tokens.md; the 6.1 s frame is the exit fade, not a contrast fault |
| g-a1-numb | sheets-pre/g-a1-numb-frames/t16.png | FAIL 1 | the NWS page crop cuts every line mid-word at its right edge ("were", "ex", "to"); crop to whole lines or widen the box so no word is cut. Source line was the stale "Preface" wording: fixed by hand to "Executive Summary and Finding 2c" |
| g-a1-gutter, g-a1-bubble-page | source line text | fixed by hand | stale "Finding 2b" from the ZBook's pre-19a4bbb9 edit_script copy; now "Finding 2c" (NWS text: both quotes sit in the discussion above Finding #2c) |
| g-intro-map-dots | brief text (built from the old brief) | FAIL 1 | a bare "0" on the below-ground line reads as "nobody"; replace it with "FOUND NO SIGN" (locked wording) beside the NIST source text; the brief now says so |
| g-a1-bubble-page | sheets-pre/g-a1-bubble-page_260s.jpg | FAIL 1 | page crop cuts every line mid-word at its LEFT edge ("ost", "owever", "terviews") and the drift widens it; same fix as g-a1-numb. Pattern: every page-crop graphic (gutter, finding31, doc-cues, doc-nwsrec2, intro pages) gets this check; build.md and buildo.md now carry the whole-lines rule |
