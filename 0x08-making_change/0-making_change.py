#!/usr/bin/python3
""" 0-making_change
"""


def makeChange(coins, total):
    """Given a pile of coins of different values, determine the fewest number
    of coins needed to meet a given amount total
    """
    count = 0
    if total <= 0:
        return 0
    sorted_coins = sorted(coins, reverse=True)
    for i in range(len(sorted_coins)):
        if sorted_coins[i] <= total:
            count += total // sorted_coins[i]
            total %= sorted_coins[i]
    return count if total == 0 else -1
