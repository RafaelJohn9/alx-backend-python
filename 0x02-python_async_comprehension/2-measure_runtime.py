#!/usr/bin/env python3
"""
coroutine that calculates run on time
"""
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() ->float:
    """
    will execute async_comprehension four times in parallel
    using asyncio.gather
    """
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            )
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
