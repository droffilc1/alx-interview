#!/usr/bin/python3
""" 0-validate_utf8 """


def count_leading_ones(byte):
    """Helper function to count the number of leading 1 bits in a byte.
    :param byte: an integer representing a byte (0-255)
    :return: the number of leading 1 bits in the byte
    """
    count = 0
    for i in range(8):
        if (byte >> (7 - i)) & 1:
            count += 1
        else:
            break
    return count


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding
    :param data: a list of integers, each representing a byte (0-255)
    :return: True if data is a valid UTF-8 encoding, else return False
    """
    data = iter(data)
    for leading_byte in data:
        leading_ones = count_leading_ones(leading_byte)
        if leading_ones == 1 or leading_ones > 4:
            # A leading byte with exactly 1 leading 1 bit is invalid,
            # as are leading bytes with more than 4 leading 1 bits.
            return False
        if leading_ones == 0:
            continue  # Single-byte character
        # Check that the correct number of following bytes have
        # the form 10xxxxxx
        for _ in range(leading_ones - 1):
            trailing_byte = next(data, None)
            if trailing_byte is None or \
                    trailing_byte >> 6 != 0b10:
                # If there are not enough bytes left or the byte does
                #  not start with 10, then the UTF-8 encoding is invalid
                return False
    return True
