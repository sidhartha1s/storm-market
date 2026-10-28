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
assert [t[2] for t in clips_above(tiles, {ANCHOR})] == [NEW], clips_above(tiles, {ANCHOR})

# one column (the 1080 px window the driver ran on before): same answer
narrow = [[538, 224 + 261 * i, t[2], 293, 783, 490] for i, t in enumerate(raw[2:])] + raw[:2]  # one tile per row, same order
assert [t[2] for t in clips_above(grid_tiles(narrow), {ANCHOR})] == [NEW]

# a clip beyond the agent panel is not a grid tile
assert grid_tiles([[1500, 300, ASB + "x", 1340, 1830, 490]]) == []
print("test_flow_driver: 3 checks PASS")

# clip_check.py: spoken numbers against the transcriber's digits (recorded Camille clip 4, 23 Oct 26)
cc = open(os.path.join(HERE, "clip_check.py"), encoding="utf-8").read()
ns2 = {}
exec("import re" + chr(10) + cc[cc.index("ONES ="):cc.index("model = WhisperModel")], ns2)
norm, diff_words = ns2["norm"], ns2["diff_words"]
line = "By Saturday, August twenty-third, more than a hundred and ten people were listed as missing in Virginia."
heard = "By Saturday, August 23rd. More than 110 people were listed as missing in Virginia."
assert diff_words(line, heard, heard) == ([], []), diff_words(line, heard, heard)
assert norm("the 1999 outbreak", norm("the nineteen ninety nine outbreak")) == ["the", "nineteen", "ninety", "nine", "outbreak"]
assert diff_words("inside their house", "inside their houses", "inside their houses") == (["house"], ["houses"]), "a real word change still shows"
line3 = "From Wednesday on, the forecast kept getting stronger, and it was right."
whole3 = "From Wednesday on the forecast kept getting stronger and it was right."
assert diff_words(line3, whole3, "From Wednesday on, the forecast kept going. | getting stronger. | and it was right.") == ([], []), "an island-only extra is a cut artefact"
assert diff_words(line3, "From Wednesday on the forecast kept getting stronger and it was not right.", "the forecast kept getting stronger | and it was not right") == ([], ["not"]), "a real extra heard in both passes counts"
assert diff_words(line3, "the forecast kept getting stronger and it was right", "From Wednesday on | and it was right") == ([], []), "a word one pass drops is not missing"
print("test_flow_driver: clip_check number forms and island extras PASS")

# the price check takes the exact quote only (review of PR 213: "130 credits?" passed for 30)
quoted_price = ns["quoted_price"]
assert quoted_price("Generate 2 videos for 30 credits?", 30)
assert not quoted_price("Generate 2 videos for 130 credits?", 30)
assert not quoted_price("Generate for 115 credits?", 15)
assert not quoted_price("Generate for 1,015 credits?", 15)
# a 1 px row jitter keeps the newest clip first
jitter = [[1047, 224, ASB + ANCHOR, 802, 1292, 490], [538, 225, "https://flow-content.google/video/" + NEW, 293, 783, 490]]
assert [t[2] for t in clips_above(grid_tiles(jitter), {ANCHOR})] == [NEW]
print("test_flow_driver: price quote and row jitter PASS")

# 29 Oct 26: the anchor was the uuid of a tile opened in the tab (ac356b2a-...); the reloaded grid showed only tokens, so
# one anchor id never matched and a landed clip sat unseen for about an hour. The driver now keeps every id in view
# after a fresh load, and the first one still in view marks where the new clips end, even when the top one has gone.
T = ["ANqvLO" + c * 80 for c in "abcd"]
NEWTOK = "ANqvLO" + "n" * 80
known = set(T[:3])  # read from a freshly loaded grid before the send
landed = [[538, 224, ASB + NEWTOK, 293, 783, 490], [1047, 224, ASB + T[1], 802, 1292, 490],
          [538, 490, ASB + T[2], 293, 783, 490], [1047, 490, ASB + T[3], 802, 1292, 490]]  # T[0]'s token is gone
assert [t[2] for t in clips_above(grid_tiles(landed), known)] == [NEWTOK], clips_above(grid_tiles(landed), known)
assert clips_above(grid_tiles(landed), {"ac356b2a-1b2c-4d5e-8f90-123456789abc"}) == [], "no known clip in view: nothing new"
print("test_flow_driver: known-set anchor PASS")

# 29 Oct 26: landing is decided from the job's own agent thread, the grid only cross-checks. Real fixtures, read-only
# from the live Flow tab: ins-paul-4's thread at 01:31 with the finished clip posted under "waiting in the queue due to
# high demand", a fresh session's empty thread, and the Videos grid at 01:32 with two runs' known sets.
import json
thread_clips, landed = ns["thread_clips"], ns["landed"]
FX = os.path.join(HERE, "fixtures")
done_html = open(os.path.join(FX, "panel-ins-paul-4-landed-0131.html"), encoding="utf-8").read()
CLIP = "1eee7965-d6ff-4655-ad03-3f91156278d9"
assert thread_clips(done_html) == [CLIP], "the agent's thumbnail is the clip; the start-frame chip in the user's bubble is not"
assert thread_clips(open(os.path.join(FX, "panel-new-session-0126.html"), encoding="utf-8").read()) == [], "zero-state cards are no clip"
g = json.load(open(os.path.join(FX, "grid-0132.json"), encoding="utf-8"))
gtiles = grid_tiles(g["raw"])
# the run that started after the clip landed counted it as known: the grid diff alone returns nothing
assert clips_above(gtiles, set(g["known_0121"])) == []
take, note = landed(thread_clips(done_html), clips_above(gtiles, set(g["known_0121"])), 1)
assert take == [CLIP] and note.startswith("[FALLBACK]"), (take, note)
# grid-only: the thread shows nothing, the grid diff shows the clip (token form): take it and say so
take, note = landed([], clips_above(gtiles, set(g["known_0113"])), 1)
assert take == [gtiles[0][2]] and take[0].startswith("ANqvLOZsQq46") and "grid" in note and note.startswith("[FALLBACK]"), (take, note)
assert landed([CLIP], [[0, 0, "ANqvLOtoken"]], 1) == ([CLIP], ""), "thread and grid agree: no note"
assert landed([], [], 1) == ([], ""), "nothing landed yet"
print("test_flow_driver: thread decides landing PASS")
