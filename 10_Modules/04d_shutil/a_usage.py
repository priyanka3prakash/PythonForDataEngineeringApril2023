import os
import shutil


def copy_file(src_dir, dest_dir, filename):
    source_path = os.path.join(src_dir, filename)
    dest_path = os.path.join(dest_dir, filename)

    if os.path.exists(dest_path):
        print("file already exists. So, deleting")
        os.remove(dest_path)

    shutil.copyfile(source_path, dest_path)


copy_file("source_dir", "destination_dir", "file1.txt")
