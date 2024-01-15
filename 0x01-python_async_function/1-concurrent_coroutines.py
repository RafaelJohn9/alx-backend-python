#!/usr/bin/env python3
"""
a function that exectues an async function n times
"""
import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List:
    """
    a function that spawns wait_random n times with the specified max_delay
    """
    wait_random = __import__('0-basic_async_syntax').wait_random

    timings = [wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
