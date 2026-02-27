#!/usr/bin/env python3

'''
This script tests out different math functions
'''
import math 
import sys

# import the number through command line 
number = sys.argv[1]
#number = 100  # dont forget to comment this out if using sys.argv
number = int(number)
print('the number is', number)

print('the square root is:', math.sqrt(number))
print('the log10 is:', math.log10(number))
print('the power 2 is:', math.pow(number,3))
