#--- Classes and Objects ---#
#
## Subjects:
#
# Question 1:
# Create a class called 'Person' that has three instance variables: 'name', 'age', and 'favorite_color'. 
# Include a method called 'introduce' that prints a message introducing the person, such as "Hello, my 
# name is [name], I am [age] years old, and my favorite color is [favorite_color]."
#
# Question 2:
# Write a class named 'Circle' with an attribute 'radius' and methods to calculate the area and 
# circumference of the circle. Use the formula pi*r^2 for the area and 2*pi*r for the circumference.
#
# Question 3:
# Create a class called 'BankAccount' that has attributes for the account holder's name, account balance,
# and account number. Include methods to deposit and withdraw money from the account, as well as a method 
# to display the account details.

# Question 1:

class Person:

    def __init__(self, name:str, age:int, favorite_color:str) -> None:
        """
        Initiates the object with the required attributes.

        Args:
            - name : str
            - age : int
            - favorite_color : str

        Returns:
            - None
        """
        
        self.name = name
        self.age = age
        self.favorite_color = favorite_color

    def introduce(self) -> None:
        """
        Introduces the person.

        Args:
            - None
        
        Returns:
            - None
        """
        
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and my favorite color is {self.favorite_color}")

# Test cases
p1 = Person("John", 25, "blue")
p2 = Person("Alice", 65, "red")
p3 = Person("Deea", 12, "violet")

p1.introduce()
p2.introduce()
p3.introduce()

# Question 2:

import math

class Circle:

    def __init__(self, radius: float) -> None:
        """
        Initiates the object with the required attributes.

        Args:
            - radius : float

        Returns:
            - None
        """
        
        self.radius = radius

    def calculate_circumference(self) -> float:
        """
        Calculates the circumference of the object 'Circle'.

        Args:
            - None
        
        Returns:
            - float : The circumference of the circle
        """

        return 2* math.pi * self.radius
    
    def calculate_area(self) -> float:
        """
        Calculates the area of the object 'Circle'.

        Args:
            - None
        
        Returns:
            - float : The area of the circle
        """

        return math.pi * self.radius ** 2
    
# Test cases:

c1 = Circle(13.4)
c2 = Circle(25.4)
c3 = Circle(345.4)

print(c1.calculate_area())
print(c2.calculate_area())
print(c3.calculate_area())
print(c1.calculate_circumference())
print(c2.calculate_circumference())
print(c3.calculate_circumference())

# Question 3:

class BankAccount:

    def __init__(self, name:str, balance:float, number:int) -> None:
        """
        Initiates the object with the required attributes.

        Args:
            - name : str
            - balance : float
            - number : int

        Returns:
            - None
        """
    
        self.name = name
        self.balance = balance
        self.number = number

    def display_account_details(self) -> None:
        """
        Displays the account details of a person.

        Args:
            - None

        Returns:
            - None
        """

        print(f"Hello {self.name}, your account with the number {self.number} has the balance : ${self.balance}")
    
    def deposit(self, sum: float) -> None:
        """
        Deposits a sum of money in the account balance.

        Args:
            - sum : float
        
        Returns:
            - None
        """
        
        if sum > 0:
            self.balance += sum
            print(f"Deposit successful! You have currently the balance of ${self.balance}.")
        else:
            raise ValueError("The sum that you are trying to deposit is invalid!")
        
    def withdraw(self, sum: float) -> None:
        """
        Withdraws money from the account balance.

        Args:
            - sum : float

        Returns:
            - None
        """

        if sum < 0:
            raise ValueError(f"The sum should be positive!")

        if sum <= self.balance:
            self.balance -= sum
            print(f"You have withdrew ${sum}!")
        else:
            print(f"Your account balance is lower than the sum of {sum}")
        
# Test cases:

acc = BankAccount("John", 300.5, 8765123585)

acc.display_account_details()
acc.deposit(345.5)
acc.withdraw(1000)
acc.withdraw(200)
acc.display_account_details()

## Corrections:

# Question 1:
# Your implementation of the Person class is correct and functional. It's clean and well-documented. No 
# improvements are needed.

# Question 2:
# Your implementation of the Circle class is correct and efficient. The code is well-structured and 
# well-documented. No improvements are needed.

# Question 3:
# Your implementation of the BankAccount class is excellent. You've covered all the necessary methods and 
# handled edge cases well. Here's a slightly improved version with more concise error handling:

class BankAccount:

    def __init__(self, name: str, balance: float, number: int) -> None:
        """
        Initiates the object with the required attributes.

        Args:
            - name : str
            - balance : float
            - number : int

        Returns:
            - None
        """
        self.name = name
        self.balance = balance
        self.number = number

    def display_account_details(self) -> None:
        """
        Displays the account details of a person.

        Args:
            - None

        Returns:
            - None
        """
        print(f"Hello {self.name}, your account with the number {self.number} has the balance : ${self.balance}")
    
    def deposit(self, sum: float) -> None:
        """
        Deposits a sum of money in the account balance.

        Args:
            - sum : float
        
        Returns:
            - None
        """
        if sum > 0:
            self.balance += sum
            print(f"Deposit successful! Your new balance is ${self.balance}.")
        else:
            raise ValueError("The sum that you are trying to deposit is invalid!")
        
    def withdraw(self, sum: float) -> None:
        """
        Withdraws money from the account balance.

        Args:
            - sum : float

        Returns:
            - None
        """
        if sum <= 0:
            raise ValueError("The sum should be positive!")

        if sum <= self.balance:
            self.balance -= sum
            print(f"You have withdrawn ${sum}!")
        else:
            print(f"Your account balance is lower than the sum of ${sum}.")
