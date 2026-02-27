#!/usr/bin/env python3

'''
This script contains solutions to all 'Try now' blocks in section Python Overview. 
'''
# Open the interactive interpreter. Type python3 in the terminal window
# Use the print() function to print something to the screen. Make sure to use parenthesis (), 
# quotes "" like in the example.

# =======================================================================================
# in the command line enter python3 to open interpreter 
print('hello world')

# ======================================================================================
# Open your text editor and add #!/usr/bin/env python3 to the top of your file. 
# There cannot be any white space above or before this line.
# Use the print() function to print something to the screen.
# Save your script.
# Make it executable with chmod +x. (You only have to do this one time per script.)
# Run the script on the command line ./yourScript.py

# in the command line enter nano yourscript.py to write a script in nano
# use the print() function to print a message
print("Hello from my python sssscript!")

# see file yourScript.py
# =======================================================================================

#In the interpreter, create and assign (=) values to variables with the following names:
#name
#institute
#birth_country (example of variable name using a_underscore)
#favoriteColor (example of variable name using camelCase)
#Use the print() function to print each variable to the screen. Don't use quotes around variables, we will talk more about this later.
 
# in the command line enter python3 to open interpreter 
# define variables
name = 'Lana'
institute = 'FBUB'
birth_country = 'Serbia'
favoriteColor = 'pink'

# print to screen (do not put variable names in quotes)
print(name) 
print(institute)
print(birth_country)

# see file numbers_strings_script.py
# =============================================================================

# In the interpreter, create a list and assign it to a variable.
# Play close attention to the the square brackets [] and the quotes ''. 
# (Either single or double quotes can be used here.)
# Be sure to give the variable a descriptive name.
# Use the print() to print the list to the screen.

# in the command line enter python3 to open interpreter 
my_list = ['one', 'two', 'three']
print(my_list)

# ==============================================================================

# In the interpreter create a dictionary and assign it to a variable.
# Play close attention to the curly braces ({}) and the quotes.
# Use the print() function to print the contents to the screen.

# in the command line enter python3 to open interpreter 
my_dictionary = {
    'key1':'value1',
    'key2': 'value2'
}
print(my_dictionary)

# =====================================================================================
# Using your text editor, create a new python script. 
# Be sure to include #!/usr/bin/env python3 on the very first line. 
# Make sure you give the script a name that ends with '.py'
# Import the sys module by typing import sys.
# Create a variable called favAnimal and assign the first command line argument to this variable, using sys.argv[1]. Need help? Check out the python docs.
# Create a variable called favGene and assign the second command line argument to this variable using sys.argv[2].
# Print the two variables to the screen.

# import packages
import sys

favAnimal = sys.argv[1]
favGene = sys.argv[2]

print(favAnimal, favGene)
# see file command_line_import.py

# ================================================================================

# In the interpreter create a list, assign it to a variable named 'experiment'.
# Use the type() function to help you determine what kind of object you have.
# Overrite the contents of 'experiment' with another value.
# Use the type() function to help you determine what kind of object you have.

experiment = [1,2,3]
print(type(experiment))
experiment = 'one, two, three'
print(type(experiment))

# ==================================================================================

# Use the Interactive interpreter to test to see if you can find an 'CAA' in the following DNA string:

# GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA
# How about 'GGG'?
# Use the in operator to test to see if the codon 'ata' in this list? How about 'agg'?
# codons = [ 'atg' , 'aaa' , 'agg' ]

dna = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
print('CAA' in dna)
print('GGG' in dna)

codons = [ 'atg' , 'aaa' , 'agg' ]
print('ata' in codons)
print('aag' in codons)

# ===================================================================================
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
  
# see file found_it_script.py
# ==============================================================================

# Using a text editor, write a script that
# Assigns a value to a variable
# Has a if/else statement in which:
# It prints out a confirmation of truth if the value is true
# It prints out "Not True" if the value is not true.
# if/elif
# The if condition is tested as before and the indented block is executed if the condition is true.
# If it's false, the indented block following the elif is executed if the first elif condition is true.
# Any remaining elif conditions will be tested in order until one is found to be true. 
# If none is true, the else indented block is executed.


my_variable = True
if my_variable == True:
    print('The variable is true')
else: 
    print('The variable is false')

# the variable can be imputted through sys or through the imput function
# for the next Try now block - see file ifelif.py
# ===================================================================================================

# Count the number of As in a DNA string (dna = 'ATGCTGCATT').
# Lowercase and print the DNA string.

dna = 'ATGCTGCATT'
A_count = dna.count('A')
print(dna.lower())

# Extract the first 6 nucleotides from this DNA string: ATTAAAGGGCCC and save the substring in a variable.
# Replace all Ts with U's in the substring. Print the new string.\

dna = 'ATTAAAGGGCCC'
first_six = dna[0:6]
dna.replace('T', 'U')
print(dna)
      
# ===================================================================================================
#
# # <!-- In the interpreter create a list of your favorite things.
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

#see replace_middle_element.py file
# ============================================================================================

# In the interpreter create a list.
# Add a new element to the end. Read about append().
# Add a new element to the beginning. Read about insert().
# Add a new element somewhere other than the beginning or the end.
# Remove an element from the end. Read about pop().
# Remove an element from the beginning.
# Remove an element from somewhere other than the beginning or the end.

my_list = [1,2,3]
my_list.append(4)
my_list.insert(0,5)
my_list.insert(1,5)
my_list.pop()
my_list.pop(0)
my_list.pop(2)

# ============================================================================================

# In your text editor create a script that uses a while loop to print out the numbers 1 to 100.
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

# see file for_loop_script_E2
# ===============================================================================================
# CHALLENGE QUESTION: Write a script that uses a while loop to calculate the factorial of 1000.

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

# see script factorial_script.py

# ==============================================================================
# define the list 
numbers_list = [101,2,15,22,95,33,2,27,72,15,52]
# also can be done through the command line
    # imoport sys
    # numbers_list = sys.argv[1]
# -------------------------------------------
# print only even numbers
# a number is even if  it  has no remainder after division with 2

for number in numbers_list:
	# check if number is even 
	if number%2 == 0:
		# print the number
		print(number)
		
# ==============================================================================
# Create a dictionary of your favorite color, book, song, and organism. 
# Use the these as the keys: color, book, song, organism.
# Print out your favorite book.

favourite_things = {
	'color' : 'pink' ,
	'book' : 'to kill a mocking bird',
	'organism' : 'sciurus vulgaris',
	'song' : 'Sweater weather'
}

print(f"my favourite book is {favourite_things['book']}")

# Print out your favorite book but use a variable in the key.
fav = 'book'
print(f"my favourite book is {favourite_things[fav]}")

# Print out your favorite organism using the literal 'organism' as the key 
# and then with using the variable fav_thing.
print(f"my favourite organism is {favourite_things['organism']}")
fav = 'organism'
print(f"my favourite organism is {favourite_things[fav]}")

# Change the value of your favorite organism.
favourite_things['organism'] = 'e. coli'
print(f"my favourite organism is {favourite_things['organism']}")

# =======================================================================
# for the next Try now block, see file dictionary_script.py





