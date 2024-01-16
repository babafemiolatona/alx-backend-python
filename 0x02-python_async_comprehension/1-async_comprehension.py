#!/usr/bin/env python3
"""Async Comprehensions"""
import random
import asyncio
from typing import Generator


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """Async Comprehensions"""
    return [i async for i in async_generator()]
