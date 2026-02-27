#!/usr/bin/env python3

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