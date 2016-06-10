#!/usr/bin/env python

InFileName = "reads100.fa"

InFile = open( InFileName, 'r' )

LineNumber = 0

OutFileName = "reads100.txt"

OutFile = open(OutFileName, 'w' )

import random
#using random functionality

for Line in InFile:

	seq1 = ['AATTGGCC', 'TTAAGGCC', 'GGCCTTAA', 'CCGGAATT']

	nucl = ['A', 'T', 'G', 'C']



	if Line [ 0 ] in nucl:
		print (random.choice(seq1)) + Line
#Line [0] in nucl looks for A/T/G/C in the first character of a line.
#Line [-1] looks at the last character of a line

	else:
		print Line

	


InFile.close()

#when running the program use '>' plus the outfile file.txt/fa to get an output file.





