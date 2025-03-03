# Temperature Converter

## Definition:
# Celsius to Fahrenheit => F = C * 9/5 + 32
# Fahrenheit to Celsius => C = (F - 32) * 5/9

## Objective:
# Create a program that converts temperatures between Celsius and Fahrenheit.

## Requirements:
# 1. Create a function called 'celsius_to_fahrenheit' that takes a single parameter celsius and converts it to Fahrenheit.
# 2. Create a function called 'fahrenheit_to_celsius' that takes a single parameter fahrenheit and converts it to Celsius.
# 3. Write a few test cases to demonstrate the functionality of your temperature converter.

def celsius_to_fahrenheit(temp: float) -> float:
    """
    Converts the celsius temperature to fahrenheit.

    Args:
        - temp : float

    Returns:
        - temp : Temperature converted in fahrenheit 
    """

    if (not isinstance(temp, float) and not isinstance(temp, int)) or temp < -273.15:
        raise ValueError("The temperature must be a number and above the minimum -273.15 degrees!")

    return (temp * 9/5) + 32

def fahrenheit_to_celsius(temp: float) -> float:
    """
    Coverts the fahrenheit temperature to celsius.

    Args:
        - temp : float
    
    Returns:
        - temp : Temperature converted in celsius.
    """

    if (not isinstance(temp, float) and not isinstance(temp, int)) or temp < -459.67:
        raise ValueError("The temperature must be a number and above the minimum -459.67 degrees!")

    return (temp - 32) * 5/9

# Test cases
print(celsius_to_fahrenheit(0))    # Expected output: 32.0
print(celsius_to_fahrenheit(100))  # Expected output: 212.0
print(fahrenheit_to_celsius(32))   # Expected output: 0.0
print(fahrenheit_to_celsius(212))  # Expected output: 100.0

# Positives:
# 1. Function Definitions: Clear and concise function definitions with proper docstrings.
# 2. Error Handling: Proper error handling for non-numeric and invalid temperature inputs.
# 3. Logic: The logic to convert between Celsius and Fahrenheit is well-implemented.
# 4. Test Cases: Including test cases to demonstrate functionality is excellent.

# Suggestions for Improvement:
# 1. Simplify Type Checking: You can simplify the type checking by using isinstance directly with a tuple:
# if not isinstance(temp, (float, int)) or temp < -273.15
#
# 2. Docstrings: Ensure the docstrings are clear and consistent. They are already well-written, but a slight 
# modification can enhance clarity.
# def celsius_to_fahrenheit(temp: float) -> float:
#     """
#     Converts the Celsius temperature to Fahrenheit.

#     Args:
#         temp (float): Temperature in Celsius.

#     Returns:
#         float: Temperature converted to Fahrenheit.
#     """
#     if not isinstance(temp, (float, int)) or temp < -273.15:
#         raise ValueError("The temperature must be a number and above the minimum -273.15 degrees!")

#     return (temp * 9/5) + 32

# def fahrenheit_to_celsius(temp: float) -> float:
#     """
#     Converts the Fahrenheit temperature to Celsius.

#     Args:
#         temp (float): Temperature in Fahrenheit.

#     Returns:
#         float: Temperature converted to Celsius.
#     """
#     if not isinstance(temp, (float, int)) or temp < -459.67:
#         raise ValueError("The temperature must be a number and above the minimum -459.67 degrees!")

#     return (temp - 32) * 5/9