#!/usr/bin/env python3
"""
a typed-annotatated function module
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    a function that adds all elements in a list
    """
    return sum(input_list)
