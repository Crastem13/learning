#--- Functions ---#
#
## Subjects:
#
# Question 1:
# Write a function called 'greet_user' that takes a user's name as an argument and prints a 
# greeting message, such as "Hello, [name]!".
#
# Question 2:
# Create a function named 'calculate_area' that takes the radius of a circle as an argument 
# and returns the area of the circle. Use the formula PI*R^2 (you can use math.pi for the 
# value of PI)
#
# Question 3:
# Write a function called 'is_prime' that takes a number as an argument and returns 'True' 
# if the number is a prime number, and 'False' otherwise.

# Question 1:
import random

def greet_user(name: str) -> str:
    """
    Greets the user.

    Args:
        - name : str

    Returns:
        - void
    """
    greets = ["Hello", "Greetings", "Hi"]

    rand = random.randint(0, 2)

    print(f"{greets[rand]}, {name}")

greet_user("John")
greet_user("Martin")
greet_user("Mike")

# Question 2:

import math

def calculate_area(radius: float) -> float:
    """
    Calculates the area of a circle.

    Args:
        - radius : float

    Returns:
        - The area of the circle rounded to 2 digits
    """

    return round(math.pi * (radius**2), 2)

print(calculate_area(10))
print(calculate_area(23.4))
print(calculate_area(1237))

# Question 3:

def is_prime(number: int) -> bool:
    """
    Checks if number is prime.

    Args:
        - number : int

    Returns:
        - Boolean value if prime or not
    """
    for i in range(2, number // 2):
        if number % i == 0:
            return False
    return True

print(is_prime(3))
print(is_prime(10))
print(is_prime(71))
print(is_prime(97))

## Corrections:

# Question 1:

# Your implementation of the greet_user function is correct and functional. One minor improvement 
# is to use the choice method from the random module, which is more concise:

import random

def greet_user(name: str) -> None:
    """
    Greets the user.

    Args:
        - name : str

    Returns:
        - void
    """
    greets = ["Hello", "Greetings", "Hi"]
    greeting = random.choice(greets)

    print(f"{greeting}, {name}!")

greet_user("John")
greet_user("Martin")
greet_user("Mike")

# Using random.choice() simplifies the random selection process.

# Question 2:

# Your implementation of the calculate_area function is correct and efficient. The code is already 
# well-written, and there's nothing to improve here:

import math

def calculate_area(radius: float) -> float:
    """
    Calculates the area of a circle.

    Args:
        - radius : float

    Returns:
        - The area of the circle rounded to 2 digits
    """
    return round(math.pi * (radius**2), 2)

print(calculate_area(10))
print(calculate_area(23.4))
print(calculate_area(1237))

# Question 3:

# Your is_prime function works for most cases, but there's a small issue: it doesn't handle edge cases 
# (like numbers less than 2) and can be optimized for efficiency. Here's an improved version:

def is_prime(number: int) -> bool:
    """
    Checks if number is prime.

    Args:
        - number : int

    Returns:
        - Boolean value if prime or not
    """
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

print(is_prime(3))
print(is_prime(10))
print(is_prime(71))
print(is_prime(97))

# This version optimizes the check for prime numbers and includes handling for edge cases.