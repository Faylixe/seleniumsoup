#!/usr/bin/python

import unittest

from seleniumsoup.page import PageFactory

url = 'http://faylixe.fr/seleniumsoup/testpage.html'

class TestPage(object):
    """ """

    factory = None

    @classmethod
    def setup_class(cls):
        """ Initialization method. Setups the page factory. """
        factory = PageFactory()

    @classmethod
    def teardown_class(cls):
        """ Terminaison method. Releases the page factory. """
        factory.quit()

    def test_tagable(self):
        """ Test tagable resources. """
        def test_head(heads):
            """ Concrete test implementation for a given h1 elements list."""
            assert len(heads) == 2
            assert heads[0].text() == 'this is an identifiable'
            assert heads[1].text() == 'this is a classifiable'
        with factory.page(url) as page:
            test_head(page.h1)
            test_head(page.div.h1)

#    def test_classifiable(self):
#        """ Test classifiable resources. """
#        with factory.page(url) as page:
#            classifiable = page(class='testclassifiable')
#            assert len(classifiable) == 1
#            assert 'this is a classifiable' in classifiable[0].text()
#            classifiables = page(class='testmulticlassifiable')
#            assert len(classifiables) == 2
#            assert classifiables[0].text() == '1'
#            assert classifiables[1].text() == '2'

    def test_identifiable(self):
        """ Test identifiable resources. """
        with factory.page(url) as page:
            identifiable = page(id='testidentifiable')
            assert identifiable is not None
            assert identifiable.text() == 'this is an identifiable'

#    def test_attribute(self):
#        """ Test attribute access """
#        with factory.page(url) as page:
#            anchors = page.a
#            assert len(anchors) == 1
#            anchor = anchors[0]
#            assert anchor['id'] == 'testlink'
#            assert anchor['name'] == 'linkname'

    def test_iterable(self):
        """ Test element iterator """
        with factory.page(url) as page:
            i = 1
            for span in page.span:
                assert span.text() == str(i)
                i += 1

#    def test_clickable(self):
#        """ Test clickable resources. """
#        with factory.page(url) as page:
#            anchors = page.a
#            assert len(anchors) == 1
#            assert anchors[0].text() == 'link'
#            anchors[0].click()
#            assert anchors[0].text() == 'clicked'

#    def test_fillable(self):
#        """ Test fillable resources. """
#        with factory.page(url) as page:
#            inputs = page.input(type='text')
#            assert len(inputs) == 1
#            inputs[0].fill('foo')
#            assert inputs[0].value() == 'foo'

#    def submitable(self):
#        """ Test submitable resources. """
#        with factory.page(url) as page:
#            form = page.form # TODO : Specialize data.
#            form.submit()
