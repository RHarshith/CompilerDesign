filein=open('icg.txt','r')
fileout=open('quadcode.txt','w')
for line in filein:
	line=line.strip().split(' ')
	if len(line)==3 and '=' in line:
		fileout.write('| '.join([line[1],line[2],' ',line[0]])+'\n')

	elif len(line)==5:
		fileout.write('| '.join([line[3],line[2],line[4],line[0]])+'\n')

	else:
		fileout.write(' '.join(line)+'\n')

filein.close()
fileout.close()