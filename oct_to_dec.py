# -----------------------------------------------------------------------------
# Script Name: oct_to_dec.py
# Description: Script to convert a octal number into a decimal
#
# Author: Dominik B.
# Created: 09.03.2024
# Version: 1.0
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
valid_input = ""
while True:
	clear_history()

	input_str = input("Enter " + valid_input + " octal number: ")
	if not (input_str.isdigit() and all(char in '01234567' for char in input_str)):
		valid_input = "valid"
		continue

	print("Decimal:", oct_to_dec(input_str))

	if input("Rerun code? (y) ").lower() != "y":
		break
