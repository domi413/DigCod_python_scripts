# -----------------------------------------------------------------------------
# Script Name: multiplicative_inverse.y
# Description: Takes two number a and b as input and returns the
#               multiplicative inverse
#
# Author: Dominik B.
#
# press ctrl+r to run the script
#
# -----------------------------------------------------------------------------

# Import libraries
from ti_system import *


def extended_euclidean_table_print(a, b):
    # Initialize lists and variables
    init_x = 0
    init_y = 1
    r = a
    table = []

    while r > 0:
        q = a // b
        r = a - b * q

        table.append([a, b, q, r, init_x, init_y])

        a = b
        b = r

    for i in range(1, len(table)):
        q = table[len(table) - 1 - i][2]
        x = table[i - 1][5]
        y = table[i - 1][4] - q * table[i - 1][5]

        table[i][4] = x
        table[i][5] = y

    # Invert the values in rows 4 and 5 (x and y)
    x_values = [row[4] for row in table]
    y_values = [row[5] for row in table]
    x_values.reverse()
    y_values.reverse()

    # Reassign the reversed values back to the table rows
    for idx, row in enumerate(table):
        row[4] = x_values[idx]
        row[5] = y_values[idx]

    # Print table

    print("_________________________")
    print("i   a   b   q   r   x   y")
    for i, row in enumerate(table, 1):
        print(
            "{:<5}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}".format(
                i, row[0], row[1], row[2], row[3], row[4], row[5]
            )
        )
    # Nspire can't handle tabs...
    # print("___________________________")
    # print("i\ta\tb\tq\tr\tx\ty")
    # for i, row in enumerate(table, 1):
    #     print(
    #         str(i)
    #         + "\t"
    #         + str(row[0])
    #         + "\t"
    #         + str(row[1])
    #         + "\t"
    #         + str(row[2])
    #         + "\t"
    #         + str(row[3])
    #         + "\t"
    #         + str(row[4])
    #         + "\t"
    #         + str(row[5])
    #     )


def extended_euclidean(a, b):
    # a is phi(n), b is the key
    x, last_x = 0, 1
    while a != 0:
        q = b // a
        b, a = a, b % a
        x, last_x = last_x - q * x, x
    return last_x


# Main
VALID_INPUT = ""
while True:
    clear_history()

    a = int(input("Enter " + VALID_INPUT + " number a (greater value): "))
    b = int(input("Enter " + VALID_INPUT + " number b: "))

    if b > a:
        VALID_INPUT = "valid"
        continue

    inverse = extended_euclidean(a, b) % a

    print(
        "The multiplicative inverse of "
        + str(a)
        + " and "
        + str(b)
        + " is: "
        + str(inverse)
    )

    if input("Print table? (y) ").lower() == "y":
        extended_euclidean_table_print(a, b)

    if input("Rerun code? (y) ").lower() != "y":
        VALID_INPUT = ""
        break
