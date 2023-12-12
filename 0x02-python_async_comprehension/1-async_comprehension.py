#!/usr/bin/env python3
"""
Coroutine that collects 10 random numbers
using async comprehension
"""
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list[int]:
    """
    returns 10 numbers
    """
    return [num async for num in async_generator()]
