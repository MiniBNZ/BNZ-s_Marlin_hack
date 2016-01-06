#!/usr/bin/python
import os
os.system('clear')
nextlinegetsthisadded = ''
needtostop = ''
import sys
filename = sys.argv[-1]

filein = open(filename,'r')
fileout = open(filename+'OUT','w')
print 'Files are open',
print '\n',
print '\n',
print '\n',
print '\n',
print '\n',
print '\n',
print '\n',
print '\n',

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
					needtostop = '1'

				if wordin == 'G2':
					print "\nM3\n",
					needtostop = '1'

				if wordin == 'G3':
					print "\nM3\n",
					needtostop = '1'

				if wordin != 'M3':
					if wordin != 'M4':
						if wordin != 'M5':
							if wordin != 'M8':
								if wordin != 'M9':
									print wordin,

	print ''
	if needtostop == '1':
#		fileout.write('M5\n')#
		print 'M5\n',
		needtostop = ''
