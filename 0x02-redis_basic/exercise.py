#!/usr/bin/env python3
"""
Using the Redis NOSQL data storage
"""

import redis
import uuid
from functools import wraps
from typing import Any, Callable, Union


class Cache:
    """an object for storing data in a Redis data storage"""
    def __init__(self):
        """
        Initializes a Cache instance by creating a
        Redis client and flushing the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store the input data in Redis using the random key and return the key.
        """
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key
