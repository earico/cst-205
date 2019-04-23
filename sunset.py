from PIL import Image
im = Image.open("eiffeltower.jpg")

def sunsetImage(picture):
	newList = []
	for p in picture.getdata():
		temp = (p[0], int(p[1]*0.4), int(p[2]*0.4))
		newList.append(temp)
	picture.putdata(newList)
	picture.show()

sunsetImage(im)
