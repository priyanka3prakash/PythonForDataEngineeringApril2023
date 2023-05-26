from PIL import Image, ImageEnhance, ImageFilter

original_image = Image.open("images/strawberries.png")
original_image.show()

grayscale = original_image.convert("L")
edge_detect = original_image.filter(ImageFilter.FIND_EDGES)
edge_detect.show()
edge_detect.save("images/edge_detect.png")


contrast_image = ImageEnhance.Contrast(original_image).enhance(3.5)  # 1.5
contrast_image.show()
contrast_image.save("images/contrast_image.png")

bright_image = ImageEnhance.Contrast(contrast_image).enhance(5)  # 1.5
bright_image.show()
bright_image.save("images/bright_image.png")
