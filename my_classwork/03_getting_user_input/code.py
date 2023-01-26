name = input("Enter your name: ")
print(name)

# the input method will only take strings - if you want to say, do math, you'll need to convert string to int or float

size_input = input("How big is your house (in square feet): ")
square_feet = int(size_input) #converts the string to int
square_meters = square_feet/ 10.8 #use the correct variable now that the string is an int
# below, the f string lets us print out a more comprehensive statement and the ':.2f' formatting syntax only shows up to two decimal places for the float
print(f"{square_feet} square feet is {square_meters:.2f} square_meters.") 

# Ask the user for their name. You can store this in a variable.
user_name = input("Please enter your name: ")
# Then, print "Hello, NAME", where NAME is the user's name
greeting = f"Hello, {user_name}!"
print(greeting)