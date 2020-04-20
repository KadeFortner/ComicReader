# Kade Fortner
# Comix Reader

from PIL import Image

# This loads our image, determines it's height and width to prepare a new image, then determines the RGB values for
# each pixel.
im = Image.open('EasyComicPage1.jpg', 'r')
pix = im.load()
width, height = im.size
newIm = Image.new("RGB", (width, height), "white")
pixel_values = list(im.getdata())
pix_val_flat = [x for sets in pixel_values for x in sets]
# A list containing all taken pixels, i.e. all panels
takenPix = []
panels = 0
Image.MAX_IMAGE_PIXELS = None


# isBlack checks each R, G, and B value of the designated pixel
# it then checks to make sure the values correspond with the minimum and maximum values.
# This ensures that our pixel is within the tolerance we allow for the color(s) we choose.
def isBlack(pixel, minValue):
    maxValue = 199
    if minValue <= pixel[0] <= maxValue:
        print("R = ", pixel[0])
        if minValue <= pixel[1] <= maxValue:
            print("G = ", pixel[1])
            if minValue <= pixel[2] <= maxValue:
                print("B = ", pixel[2])
                return True


# Panel finding function
def findPanel(image):
    global panels
    global takenPix

    print(width, height)
    # We go through each pixel
    for j in range(height):
        for i in range(width):
            # We store found taken pixels in our takenPix list
            if (i, j) not in takenPix:
                # Using our isBlack function, we determine if our pixel is black-ish
                if not isBlack(pix[i, j], 0):
                    # If the pixel is not black, we move to the right
                    i = i + 1
                    print("i = ", i, ". j = ", j)
                elif isBlack(pix[i, j], 0):
                    print("FOUND A BLACKish PIXEL AT i = " + str(i) + " and j = " + str(j))
                    newIm.putpixel((i, j), (0, 0, 255))

                    # When the first black pixel is found, we assume it the start of the panel
                    # We set our cropping coordinates accordingly
                    top = j
                    left = i

                    # From here, we continue to the right until we encounter a non-black pixel
                    while isBlack(pix[i, j], 0):
                        print("FOUND A BLACKish PIXEL AT i = " + str(i) + " and j = " + str(j))
                        newIm.putpixel((i, j), (0, 0, 255))
                        i = i + 1
                        print("i = ", i, ". j = ", j)

                    # We move to the left, to our last found black pixel
                    i = i - 1
                    print("i = ", i, ". j = ", j)

                    # We now move to the downwards until we find a non-black pixel
                    while isBlack(pix[i, j], 0):
                        print("FOUND A BLACKish PIXEL AT i = " + str(i) + " and j = " + str(j))
                        newIm.putpixel((i, j), (0, 0, 255))
                        j = j + 1
                        print("i = ", i, ". j = ", j)

                    # Once found, we move back to our last black pixel, and set our bottom-right coordinates for
                    # cropping
                    j = j - 1
                    right = i
                    bottom = j
                    print("Top = ", top)
                    print("Left = ", left)
                    print("Right = ", right)
                    print("Bottom = ", bottom)

                    # Add this to our number of panels found
                    panels = panels + 1
                    print("Done with", panels, "panel(s)")

                    # We now store the entirety of the panel's coordinates
                    for y in range(top, bottom + 1):
                        for x in range(left, right + 1):
                            takenPix.append((x, y))

                    # We now add anything in between our panels and remove duplicates
                    for m in range(takenPix[0][1], takenPix[-1][1]):
                        for n in range(takenPix[0][0], takenPix[-1][0]):
                            takenPix.append((n, m))
                    takenPix = list(dict.fromkeys(takenPix))

                    newIm.show()
                    # Crop, show, repeat
                    panel = im.crop((left, top, right, bottom))
                    panel.show()

                    findPanel(im)

                else:
                    print("Something is wrong")

            elif (i, j) in takenPix:
                print(i, ", ", j, " already taken.")
                i = i + 1
        j = 0
    i = 0


#############################
###         Main          ###
#############################


findPanel(im)
