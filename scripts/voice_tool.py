#!/usr/bin/env python3
"""Where the narration voice tool lives, and whether every piece of it is present.

Owner 7 Oct 26: everything storm-market uses stays inside the repo folder. The voice tool is
  scripts/tts_clone.py           tracked
  external.pocket_venv_python    .venv-pocket/ in the MAIN checkout (gitignored, 4.9 GB;
                                 package list: scripts/voice_requirements.txt)
  external.voice_ref             tracked, md5 pinned in external.voice_ref_md5
  external.hf_home               .models/hf in the MAIN checkout (gitignored): the cloning
                                 weights (gated repo kyutai/pocket-tts), the faster-whisper
                                 model and the Hugging Face login token
Paths in config.yaml are absolute into the main checkout so every worktree shares one copy.

  python3 scripts/voice_tool.py     one PASS/FAIL line per piece, exit 1 if any is missing
"""
import hashlib
import os
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
WEIGHTS = "hub/models--kyutai--pocket-tts/snapshots/*/languages/english*/model.safetensors"


def load_ext():
    return yaml.safe_load((REPO / "config.yaml").read_text(encoding="utf-8"))["external"]


def use_repo_models(ext=None):
    """Point every Hugging Face download and lookup in this process (and its children) at the repo."""
    os.environ["HF_HOME"] = (ext or load_ext())["hf_home"]


def checks(ext=None):
    """[(piece, ok, what to do when it is missing)]"""
    ext = ext or load_ext()
    hf = Path(ext["hf_home"])
    ref = Path(ext["voice_ref"])
    login = f'HF_HOME="{hf.as_posix()}" hf auth login'
    return [
        ("voice venv", Path(ext["pocket_venv_python"]).is_file(),
         f"{ext['pocket_venv_python']} is missing: rebuild .venv-pocket from scripts/voice_requirements.txt"),
        ("clone script", (REPO / "scripts" / "tts_clone.py").is_file(), "scripts/tts_clone.py is missing: git checkout it"),
        ("voice reference", ref.is_file() and hashlib.md5(ref.read_bytes()).hexdigest() == ext["voice_ref_md5"],
         f"{ref} is missing or its md5 is not {ext['voice_ref_md5']}"),
        ("cloning weights", any(hf.glob(WEIGHTS)),
         f"no kyutai/pocket-tts weights under {hf}: " + (
             "the next narration run downloads them" if (hf / "token").is_file()
             else f"log in first ({login}), on the account that accepted the terms at "
                  "https://huggingface.co/kyutai/pocket-tts; the next narration run then downloads them")),
    ]


def missing(ext=None, allow_download=False):
    """Fix-it lines for the pieces a narration run cannot start without. With allow_download the
    weights may be absent as long as the login that can fetch them is present."""
    ext = ext or load_ext()
    out = []
    for piece, ok, fix in checks(ext):
        if ok or (allow_download and piece == "cloning weights" and (Path(ext["hf_home"]) / "token").is_file()):
            continue
        out.append(f"{piece}: {fix}")
    return out


if __name__ == "__main__":
    rows = checks()
    for piece, ok, fix in rows:
        print(f"{'PASS' if ok else 'FAIL'}  {piece}" + ("" if ok else f" — {fix}"))
    sys.exit(0 if all(ok for _, ok, _ in rows) else 1)
