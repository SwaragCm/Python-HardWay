from sys import argv
# Use argv to get a filename
script, filename = argv
# Here we are opening the file which we passed as a command line argument and assigning that resulting file, to a variable.
txt=open(filename)

print(f"Here's your file {filename}:")
print(txt.read())   #this line read the contents of the file using read()

print("Type the filename again:")
# This line captures the user's input (the filename) using the input() function and assigns it to the variable file_again.
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())