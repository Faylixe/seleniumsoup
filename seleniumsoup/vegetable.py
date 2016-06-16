#!/usr/bin/python

"""
"""

class Vegetable:
    """A vegetable is the main resource for making a great soup.

    More seriously, a vegtable represents the basic abstraction of a web page
    element. It provides default access operation over such element namely :

    * Finding element(s) from tag name using attribute access operator.

    * Finding a element with unique id using call operator ().
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
        """Syntaxic sugar which can either allow to retrieve HTML element using
        unique attribute property such as id or name (assuming there are unique
        across the target document). Or performing attributes filtering if this
        instance is a Vegetables.

        Such filtering is efficient when the set of parent elements is not too
        big.

        :param **kwargs: HTML (attribute, value) mapping.
        :returns: Matched element(s).
        """
        attributes = kwargs.keys()
        if len(attributes) == 1:
            if attributes[0] == 'id':
                id = kwargs['id']
                return self.locate(lambda e : e.find_element_by_id(id))
            elif attributes[0] == 'name':
                name = kwargs['name']
                return self.locate(lambda e: e.find_elements_by_name(name))
        elif isinstance(self, Vegetables):
            # TODO : Implements multi attribute filtering.
            pass
        # TODO : Consider raise error ?
        return None

    def locate(self, locator):
        """Locates and collects child HTML element(s) using the given locator.

        TODO : Explain algorithm ?

        :param locator: Function that retrieves web element(s) from a given one.
        :returns: Located element using the given locator from this root.
        """
        elements = self.candidates()
        if isinstance(elements, list):
            for element in elements:
                seed = locator(element)
                if seed is not None:
                    return CookVegetable(seed)
        else:
            seed = locator(elements)
            return CookVegetable(seed)

    def candidates(self):
        """ To document
        """
        return self.root

class CookVegetable(Vegetable):
    """ To document.
    """

    def __init__(self, root):
        """Default constructor.

        :param root:
        """
        Vegetable.__init__(self, root)

    def __getitem__(self, attribute):
        """HTML Element attribute getter.

        :param attribute: Name of the attribute to retrieve.
        :returns: Attribute value if any.
        """
        # TODO : Ensure get_attribute return type if not found.
        return self.root.get_attribute(attribute)

    def text(self):
        """HTML Element text getter.

        :returns: Text of this element.
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
            self.elements = self.root.locate(self.locator)
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
