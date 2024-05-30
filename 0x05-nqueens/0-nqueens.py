#!/usr/bin/python3
"""0-nqueens
Implements queens puzzle.
"""
import sys


def nqueens(n):
    """Implements queens puzzle."""
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    elif n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    state = []
    search(state, solutions, n)
    return solutions


# Helper functions
def is_valid_state(state, n):
    """Check if it is a valid state."""
    return len(state) == n


def get_candidates(state, n):
    """Ensures the queen is placed in the right position."""
    if not state:
        return range(n)

    # Find the next position in the state to populate
    position = len(state)
    candidates = set(range(n))
    # Remove candidates that place the queen into attacks
    for row, col in enumerate(state):
        # Discard the column index if it is occupied by a queen
        candidates.discard(col)
        dist = position - row
        # Discard diagonals
        candidates.discard(col + dist)
        candidates.discard(col - dist)
    return candidates


def search(state, solutions, n):
    """Searches for the right position to place the queen."""
    if is_valid_state(state, n):
        # Format the solution as a list of coordinates
        solutions.append([[i, state[i]] for i in range(n)])
        return

    for candidate in get_candidates(state, n):
        # Recurse
        state.append(candidate)
        search(state, solutions, n)
        state.pop()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = nqueens(n)
    for solution in solutions:
        print(solution)
