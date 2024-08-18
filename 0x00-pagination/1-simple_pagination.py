#!/usr/bin/env python3
"""
This module implements a simple pagination class.
"""
import csv
import math
from typing import List, Tuple


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """
        A function that takes two integers and returns tuple of size two
        containing a start index and an end index.
        """
        end = page * page_size
        start = end - page_size
        return (start, end)

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        A function that returns the list of pages per the requested current
        page and the page sizes.
        """
        assert type(page) is int
        assert type(page_size) is int
        assert page > 0
        assert page_size > 0

        dataset = self.dataset()
        start, end = Server.index_range(page, page_size)
        if end <= len(dataset):
            return dataset[start:end]
        else:
            return []
