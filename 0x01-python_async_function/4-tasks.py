#!/usr/bin/env python3
"""
a function that exectues an async function n times
"""
import asyncio
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    a function that spawns wait_random n times with the specified max_delay
    """
    task_wait_random = __import__('3-tasks').task_wait_random

    timings = [task_wait_random(max_delay) for _ in range(n)]
    return [await timing for timing in asyncio.as_completed(timings)]
