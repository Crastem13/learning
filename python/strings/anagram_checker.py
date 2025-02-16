# Anagram Checker
#
# Description:
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.
#
# Objective : Create a program that checks if two strings are anagrams of each other.
#
# Requirements:
# 1. Create a function called is_anagram that takes two parameters str1 and str2.
# 2. Normalize the strings by converting them to lowercase and removing all non-alphanumeric 
# characters (e.g., punctuation, spaces).
# 3. Check if the sorted characters of both strings are equal.
# 4. Return True if the strings are anagrams, otherwise return False.
# 5. Write a few test cases to demonstrate the functionality of your anagram checker.


def remove_non_alphanumeric(text: str) -> str:
    """
    Removes all the non-alphanumeric characters from a string.

    Args:
        - text : str
    """
    return ''.join(char for char in text if char.isalnum())

def is_anagram(str1: str, str2:str) -> bool:
    """
    Check if two strings are anagrams of each other.

    Args:
        - str1 : str
        - str2 : str
    """
    # check if the arguments are strings
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("One of the arguments is not a String!")

    # convert the strings to lowercase
    str1 = remove_non_alphanumeric(str1.lower())
    str2 = remove_non_alphanumeric(str2.lower())

    # sort the strings and compare them
    return sorted(str1) == sorted(str2)

# Test cases
print(is_anagram("listen", "silent"))  # Expected output: True
print(is_anagram("triangle", "integral"))  # Expected output: True
print(is_anagram("hello", "world"))  # Expected output: False

# Positives:
# 1. Function Definitions: Clear and concise function definitions with proper docstrings.
# 2. Normalization: Good job converting strings to lowercase.
# 3. Logic: The logic to sort the strings and compare them is well-implemented.
# 4. Error Handling: Proper error handling for non-string inputs.

# Suggestions for Improvement:
#
# 1. Add more test cases to check the robustness of the function.
# 2. Remove Non-Alphanumeric Characters: Consider removing punctuation and spaces from the 
# strings before comparing them to account for cases where strings may have special characters 
# or spaces.