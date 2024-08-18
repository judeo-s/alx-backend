#!/usr/bin/env python3

"""
A python script that returns an index range
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    A function that takes two integers and returns tuple of size two containing
    a start index and an end index.
    """
    end = page * page_size
    start = end - page_size
    return (start, end)
