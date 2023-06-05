"""
pip install pillow
"""

# import PIL

# print(PIL)
# print(dir(PIL))

import os

from PIL import Image, ImageDraw

os.makedirs("images", exist_ok=True)


img = Image.new("RGB", (600, 30), color="red")
#                mode,  size,    color


print(img)

img.save("images/pil_red.png")
