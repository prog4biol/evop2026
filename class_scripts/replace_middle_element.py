#!/usr/bin/env python3

'''
This script takes a list as an input, as well as an additional item. 
'''

# <!-- In the interpreter create a list of your favorite things.
# Use the print() function print out the middle element.
# Now replace the middle element with a different item, your favorite song, or song bird.
# Use the same print statement from #2 to print your new list. -->

# import packages
import sys

my_list = sys.argv[1]
new_item = sys.argv[2]

# automatic check to find the middle of the script
# if the script has an odd number of elements, the index of the middle item can be determined
# If the script has an even number of elements, the new item replaces the item with a greater index

middle_index = len(my_list) // 2
my_list[middle_index] = new_item 
print(my_list)

