#!/usr/bin/python

import unittest

from seleniumsoup.page import Page

url = 'https://cbracco.github.io/html5-test-page/'

class PageTests(unittest.TestCase):
    """ """

    def setUp(self):
        """ Initialization method. Setups the page factory. """
        self.factory = PageFactory()

    def tearDown(self):
        """ Terminaison method. Releases the page factory. """
        self.factory.quit()

    def test_identifiable(self):
        """ Test identifiable resources. """
        with self.factory.page(url) as page:
            section = page('') # TODO : Test section content.

    def test_tagable(self):
        """ Test tagable resources. """
        with self.factory.page(url) as page:
            menu = page.nav # TODO : Check menu content
            items = menu.a
            assert len(items) == 26

    def test_classable(sef):
        """ Test classable resources. """
        with self.factory.page(url) as page:
            classable = page[''] # TODO : Check classable content

    def test_clickable(self):
        """ Test clickable resources. """
        with self.factory.page(url) as page:
            anchor = page.a # TODO : Specialize data.
            anchor.click()
            # TODO : Implement test.

    def test_fillable(self):
        """ Test fillable resources. """
        with self.factory.page(url) as page:
            text_input = page.input
            pass # TODO : Implement test.

    def submitable(self):
        """ Test submitable resources. """
        with self.factory.page(url) as page:
            form = page.form # TODO : Specialize data.
            form.submit()
