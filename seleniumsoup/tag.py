#!/usr/bin/python

from seleniumsoup.documentpath import DocumentPath

class Tag(DocumentPath):
    """
    """

    def __init__(self, parent, tag):
        """
        """
        DocumentPath._init__(self)
        self.tag = tag

    def get(self):
        """ """
        element = self.get()
        return element.find_elements_by_tag(self.tag)
