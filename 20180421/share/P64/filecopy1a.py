sourcefile='test.txt'
targetfile='new_test.txt'

print('source file [',sourcefile, ']')
print('target file [',targetfile, ']')

with open(sourcefile) as fin:
	with open(targetfile, 'w+')  as fout:
		line=fin.readline()
		while line:
			fout.write(line)
			line=fin.readline()
			
print('DONE')


