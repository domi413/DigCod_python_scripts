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
def dec_to_oct(dec_num):
	return str(oct(int(dec_num))[2:])


# Main
valid_input = ""
while True:
	clear_history()

	input_str = input("Enter " + valid_input + " decimal number: ")
	if not input_str.isdigit():
		valid_input = "valid"
		continue

	print("Decimal:", dec_to_oct(input_str))

	if input("Rerun code? (y) ").lower() != "y":
		break
