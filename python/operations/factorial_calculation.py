# Factorial Calculation

## Definition:
# The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.

## Objective:
# Create a program that calculates the factorial of a given number.

# Requirements:
# 1. Create a function called factorial that takes a single parameter n.
# 2. Calculate the factorial of n using a loop or recursion.
# 3. Return the factorial of n.
# 4. Write a few test cases to demonstrate the functionality of your factorial calculator.

def factorial(n: int) -> int:
    """
    Calculate the factorial of a given number.
    
    Args:
        - n : int

    Returns:
        - int : The factorial of n
    """
    # check if the argument is a positive integer
    if not isinstance(n, int) or n < 0:
        raise ValueError("The argument is not a positive Integer!")
    
    # handle the base case when n = 0 or n = 1
    if n == 0 or n == 1:
        return 1
    
    # calculate the factorial of n
    fact = 1

    for i in range(1, n+1):
        fact *= i

    return fact

# Test cases
print(factorial(0))   # Expected output: 1
print(factorial(1))   # Expected output: 1
print(factorial(2))   # Expected output: 2
print(factorial(5))   # Expected output: 120
print(factorial(10))   # Expected output: 3628800
print(factorial(-20))   # Expected output: ValueError
print(factorial("24"))   # Expected output: ValueError

# Positives:
# 1. Function Definitions: Clear and concise function definitions with proper docstrings.
# 2. Error Handling: Proper error handling for non-integer and negative inputs.
# 3. Logic: The logic to calculate the factorial using a loop is well-implemented.
# 4. Test Cases: Including test cases to demonstrate functionality is excellent.

# Suggestions for Improvement:
# 1. Consistent Naming Conventions: While the naming is clear, sticking to a consistent 
# style without spaces between function names and parentheses can be more conventional:
# def factorial(n: int) -> int:

# 2. Type Hints in Docstrings: It's great to have type hints in the function signature. 
# For completeness, you might want to also include them in the docstring.

# 3. Returning Type: Ensure the return type is indicated in the docstring as well:
# """
# Calculate the factorial of a given number.
#
# Args:
#     n (int): The number to calculate the factorial for.
#
# Returns:
#     int: The factorial of the number.
# """