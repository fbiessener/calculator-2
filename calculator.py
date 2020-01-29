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

    user_input = input("")

    tokens = user_input.split(" ")

    count = 0

    # if 2 or fewer tokens
    if len(tokens) <= 2:
        return "Not enough inputs"

    while count < len(tokens):
        # quits
        if tokens[0] == "q":
            break

        # This solves addition inputs
        elif tokens[0] == "+":
            return (add(float(tokens[1]), float(tokens[2])))

        # This solves subtraction inputs
        elif tokens[0] == "-":
            return (subtract(float(tokens[1]), float(tokens[2])))


        # This solves multiply inputs
        elif tokens[0] == "*":
            return (multiply(float(tokens[1]), float(tokens[2])))


        # This solves divide inputs
        elif tokens[0] == "/":
            return (divide(float(tokens[1]), float(tokens[2])))


        # This solves square inputs
        elif tokens[0] == "square":
            return (square(float(tokens[1])))


        # This solves cube inputs
        elif tokens[0] == "cube":
            return (cube(float(tokens[1])))

        # This solves pow inputs
        elif tokens[0] == "pow":
            return (pow(float(tokens[1]), float(tokens[2])))

        # This solves mod inputs
        elif tokens[0] == "mod":
            return (mod(float(tokens[1]), float(tokens[2])))

        else:
            return "Please enter an operator followed by two integers"


        count += 1


calculator()

