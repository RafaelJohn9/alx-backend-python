#!/usr/bin/env python3
"""
a typed-annotatated function module
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    a function that adds all elements in a list
    """
    return sum(mxd_lst)
