#!/usr/bin/env python3
'''
this script tests to see if the number is positive or negative. 
	if positive, test if its bigger ir smaller than 50 
		if smaller test if its an even numeber 
		if larger test if divisible by 3
'''
# input of the count through command line 

import sys
# dont forget to delete the previous assignment of count! 
# grabs the argument from command line 
count = sys.argv[1]
count = int(count)

# if argument is not provided, print a warning
if not count: 
	print('A number must be provided! :( Try again :) ')
	 

# is the number positive  (not non-negative)
if count > 0:
	# check if bigger than 50 
	if count < 50: 
		# if smaller than 50, check if even 
		if count%2 == 0:
			# if the number is even, print message
			print('The number is positive, smaller than 50 and even')
		else: 
			print('the number is positive, smaller than 50, not even')
	elif count > 50: 
		# if the number is larger than 50, check if divisible by 3
		if count%3 ==0: 
			# print message
			print('the number is positive, larger than 50 and divisible by 3')
		else:
			print('the number is positive, larger than 50 but not divisible by 3')
	else:
		print('The number is exactly 50')

elif count<0: 
	print('the number is negative')
else:
	print('the number is 0')			


