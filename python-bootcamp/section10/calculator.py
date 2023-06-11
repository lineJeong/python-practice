from calculator_art import logo
import os


def calculator(first_number, operation, next_number):
    if operation == "+":
        return first_number + next_number
    elif operation == "-":
        return first_number - next_number
    elif operation == "*":
        return first_number * next_number
    elif operation == "/":
        return first_number / next_number

while True:
    print(logo)
    first_number = float(input("What's the first number?: "))
    print("+\n-\n*\n/")

    sholud_continue = True

    while sholud_continue == True:
        operation = input("pick an operator: ")
        next_number = float(input("What's the next number?: "))

        result = calculator(first_number, operation, next_number)
        print(result)

        continue_answer = input(
            f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation: ")

        if continue_answer == "y":
            first_number = result

        if continue_answer == "n":
            os.system('clear')
            sholud_continue = False
