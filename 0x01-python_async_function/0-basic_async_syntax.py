#!/usr/bin/env python3
"""
asynchronous coroutine
"""
import asyncio
import random


async def wait_random(max_delay = 10):
    """
    takes in an integer argument, with a default value of 10
    named wait_random that waits for a random delay between 0
    and max_delay and eventually returns it
    """
    randomValue = random.uniform(0, max_delay + 0.1)
    await asyncio.sleep(randomValue)
    return randomValue
