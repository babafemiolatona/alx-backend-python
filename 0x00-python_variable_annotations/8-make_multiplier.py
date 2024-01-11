#!/usr/bin/env python3
"""Complex types - functions"""


def make_multiplier(multiplier: float) -> callable:
    """Returns a function that multiplies a float by multiplier."""
    def multiply_by_multiplier(number: float) -> float:
        """Returns the product of number and multiplier."""
        return number * multiplier
    return multiply_by_multiplier
