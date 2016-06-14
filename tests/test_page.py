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
            identifiable = page('testidentifiable')
            assert not identifiable is None
            assert identifiable.text() == 'this is an identifiable'

    def test_classifiable(self):
        """ Test classifiable resources. """
        with self.factory.page(url) as page:
            classifiables = page['testclassifiable']
            assert len(classifiables) == 1
            assert classifiables[0].text() == 'this is a classifiable'

    def test_multiclassifiable(self):
        """ Test classifiable resources with several matches. """
        with self.factory.page(url) as page:
            classifiables = page['testclassifiable']
            assert len(classifiables) == 2
            assert classifiables[0].text() == '1'
            assert classifiables[1].text() == '2'

    def test_tagable(self):
        """ Test tagable resources. """
        with self.factory.page(url) as page:
            menu = page.nav # TODO : Check menu content
            items = menu.a
            assert len(items) == 26

    def test_clickable(self):
        """ Test clickable resources. """
        with self.factory.page(url) as page:
            anchor = page.a
            assert len(anchor) == 1
            assert anchor[0].text() == 'link'
            anchor[0].click()
            assert anchor[0].text() == 'clicked'

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
