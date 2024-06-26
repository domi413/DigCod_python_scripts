# -----------------------------------------------------------------------------
# Script Name: any_complement.py
# Description: Script to convert a number in complement x
#               into another number in complement y
#
# Author: Dominik B.
#
# press ctrl+r to run the script
#
# -----------------------------------------------------------------------------

# Import libraries
from ti_system import *


# Functions
def is_valid_number(number, base):
    """Check if the number is valid in the given base"""
    try:
        int(number, base)
        return True
    except ValueError:
        return False


def convert_base(number, from_base, to_base):
    """Convert a number from base `from_base` to base `to_base`"""
    if from_base == to_base:
        return number

    # Convert from any base to decimal
    decimal_value = int(number, from_base)

    # Early return if target base is decimal
    if to_base == 10:
        return str(decimal_value)

    # Convert decimal to any other base
    if decimal_value == 0:
        return "0"

    digits = []
    while decimal_value:
        digits.append(int(decimal_value % to_base))
        decimal_value //= to_base

    # Creating base-n string representation
    if to_base <= 10:
        return "".join(str(x) for x in reversed(digits))
    # For bases greater than 10
    characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return "".join(characters[x] for x in reversed(digits))


# Main
VALID_INPUT = ""
while True:
    clear_history()

    inp_val = input("Enter " + VALID_INPUT + " number: ")
    inp_type = input("Enter " + VALID_INPUT + " complement of this number: ")
    out_type = input("Enter " + VALID_INPUT + " complement to convert to: ")

    if not (inp_type.isdigit() and out_type.isdigit()):
        VALID_INPUT = "valid"
        continue

    inp_type, out_type = int(inp_type), int(out_type)
    if not is_valid_number(inp_val, inp_type):
        VALID_INPUT = "valid"
        continue

    print(
        "Value in base "
        + str(out_type)
        + ": "
        + convert_base(inp_val, inp_type, out_type)
    )

    if input("Rerun code? (y) ").lower() != "y":
        VALID_INPUT = ""
        break
