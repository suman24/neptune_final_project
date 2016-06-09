#!/usr/bin/env python

InFileName = "reads100.fa"

InFile = open( InFileName, 'r' )

LineNumber = 0

OutFileName = "reads100.txt"

OutFile = open(OutFileName, 'w' )



for Line in InFile:

	seq1 = "AAAA"
	seq2 = "TTTT"
	seq3 = "GGGG"
	seq4 = "CCCC"

	nucl1 = ['A']
	nucl2 = ['T']
	nucl3 = ['G']
	nucl4 = ['C']


	if Line [ 0 ] in nucl1:
		print seq1 + Line

	elif Line [ 0 ] in nucl2:
		print seq2 + Line

	elif Line [ 0 ] in nucl3:
		print seq3 + Line

	elif Line [ 0 ] in nucl4:
		print seq4 + Line

	else:
		print Line

	


InFile.close()