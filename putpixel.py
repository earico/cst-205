import secrets
from PIL import Image

im = Image.open("dodgerstadium-fireworks.png")
width, height = im.size

for x in range(width):
	for y in range(height):
		rgb_val = (secrets.choice(range(40,200)),
			   secrets.choice(range(150,170)),
			   secrets.choice(range(50,200)))
		im.putpixel((x,y), rgb_val)
im.save("dodgerstadium-fireworks.png")
