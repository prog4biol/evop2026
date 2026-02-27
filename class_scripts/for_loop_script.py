#!/usr/bin/env python3

# define the list 
numbers_list = [101,2,15,22,95,33,2,27,72,15,52]
# also can be done through the command line
# -------------------------------------------
# print only even numbers
# a number is even if  it  has no remainder after division with 2

for number in numbers_list:
	# check if number is even 
	if number%2 == 0:
		# print the number
		print(number)

