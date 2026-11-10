"""Self-check for scripts/stage.py: python3 scripts/test_stage.py"""
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import stage as s


def refused(fn, *args):
    try:
        fn(*args)
    except SystemExit as e:
        return str(e)
    raise AssertionError(f"{fn.__name__}{args} was not refused")


# the record line round-trips words and shown text that hold quotes and pipes
words, shown = 'he said "go" | then "no | wait"', "https://x.test/a?b=1|2"
line = s.format_line("hook-intro", "2026-11-11", words, "devq", shown)
assert s.parse_lines("# header\n" + line + "\nprose\n") == [("hook-intro", "2026-11-11", words, "devq", shown)]
tricky = 'quote me: "x" | chat | shown: y'  # words that look like the line's own tail
assert s.parse_lines(s.format_line("draft", "2026-11-11", tricky, "chat", "renders/d.mp4"))[0][2] == tricky

# the angle heading as the shipped episodes really write it, including a lock block that is not the first heading
assert s.angle_lock('## Angle (locked by the owner, 9 Oct 26: "Do a mix")\n') == "2026-10-09"
assert s.angle_lock("## Status: tick\n\n## Angle (locked by the owner, 22 Oct 26: \"cand1\", ...)\n") == "2026-10-22"
assert s.angle_lock("## Angle (PROVISIONAL, owner pick pending)\n") is None
real = Path(__file__).resolve().parent.parent / "episodes"
for slug in ("ep4-el-reno", "ep-palm-sunday-1965", "ep-joplin-2011", "ep-moore-1999", "ep-camille-1969",
             "ep-mayfield-2021", "ep-buffalo-2022", "ep-appalachian-1950", "ep-galveston-1900"):
    assert s.angle_lock((real / slug / "angle.md").read_text(encoding="utf-8")), slug

# gate states: a deferral never closes a gate, no gates.md means "no record", never approval
ev = [("defer:packaging", "2026-11-03", "picks later", "chat", "thumbs/"), ("hook-intro", "2026-11-04", "ok", "chat", "x")]
st = s.gate_states(ev, "2026-10-26", True)
assert st == {"angle": "ok 2026-10-26", "packaging": "deferred 2026-11-03", "hook-intro": "ok 2026-11-04",
              "draft": "OPEN", "retake": "-"}, st
assert s.gate_states(ev + [("packaging", "2026-11-05", "t2", "chat", "x")], None, True)["packaging"] == "ok 2026-11-05"
none = s.gate_states([], None, False)
assert none["angle"] == none["packaging"] == "no record" and none["retake"] == "-"

# machine stage: first unmet, later artifacts prove earlier steps
f = dict(script=True, draft=False, master=False, uploads=False, published=False, jobs=["DONE", "READY"])
assert s.stage_of(f) == "build"
assert s.stage_of(dict(f, jobs=["DONE", "DONE"])) == "draft"
assert s.stage_of(dict(f, jobs=[])) == "build"
assert s.stage_of(dict(f, script=False)) == "script"
assert s.stage_of(dict(f, draft=True)) == "master"
assert s.stage_of(dict(f, script=False, master=True)) == "uploads"
assert s.stage_of(dict(f, master=True, uploads=True)) == "published"
assert s.stage_of(dict(f, uploads=True, published=True)) == "DONE"

# waiting on: packaging blocks only the published step; hook-intro blocks the build; the angle blocks everything
ok = {g: "ok 2026-11-01" for g in s.GATES}
assert s.waiting_on("build", dict(ok, packaging="OPEN"), "e10-x") == "MACHINE lanes.py status episodes/e10-x"
assert s.waiting_on("published", dict(ok, packaging="no record"), "e10-x") == "OWNER packaging"
assert s.waiting_on("published", dict(ok, packaging="deferred 2026-11-03"), "e10-x") == "OWNER packaging"
assert s.waiting_on("build", dict(ok, **{"hook-intro": "OPEN"}), "e10-x") == "OWNER hook-intro"
assert s.waiting_on("master", dict(ok, draft="OPEN"), "e10-x") == "OWNER draft"
assert s.waiting_on("uploads", dict(ok, packaging="OPEN"), "e10-x").startswith("MACHINE ship.py")
assert s.waiting_on("draft", dict(ok, angle="no record"), "e10-x") == "OWNER angle"
assert s.waiting_on("DONE", ok, "e10-x") == "DONE"

# same slug in several checkouts: newest branch-only commit wins, else main, else the first worktree holding it
assert s.pick_checkout([0, 1, 2], [0, 0, 0]) == 0
assert s.pick_checkout([0, 1, 2], [0, 50, 90]) == 2
assert s.pick_checkout([2, 3], [0, 0, 0, 0]) == 2

