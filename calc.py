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

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\nSelect an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operation = int(input("Enter the number corresponding to your desired operation: "))

result = 0

if operation == 1:
    result = addition(num1, num2)
elif operation == 2:
    result = subtraction(num1, num2)
elif operation == 3:
    result = multiplication(num1, num2)
elif operation == 4:
    result = division(num1, num2)
else:
    print("Invalid operation selected.")

print("The result is:", result)