#!/usr/bin/env python3
"""
This module implements a simple pagination class.
"""
import csv
import math
from typing import List, Tuple, Dict


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
        """
        Cached dataset
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        A method that takes arguments and returns a dictionary containning the
        following key-value pairs

        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        """
        dataset_page = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = total_items // page_size

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": (page_size if page_size <= len(dataset_page) else
                          len(dataset_page)),
            "page": page,
            "data": dataset_page,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
