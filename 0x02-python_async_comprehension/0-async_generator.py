#!/usr/bin/env python3
"""
a coroutined that takes no arg
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    loops 10 times and yield a rand value after each loop
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield(random.uniform(0, 10))
