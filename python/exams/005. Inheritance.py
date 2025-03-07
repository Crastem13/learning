# Inheritance
#
# Question 1: Create a base class called Vehicle with attributes make, model, and year, 
# and a method display_info to print these details. Then, create a subclass called Car 
# that adds an attribute number_of_doors. Override the display_info method in Car to 
# include the number of doors.
#
# Question 2: Write a base class called Shape with a method calculate_area, which raises 
# a NotImplementedError (since each shape will implement this differently). Create two 
# subclasses, Rectangle and Triangle, which override calculate_area to compute and return 
# the area based on appropriate formulas.
#
# Question 3: Create a base class called BankAccount with attributes account_holder and 
# balance. Include methods for depositing, withdrawing, and displaying balance. Then, 
# create a subclass SavingsAccount that adds an attribute interest_rate. Add a method 
# in SavingsAccount to calculate the balance after applying interest for a given period 
# (in years).

# Question 1

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"The vehicle has the following details:\n- make: {self.make};\n- model: {self.model};\n- year: {self.year}")

class Car(Vehicle):
    def __init__(self, number_of_doors):
        self.number_of_doors = number_of_doors

    def display_info(self):
        return super().display_info()