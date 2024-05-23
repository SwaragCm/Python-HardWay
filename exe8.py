# Create a variable and assign some values as placeholder in it for to insert values in future using .format()
formatter="{} {} {} {}"
#print the variable  by inserting values(via through .format()) respectively to the placeholders in our variable
print(formatter.format(1,2,3,4)) 
print(formatter.format("one","two","three","four"))
print(formatter.format(True,False,False,True))
print(formatter.format(formatter,formatter,formatter,formatter)) #this syntax is actually printing our variable values, here it is an empty placeholder {}
print(formatter.format(
    "try your","own text here","may be a poem","or a song about fear"
    ))