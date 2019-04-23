from PIL import Image
im = Image.open("rgb-gradient.jpg")
width, height = im.size

for x in range(width):
	for y in range(height):
		im.histogram()

