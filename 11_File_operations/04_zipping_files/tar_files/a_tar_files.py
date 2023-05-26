"""
Purpose: Working with tar files
"""

import tarfile
import os

# print(dir(tarfile))


for file_name in os.listdir("files"):
    os.path.join(os.getcwd(), file_name)

    print(file_name, tarfile.is_tarfile(file_name))
