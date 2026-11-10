#!/usr/bin/env python3
"""Deliverables, the mechanical part of CLAUDE.md step 7: final names in the main checkout and the uploads folder.

  python3 scripts/ship.py episodes/<slug> <master-basename> [--dry-run]

Needs the episode's E number (`e<nn>-` slug or the tracked `E<nn>-<topic>-metadata.md`) and that metadata file.
In the MAIN checkout (first `git worktree list` entry), with label = E<nn>-<topic>:
  renders/<basename>-master.mp4 and renders/<basename>.srt (master_deliverables.py's names), found in this checkout or
  the main one, move to renders/<label>-final-master.mp4 / .srt, md5 before and after; the metadata is copied beside them;
  uploads/<label>/ gets hard links to the master and SRT ([FALLBACK] copy only when a link is impossible), a copy of the
  metadata, every thumbs/<label>-thumb-* image, and <label>-titles.txt: the metadata's "## Title" section.
It never deletes: other renders are listed for the session to decide. A final that differs (md5) from the incoming one
is a FAIL naming both. --dry-run prints every action and changes nothing; a second run is a no-op.
"""
import argparse
import hashlib
import os
import re
import shutil
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import episode  # noqa: E402
import stage  # noqa: E402

IMAGES = {".png", ".jpg", ".jpeg", ".webp"}
TITLE = re.compile(r"^## Title\b.*?(?=^## |\Z)", re.S | re.M)


def md5(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def titles(meta_bytes):
    """The metadata's "## Title" section through its last non-blank line, in the file's own line endings; None without one."""
    text = meta_bytes.decode("utf-8")
    m = TITLE.search(text)
    if not m:
        return None
    return (m.group(0).rstrip("\r\n") + ("\r\n" if "\r\n" in text else "\n")).encode("utf-8")


def fail(msg):
    sys.exit(f"[ship] FAIL: {msg}")


def same_content(a, b):
    return a.exists() and b.exists() and (os.path.samefile(a, b) or md5(a) == md5(b))


def plan(ep, basename, main_root):
    """[(op, src, dst)] with op in keep | move | link | copy | write (src is bytes for write), plus the non-final renders."""
    label = episode.label(ep)
    if not label:
        fail(f"{ep.name} has no E number: name the slug e<nn>-<topic> or add the tracked E<nn>-<topic>-metadata.md")
    meta = ep / f"{label}-metadata.md"
    if not meta.exists():
        fail(f"{meta} is missing: write and commit the metadata before shipping")
    d = stage.deliverables(main_root, ep.name, label)
    steps = []
    for kind, incoming_name in (("master", f"{basename}-master.mp4"), ("srt", f"{basename}.srt")):
        final = d[kind]
        incoming = [p for p in dict.fromkeys((ep / "renders" / incoming_name, d["renders"] / incoming_name)) if p.exists()]
        if final.exists():
            for p in incoming:
                if md5(p) != md5(final):
                    fail(f"{final} exists and differs (md5) from the incoming {p}; nothing was overwritten")
            steps.append(("keep", None, final))
        elif incoming:
            steps.append(("move", incoming[0], final))
        else:
            fail(f"no {final.name} and no {incoming_name} in {ep / 'renders'} or {d['renders']}")
    meta_bytes = meta.read_bytes()
    want = [("write", meta_bytes, d["metadata"])]
    for kind in ("master", "srt"):
        dst = d[f"up_{kind}"]
        if dst.exists() and not same_content(d[kind], dst) and d[kind].exists():
            fail(f"{dst} differs (md5) from {d[kind]}; nothing was overwritten")
        steps.append(("keep" if dst.exists() else "link", d[kind], dst))
    want.append(("write", meta_bytes, d["up_metadata"]))
    for t in sorted((ep / "thumbs").glob(f"{label}-thumb-*")):
        if t.suffix.lower() in IMAGES:
            want.append(("write", t.read_bytes(), d["uploads"] / t.name))
    title = titles(meta_bytes)
    if title:
        want.append(("write", title, d["up_titles"]))
    for _, data, dst in want:
        steps.append(("keep" if dst.exists() and dst.read_bytes() == data else "write", data, dst))
    finals = {d["master"].name, d["srt"].name, d["metadata"].name}
    moving = {s for op, s, _ in steps if op == "move"}
    others = sorted({p for r in (ep / "renders", d["renders"]) if r.is_dir() for p in r.iterdir()
                     if p.name not in finals and p not in moving})
    return steps, others


def apply(steps):
    """Carry out a plan; keep steps are skipped."""
    for op, src, dst in steps:
        if op == "keep":
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        if op == "move":
            before = md5(src)
            try:
                os.rename(src, dst)  # never replaces: on Windows a rename onto an existing file fails
            except OSError as e:
                print(f"[FALLBACK] copied instead of moved: {e}; the source stays")
                shutil.copy2(src, dst)
            if md5(dst) != before:
                fail(f"md5 changed moving {src} to {dst}")
        elif op == "link":
            try:
                os.link(src, dst)
            except OSError as e:
                print(f"[FALLBACK] copied instead of hard-linked: {e}")
                shutil.copy2(src, dst)
        elif op == "write":
            dst.write_bytes(src)


def describe(op, src, dst):
    return f"{op:<6}{'' if src is None or isinstance(src, bytes) else f'{src} -> '}{dst}"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("ep", type=Path)
    ap.add_argument("basename")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(argv)
    steps, others = plan(a.ep.resolve(), a.basename, stage.checkouts()[0][0])
    for s in steps:
        print(("[dry-run] " if a.dry_run else "") + describe(*s))
    if not a.dry_run:
        apply(steps)
    print("non-final renders (not deleted; the session decides):" + ("".join(f"\n  {p}" for p in others) or " none"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
