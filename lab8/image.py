from PIL import Image

im = Image.open('MFDOOM.jpg')

#print(dir(im))

class Song:
	def __init__(self, artist, genre, length, album):
		self.artist = artist
		self.genre = genre
		self.length = length
		self.album = album

	def display(self):
		print("Artist: " + self.artist)
		print("Genre: " + self.genre)
		print("Length: " + self.length)
		print("Album: " + self.album)

RedRedWine = Song("UB40", "Reggae", "204", "Labour of Love")
KonKarne = Song("MF DOOM", "Hip-Hop", "256", "MM.. FOOD")

RedRedWine.display()
print()
KonKarne.display()
