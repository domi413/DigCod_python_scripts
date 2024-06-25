# -----------------------------------------------------------------------------
# Script Name: oct_to_dec.py
# Description: Script to convert a octal number into a decimal
#
# Author: Dominik B.
#
# press ctrl+r to run the script
#
# -----------------------------------------------------------------------------

# Import libraries
from math import *

from ti_system import *


# Functions
def oct_to_dec(oct_str):
    return int(oct_str, 8)


# Main
VALID_INPUT = ""
while True:
    clear_history()

    input_str = input("Enter " + VALID_INPUT + " octal number: ")
    if not (input_str.isdigit() and all(char in "01234567" for char in input_str)):
        VALID_INPUT = "valid"
        continue

    print("Octal:", oct_to_dec(input_str))

    if input("Rerun code? (y) ").lower() != "y":
        VALID_INPUT = ""
        break