with tempfile.TemporaryDirectory() as t:
    main, wt = Path(t) / "main", Path(t) / "wt"
    ep = wt / "episodes" / "ep-test-1900"
    ep.mkdir(parents=True)

    # record: refusals, header once, append-only, earlier bytes untouched
    assert "unknown gate" in refused(s.record, ep, "acts", "yes", "x", "chat")
    assert "required" in refused(s.record, ep, "angle", "  ", "x", "chat")
    assert "required" in refused(s.record, ep, "angle", "yes", "", "chat")
    assert "chat or devq" in refused(s.record, ep, "angle", "yes", "x", "email")
    assert "line break" in refused(s.record, ep, "angle", "yes\nno", "x", "chat")
    assert not (ep / "gates.md").exists()
    s.record(ep, "angle", 'c2 "the wire" | go', "angle.md", "chat", today="2026-11-10")
    first = (ep / "gates.md").read_bytes()
    with open(ep / "gates.md", "ab") as fh:
        fh.write(b"- note without newline")
    s.record(ep, "defer:packaging", "picks later", "thumbs/", "devq", today="2026-11-11")
    text = (ep / "gates.md").read_text(encoding="utf-8")
    assert text.encode().startswith(first) and text.count(s.HEADER) == 1, text
    assert text.endswith('- note without newline\n- defer:packaging | 2026-11-11 | "picks later" | devq | shown: thumbs/\n'), text
    assert [e[0] for e in s.parse_lines(text)] == ["angle", "defer:packaging"]
    assert s.parse_lines(text)[0][2] == 'c2 "the wire" | go'

    # read_episode: no media anywhere stops at script; masters and uploads are read from the main checkout only
    (ep / "E10-test-1900-metadata.md").write_text("x", encoding="utf-8")
    r = s.read_episode(ep, main)
    assert (r["label"], r["stage"], r["states"]["angle"], r["states"]["packaging"]) == \
        ("E10-test-1900", "script", "ok 2026-11-10", "deferred 2026-11-11"), r
    assert r["waiting"] == "MACHINE write episodes/ep-test-1900/edit_script.md", r
    d = s.deliverables(main, ep.name, "E10-test-1900")
    d["renders"].mkdir(parents=True)
    (d["renders"] / "x-draft.mp4").write_bytes(b"v")
    assert s.read_episode(ep, main)["stage"] == "master"
    d["master"].write_bytes(b"m")
    (ep / "renders").mkdir()
    (ep / "renders" / "E10-test-1900-final-master.mp4").write_bytes(b"m")  # a worktree copy is not the shipped master
    assert s.read_episode(ep, main)["stage"] == "uploads"
    d["uploads"].mkdir(parents=True)
    d["up_master"].write_bytes(b"m")
    r = s.read_episode(ep, main)
    assert (r["stage"], r["waiting"]) == ("published", "OWNER packaging"), r
    s.record(ep, "packaging", "t2, title 3", "uploads/E10-test-1900/", "chat", today="2026-11-12")
    assert s.read_episode(ep, main)["waiting"].startswith("MACHINE upload")
    s.record(ep, "published", "https://youtu.be/x", "https://youtu.be/x", "chat", today="2026-11-13")
    assert s.read_episode(ep, main)["waiting"] == "DONE"

    print(s.render_board([dict(s.read_episode(ep, main), **{"from": "wt"})]))

# the real board runs and reads every checkout
rows = s.board_rows()
slugs = {r["slug"] for r in rows}
assert {"ep-galveston-1900", "ep4-el-reno"} <= slugs, slugs
# videos made before the angle-first rule have no angle.md and stay off the board
assert not {"ep-enderlin-2025", "ep1-joplin", "ms-krakatoa-1883"} & slugs, slugs
# a worktree whose folder was removed without `git worktree prune` is still listed by git: the board skips it
real_checkouts = s.checkouts
s.checkouts = lambda: real_checkouts() + [(Path("Z:/no/such/worktree"), "gone", "0" * 40)]
assert {r["slug"] for r in s.board_rows()} == slugs
s.checkouts = real_checkouts
gal = next(r for r in rows if r["slug"] == "ep-galveston-1900")
assert gal["label"] == "E09-galveston-1900" and gal["states"]["angle"] == "ok 2026-10-26", gal
assert all(len(l) <= 160 for l in s.render_board(rows).splitlines())

print("[test_stage] PASS")
