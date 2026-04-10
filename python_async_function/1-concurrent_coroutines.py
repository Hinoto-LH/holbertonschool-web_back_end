#!/usr/bin/env python3
"""Module for wait_n coroutine"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times and return delays in ascending order"""
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    for coro in asyncio.as_completed(tasks):
        delays.append(await coro)
    return delays
