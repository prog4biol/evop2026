#!/usr/bin/env python3

# use range to print numbers between 1 and 100
# input can also be done through command line

# import package
import sys
upper_number = int(sys.argv[1]) # dont forget to switch to integer! 

# it would be a good idea to make sure that only the number larger than 1 is
# used

# check if input is larger than 1
if upper_number <1:
	print('The number must be larger or equal to 1')

# print numbers up to and including the number from input
for number in range(1, upper_number+1):
	print(number)
