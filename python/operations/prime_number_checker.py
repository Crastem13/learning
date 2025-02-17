# Prime Number Checker

## Definition:
# A prime number is a natural number greater than 1 that has no positive divisors other 
# than 1 and itself. In other words, a prime number ( p ) is a number that cannot be 
# formed by multiplying two smaller natural numbers.

## Objective: 
# Create a program that checks if a given number is a prime number.

## Requirements:
# 1. Create a function called is_prime that takes a single parameter n.
# 2. Check if n is a prime number.
# 3. Return True if n is prime, otherwise return False.
# 4. Write a few test cases to demonstrate the functionality of your prime number checker.

import math

def is_prime(n: int) -> bool:
    """
    Check if a given number is a prime number.
    
    Args:
        - n : int
    """

    # check if the argument is a positive integer, greater than 1
    if not isinstance(n, int) or n <= 1:
        raise ValueError("The argument is not a positive Integer greater than 1!")
    
    # check if n is divisible by any number other than 1 and itself
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False

    #-----------------------------------------#
    # Optimized prime-checking algorithm
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    # END - Optimized prime-checking algorithm
    #-----------------------------------------#

    # if no divisors other than 1 and n are found, n is a prime number
    return True

# Test cases
print(is_prime(2))    # Expected output: True
print(is_prime(9))    # Expected output: False
print(is_prime(71))    # Expected output: True
print(is_prime(51))    # Expected output: False
#print(is_prime(-32))    # Expected output: ValueError
#print(is_prime(1))    # Expected output: ValueError
#print(is_prime(0))    # Expected output: ValueError

# Positives:
# 1. Function Definitions: Clear and concise function definitions with proper docstrings.
# 2. Error Handling: Proper error handling for non-integer and non-positive inputs.
# 3. Logic: The logic to check if a number is prime is well-implemented.
# 4. Test Cases: Including test cases to demonstrate functionality is excellent.

# Suggestions for Improvement:
# 1. Optimize Prime Check: You can optimize the prime-checking algorithm by reducing the 
# number of iterations in the loop. Instead of checking up to n // 2 + 1, you can check up 
# to the square root of n. This optimization will reduce the time complexity of the 
# algorithm.
# 2. Additional Edge Cases: Consider handling edge cases, such as negative numbers and 1, 
# separately.