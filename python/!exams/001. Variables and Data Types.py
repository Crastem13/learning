#--- Variables and Data Types ---#
#
## Subjects
#
# 1. Question 1: Create a Python script that asks the user for their name, age, and favourite color. 
# Store these values in appropiately named variables, and then print a sentence that insorporates 
# all three pieces of information.
#
# 2. Question 2: Write a program that converts a given number of seconds to hours, minutes, and 
# seconds. For example, 3661 seconds should be converted to 1 hour, 1 minute, and 1 second.
#
# 3. Question 3: Create a script that takes two numbers as input from the user and prints their sum, 
# difference, product, and quotient.

# Question 1

name = input("Your name: ")
age = int(input("Your age: "))
fav_col = input("Your favourite color: ")

print(f"{name} is {age} years old and his favourite color is {fav_col}")

# Question 2

user_input = int(input("Enter the number of seconds: "))

if user_input > 60:
    seconds = user_input % 60
elif user_input < 60 or user_input >= 0:
    seconds = user_input
else:
    raise ValueError("The seconds should be a positive integer number!")

minutes = user_input // 60
hours = minutes // 60
minutes = minutes % 60

print(f"{user_input} seconds are equal to: {hours} hours, {minutes} minutes and {seconds} seconds.")

# Question 3

num1 = float(input("First number: "))
num2 = float(input("Second number: "))

print(f"The sum of {num1} with {num2} is {num1 + num2}")
print(f"The substraction of {num1} with {num2} is {num1 - num2}")
print(f"The product of {num1} with {num2} is {num1 * num2}")
print(f"The quotient of {num1} with {num2} is {num1 // num2}")

### Correction:

# Question 1:
# Your code is correct and works as expected. However, there's a small improvement you can make for 
# readability. Here's a revised version:

name = input("Your name: ")
age = int(input("Your age: "))
fav_col = input("Your favourite color: ")

print(f"{name} is {age} years old and their favourite color is {fav_col}.")

# I changed "his" to "their" for a more inclusive approach.

# Question 2:
# Your code handles the conversion correctly, but the logic for handling seconds and minutes can be 
# simplified. Here's an improved version:

user_input = int(input("Enter the number of seconds: "))

if user_input < 0:
    raise ValueError("The seconds should be a positive integer number!")

hours = user_input // 3600
minutes = (user_input % 3600) // 60
seconds = user_input % 60

print(f"{user_input} seconds are equal to: {hours} hours, {minutes} minutes, and {seconds} seconds.")

# This version calculates the hours, minutes, and seconds in a more straightforward manner.

# Question 3:
# Your code is mostly correct, but there's a small error in the quotient calculation. You should use the 
# '/' operator for division instead of the // operator, which performs integer division. Here's a 
# corrected version:

num1 = float(input("First number: "))
num2 = float(input("Second number: "))

print(f"The sum of {num1} and {num2} is {num1 + num2}")
print(f"The subtraction of {num1} and {num2} is {num1 - num2}")
print(f"The product of {num1} and {num2} is {num1 * num2}")
print(f"The quotient of {num1} and {num2} is {num1 / num2}")

# Using / ensures that the division result is a float.