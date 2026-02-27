#!/usr/bin/env python3

# create a dictionary of genes

genes = {
'geneA': 'ATGATAGATGATAGATCATCGACTGACTGCATCAGCATCAGCATCGC',
'geneB': 'AGAGAGATGATAGTAACATCGATCAGCATCAGCTACG',
'geneC': 'CTGCTCAGCATCAGCTAGCTACGACTACGACTAGCATCGATCACGATCAGCA'
}

# Use for loop to print each gene name:
# there are multiple ways to do this 

# 1) iterate through both key and value
print('Printing for key-value method')
for key in genes:
	print(key)

'''
# this grabs the key and the value 
for key,value in genes.items():
	print(key)
	print(value)
'''

# 2) dictionaries have a method ".keys" to extract all keys
# dict.keys() returns an object that can be put into a list 
# list(dict.keys())
print('Printing for built-in method')
for key in list(genes.keys()):
	print(key) 
# --------------------------------------------------------
# add  the sequence to the print statement:
for key,value in genes.items():
	print(f'{key} \t {value}')

# --------------------------------------------------------
# replace seq with length in the print statement

for key,value in genes.items():
	print(f'{key} \t {len(value)}')

# --------------------------------------------------------
# 5. Add the number of As with the length 
# 6. Add the number of Ts 
# 7. Add the G number 
print('Add the number of As')
for key, value in genes.items():
	name = key
	length = len(value)	
	A_count = value.count('A')
	T_count = value.count('T')
	G_count = value.count('G')
	C_count = value.count('C')
	print(f'{name} \t {length}\t {A_count}\t{T_count}\t{C_count}\t{G_count}')

# this can also be done with two loops:
print('\n--------alternative way-----------------------')
for key, value in genes.items():
	name = key
	length = len(value)
	
	nt_dict= {}
	nt_counts = []
	for nt in ['A', 'T', 'C', 'G']:
		nt_counts.append(value.count(nt))
		nt_dict[nt]=value.count(nt)
	# nt_counts is a list with counts for A, T, C, G (in order)
	print(f'{name}\t{length}\t{nt_counts[0]}\t{nt_counts[1]}\t{nt_counts[2]}\t{nt_counts[3]}')

#----------------------------------------------------------

# add the GC% to the print statement 
print('\n-----------GC content-------------------------')

for key, value in genes.items():
	name = key
	seq = value
	C_count = seq.count('C')
	G_count = seq.count('G')
	GC_content = (C_count + G_count)/len(seq)*100
	print(f'{name}\t{len(seq)}\t{GC_content:.2f}')
	
	# round(number,decimals)
