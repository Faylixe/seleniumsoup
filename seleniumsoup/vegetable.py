#!/usr/bin/python

"""
"""

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

    def __call__(self, **kwargs):
        """

        :param **kwargs:
        :returns:
        """
        attributes = kwargs.keys()
        if 'id' in attributes:
            return self.identifiable(kwargs['id'])
        return None

    def identifiable(self, id):
        """

        :param id:
        :returns:
        """
        elements = self.candidates()
        if isinstance(elements, list):
            for element in elements:
                seed = element.find_element_by_id(id)
                if seed is not None:
                    return Vegetable(seed)
        else:
            seed = elements.find_element_by_id(id)
            return Vegetable(seed)

    def __getitem__(self, attribute):
        """Attribute getter.

        :param classname:
        :returns:
        """
        pass
        # TODO : Return attributes for root element.

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

    def __call__(self, **kwargs):
        """ Attribute filtering. """
        for attribute in kwargs.keys():
            pass
        return

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
            collector = lambda c : map(lambda s : self.elements.apppend(Vegetable(s)), c)
            if isinstance(parentCandidates, list):
                map(collector, parentCandidates)
            else:
                collector(parentCandidates)
        return self.elements

    def __getitem__(self, index):
        """ """
        return self.candidates()[index]

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
