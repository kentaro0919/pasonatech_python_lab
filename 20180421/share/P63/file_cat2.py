fin=open('test.txt')
line=fin.readline()
while line:
	print(line,end="")
	line=fin.readline()

fin.close()
