# import argv object from sys module.
from sys import argv
# unpacks the arguments and assigned to four variables
script, first, second, third = argv

print("The script is called:", script)  #This line prints out the name of the script

# This line prints out the value of the first command-line argument passed to the script. like vice versa
print("Your first variable is:", first) 

print("Your second variable is:", second)
print("Your third variable is:", third)

# Before run the program you must pass 3 command line arguments ,otherwise this will get error.