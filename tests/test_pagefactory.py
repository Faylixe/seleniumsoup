#!/usr/bin/python

from nose.tools import nottest

from seleniumsoup.page import PageFactory

url = 'http://faylixe.fr/seleniumsoup/testpage.html'

def test_factory():
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

@nottest
def parametrized_factory_test(browser):
    """ Test page retrieval using factory for the given browser type. """
    factory = PageFactory(browser)
    assert factory.browser == browser
    with factory:
        with factory.page(url) as page:
            assert page.title == 'testtitle'

def test_firefox():
    """ Test page retrieval using firefox based factory. """
    parametrized_factory_test('firefox')

def test_chrome():
    """ Test page retrieval using chrome based factory. """
    parametrized_factory_test('chrome')

def test_phantomjs():
    """ Test page retrieval using phantomjs based factory. """
    parametrized_factory_test('phantomjs')
