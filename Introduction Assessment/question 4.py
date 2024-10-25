# Ask the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask the user for an operation
operation = input("Enter an operation (+, -, *, /): ")

# Perform the operation and print the result
if operation == '+':
    result = num1 + num2
    print("The result is:", result)
elif operation == '-':
    result = num1 - num2
    print("The result is:", result)
elif operation == '*':
    result = num1 * num2
    print("The result is:", result)
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print("The result is:", result)
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operation. Please enter one of +, -, *, /")
