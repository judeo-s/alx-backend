#!/usr/bin/env python3
"""
A module to represent a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A class implements a basic caching system
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key and key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
