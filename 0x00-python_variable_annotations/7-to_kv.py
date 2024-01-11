#!/usr/bin/env python3
"""
Complex types function
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    a function that takes a string k and an int OR float v
    as arg and returns a tuple.
    """
    return (k, float(v ** 2), )
