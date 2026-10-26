# Question 1: Variable Assignment and String Manipulation


name = input ("please insert your name:")

# TODO: Ask the user for their age and store it in a variable
age = input ("please insert your age:")
# TODO: Print a greeting using the name and age variables
print (f"hi {name} you are {age} years old")


#------------------------------------------------------------------------------------
# Question 2: Integer Operations

# TODO: Ask the user for the length of a rectangle and store it as an integer
length = int(input ("enter the length:"))
# TODO: Ask the user for the width of a rectangle and store it as an integer
width = int (input ("enter the width:" ))
# TODO: Calculate the area of the rectangle
area = length * width
# TODO: Print the result
print ("area:" ,area)
#------------------------------------------------------------------------------------
# Question 3: Working with Floats

# TODO: Ask the user for a temperature in Celsius and store it as a float
celsius = 20.01
# TODO: Convert the temperature to Fahrenheit using the formula: (C * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32
# TODO: Print the result rounded to two decimal places
print (fahrenheit, round(fahrenheit, 2 ))
