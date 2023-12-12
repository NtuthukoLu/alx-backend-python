#!/usr/bin/env python3
"""
measure_runtime coroutine uses
asyncio.gather to excute async comprehension
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    time module is used to measure total runtime
    main coroutine demonstrates how to measure_runtime
    """
    start_time = time.time()

    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
    )

    end_time = time.time()
    total_runtime = end_time - start_time

    return total_runtime
