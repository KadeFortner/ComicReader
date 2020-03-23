# Kade Fortner
# Capstone stuff

import numpy
from PIL import Image


im = Image.open('EasyComicPage1.jpg', 'r')

pix = im.load()
width, height = im.size
newIm = Image.new("RGB", (width, height), "white")
pixel_values = list(im.getdata())
pix_val_flat = [x for sets in pixel_values for x in sets]
print(pixel_values)

for i in range(width):
    for j in range(height):
        # Get Pixel
        if pix[i, j] == (0, 0, 0):
            print("FOUND A BLACK PIXEL AT X = " + str(i) + " and Y = " + str(j))
            newIm.putpixel((i, j), (0, 0, 255))

im.show()
newIm.show()