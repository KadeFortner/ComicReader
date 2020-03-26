# Kade Fortner
# Capstone stuff

import numpy as np
import cv2
from PIL import Image


# isBlack checks each R, G, and B value of the designated pixel
# it then checks to make sure the values correspond with the minimum and maximum values.
# This ensures that our pixel is within the tolerance we allow for the color(s) we choose.
def isBlack(pixel, minValue, maxValue):
    if minValue <= pixel[0] <= maxValue:
        print("R = ", pixel[0])
        if minValue <= pixel[1] <= maxValue:
            print("G = ", pixel[1])
            if minValue <= pixel[2] <= maxValue:
                print("B = ", pixel[2])
                return True


im = Image.open('EasyComicPage1.jpg', 'r')

# This loads our image, determines it's height and width to prepare a new image, then determines the RGB values for
# each pixel.
pix = im.load()
width, height = im.size
newIm = Image.new("RGB", (width, height), "white")
pixel_values = list(im.getdata())
pix_val_flat = [x for sets in pixel_values for x in sets]
# print(pixel_values)

count = 0;

# We now iterate through our list of pixels, using our isBlack function to determine if said pixel is within our
# designated color spectrum. In this case, black.
for i in range(width):
    for j in range(height):
        if isBlack(pix[i, j], 0, 155):
            count = count + 1
            print("FOUND A BLACKish PIXEL AT X = " + str(i) + " and Y = " + str(j))
            print(pix[i, j])
            # This will mask the found pixels in blue in a new image.
            newIm.putpixel((i, j), (0, 0, 255))

# We end by showing our current count of total pixels found/confirmed, then show our previous image, followed by the
# new image, masked in blue.
print(count)
im.show()
newIm.show()
