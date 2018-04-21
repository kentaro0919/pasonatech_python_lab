with open('test.txt') as fin:
	line=fin.readline()
	while line:
		print(line,end="")
		line=fin.readline()

print(fin.closed)
