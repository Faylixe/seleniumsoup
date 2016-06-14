#!/usr/bin/python

import unittest

from seleniumsoup.page import PageFactory

url = 'http://faylixe.fr/seleniumsoup/testpage.html'

class PageFactoryTests(unittest.TestCase):
    """ PageFactory class test case. """

    def test_factory(self):
        """ Test case for page factory usage. """
        factory = PageFactory()
        assert factory.browser == 'firefox'
        assert len(factory.available) == 0
        with factory:
            with factory.page(url) as first:
                pass
            assert len(factory.available) == 1
            with factory.page(url) as first:
                with factory.page(url) as second:
                    pass
            assert len(factory.available) == 2
        assert len(factory.available) == 0

    def parameterizedFactoryTest(self, browser):
        """ Test page retrieval using factory for the given browser type. """
        factory = PageFactory(browser)
        assert factory.browser == browser
        with factory:
            with factory.page(url) as page:
                text = page.text()
                assert 'link' in text
                assert 'this is an identifiable' in text
                assert 'this is a classifiable' in text
                assert '1 2' in text

    def test_firefox(self):
        """ Test page retrieval using firefox based factory. """
        self.parameterizedFactoryTest('firefox')

    def test_chrome(self):
        """ Test page retrieval using chrome based factory. """
        self.parameterizedFactoryTest('chrome')

    def test_phantomjs(self):
        """ Test page retrieval using phantomjs based factory. """
        self.parameterizedFactoryTest('phantomjs')
