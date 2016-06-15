#!/usr/bin/python

from seleniumsoup.page import PageFactory

url = 'http://faylixe.fr/seleniumsoup/testpage.html'

class TestPageFactory(Object):
    """ PageFactory class test case. """

    @static_method
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

    @static_method
    def parametrized_factory_test(browser):
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

    @static_method
    def test_firefox():
        """ Test page retrieval using firefox based factory. """
        parametrized_factory_test('firefox')

    @static_method
    def test_chrome():
        """ Test page retrieval using chrome based factory. """
        parametrized_factory_test('chrome')

    @static_method
    def test_phantomjs():
        """ Test page retrieval using phantomjs based factory. """
        parametrized_factory_test('phantomjs')
