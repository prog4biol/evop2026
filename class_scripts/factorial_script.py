#!/usr/bin/env python3
'''
This script calculates a fatorial of a number
and inputs the argument through the command line
'''

# import packages
import sys

# define number for calculation from input argument
number = sys.argv[1]
number = int(number)
# Factorial loop - cannot start at zero  
count = 1
factorial = 1
while count <= number:
	factorial = factorial * count
	count = count +1
print(f'The factorial of number {number} is {factorial}')




	

number
