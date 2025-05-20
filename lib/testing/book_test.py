#!/usr/bin/env python3

from book import Book

import io
import sys

class TestBook:
    '''Book in book.py'''

    def test_has_title_and_page_count(self):
        '''has the title and page_count passed into __init__, and values can be set to new instance.'''
        book = Book("And Then There Were None", 272)
        assert(book.page_count == 272)
        assert(book.title == "And Then There Were None")

    def test_requires_int_page_count(self):
        '''prints "page_count must be an integer" if page_count is not an integer.'''
        book = Book("And Then There Were None", 272)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        book.page_count = "not an integer"
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "page_count must be an integer\n"

    def test_can_turn_page(self):
        '''outputs "Flipping the page...wow, you read fast!" when method turn_page() is called'''
        book = Book("The World According to Garp", 69)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        book.turn_page()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Flipping the page...wow, you read fast!\n")
        def test_page_count_setter_accepts_integers(self):
            '''allows setting page_count to an integer value.'''
            book = Book("1984", 328)
            book.page_count = 500
            assert book.page_count == 500

        def test_page_count_setter_rejects_non_integers(self):
            '''does not allow setting page_count to a non-integer value.'''
            book = Book("1984", 328)
            captured_out = io.StringIO()
            sys.stdout = captured_out
            book.page_count = "three hundred"
            sys.stdout = sys.__stdout__
            assert captured_out.getvalue() == "page_count must be an integer\n"
            assert book.page_count == 328  # Ensure the value didn't change
            def test_init_assigns_attributes(self):
                '''__init__ assigns title and page_count correctly.'''
                book = Book("To Kill a Mockingbird", 281)
                assert book.title == "To Kill a Mockingbird"
                assert book.page_count == 281