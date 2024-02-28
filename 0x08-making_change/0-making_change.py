#!/usr/bin/python3
""" Making Change interview algorithm
"""


def makeChange(coins, total):
    """ Make change function
    """
    if total == 0:
        return 0
    sorted_list = sorted(coins, reverse=True)
    count = 0
    for coin in sorted_list:
        while total >= coin:
            total -= coin
            count += 1
    if total > 0:
        return (-1)
    else:
        return (count)