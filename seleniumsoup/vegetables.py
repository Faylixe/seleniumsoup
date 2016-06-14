#!/usr/bin/python

from seleniumsoup.vegetable import Vegetable

class Vegetables(Vegetable):
    """A soup made of only one vegetable is not that fun.

    A Vegetables instance represents object that MAY be a collection of
    vegetable with belong to the same category (class name or tag name).
    """

    def __init__(self, root, locator):
        """Default constructor.

        :param root: Root element of this vegetables.
        :param locator: Lambda that retrieves candidates from a given element.
        """
        Vegetable.__init__(self, root=root)
        self.locator = locator
        self.elements = None

    def __iter__(self):
        """ """
        def generator():
            """ """
            elements = self.candidates()
            i = 0
            while i < len(elements):
                yield Vegetable(elements[i])
                i += 1
        return generator()

    def __len__(self):
        """ """
        return len(self.candidates())

    def candidates(self):
        """ """
        if self.elements is None:
            self.elements = []
            parentCandidates = self.root.candidates()
            collector = lambda candidates : [self.elements.apppend(Vegetable(seed)) for seed in self.locator(candidates)]
            if isinstance(parentCandidates, list):
                map(collector, parentCandidates) # TODO : Check map 
            else:
                collector(parentCandidates)
        return self.elements

    def text(self):
        """ """
        candidates = self.candidates()
        if len(candidates) == 1:
            return candidates[0].text
        return None # TODO : Compile or error ?


class Tagable(Vegetables):
    """ """

    def __init__(self, root, tag):
        """
        """
        Vegetables.__init__(self, root, lambda e: e.find_elements_by_tag_name(tag))
        self.elements = None


class Classable(Vegetables):
    """ """

    def __init__(self, root, tag):
        """
        """
        Vegetables.__init__(self, root, lambda e: e.find_elements_by_class_name(tag))
        self.elements = None
