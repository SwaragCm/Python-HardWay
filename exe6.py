types_of_people=10
# initialized format string to a variable
x = f"There are {types_of_people} types of people"

binary = "binary"
do_not = "don't"
y=f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
# used .format()
joke_evaluation = "Isn't that joke so funny?! {}"  #here i used {} for to concatenate another value to this string 
# print the variable which has the string value , also used .format() to concatenate another value to the existing string
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."
# here concatenation is happening with the help of +
print(w + e)
