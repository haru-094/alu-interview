#!/usr/bin/python3
"""Minimum operations to reach n H characters."""


def minOperations(n):
    """Return the fewest copy/paste operations needed to reach n Hs."""
    if n < 2:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
