#!/usr/bin/env python3
"""
a function that is used to measure execution time for a certain function
"""
import asyncio
import timeit


def measure_time(n: int, max_delay: int) -> float:
    """
    measures total execution time for wait_n(n, max_delay)
    """
    wait_n = __import__('1-concurrent_coroutines').wait_n
    startTime = timeit.default_timer()
    asyncio.run(wait_n(n, max_delay))
    endTime = timeit.default_timer()
    totalTime = endTime - startTime
    average = totalTime / n
    return average
