def summarize(a, b):
    result = a + b
    return result


def subtraction(a, b):
    result = a - b
    return result


def multiplying(a, b):
    while True:
        if b == 0:
            print("Multiplying by ZERO 0.00 is ALWAYS ZERO 0.00!!!Are you ok?")
            b = float(input(f"Enter second number again with caution: "))
        else:
            result = a * b
            return result


def dividing(a, b):
    while True:
        if b == 0:
            print("Dividing by ZERO 0.00 is not permitted")
            b = float(input(f"Enter second number again with caution: "))
        else:
            result = a / b
            return result


while True:
    print("press 1 or type Adding")
    print("press 2 or type Subtraction")
    print("press 3 or type Multiplying")
    print("press 4 or type Dividing")
    print("press 5 or type Exit")
    user_input = input(f"Enter your choice: ").lower()

    if user_input == "exit" or user_input == "5":
        print("Bye,bye!!!")
        break

    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    if user_input == "adding" or user_input == "1":
        print(summarize(x, y))
    if user_input == "subtraction" or user_input == "2":
        print(subtraction(x, y))
    if user_input == "multiplying" or user_input == "3":
        print(multiplying(x, y))
    if user_input == "dividing" or user_input == "4":
        print(dividing(x, y))
