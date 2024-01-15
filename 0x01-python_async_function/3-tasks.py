#!/usr/bin/env python3
"""
a function used to create asycio tasks
"""
import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    a function that takes an int and returns asyncio.Task
    """
    wait_random = __import__('0-basic_async_syntax').wait_random
    return asyncio.create_task(wait_random(max_delay))
