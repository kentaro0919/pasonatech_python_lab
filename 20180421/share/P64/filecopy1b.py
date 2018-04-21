sourcefile='test.txt'
targetfile='new_test.txt'

def filecopy1(sourcefile,targetfile):
	with open(sourcefile) as fin:
		with open(targetfile, 'w+')  as fout:
			line=fin.readline()
			while line:
				fout.write(line)
				line=fin.readline()
			

print('source file [',sourcefile, ']')
print('target file [',targetfile, ']')

filecopy1(sourcefile,targetfile)
print('DONE')


