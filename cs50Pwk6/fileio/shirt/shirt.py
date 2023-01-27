import sys
from PIL import Image, ImageOps
import os

imgLength = len(sys.argv)

if imgLength < 3: 
    sys.exit("Too few command-line arguments")

if imgLength > 3:
    sys.exit("Too much command-line arguments")

image1 = sys.argv[1]
image2 = sys.argv[2]

filename1, file_extension1 = os.path.splitext(image1)
if file_extension1.lower() not in [".jpg",".jpeg",".png"]:
    sys.exit("Invalid input")

filename2, file_extension2 = os.path.splitext(image2)
if file_extension2.lower() not in [".jpg",".jpeg",".png"]:
    sys.exit("Invalid Output")

if file_extension1 != file_extension2:
    sys.exit("Input and output have different extensions")

if not os.path.exists(image1):
    sys.exit("Input image file not found")
image_before = Image.open(image1)

if not os.path.exists("shirt.png"):
    sys.exit("Shirt image file not found")
image_shirt = Image.open("shirt.png")

image_before_fit = ImageOps.fit(image_before, image_shirt.size) 

# new_image = Image.new("RGB", image_shirt.size)
# new_image.paste(image_before_fit)
# new_image.paste(image_shirt, (0, 0), image_shirt)

image_before_fit.paste(image_shirt, image_shirt)
image_before_fit.save(sys.argv[2])

image_before_fit.show()
