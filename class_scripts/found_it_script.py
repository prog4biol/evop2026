#!/usr/bin/env python3

# In your text editor create a script that prints 'FOUND IT!!' if this string of 
# nucleotides: 'TTCGTATT', is found in this string of 
# DNA: 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
# else
# Theif portion of the if/else statement behave as before.
# The first indented block is executed if the condition is true.
# If the condition is false, the second indented else block is executed.

dna = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
if 'ATTCGTATTG' in dna:
  print('FOUND IT!!')
else:
  print('did not find TTCGTATT in your dna sequence')
  