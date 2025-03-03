# Fibonacci Sequence

## Definition: 
# The Fibonacci sequence is a series of numbers in which each number (Fibonacci number) is the 
# sum of the two preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc.
#
# In mathematical terms, the sequence is defined by the recurrence relation:
# [ F(n) = F(n-1) + F(n-2) ]
#
# with seed values:
# [ F(0) = 0, \quad F(1) = 1 ]

## Objective: 
# Create a program that generates the Fibonacci sequence up to a specified number of terms.

# Requirements:
# 1. Create a function called fibonacci that takes a single parameter n (the number of terms).
# 2. Generate the Fibonacci sequence up to the nth term.
# 3. Return a list containing the Fibonacci sequence.
# 4. Write a few test cases to demonstrate the functionality of your Fibonacci sequence generator.

def fibonacci_sequence(n: int) -> list:
    """
    Generate the fibonacci sequence up to the nth term.
    
    Args:
        - n : int
    """

    # check if the argument is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("The argument is not a positive Integer!")

    # handle the base case when n = 1
    if n == 1: return [0]
    
    # initialize the fib_sequence list with the first two terms
    fib_sequence = [0, 1]

    # handle the case when n = 2
    if n == 2: return fib_sequence

    # generate the fibonacci sequence up to the nth term
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])

    return fib_sequence

# Test cases
# print(fibonacci_sequence(0))   # Expected output: [0]
print(fibonacci_sequence(1))   # Expected output: [0, 1]
print(fibonacci_sequence(2))   # Expected output: [0, 1, 1]
print(fibonacci_sequence(3))   # Expected output: [0, 1, 1, 2]
print(fibonacci_sequence(4))   # Expected output: [0, 1, 1, 2, 3]
print(fibonacci_sequence(10))  # Expected output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Positives:
# 1. Function Definitions: Clear and concise function definitions with proper docstrings.
# 2. Error Handling: Proper error handling for non-integer and non-positive inputs.
# 3. Logic: The logic to generate the Fibonacci sequence up to the nth term is well-implemented.
# 4. Test Cases: Including test cases to demonstrate functionality is excellent.

# Suggestions for Improvement:
# 1. Starting Sequence: Typically, the Fibonacci sequence starts with [0, 1] instead of [1, 1]. However, if [1, 1] is your intended starting point, that's perfectly fine.
# 2. Edge Cases: You might want to consider handling more edge cases, such as n = 0.