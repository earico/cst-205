from PIL import Image
import pickle
im = Image.open("rgb-gradient.jpg")
width, height = im.size

def task1():
	my_dict =  {
		"red": [0, 0, 0, 0],
		"green": [0, 0, 0, 0],
		"blue": [0, 0, 0, 0]
	}

	for x in range(width):
		for y in range(height):
			r, g, b = im.colors()

			if r >= 0 and r <= 63:
				my_dict["red"][0] = my_dict["red"][0] + 1
			if r >= 64 and r <= 127:
				my_dict["red"][1] = my_dict["red"][1] + 1

	print(my_dict["red"])

task1()
