# Kade Fortner
# Capstone stuff

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
Image.MAX_IMAGE_PIXELS = None


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


# Panel finding function
def findPanel(image):
    print(width)
    print(height)
    i = 0
    j = 0
    exit = 0
    while exit == 0:
        while (i * j) not in takenPix:
            for j in range(height):
                for i in range(width):
                    if not isBlack(pix[i, j], 0, 199):
                        i = i + 1
                        print("i = ", i, ". j = ", j)
                    elif isBlack(pix[i, j], 0, 243):
                        print("FOUND A BLACKish PIXEL AT X = " + str(i) + " and Y = " + str(j))
                        takenPix.append((i * j))
                        top = i
                        print("Top = ", top)
                        left = j
                        print("Left = ", left)
                        while isBlack(pix[i, j], 0, 243):
                            print("FOUND A BLACKish PIXEL AT X = " + str(i) + " and Y = " + str(j))
                            i = i + 1
                            print("i = ", i, ". j = ", j)
                        i = i - 1
                        print("i = ", i, ". j = ", j)
                        right = i
                        print("Right = ", right)
                        while isBlack(pix[i, j], 0, 243):
                            print("FOUND A BLACKish PIXEL AT X = " + str(i) + " and Y = " + str(j))
                            j = j + 1
                            print("i = ", i, ". j = ", j)
                        bottom = j
                        print("Bottom = ", bottom)
                        print("Done with first panel")

                        takenPix.append(i * j)
                        panel = im.crop((left, top, right, bottom))

                        # Shows the image in image viewer
                        panel.show()
                        exit = 1

                    else:
                        print("Something is wrong")
                j = 0
            i = 0
        i = i + 1



#############################
###         Main          ###
#############################


findPanel(im)




'''
# We now iterate through our list of pixels, using our isBlack function to determine if said pixel is within our
# designated color spectrum. In this case, black.
count = 0;

for i in range(width):
    for j in range(height):
        if isBlack(pix[i, j], 0, 240):
            newIm.putpixel((i, j), (0, 0, 255))
            count = count + 1
            print("FOUND A BLACKish PIXEL AT X = " + str(i) + " and Y = " + str(j))
            x = i
            while isBlack(pix[x, j], 0, 240):
                x = x + 1
                print("New pixel: ", pix[x, j])
                print("At X = ", x, " and j = ", j)
            i = x
            top = x * j
            y = j
            while isBlack(pix[x, y], 0, 240):
                y = y + 1
                print("New pixel: ", pix[x, y])
                print("At X = ", x, " and y = ", y)
            j = y

            # This will mask the found pixels in blue in a new image.
            # newIm.putpixel((i, j), (0, 0, 255))
        else:
            print("NON-COLORED PIXEL AT X = " + str(i) + " and Y = " + str(j))


# We end by showing our current count of total pixels found/confirmed, then show our previous image, followed by the
# new image, masked in blue.

print(count)
im.show()
newIm.show()
'''
