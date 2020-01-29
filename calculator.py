"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

# psuedocode
# repeat forever:
#    read input
#    tokenize input
#    if the first token is "q":
#        quit
#    else:
#        decide which math function to call based on first token


def calculator():
    count = 0

    while True:

        user_input = input("")
        tokens = user_input.split(" ")

        # quits
        if tokens[0] == "q":
            break

        # if 2 or fewer tokens
        if len(tokens) <= 2:
            print("Not enough inputs")

        # This solves addition inputs
        elif tokens[0] == "+":
            print(add(float(tokens[1]), float(tokens[2])))

        # This solves subtraction inputs
        elif tokens[0] == "-":
            print(subtract(float(tokens[1]), float(tokens[2])))


        # This solves multiply inputs
        elif tokens[0] == "*":
            print(multiply(float(tokens[1]), float(tokens[2])))


        # This solves divide inputs
        elif tokens[0] == "/":
            print(divide(float(tokens[1]), float(tokens[2])))


        # This solves square inputs
        elif tokens[0] == "square":
            print(square(float(tokens[1])))


        # This solves cube inputs
        elif tokens[0] == "cube":
            print(cube(float(tokens[1])))

        # This solves pow inputs
        elif tokens[0] == "pow":
            print(pow(float(tokens[1]), float(tokens[2])))

        # This solves mod inputs
        elif tokens[0] == "mod":
            print(mod(float(tokens[1]), float(tokens[2])))

        else:
            print("Please enter an operator followed by two integers")


        count += 1


calculator()

