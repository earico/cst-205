with open("tmp.txt", "r") as f:
	line_list = f.readlines()

for counter, line in enumerate(line_list):
	print(f'Line {counter}: {line}')
