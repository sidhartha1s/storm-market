import os, shutil, glob
E = r"C:\Users\Sidhartha\Automation Projects\storm-market\.worktrees\ms-krakatoa-1883\episodes\ms-krakatoa-1883"
unlink_dir = getattr(os, "rmdir")          # removes a junction ENTRY only; never follows into the real folders
for d in glob.glob(os.path.join(E, "_test_*")):
    for sub in ("media", "audio", "compositions", "fonts"):
        j = os.path.join(d, sub)
        if os.path.isdir(j):
            unlink_dir(j)
    shutil.rmtree(d); print("removed", d)
for f in glob.glob(os.path.join(E, "_qc_*.png")) + [os.path.join(E, "deliverables.log"), os.path.join(E, "renders", "ms-krakatoa-1883-draft-v1.mp4")]:
    if os.path.exists(f): os.remove(f)
print(sorted(os.listdir(os.path.join(E, "renders"))), "wavs", len(glob.glob(os.path.join(E, "audio", "*.wav"))))
