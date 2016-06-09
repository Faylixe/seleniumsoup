#!/usr/bin/python3


class Matcher:
    """ """

    def __init__(self, root):
        """ Default constructor. """
        self.root = root

    def __getitem__(self, index):
        """ Tag getter """
        return Tag(self, index)

    def __getattr__(self, attr):
        """ Id getter. """
        element = root.get()
        return element.find_element_by_id(attr)

    def get(self):
        """ """
        return self.root

class Tag(Matcher):
    """ """

    def __init__(self, element, tag):
        """ """
        Matcher._init__(self)
        self.element = element
        self.tag = tag

    def get(self):
        """ """
        return element.find_elements_by_tag(self.tag)

class Browser(Matcher):
    """ Top level matcher. """

    def __init__(self, url, driver=None):
        """Default constructor.
        """
        browser = webdriver.Firefox() # TODO : Use driver parameter.
        browser.get(url)
        Matcher.__init__(browser)
