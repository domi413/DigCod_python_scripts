# -----------------------------------------------------------------------------
# Script Name: modulo_calculator.py
# Description: Script to calculate the modulo of two numbers
#
# Author: Dominik B.
#
# press ctrl+r to run the script
#
# -----------------------------------------------------------------------------

# Import necessary libraries
from ti_system import *


# Functions
def evaluate_expression(expression):
    """Evaluate the expression where ** is used for exponentiation."""
    if "**" in expression:
        display_expr = expression.replace("**", "^")
    else:
        display_expr = expression
    try:
        result = eval(expression)
        return result, display_expr
    except Exception:
        return None, display_expr


def calculate_modulo(num1, num2):
    """Returns the modulo of num1 by num2."""
    return num1 % num2


# Main
VALID_INPUT = ""
while True:
    clear_history()

    print("You can use ** for x^n e.g. 4**3 = 4^3")
    input_num1_str = input(VALID_INPUT + "first number: ")
    evaluated_num1, display_num1 = evaluate_expression(input_num1_str)
    if evaluated_num1 is None:
        VALID_INPUT = "valid "
        continue

    input_num2_str = input(VALID_INPUT + "second number: ")
    evaluated_num2, display_num2 = evaluate_expression(input_num2_str)
    if evaluated_num2 is None or evaluated_num2 == 0:
        VALID_INPUT = "valid "
        continue

    result = calculate_modulo(evaluated_num1, evaluated_num2)
    print(input_num1_str + " % " + input_num2_str + " = " + str(result))

    if input("Rerun code? (y) ").lower() != "y":
        VALID_INPUT = ""
        break
