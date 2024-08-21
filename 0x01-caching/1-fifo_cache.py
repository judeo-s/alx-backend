#!/usr/bin/env python3
"""
A module to represent a FIFOCache
"""
from base_caching import BaseCaching
from typing import Any


class FIFOCache(BaseCaching):
    """
    A class representing how FIFOCaching works
    """
    __queue = []

    def __init__(self):
        """
        A constructor to initiate the FIFOCache class
        """
        super().__init__()

    def put(self, key: Any, item: Any):
        """
        A method to put items in a cache
        """
        if key and item:
            if key in FIFOCache.__queue:
                pass
            else:
                FIFOCache.__queue.append(key)
                if len(FIFOCache.__queue) > BaseCaching.MAX_ITEMS:
                    discarded_key = FIFOCache.__queue.pop(0)
                    self.cache_data.pop(discarded_key)
                    print(f"DISCARD: {discarded_key}")
                self.cache_data[key] = item
