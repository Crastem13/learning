# Simple Text-Based Adventure Game

## Objective:
# Create a simple text-based adventure game that allows the player to navigate through a series of rooms.

## Requirements:
# 1. Create a class called Room that represents a room in the game.
# 2. Each room should have a name, description, and exits that lead to other rooms.
# 3. Create a class called Game that manages the player's navigation through the rooms.
# 4. Allow the player to navigate through the rooms by typing commands such as "go north," "go south," etc.
# 5. Write a few test cases to demonstrate the functionality of your game.

class Room:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.exits = {}

    def add_exit(self, direction: str, room):
        self.exits[direction] = room

    def get_exit(self, direction: str):
        return self.exits.get(direction)
    
    def __str__(self):
        return f"{self.name}: {self.description}"
    
class Game:
    def __init__(self, start_room: Room):
        self.current_room = start_room

    def play(self):
        print("Welcome to the text-based adventure game!")
        print("Type 'quit' to exit the game.")
        print(self.current_room)
    
        while True:
            command = input("Enter your command: ")
            if command == "quit":
                print("Thanks for playing!")
                break
            elif command.startswith("go "):
                direction = command.split()[1]
                next_room = self.current_room.get_exit(direction)
                if next_room:
                    self.current_room = next_room
                    print(self.current_room)
                else:
                    print("You cannot go that way. Try a different direction.")
            else:
                print("Invalid command. Try again.")

# Test cases
# Create rooms
kitchen = Room("Kitchen", "A room to cook and eat.")
bedroom = Room("Bedroom", "A room to sleep and relax.")
garden = Room("Garden", "A room with beautiful flowers and plants.")

# Connect rooms
kitchen.add_exit("north", bedroom)
bedroom.add_exit("south", kitchen)
bedroom.add_exit("east", garden)
garden.add_exit("west", bedroom)

# Start the game
game = Game(kitchen)
game.play()

# Positives:
# 1. Class Definitions: Clear and concise class definitions for Room and Game with proper initialization methods.
# 2. Game Logic: The logic for navigating through rooms and handling user input is well-implemented.
# 3. String Representation: Using the __str__ method for room descriptions enhances the user experience.
# 4. Test Cases: Including test cases to demonstrate functionality is excellent.

# Suggestions for Improvement:
# 1. Type Hints for Methods: Adding type hints for methods, such as the add_exit and get_exit methods in the Room 
# class, can improve code readability:
# def add_exit(self, direction: str, room: 'Room') -> None:
#     self.exits[direction] = room

# def get_exit(self, direction: str) -> 'Room':
#     return self.exits.get(direction)

# 2. Handling Invalid Commands: You might want to provide more user-friendly messages or help information for 
# invalid commands to improve the user experience.
# 3. Additional Features: Consider adding more features, such as items in rooms, inventory management, or more 
# complex interactions.

# Revised Code:

class Room:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.exits = {}

    def add_exit(self, direction: str, room: 'Room') -> None:
        self.exits[direction] = room

    def get_exit(self, direction: str) -> 'Room':
        return self.exits.get(direction)
    
    def __str__(self) -> str:
        return f"{self.name}: {self.description}"
    
class Game:
    def __init__(self, start_room: Room):
        self.current_room = start_room

    def play(self) -> None:
        print("Welcome to the text-based adventure game!")
        print("Type 'quit' to exit the game.")
        print(self.current_room)
    
        while True:
            command = input("Enter your command: ")
            if command == "quit":
                print("Thanks for playing!")
                break
            elif command.startswith("go "):
                direction = command.split()[1]
                next_room = self.current_room.get_exit(direction)
                if next_room:
                    self.current_room = next_room
                    print(self.current_room)
                else:
                    print("You cannot go that way. Try a different direction.")
            else:
                print("Invalid command. Try 'go [direction]' or 'quit'.")

# Test cases
# Create rooms
kitchen = Room("Kitchen", "A room to cook and eat.")
bedroom = Room("Bedroom", "A room to sleep and relax.")
garden = Room("Garden", "A room with beautiful flowers and plants.")

# Connect rooms
kitchen.add_exit("north", bedroom)
bedroom.add_exit("south", kitchen)
bedroom.add_exit("east", garden)
garden.add_exit("west", bedroom)

# Start the game
game = Game(kitchen)
game.play()
