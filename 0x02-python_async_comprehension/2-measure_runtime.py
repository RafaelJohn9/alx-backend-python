#!/usr/bin/env python3
"""
coroutine that calculates run on time
"""
from asyncio import gather
from time import perf_counter
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    will execute async_comprehension four times in parallel
    using asyncio.gather
    """
    start_time = perf_counter()
    await gather(*(async_comprehension() for _ in range(4)))
    return perf_counter() - start_time
