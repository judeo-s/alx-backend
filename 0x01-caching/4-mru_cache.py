#!/usr/bin/env python3
"""
A module to represent a LRU cache system
"""
from base_caching import BaseCaching
from typing import Any


class MRUCache(BaseCaching):
    """
    A class representing how LRUCaching works
    """
    __table = {}

    def __init__(self):
        """
        A constructor to initiate the LRUCache class
        """
        super().__init__()

    def find_most(self) -> int:
        """
        A method to find the most weight in the cache
        """
        least_key = None
        least = 0
        for key in MRUCache.__table.keys():
            if MRUCache.__table[key] > least:
                least = MRUCache.__table[key]
                least_key = key
        return least_key

    def reduce_weights(self):
        """
        A method to reduce weights for MRU cache entries
        """
        for key in MRUCache.__table.keys():
            MRUCache.__table[key] -= 1

    def put(self, key: Any, item: Any):
        """
        A method to put items in a cache
        """
        if key and item:
            if key in MRUCache.__table.keys():
                pass
            else:
                if len(MRUCache.__table) == BaseCaching.MAX_ITEMS:
                    l_key = self.find_most()
                    MRUCache.__table.pop(l_key)
                    self.cache_data.pop(l_key)
                    print(f"DISCARD: {l_key}")
            self.reduce_weights()
            MRUCache.__table[key] = BaseCaching.MAX_ITEMS
            self.cache_data[key] = item

    def get(self, key: Any):
        """
        Get an item from cache
        """
        if key and key in self.cache_data.keys():
            self.reduce_weights()
            MRUCache.__table[key] = BaseCaching.MAX_ITEMS
            return self.cache_data[key]
        else:
            return None
