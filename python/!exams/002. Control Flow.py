#--- Control Flow ---#

## Subjects:
#
# 1. Question 1:
# Write a Python program that takes an integer input from user and determines whether it 
# is odd or even. Print a message indicating the result.
#
# 2. Question 2:
# Create a script that prompts the user to enter a number between 1 and 10. If the number 
# is within the range, print a success message. If not, ask the user to enter a valid 
# number until they do so.
#
# 3. Question 3:
# Write a program that simulates a simple number guessing game. The program should randomly 
# select a number between 1 and 100. The user should then try to guess the number, with the 
# program providing feedback on wheter each guess is too high, too low, or correct. The game 
# should continue until the user guesses the correct number or chooses to quit.

# Question 1:

user_input = int(input("Insert an integer number: "))

print(f"{user_input} is even!" if user_input % 2 == 0 else f"{user_input} is odd!")

# Question 2:

while True:
    user_input = int(input("Insert a number between 1 and 10: "))

    if user_input >= 1 and user_input <= 10:
        print("Success!")
        break
    else:
        print("Try again!")

# Question 3:

import random

number = random.randint(1, 100)

while True:
    guess = input("Guess the number which is between 1 and 100 or write 'quit' if you want to exit: ")

    if guess == "quit":
        print("Goodbye!")
        break

    try:
        guess = int(guess)
    except ValueError:
        print("Please insert a number between 1 and 100 or 'quit' in order to exit!")
        continue

    if guess < 1 or guess > 100:
        print("The number should be between 1 and 100! Try again!")
        continue

    if guess == number:
        print("You guessed the number! Good job!")
        break

    if guess > number:
        print("Too high! Try again!")
    
    if guess < number:
        print("Too low! Try again!")

## Corrections:
#
# Question 1:

user_input = int(input("Insert an integer number: "))

result = "even" if user_input % 2 == 0 else "odd"
print(f"{user_input} is {result}!")

# Question 2:

while True:
    user_input = int(input("Insert a number between 1 and 10: "))

    if 1 <= user_input <= 10:
        print("Success!")
        break
    else:
        print("Try again!")

# Question 3:

import random

number = random.randint(1, 100)

while True:
    guess = input("Guess the number between 1 and 100 or type 'quit' to exit: ")

    if guess.lower() == "quit":
        print("Goodbye!")
        break

    try:
        guess = int(guess)
        if 1 <= guess <= 100:
            if guess == number:
                print("You guessed the number! Good job!")
                break
            elif guess > number:
                print("Too high! Try again!")
            else:
                print("Too low! Try again!")
        else:
            print("The number should be between 1 and 100! Try again!")
    except ValueError:
        print("Please enter a valid number between 1 and 100 or 'quit' to exit!")
