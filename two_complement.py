# -----------------------------------------------------------------------------
# Script Name: dec_to_oct.py
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
def two_complement_to_dec(bin_str):
	if bin_str[0] == '0':  # positive number
		return int(bin_str, 2)
	else:
		return -((1 << len(bin_str)) - int(bin_str, 2))

# Main
valid_input = ""
while True:
	clear_history()

	input_str = input("Enter " + valid_input + " decimal number: ")
	if not (input_str.isdigit() and all(char in '01' for char in input_str)):
		valid_input = "valid"
		continue

	print("Decimal:", two_complement_to_dec(input_str))

	if input("Rerun code? (y) ").lower() != "y":
		break
