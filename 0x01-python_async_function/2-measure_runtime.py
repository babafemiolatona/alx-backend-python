#!/usr/bin/env python3
"""Measure the runtime"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the runtime of wait_n

    Args:
        n (int, optional): Number of times to execute the coroutine
                           (default is 0).
        max_delay (int, optional): Maximum delay in seconds (default is 10).

    Returns:
        float: Average runtime of wait_n.
    """
    start = time.perf_counter()
    await wait_n(n, max_delay)
    end = time.perf_counter()
    return (end - start) / n
