#!/usr/bin/env python3
"""Module for async_comprehension coroutine"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers via async comprehension"""
    return [v async for v in async_generator()]
