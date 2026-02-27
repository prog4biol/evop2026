#!/usr/bin/env python3

'''
This script is a FASTA parser  that uses Biopython
'''

# Import
from Bio import SeqIO 
import sys

#  grab filename
filename = sys.argv[1] #is already in string format

# parse the file 
for sequence in SeqIO.parse(filename, 'fasta'):
	# grab sequence ID 
	#print(f'ID: {sequence.id}')

	#translate sequence
	# check if sequence is divisible by 3 
	if  len(sequence)%3 == 0:
		#print(f'\ntranslation: {sequence.seq.translate(to_stop=False)}')
		print(f'{sequence.id}\t{sequence.seq.translate(to_stop=False)}')
	else:
		print(f'Sequence is not divisible by 3')

	
	# Try to translate from the start codon
	# find AUG, then check if multiple of 3, then translate 
