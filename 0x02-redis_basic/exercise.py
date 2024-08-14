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

    def get(
        self,
        key: str,
        fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis using the provided key and optionally
        convert it using the provided function.
        """
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        """
        Retrieve data from Redis and convert it to a string.
        """
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """
        Retrieve data from Redis and convert it to an integer.
        """
        return self.get(key, lambda x: int(x))
