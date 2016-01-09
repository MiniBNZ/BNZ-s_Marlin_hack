#!/usr/bin/python
import os
os.system('clear')
nextlinegetsthisadded = ''
needtostop = ''
import sys
filename = sys.argv[-1]

filein = open(filename,'r')
fileout = open(filename+'OUT','w')

for linein in filein:

	if linein !='':
		if nextlinegetsthisadded !='':
			linein = linein + nextlinegetsthisadded
			nextlinegetsthisadded = ''

		if linein[:1] == 'F': 
			nextlinegetsthisadded = linein
		else:
			for wordin in linein.split():
				if wordin == 'G1':
					print "\nM3\n",
					fileout.write('\nM3\n')
					needtostop = '1'

				if wordin == 'G2':
					print "\nM3\n",
					fileout.write('\nM3\n')
					needtostop = '1'

				if wordin == 'G3':
					print "\nM3\n",
					fileout.write('\nM3\n')
					needtostop = '1'

				if wordin != 'M3':
					if wordin != 'M4':
						if wordin != 'M5':
							if wordin != 'M8':
								if wordin != 'M9':
									fileout.write(wordin+' ')
									print wordin,


	print ''
	if needtostop == '1':
		fileout.write('\nM5\n')
		print 'M5\n',
		needtostop = ''
fileout.write("\nM5\n")
fileout.close()
filein.close()
