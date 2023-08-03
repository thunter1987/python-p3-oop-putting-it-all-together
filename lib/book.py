#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
        if page_count is not type(int):
            print("page_count must be an integer")
        else:
            self.page_count = page_count