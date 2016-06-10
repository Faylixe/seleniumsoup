#!/usr/bin/python

from selenium import webdriver

class Vegetable:
    """
    """

    def __init__(self, root=None):
        """Default constructor.

        :param root:
        """
        self.root = root

    def __getattr__(self, tag):
        """Tag getter

        :param tag:
        :returns:
        """
        return Tag(self, tag)

    def __call__(self, id):
        """Id getter.

        :param id:
        :returns:
        """
        candidates = self.getCandidates()
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

    def getCandidates(self):
        """ """
        return self.root

    def text(self):
        """

        :returns:
        """
        if self.root is None:
            return "" # TODO : Consider throwing error.
        return self.root.text

class Tag(Vegetable):
    """
    TODO : Make it iterable
    """

    def __init__(self, root, tag):
        """
        """
        Vegetable.__init__(self, root=root)
        self.tag = tag
        self.elements = None

    def __iter__(self):
        """ """
        def generator():
            """ """
            elements = self.getCandidates()
            i = 0
            while i < len(elements):
                yield Vegetable(elements[i])
                i += 1
        return generator()

    def __len__(self):
        """ """
        return len(self.getCandidates())

    def getCandidates(self):
        """ """
        if self.elements is None:
            parentCandidates = self.root.getCandidates()
            if isinstance(parentCandidates, list):
                self.elements = [c for candidates in parentCandidates for c in candidates.find_elements_by_tag_name(self.tag)]
            else:
                self.elements = parentCandidates.find_elements_by_tag_name(self.tag)
        return self.elements

    def text(self):
        """ """
        candidates = self.getCandidates()
        if len(candidates) == 1:
            return candidates[0].text
        return None # TODO : Compile or error ?

class Page(Vegetable):
    """ Top level matcher.
    """

    def __init__(self, url, driver=None):
        """Default constructor.
        """
        self.url = url

    def __enter__(self):
        """ """
        self.root = webdriver.Firefox() # TODO : Use driver parameter.
        self.root.get(self.url)
        return self

    def __exit__(self, type, value, traceback):
        """ """
        self.root.quit()
