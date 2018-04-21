fin=open('test.txt')
lines=fin.readlines()
for line in lines:
	print(line,end="")

fin.close()

