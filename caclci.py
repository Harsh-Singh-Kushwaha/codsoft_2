5

def calculator():

    Number1 = float(input("Enter the first number: "))
    operator = input("Enter the operation (+, -, *, /): ")
    number2 = float(input("Enter the second number: "))

    if operator == '+':
        result = Number1 + number2
        print(f"The result is: {result}")
    elif operator == '-':
        result = Number1 - number2
        print(f"The result is: {result}")
    elif operator == '*':
        result = Number1 * number2
        print(f"The result is: {result}")
    elif operator == '/':
        if number2 != 0:
            result = Number1 / number2
            print(f"The result is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please use +, -, *, or /.")

calculator()
