# Unit test for the Flow driver's grid reading: python3 scripts/flow/test_flow_driver.py
import importlib.util, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "ad_gen.py"), encoding="utf-8").read()
# ad_gen.py loads its jobs file at import; take only the pure helpers it defines
helpers = src[src.index("def grid_tiles(raw):"):src.index("def failed_cards(page):")]
ns = {}
exec("import re" + chr(10) + helpers, ns)
grid_tiles, clips_above = ns["grid_tiles"], ns["clips_above"]

# Recorded 23 Oct 26 16:33 on the 1920 px driver window: a 2-column grid, the new clip top-left, the anchor top-right,
# the agent panel's chat thumbnail at left 1350 (width 215) and the Google avatar at 32 px.
ASB = "https://flow.google.com/asb/"
ANCHOR = "ANqvLOYlJjHUSSTWbgbv9l4GGe8GZ6KUDB37gPZBl8gJvNk8GSjcM6HRH3Y_mDJjrxr0uMByqDPlpPNKE5x8ffnot9vr"
NEW = "6fa051dc-f0c3-4dcd-92d3-35f32fd970f8"
raw = [
    [1457, 252, "https://flow-content.google/image/" + NEW, 1350, 1565, 215],  # chat thumbnail of the new clip
    [40, 40, "https://lh3.google.com/u/0/ogw/avatar=s64-c-mo", 24, 56, 32],
    [538, 224, "https://flow-content.google/video/" + NEW, 293, 783, 490],
    [1047, 224, ASB + ANCHOR, 802, 1292, 490],
    [538, 490, ASB + "ANqvLObCBI0xB6lP1YSLC0OhRRIv2qDBL5rlRZakRVWFaJAqPP6SVrxLZFcucz1WH5yGMHpnCtzyEBiyI8sXJwnqbU1_", 293, 783, 490],
    [1047, 490, ASB + "ANqvLObkkSze4WLMMLR16mSvF3-vEtbnBKCXvq1FcVckfRFUScNKjSytWUTdvxcK6r6lq3riwIT2F8Gj4ZVHIqqlZSfT", 802, 1292, 490],
]
tiles = grid_tiles(raw)
assert [t[2][:8] for t in tiles] == ["6fa051dc", "ANqvLOYl", "ANqvLObC", "ANqvLObk"], tiles
assert [t[2] for t in clips_above(tiles, ANCHOR)] == [NEW], clips_above(tiles, ANCHOR)

# one column (the 1080 px window the driver ran on before): same answer
narrow = [[x if x < 800 else x, y if x < 800 else y + 261, s, l if l < 800 else l - 509, r if l < 800 else r - 509, w] for x, y, s, l, r, w in raw]
assert [t[2] for t in clips_above(grid_tiles(narrow), ANCHOR)] == [NEW]

# a clip beyond the agent panel is not a grid tile
assert grid_tiles([[1500, 300, ASB + "x", 1340, 1830, 490]]) == []
print("test_flow_driver: 3 checks PASS")

# clip_check.py: spoken numbers against the transcriber's digits (recorded Camille clip 4, 23 Oct 26)
cc = open(os.path.join(HERE, "clip_check.py"), encoding="utf-8").read()
ns2 = {}
exec("import re" + chr(10) + cc[cc.index("ONES ="):cc.index("model = WhisperModel")], ns2)
norm = ns2["norm"]
line = "By Saturday, August twenty-third, more than a hundred and ten people were listed as missing in Virginia."
heard = "By Saturday, August 23rd. More than 110 people were listed as missing in Virginia."
want = norm(line)
assert [w for w in want if w not in norm(heard, want)] == [], (want, norm(heard, want))
assert [w for w in norm(heard, want) if w not in want] == [], norm(heard, want)
assert norm("the 1999 outbreak", norm("the nineteen ninety nine outbreak")) == ["the", "nineteen", "ninety", "nine", "outbreak"]
assert "houses" in [w for w in norm("inside their houses") if w not in norm("inside their house")], "a real word change still shows"
line3 = norm("From Wednesday on, the forecast kept getting stronger, and it was right.")
whole3 = norm("From Wednesday on the forecast kept getting stronger and it was right.", line3)
island3 = norm("From Wednesday on, the forecast kept going. | getting stronger. | and it was right.", line3)
assert [w for w in island3 if w not in line3 and w in whole3] == [], "an island-only extra is a cut artefact"
assert [w for w in norm("it was not right", line3) if w not in line3] == ["not"], "a real extra heard in the whole clip still counts"
print("test_flow_driver: clip_check number forms and island extras PASS")
