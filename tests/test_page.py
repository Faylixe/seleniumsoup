#!/usr/bin/python

import unittest

from seleniumsoup.page import Page

url = 'https://cbracco.github.io/html5-test-page/'

class PageTests(unittest.TestCase):
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

    def test_click(self):
        """ """
        pass
