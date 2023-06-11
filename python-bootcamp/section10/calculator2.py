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

print(logo)
num1 = int(input("What's the first number?: "))
print("+\n-\n*\n/")
operation_symbol = input("pick an operator: ")
num2 = int(input("What's the next number?: "))

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
