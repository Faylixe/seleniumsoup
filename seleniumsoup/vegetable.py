#!/usr/bin/python

"""
"""

from selenium import webdriver

class Vegetable:
    """A vegetable is the main resource for making a great soup.

    More seriously, a vegtable represent the basic abstraction of a web page
    element. It provides default access operation over such element namely :

    * Finding a element with unique id.
    * Finding element(s) from tag name.
    * Finding element(s) from class name.
    """

    def __init__(self, root=None):
        """Default constructor.

        :param root:
        """
        self.root = root

    def __getattr__(self, tag):
        """

        :param tag:
        :returns:
        """
        return Tag(self, tag)

    def __call__(self, id):
        """Id getter.

        :param id:
        :returns:
        """
        candidates = self.candidates()
        if isinstance(candidates, list):
            pass # TODO : Perform search over
        seed = candidates.find_element_by_id(id)
        return Vegetable(seed)

    def __getitem__(self, klass):
        """Class getter

        :param klass:
        :returns:
        """
        return Class(self, klass)

    def candidates(self):
        """
        """
        return self.root

    def text(self):
        """

        :returns:
        """
        if self.root is None:
            return "" # TODO : Consider throwing error.
        return self.root.text

class Vegetables(Vegetable):
    """A soup made of only one vegetable is not that fun.

    A Vegetables instance represents object that MAY be a collection of
    vegetable with belong to the same category (class name or tag name).
    """

    def __init__(self, root, locator):
        """
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
            parentCandidates = self.root.candidates()
            if isinstance(parentCandidates, list):
                self.elements = [c for candidates in parentCandidates for c in candidates.find_elements_by_tag_name(self.tag)]
            else:
                self.elements = parentCandidates.find_elements_by_tag_name(self.tag)
        return self.elements

    def text(self):
        """ """
        candidates = self.candidates()
        if len(candidates) == 1:
            return candidates[0].text
        return None # TODO : Compile or error ?

class Tag(Vegetables):
    """ """

    def __init__(self, root, tag):
        """
        """
        Vegetables.__init__(self, root, lambda e: e.find_elements_by_tag_name(tag))
        self.elements = None
