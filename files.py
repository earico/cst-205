with open("tmp.txt", "w") as temp:
	for i in range(9):
		temp.write("hello world\n")

with open("tmp.txt", "r") as temp:
	read_out = temp.read()

print(read_out)
