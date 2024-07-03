#!/usr/bin/python3
"""0-prime_game
"""


def isWinner(x, nums):
    """Determines the winner of multiple rounds of a game where players take
    turns removing primes and their multiples.

    Parameters:
    x (int): The number of rounds.
    nums (list of int): The list of maximum numbers for each round.

    Returns:
    str: The name of the player with the most wins ('Maria' or 'Ben'), or None
         if the number of wins is tied.
    """
    def sieve(n):
        """Generates a list of prime numbers up to n using the Sieve of
         Eratosthenes.

         Parameters:
         n (int): The upper limit for generating prime numbers.

         Returns:
         list of int: A list of prime numbers up to n.
         """
        is_prime = [True] * (n + 1)  # Initialize a list to mark prime numbers
        p = 2
        while (p * p <= n):
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        primes = [p for p in range(2, n + 1) if is_prime[p]]
        return primes

    max_n = max(nums)  # Find the maximum number in nums to limit the sieve
    primes = sieve(max_n)

    def play_game(n):
        """Simulates a game where players take turns removing primes and their
        multiples.

        Parameters:
        n (int): The maximum number in the set for the game.

        Returns:
        int: The number of moves made in the game.
        """
        moves = 0
        available = [True] * (n + 1)  # Track available numbers
        for prime in primes:
            if prime > n:
                break
            if available[prime]:
                moves += 1
                for multiple in range(prime, n + 1, prime):
                    available[multiple] = False
        return moves

    maria_wins = 0
    ben_wins = 0

    # Simulate each round of the game
    for n in nums:
        moves = play_game(n)
        if moves % 2 == 1:
            maria_wins += 1  # Maria wins if the number of moves is odd
        else:
            ben_wins += 1  # Ben wins if the number of moves is even

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
