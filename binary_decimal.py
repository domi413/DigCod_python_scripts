# -----------------------------------------------------------------------------
# Script Name: binary_decimal.py
# Description: Script to calculate the floating dot decimal out of a decimal comma number
#
# Author: Dominik B.
# Created: 09.03.2024
# Version: 1.0
#
# press ctrl+r to run the script
#
# How to save the script on Handheld:
# 1. Connect the Handheld to the computer
# 2. Open the TI-Nspire Students software
# 3. Create new python script
# 4. File -> Save to Handheld
#
# or another option...
# 1. open chrome (yeah you must use chrome..)
# 2. go to https://nspireconnect.ti.com/nsc/
# 3. -> transfer file
#
# -----------------------------------------------------------------------------

# Import libraries
from math import *
from ti_system import *

# Functions
def decimal_to_binary_with_point(decimal_number, precision):
	# Split the number into its integer and fractional part
	integer_part = int(decimal_number)
	fractional_part = decimal_number - integer_part

	# Convert the integer part to binary
	binary_integer_part = bin(integer_part).replace('0b', '')

	# Convert the fractional part to binary
	fractional_bits = []
	while fractional_part > 0 and len(fractional_bits) < precision:
		fractional_part *= 2
		bit = int(fractional_part)
		fractional_bits.append(str(bit))
		fractional_part -= bit

	# Combine both parts
	binary_fractional_part = ''.join(fractional_bits)

	# Add a space every 4 bits for integer part
	spaced_integer_part = ' '.join([binary_integer_part[i:i+4] for i in range(0, len(binary_integer_part), 4)])

	# Add a space every 4 bits for fractional part
	spaced_fractional_part = ' '.join([binary_fractional_part[i:i+4] for i in range(0, len(binary_fractional_part), 4)])

	return spaced_integer_part + '.' + spaced_fractional_part


# Main
while True:
	clear_history()

	valid_input = ""
	while True:
		try:
			input_number = float(input("Enter a " + valid_input + " decimal number: "))
			if input_number < 0:
				valid_input = "valid"
				continue
			break
		except ValueError:
			valid_input = "valid"
			continue

	valid_input = ""
	while True:
		try:
			input_precision = int(input("Enter " + valid_input + " precision of datatype: "))
			if input_precision < 0:
				valid_input = "valid"
				continue
			break
		except ValueError:
			valid_input = "valid"
			continue

	print(decimal_to_binary_with_point(input_number, input_precision))

	if input("Rerun code? (y) ").lower() != "y":
		break
