#!/usr/bin/env python3
"""
correct ducktyped annotations
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    duck type annotations added
    """
    if lst:
        return lst[0]
    else:
        return None
