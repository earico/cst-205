from PIL import Image
im = Image.new("RGB", (18, 29))

width = 18
height = 29

with open("mona.txt", "r") as mona:
	lines = [line.split() for line in mona]

for y in range(height):
	for x in range(width):
		z = int(lines[y][x])
		im.putpixel((x, y), (z, z, z))
im.show()
