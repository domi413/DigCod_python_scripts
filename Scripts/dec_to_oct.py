# -----------------------------------------------------------------------------
# Script Name: dec_to_oct.py
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
def dec_to_oct(dec_num):
    return str(oct(int(dec_num))[2:])


# Main
VALID_INPUT = ""
while True:
    clear_history()

    input_str = input("Enter " + VALID_INPUT + " decimal number: ")
    if not input_str.isdigit():
        VALID_INPUT = "valid"
        continue

    print("Decimal:", dec_to_oct(input_str))

    if input("Rerun code? (y) ").lower() != "y":
        VALID_INPUT = ""
        break
