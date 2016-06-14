#!/usr/bin/python

"""
"""

from seleniumsoup.vegetables import Tagable, Classable

class Vegetable:
    """A vegetable is the main resource for making a great soup.

    More seriously, a vegtable represents the basic abstraction of a web page
    element. It provides default access operation over such element namely :

    * Finding a element with unique id using call operator ().
    * Finding element(s) from tag name using attribute access operator.
    * Finding element(s) from class name using index operator [].
    """

    def __init__(self, root=None):
        """Default constructor.

        :param root:
        """
        self.root = root

    def __getattr__(self, tag):
        """Syntaxic sugar for retriving all child element from this vegetable
        root using attribute access operator using attribute name as HTML tag
        filter.

        :param tag: Tag name of child elements we want to retrieve.
        :returns: A new Tag element instance.
        """
        return Tagable(self, tag)

    def __call__(self, id):
        """Syntaxic sugar for retriving all child element from this vegetable
        root using call access operator using given parameter as HTML element
        id filter.

        :param id: Identifier of the child element we want to retrieve.
        :returns:
        """
        candidates = self.candidates()
        if isinstance(candidates, list):
            for candidate in candidates:
                result = candidate(id)
                if result != None:
                    return result
        else:
            seed = candidates.find_element_by_id(id)
            return Vegetable(seed)
        return None

    def __getitem__(self, classname):
        """Class getter

        :param classname:
        :returns:
        """
        return Classable(self, classname)

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

    def click(self):
        """ """
        pass

    def fill(self, text):
        """ """
        pass

    def submit(self):
        """ """
        pass
