#!/usr/bin/env python3
"""ep5 v3 family-repeat swap pass. Each entry: (old element id, replacement line(s)).
Replaces the WHOLE tag line matched by id=. Verifies exactly-once per id, prints a report.
"""
import re
import sys
from pathlib import Path

P = Path(__file__).parent / "index.html"
h = P.read_text(encoding="utf-8")

G = 'style="filter: brightness(0.9) saturate(0.85) contrast(1.05)"'   # unified broadcast grade
U = 'style="filter: saturate(0.9) contrast(1.06)"'                    # subtle unify

def V(eid, src, st, du, extra="", style=U):
    cb = f' data-callback="{extra}"' if extra else ""
    return (f'  <video id="{eid}" src="media/scenes/{src}" {style} data-start="{st}"'
            f' data-duration="{du}" data-track-index="1"{cb} muted></video>')

SWAPS = [
 ("vx-goes4pb1",      [V("vx-wdropb3hill1","wdropb3-hillflames.mp4","219.96","8.5")]),
 ("vx-tf144c1",       [V("vx-chin3hold1","chin3-holdlight.mp4","393.88","5.0")]),
 ("vx-burnaer01b1",   [V("vx-wdrop3door1","wdrop3-doorplume.mp4","424.5","6.5")]),
 ("vx-burnaer01c1",   [V("vx-wdropb3down1","wdropb3-bucketdown.mp4","478.98","8.0")]),
 ("vx-fftruck02b2",   [V("vx-itf3dphone1","itf3-dispatchphone.mp4","661.86","7.94")]),
 ("vx-fire02a3",      [V("vx-itf3carport1","itf3-carport.mp4","684.0","8.0",style=G)]),
 ("vx-nightroad01c2", [V("vx-itf3broad1","itf3-burnedroad.mp4","768.46","6.5")]),
 ("vx-nightroad01a2", [V("vx-wdropb3down2","wdropb3-bucketdown.mp4","801.0","6.5","the water war from above, again")]),
 ("vx-burnaer02e1",   [V("vx-itf3agrid1","itf3-aftermathgrid.mp4","821.9","9.0",style=G)]),
 ("vx-burnaer01d2",   [V("vx-itf3rubble1","itf3-rubbleman.mp4","830.9","5.0")]),
 ("vx-burnaer02f1",   [V("vx-itf3cleanup1","itf3-cleanupaerial.mp4","835.9","9.5",style=G)]),
 ("vx-burnaer01a3",   [V("vx-itf3rivsc1","itf3-riverscenic.mp4","847.52","7.5")]),
 ("vx-burnaer02c2",   [V("vx-chin3carry1","chin3-carryrig.mp4","855.0","8.0")]),
 ("vx-carrbrolle1",   [V("vx-itf3brush1","itf3-brushflames.mp4","863.0","5.0",style=G)]),
 ("vx-tf144c2",       [V("vx-bhawk3load1","bhawk3-bucketload.mp4","874.34","7.7")]),
 ("vx-maffsb3",       [V("vx-itf3dusk1","itf3-duskmirror.mp4","905.54","6.0")]),
 ("c-usgsbefore3",    [V("vx-itf3nhill1","itf3-nighthill.mp4","970.9","5.0",style=G)]),
 ("vx-blackhawkb1",   [V("vx-itf3dmic1","itf3-dispatchmic.mp4","975.9","8.0")]),
 ("c-modiscamp1",     [V("vx-bhawk3rivsun1","bhawk3-riversunset.mp4","983.9","7.54")]),
 ("vx-blackhawkc1",   [V("vx-bhawk3chief1","bhawk3-crewchief.mp4","996.44","8.0")]),
 ("c-modiscamp2",     [V("vx-itf3wing1","itf3-wingplume.mp4","1023.94","5.0")]),
 ("c-landsatcamp2",   [V("vx-itf3ckpt1","itf3-cockpitplume.mp4","1054.0","5.0")]),
 ("vx-daytonight2",   [V("vx-itf3pyrocol1","itf3-pyrocolumn.mp4","1092.02","8.0")]),
 ("vx-notdietoday2",  [V("vx-itf3heli1","itf3-heliplume.mp4","1100.02","8.76")]),
 ("vx-blackhawkc2",   [V("vx-itf3ffwalk1","itf3-ffwalk.mp4","1162.7","5.7",style=G),
                       V("vx-itf3embers1","itf3-embers.mp4","1168.4","3.4")]),
 ("vx-blackhawkd2",   [V("vx-itf3dash1","itf3-dashfire.mp4","1171.8","3.8"),
                       V("vx-itf3hnight1","itf3-housenight.mp4","1175.6","3.1")]),
 ("vx-icant3",        [V("vx-itf3badge1","itf3-badge.mp4","1275.99","5.0")]),
 ("c-usgsafter3",     [V("vx-itf3sign1","itf3-slowsign.mp4","1421.67","2.4"),
                       V("vx-itf3tape1","itf3-redtape.mp4","1424.07","3.38")]),
 ("vx-housegone2",    [V("vx-itf3xfmr1","itf3-transformer.mp4","1441.0","3.03")]),
 ("vx-burnaer01d3",   [V("vx-itf3cleanup2","itf3-cleanupaerial.mp4","1444.03","5.5","the lots being cleared, under the count",style=G)]),
 ("vx-burnaer02f2",   [V("vx-itf3hflare1","itf3-houseflare.mp4","1458.53","3.2",style=G)]),
 ("c-camprelief2",    [V("vx-itf3rivsc2","itf3-riverscenic.mp4","1474.73","5.0","calm water — she named the child after him")]),
 ("vx-burnaer02d3",   [V("vx-itf3agrid2","itf3-aftermathgrid.mp4","1498.47","8.0","the lots where the names lived",style=G)]),
 ("vx-honearemains2", [V("vx-itf3evac1","itf3-evacuees.mp4","1537.03","5.6")]),
 ("vx-maffsc2",       [V("vx-itf3watch1","itf3-wristwatch.mp4","1587.03","4.2")]),
 ("vx-carrbrolld2",   [V("vx-itf3broad2","itf3-burnedroad.mp4","1617.27","8.0","the road the verdict names")]),
 ("vx-carrwaterc2",   [V("vx-itf3heli2","itf3-heliplume.mp4","1657.85","8.0","the plume they flew into")]),
 ("vx-carrbrollc2",   [V("vx-wdropb3hill2","wdropb3-hillflames.mp4","1673.85","8.0","the hillside that started the case")]),
 ("vx-tf144c3",       [V("vx-itf3carport2","itf3-carport.mp4","1681.85","8.0","the burning home the fine priced",style=G)]),
 ("vx-carrbrolle2",   [V("vx-chin3carry2","chin3-carryrig.mp4","1758.41","8.0","the recovery work that outlived the fine")]),
 ("vx-tf144d3",       [V("vx-bhawk3rivsun2","bhawk3-riversunset.mp4","1802.48","12.0","one long look back down the river")]),
 ("vx-carrbrollb3",   [V("vx-itf3ffwalk2","itf3-ffwalk.mp4","1814.48","4.0","walking toward it, one more time",style=G)]),
 ("vx-tf144a3",       [V("vx-itf3tape2","itf3-redtape.mp4","1822.48","4.0","the tape that closed each door")]),
 ("vx-carrbrolld3",   [V("vx-itf3dphone2","itf3-dispatchphone.mp4","1840.48","8.0","the phones that never stopped")]),
 ("vx-carrwatera3",   [V("vx-itf3badge2","itf3-badge.mp4","1856.48","5.1","the badge that answered anyway")]),
 ("vx-maffsb2",       [V("vx-itf3dash2","itf3-dashfire.mp4","1869.61","3.5","recap — the drive through fire")]),
 ("vx-carrbrolle3",   [V("vx-itf3dusk2","itf3-duskmirror.mp4","1889.11","8.0","recap — dusk where it began")]),
]

lines = h.split("\n")
report, errors = [], []
for old_id, new_lines in SWAPS:
    idx = [i for i, ln in enumerate(lines) if f'id="{old_id}"' in ln]
    if len(idx) != 1:
        errors.append(f"{old_id}: matched {len(idx)} lines")
        continue
    lines[idx[0]:idx[0]+1] = new_lines
    report.append(f"{old_id} -> {', '.join(re.search(chr(34)+'([^'+chr(34)+']+)', nl).group(1) for nl in new_lines)}")
if errors:
    print("ERRORS:"); [print(" ", e) for e in errors]; sys.exit(1)
P.write_text("\n".join(lines), encoding="utf-8")
print(f"applied {len(report)} swaps")
