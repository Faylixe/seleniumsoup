#!/usr/bin/python

"""
"""

import unittest

from seleniumsoup.page import PageFactory

url = 'https://cbracco.github.io/html5-test-page/'

class PageFactoryTests(unittest.TestCase):
    """ """

    def test_factory(self):
        """ """
        with PageFactory() as factory:
            # TODO : Test
            pass
