import glob
import os

files = glob.glob("???.png")
files.sort()
img_num = 1
img_prefix = "f"
for f in files:
    if f == "009.png":
        img_num = 1
        img_prefix = "p"
    if f in ["053.png", "204.png", "357.png"]:
        os.symlink(f, "%s%04d-image1.png" % (img_prefix, img_num - 1))
    else:
        os.symlink(f, "%s%04d.png" % (img_prefix, img_num))
        img_num += 1
