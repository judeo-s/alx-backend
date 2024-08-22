#!/usr/bin/env python3
"""
A module to represent a LIFOCache
"""
from base_caching import BaseCaching
from typing import Any


class LIFOCache(BaseCaching):
    """
    A class representing how LIFOCaching works
    """
    __stack = []

    def __init__(self):
        """
        A constructor to initiate the LIFOCache class
        """
        super().__init__()

    def put(self, key: Any, item: Any):
        """
        A method to put items in a cache
        """
        if key and item:
            if key in LIFOCache.__stack:
                LIFOCache.__stack.remove(key)
                LIFOCache.__stack.append(key)
                self.cache_data[key] = item
            else:
                if len(LIFOCache.__stack) == BaseCaching.MAX_ITEMS:
                    discarded_key = LIFOCache.__stack.pop()
                    self.cache_data.pop(discarded_key)
                    print(f"DISCARD: {discarded_key}")
                LIFOCache.__stack.append(key)
                self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from cache
        """
        if key and key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
