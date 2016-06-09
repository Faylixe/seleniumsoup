#!/usr/bin/python

class DocumentPath:
    """
    """

    def __init__(self, parent):
        """ Default constructor. """
        self.parent = parent

    def __getitem__(self, index):
        """ Tag getter """
        return Tag(self, index)

    def __call__(self, id):
        """ Id getter. """
        element = root.get()
        return element.find_element_by_id(id)

    def get(self):
        """ """
        return self.parent
