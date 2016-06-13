#!/usr/bin/python

import unittest

from seleniumsoup.page import PageFactory

url = 'https://cbracco.github.io/html5-test-page/'

class PageFactoryTests(unittest.TestCase):
    """ PageFactory class test case. """

    def test_factory(self):
        """ Test case for page factory usage. """
        factory = PageFactory()
        assert factory.browser == 'firefox'
        assert factory.available == 0
        with factory:
            with factory.page(url) as first:
                pass
            assert factory.available == 1
            with factory.page(url) as first:
                with factory.page(url) as second:
                    pass
            assert factory.available == 2
        assert factory.available == 0
