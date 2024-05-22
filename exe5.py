my_name = "Zed A. Shaw"
my_age = 35
my_height = 74
my_weight = 180
my_eyes = "Blue"
my_teeth = "white"
my_hair = "Brown"

# used format string mechanism for to embed variables inside a string
print(f"Lets talk about {my_name}")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy")
print(f"Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# performed addition and assigned that result to a new variable called "total"
total = my_age + my_height + my_weight

# printed using format string mechanism
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")
