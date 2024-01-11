#!/usr/bin/env python3
"""Complex types - mixed list"""
from typing import List


def sum_mixed_list(mxd_list: List[int, float]) -> float:
    """
        Takes a list mxd_lst of integers and floats
        and returns their sum as a float
    """
    return sum(mxd_list)
