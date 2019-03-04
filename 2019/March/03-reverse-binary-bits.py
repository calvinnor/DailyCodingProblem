# Problem

"""

Given a 32-bit integer,
return the number with its bits reversed.

For example, given the binary number
1111 0000 1111 0000 1111 0000 1111 0000, return
0000 1111 0000 1111 0000 1111 0000 1111.

Asked by: Facebook

"""


# Code Section


# Utility function to convert an integer to it's 32-bit binary representation
def to_binary(number: int) -> str:
    return '{:032b}'.format(number)


# Utility function to convert a binary number to int
def to_int(binary_number: str) -> int:
    return int(binary_number, 2)


def reverse_bits(number: int) -> int:
    """
    We need to extract each digit and build the resulting number.

    Python's bin(number) returns a String representation of the binary number
    We then simply reverse the digits and build the result.
    """

    # Ignore the 0b prefix
    number = bin(number)[2:]

    # Convert to a 32 bit number
    while len(number) < 32:
        number = '0' + number

    binary_number = ""

    for digit in number:
        if digit == '0':
            binary_number += '1'

        elif digit == '1':
            binary_number += '0'

    # Parse to an integer base 2
    return to_int(binary_number)


# Test Cases

# Example
assert to_binary(reverse_bits(to_int('11110000111100001111000011110000'))) == '00001111000011110000111100001111'

# More random tests
assert to_binary(reverse_bits(to_int('01000010100100001011110101111111'))) == '10111101011011110100001010000000'
assert to_binary(reverse_bits(to_int('11000100000000100101100000101010'))) == '00111011111111011010011111010101'
assert to_binary(reverse_bits(to_int('10000101110011111100111000110000'))) == '01111010001100000011000111001111'
assert to_binary(reverse_bits(to_int('00100001100110001010111111010000'))) == '11011110011001110101000000101111'
assert to_binary(reverse_bits(to_int('10010110010001101000101001110010'))) == '01101001101110010111010110001101'
assert to_binary(reverse_bits(to_int('00011010000111010100110110000111'))) == '11100101111000101011001001111000'
assert to_binary(reverse_bits(to_int('00111000101011001100000110001010'))) == '11000111010100110011111001110101'
assert to_binary(reverse_bits(to_int('11101000011000000001011010011010'))) == '00010111100111111110100101100101'
assert to_binary(reverse_bits(to_int('11001010100001010101110110011010'))) == '00110101011110101010001001100101'
assert to_binary(reverse_bits(to_int('10010010101000101000100101001011'))) == '01101101010111010111011010110100'
