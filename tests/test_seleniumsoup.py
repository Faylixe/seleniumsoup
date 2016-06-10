#!/usr/bin/python

import unittest

from seleniumsoup.vegetable import Page

url = 'https://cbracco.github.io/html5-test-page/'

class SeleniumSoupTest(unittest.TestCase):
    """ """

    def test_tag(self):
        """ """
        with Page(url) as page:
            menu = page.nav
            # TODO : Test menu content.

    def test_multitag(self):
        """ """
        with Page(url) as page:
            menu = page.nav
            items = menu.a
            assert len(items) == 26
