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
    continue_answer = ""
    sholud_continue = True
    result = 0

    print(logo)
    first_number = float(input("What's the first number?: "))
    print("+\n-\n*\n/")

    while sholud_continue == True:
        operation = input("pick an operator: ")
        next_number = float(input("What's the next number?: "))

        if continue_answer == "":
            result = calculator(first_number, operation, next_number)
        else:
            result = calculator(result, operation, next_number)

        print(result)

        continue_answer = input(
            "Type 'y' to continue calculating with 10.0, or type 'n' to start a new calculation: ")

        if continue_answer == "n":
            os.system('clear')
            sholud_continue = False
