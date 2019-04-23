from PIL import Image
im = Image.open('dodgerstadium-fireworks.png')

width, height = im.size

big_pixel_list = []

for x in range(width):
	for y in range(height):
		big_pixel_list.append(im.getpixel((x,y)))

print(big_pixel_list)
