import string

def remove_punctuation(text: str) -> str:
    """
    Removes all the punctuation from a string. It uses the string library and a translator.

    Args:
        - text : string
    """
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

def is_palindrome(text: str) -> bool:
    """
    Checks if a text is a palindrome or not. 

    Args:
        - text : str
    """

    if not isinstance(text, str):
        raise ValueError("The argument is not a String!")

    text = str.lower(text) # lowercase the str
    text = remove_punctuation(text) # remove the punctuation
    text = ''.join(text.split()) # removes all the spaces

    # compare the first half of str with the second half of it inversed
    for i in range(len(text) // 2):
        if text[i] != text[-i-1]:
            return False
    return True
    # return text == text[::-1]

# Test cases
print(is_palindrome("A man, a plan, a canal: Panama"))  # Expected output: True
print(is_palindrome("racecar"))  # Expected output: True
print(is_palindrome("hello"))  