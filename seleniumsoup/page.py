#!/usr/bin/python

"""
"""

from seleniumsoup.vegetable import Vegetable

def createDriver(browser):
    """Creates and returns new webdriver instance.

    :param browser: Browser to create driver for.
    :returns: Created driver instance.
    """
    return webdriver.Firefox()

class PageFactory:
    """A PageFactory instance acts as a webdriver cache
    which is controlled using context manager.

    Such factory should be used to create page, which will be
    released once context is out. Once the factory context is
    out, then every driver instance in the cache will be killed.
    """

    def __init__(self, browser='firefox'):
        """Factory constructor.

        :param browser: Browser type this cache supports.
        """
        self.browser = browser
        self.available = []
        self.used = []

    def __enter__(self):
        """

        :returns:
        """
        return self

    def __exit__(self, type, value, traceback):
        """

        :param type:
        :param value:
        :param traceback:
        """
        for driver in self.available:
            driver.quit()
        self.available.clear()

    def driver(self):
        """Retrieves a driver instance from the cache.

        If there is no instance available, it will create one.

        :returns: Required driver instance.
        """
        if len(self.available) == 0:
            driver = createDriver(self.browser)
            self.available.append(driver)
        instance = self.available.pop(0)
        self.locked.append(instance)
        return instance

    def release(self, driver):
        """Releases the given driver instance.

        :param driver: Web driver instance to be released.
        """
        self.used.remove(driver)
        self.available.append(driver)

    def page(self, url):
        """
        """
        return Page(url, factory=self)

class DefaultPageFactory:
    """
    """

    def driver(self):
        """ """
        return createDriver() # TODO : Default parameter ?

    def release(self, driver):
        """ """
        driver.quit()

""" Default factory used for stand alone page. """
defaultFactory = PageFactory()

# TODO : Consider adding shutdown hook for clean default factory ?

class Page(Vegetable):
    """Context manager that represents a web document.

    TO DOCUMENT

    """

    def __init__(self, url, factory=defaultFactory):
        """Default constructor.

        :param url: URL of the contextual web document.
        :param factory: (Optional) TO DOCUMENT.
        :return: Page instance.
        """
        self.url = url
        self.factory = factory

    def __enter__(self):
        """ TO DOCUMENT

        :returns:
        """
        self.root = self.factory.driver()
        self.root.get(self.url)
        return self

    def __exit__(self, type, value, traceback):
        """ TO DOCUMENT

        :param type:
        :param value:
        :param traceback:
        """
        self.factory.release(self.root)
