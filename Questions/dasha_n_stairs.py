# Inputs and type casting
a = int(raw_input("Enter steps (a) : "))
b = int(raw_input("Enter steps (b) : "))

# Logic 

if a is b or abs(a - b) is 0:  # To be able to climb the stairs the difference must be either absolute 1 or they are same
    print("yes")
else:  # else the case won't exist at all
    print("no")

