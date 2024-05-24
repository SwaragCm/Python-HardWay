# create functions using def
def print_two(*args):   #this function takes number of arguments
    arg1,arg2=args      #unpacks the first two arguments, and assigns them to arg1 and arg2 respectively. 
    print(f"arg1: {arg1},arg2: {arg2}")

# This function takes exactly two arguments, arg1 and arg2, and directly prints them out.
def print_two_again(arg1,arg2): 
    print(f"arg1: {arg1},arg2: {arg2}")

# This function takes one argument arg1 and prints it out.
def print_one(arg1):
    print(f"arg1: {arg1}")

# This function takes no arguments and simply prints "I got nothing...".
def print_none():
    print("I got nothing...")


#  Calls print_two with two arguments "zed" and 22. It unpacks these arguments into arg1 and arg2, then prints them.
print_two("zed",22)
# Calls print_one with one argument "first !", which is then printed out.
print_two_again("swag",25)
print_one("first !")
print_none()