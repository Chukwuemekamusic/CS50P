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

image_before = Image.open(image1)
image3 = Image.open("shirt.png")

image_before_fit = ImageOps.fit(image_before, image3.size, bleed=0.0, centering=(0.5, 0.5)) 

new_image = Image.new("RGB", image3.size)
new_image.paste(image_before_fit)
new_image.paste(image3, (0, 0), image3)

new_image.save(sys.argv[2])
