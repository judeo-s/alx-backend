#!/usr/bin/env python3
"""
A module to represent a LRU cache system
"""
from base_caching import BaseCaching
from typing import Any


class LRUCache(BaseCaching):
    """
    A class representing how LRUCaching works
    """
    __table = {}

    def __init__(self):
        """
        A constructor to initiate the LRUCache class
        """
        super().__init__()

    def find_least(self) -> int:
        """
        A method to find the least weight in the cache
        """
        least_key = None
        least = BaseCaching.MAX_ITEMS
        for key in LRUCache.__table.keys():
            if LRUCache.__table[key] < least:
                least = LRUCache.__table[key]
                least_key = key
        return least_key

    def reduce_weights(self):
        """
        A method to reduce weights for LRU cache entries
        """
        for key in LRUCache.__table.keys():
            LRUCache.__table[key] -= 1

    def put(self, key: Any, item: Any):
        """
        A method to put items in a cache
        """
        if key and item:
            if key in LRUCache.__table.keys():
                pass
            else:
                if len(LRUCache.__table) >= BaseCaching.MAX_ITEMS:
                    l_key = self.find_least()
                    LRUCache.__table.pop(l_key)
                    self.cache_data.pop(l_key)
                    print(f"DISCARD: {l_key}")
            self.reduce_weights()
            LRUCache.__table[key] = BaseCaching.MAX_ITEMS
            self.cache_data[key] = item

    def get(self, key: Any):
        """
        Get an item from cache
        """
        if key and key in self.cache_data.keys():
            self.reduce_weights()
            LRUCache.__table[key] = BaseCaching.MAX_ITEMS
            return self.cache_data[key]
        else:
            return None
