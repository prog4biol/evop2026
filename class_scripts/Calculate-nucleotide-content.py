#!usr/bin/env python3

# importing sys module to use sys.argv to take in argument from command line
import sys

# importing modules from Biopython to recognize fasta format
from Bio import SeqIO
import Bio.SeqUtils

# taking in user input file from command line
infile = sys.argv[1]

# declaring empty lists
ids = []
seqs = []

# using a for look to loop through fasta sequences in input file
# appending the ids and sequences
for seq_record in SeqIO.parse(infile, 'fasta'):
    ids.append(seq_record.id)
    seqs.append(seq_record.seq)

# taking the length of the ids (number of list elements) for the number of contigs
print(f'number of contigs: {len(ids)}')

# looping through the contigs to get the total sequence length
total = ''
for contig in seqs:
    total = total + contig  # adding each contig onto the total

# declaring an empty dictionary
content = {}
for base in total:
    if base not in content.keys(): # if first time encoutering the key, start keepinng count
        content[base] = 1
    else: # else key has been establishe and are increasing count
        content[base] += 1

# looping through keys and printing out each key (nucleotide) and its value (count)
for nucleotide in content.keys():
    print(f'{nucleotide}: {content[nucleotide]}')

# proportion of genome comprised of gaps (N)
print(f'proportion of gaps: {content['N'] / len(total):.2%}')

# parse fasta file
# how many contigs are there?
# what is the nucleotide content of both masked(lowercase) and not (upper)
# what proportion of genome is comprised of gaps (NNN)?

