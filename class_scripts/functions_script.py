#!/usr/bin/env python3

'''
This script defines a GC_content function  and uses it to calculate GC content of 
sequences in a provided file
'''

# import package and define filename
import sys
filename = sys.argv[1] # in string format

# ----------------------------------------------------
# write  function that caclulates the GC content 

def gc_content(seq):
	# remember, python is case sensitive
	# this is the place to make sure our sequence is in all upper or all lower script
	seq = seq.upper() # we can also do seq=seq.lower()

	# calculate C and G content
	c_count = seq.count('C') # use lowercase 'c' and 'g' if using seq.lower()
	g_count = seq.count('G')
	gc_percent = (c_count + g_count)/len(seq)*100

	# return the result
	return gc_percent

# open the file and for each sequence calculate GC content
# this can also be done multiple ways
# we can write a function to load sequences in the dictionary or 
# we can process them in the body of the script

# process through the body 
with open(filename, 'r') as f: 
	for line in f:
		line = line.strip()
		# store gene name and sequence in variables gene and seq
		gene,seq = line.split('\t') # check your file for separator

		# calculate gc content
		gc =  gc_content(seq)
		print(f'gene {gene} has {gc:.2f}% GC content')
