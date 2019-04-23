audio_formats = ["flac", "m4a", "mp3", "wav", "ogg", "aiff"]
with open("tmp2.txt", "w") as g:
	g.write(str(audio_formats))

with open("tmp2.txt", "r") as h:
	my_list = h.read()

print(my_list)
print(my_list[0])
