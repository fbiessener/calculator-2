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


def calculator(input_str):
    tokens = input_str.split(" ")

    if tokens[0] == "+":
        return (add(int(tokens[1]), int(tokens[2]))


#calculator("+ 2 3")


# "Not enough inputs"
# "Please enter an operator followed by two integers"

# Your code goes here
