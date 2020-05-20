import os
import glob
import shutil
from pathlib import Path

src_dir = "source"
dst_dir = "destination"
extensions = [".jpg", ".png"]

# for jpgFile in glob.iglob(os.path.join(src_dir, "*.*g")):
    # shutil.copy(jpgFile, dst_dir)

for src_dir, dirs, files in os.walk(src_dir, topdown=False):
    for name in files:
        if Path(name).suffix.lower() in extensions:
            shutil.copy(os.path.join(src_dir, name), os.path.join(dst_dir, name))

print('All files copied successfully')



