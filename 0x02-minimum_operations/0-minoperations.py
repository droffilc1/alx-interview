#!/usr/bin/python3
""" 0-minoperations """


def minOperations(n):
    """Calculates the fewest number of operations needed to result in exactly
    n H characters in the file.

     The operations allowed are:
    - Copy all (copies the entire content)
    - Paste (pastes the last copied content)
    """
    # If n is less than 2, no operations are required (already 1 'H' or less)
    if n < 2:
        return 0

    # The initial block size to consider for operations (we start with 2)
    current_length = 2

    # To count the number of operations performed
    operations = 0

    # Loop until we reach exactly 1, which indicates that the operation process
    # is complete
    while n > 1:
        # If n is divisible by current_length, it means this length can be
        # used for operations
        if n % current_length == 0:
            # Divide n by current_length to reduce the problem size
            n = n / current_length
            # Add current_length to operations count
            operations += current_length
        else:
            # If not divisible, increment current_length to check larger blocks
            current_length += 1

    # Return the total number of operations required
    return operations
