#!/usr/bin/python

class Vegetable:
    """
    """

    def __init__(self, element):
        """ Default constructor. """
        self.element = element

    def __getattr__(self, tag):
        """ Tag getter """
        return Tag(self, tag)

    def __call__(self, id):
        """ Id getter. """
        candidates = get()
        if isinstance(candidates, Vegetable):
            seed = parent.find_element_by_id(id)
            return Vegetable(seed)
        # TODO : perform search over candidate.
        return None

    def __getitem__(self, klass):
        """ class getter """
        return Class(self, klass)

    def get(self):
        """ """
        return self.element

    def text(self):
        """ """
        return element.text

    def click(self):
        """ """
        element.click()
