# -----------------------------------------------------------------------------
# Script Name: utf8_encode_decode.py
# Description: Script to encode and decode UTF-8 characters.
#
# Author: Dominik B.
#
# Press CTRL+R to run the script
# -----------------------------------------------------------------------------


# Import libraries
from ti_system import *


# Functions
def encode_utf8(char):
    """Encode a single character to UTF-8."""
    code_point = ord(char)
    if code_point < 0x80:  # 1-byte characters
        return [code_point]
    if code_point < 0x800:  # 2-byte characters
        return [0b11000000 | (code_point >> 6), 0b10000000 | (code_point & 0b00111111)]
    if code_point < 0x10000:  # 3-byte characters
        return [
            0b11100000 | (code_point >> 12),
            0b10000000 | ((code_point >> 6) & 0b00111111),
            0b10000000 | (code_point & 0b00111111),
        ]
    return [
        0b11110000 | (code_point >> 18),
        0b10000000 | ((code_point >> 12) & 0b00111111),
        0b10000000 | ((code_point >> 6) & 0b00111111),
        0b10000000 | (code_point & 0b00111111),
    ]


def decode_utf8(bytes_array):
    """Decode a list of bytes to a UTF-8 character."""
    if len(bytes_array) == 1:
        return chr(bytes_array[0])
    if len(bytes_array) == 2:
        return chr(((bytes_array[0] & 0b00011111) << 6) | (bytes_array[1] & 0b00111111))
    if len(bytes_array) == 3:
        return chr(
            ((bytes_array[0] & 0b00001111) << 12)
            | ((bytes_array[1] & 0b00111111) << 6)
            | (bytes_array[2] & 0b00111111)
        )
    if len(bytes_array) == 4:
        return chr(
            ((bytes_array[0] & 0b00000111) << 18)
            | ((bytes_array[1] & 0b00111111) << 12)
            | ((bytes_array[2] & 0b00111111) << 6)
            | (bytes_array[3] & 0b00111111)
        )
    return None


# Main
VALID_INPUT = True
while True:
    clear_history()

    if not VALID_INPUT:
        print("Enter valid input..")

    action = input("Do you want to (e)ncode or (d)ecode? ")
    if action.lower() == "e":
        char = input("Enter (only one) character to encode: ")
        if len(char) != 1:
            VALID_INPUT = False
            continue

        encoded = encode_utf8(char)
        print("Encoded bytes:", ["{0:08b}".format(byte) for byte in encoded])
    elif action.lower() == "d":
        print("You can only input bytes for a single character")
        byte_str = input("Enter bytes to decode (space-separated, binary): ")

        if not (byte_str.isdigit() and all(char in "01" for char in byte_str)):
            continue

        bytes_list = [int(b, 2) for b in byte_str.split()]
        decoded = decode_utf8(bytes_list)
        print("Decoded character:", decoded)
    else:
        VALID_INPUT = False
        continue

    if input("Try again? (y/n): ").lower() != "y":
        break
    VALID_INPUT = True
