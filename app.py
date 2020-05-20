import os
import glob
import shutil
from pathlib import Path

src_dir = "source"
dst_dir = "destination"
extensions = [".jpg", ".png"]
count = 0

for src_dir, dirs, files in os.walk(src_dir, topdown=False):
    for name in files:
        if Path(name).suffix.lower() in extensions:
            count= count+1
            shutil.copy(os.path.join(src_dir, name), os.path.join(dst_dir, name))

print("Files copied " + str(count))



