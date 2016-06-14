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
