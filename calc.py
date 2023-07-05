
def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Cannot divide by zero."

print("Welcome to the Basic Calculator Program!")

while True:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue

    print("\nSelect an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    operation = input("Enter the number corresponding to your desired operation: ")

    if operation == '5':
        print("Exiting the calculator program. Goodbye!")
        break

    try:
        operation = int(operation)
    except ValueError:
        print("Invalid operation selected. Please enter a valid operation.")
        continue

    result = 0

    if operation == 1:
        result = addition(num1, num2)
    elif operation == 2:
        result = subtraction(num1, num2)
    elif operation == 3:
        result = multiplication(num1, num2)
    elif operation == 4:
        if num2 != 0:
            result = division(num1, num2)
        else:
            print("Error: Cannot divide by zero.")
            continue
    else:
        print("Invalid operation selected. Please try again.")
        continue

    print("The result is:", result)
