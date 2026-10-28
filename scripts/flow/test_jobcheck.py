# Start-frame lock: the global v2 frame or an episode's own media/paul/paul-start-frame-*; never a sheet or a stray image.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from jobcheck import errors

def job(frame):
    return {"jobs": [{"name": "j", "frame": frame, "prompt": "@char1 speaks"}]}

W = "C:/Users/S/Automation Projects/storm-market/.worktrees/ep-buffalo-2022"
assert errors(job(W + "/assets/paul/paul-start-frame-omni-v2.png")) == []
assert errors(job(W.replace("/", "\\") + r"\episodes\ep-buffalo-2022\media\paul\paul-start-frame-christmas.png")) == []
assert errors(job(W + "/assets/paul/paul-sheet-c.png")), "the character sheet must never be the frame"
assert errors(job(W + "/episodes/ep-buffalo-2022/media/paul/inputs/paul-desk-frame.jpg")), "only paul-start-frame-* files"
assert errors(job(W + "/assets/paul/paul-start-frame-omni.jpg")), "v1 global frame stays refused"
print("test_jobcheck OK")
