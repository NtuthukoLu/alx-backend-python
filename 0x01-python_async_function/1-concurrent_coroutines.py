#!/usr/bin/env python3
"""
Multiple coroutines
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function that calls `n` instances of wait_random.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    wait_list = []
    for task in asyncio.as_completed(tasks):
        result = await task
        wait_list.append(result)
    return wait_list
