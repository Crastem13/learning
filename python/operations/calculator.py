def calculator(num1, num2, operation):
    switcher = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y if y != 0 else "Division by 0 is not possible!",
    }

    if not isinstance(num1, int) or not isinstance(num2, int):
        raise ValueError("The argument is not a Integer!")

    func = switcher.get(operation, lambda x, y: "Invalid operation!")

    return func(num1, num2)

print(calculator(4, 5, "+"))
print(calculator(10, 5, "-"))
print(calculator(2, 3, "*"))
print(calculator(15, 5, "/"))
print(calculator(20, 0, "/"))
print(calculator(20, 0, "%"))