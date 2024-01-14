from calculator_art import logo
import os

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)

    num1 = float(input("What is the first number? : "))
    should_go_on = True

    while should_go_on:

        for operation in operations:
            print(operation)
        
        operation_symbol = input("Pick an operation. ")
        calculator_function = operations[operation_symbol]
        num2 = float(input("What is the next number? : "))

        result = calculator_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")

        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation. ") == 'y':
            num1 = result
        else:
            os.system("clear")
            should_go_on = False
            calculator()

calculator()