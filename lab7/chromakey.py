from PIL import Image
img = Image.open("EmiliePreyer.jpg")

print("Size of image: " + str(img.width) + " by " + str(img.height))

def chroma():
    for x in range(img.width):
        for y in range(img.height):
            coord = img.getpixel((x,y))
            if(coord[0] == 255):
                return coord

print(chroma())
