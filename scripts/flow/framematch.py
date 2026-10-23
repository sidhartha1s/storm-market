"""How far a clip's opening frame strays from the start frame it was made from (0 = identical, 255 = opposite).

Mean absolute grey difference at 96x54 over the first frame, after a 0.5 s seek past any fade-in.
"""
import subprocess, sys
from PIL import Image, ImageChops, ImageStat

SIZE = (96, 54)


def first_frame(mp4):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", "0.5", "-i", mp4, "-frames:v", "1", "-vf", f"scale={SIZE[0]}:{SIZE[1]},format=gray",
                          "-f", "rawvideo", "-"], capture_output=True, check=True).stdout
    return Image.frombytes("L", SIZE, raw)


def distance(mp4, frame_path):
    ref = Image.open(frame_path).convert("L").resize(SIZE)
    return ImageStat.Stat(ImageChops.difference(first_frame(mp4), ref)).mean[0]


if __name__ == "__main__":
    print(f"{distance(sys.argv[1], sys.argv[2]):.1f}")
