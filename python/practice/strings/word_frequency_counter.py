import string

def remove_punctuation(text: str) -> str:
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

def word_frequency(text: str) -> dict:
    # Your code here
    
    text = str.lower(text) # convert to lowercase
    text = remove_punctuation(text) # remove punctuation
    text = text.split() # split the text
    word_dict = dict() # create a dictionary

    # iterate through the text and populate the dictionary
    for word in text:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1

    return word_dict

# Test cases
text = "Hello world! Hello everyone."
print(word_frequency(text))  # Expected output: {'hello': 2, 'world': 1, 'everyone': 1}

text = "Python is great. Python is fun."
print(word_frequency(text))  # Expected output: {'python': 2, 'is': 2, 'great': 1, 'fun': 1}