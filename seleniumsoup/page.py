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
    """
    """

    def __init__(self, browser):
        """Factory constructor.

        :param browser: Browser type this cache supports.
        """
        self.browser = browser
        self.available = []

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

    def driver(self):
        """Retrieves a driver instance from the cache.

        If there is no instance available, it will create one.

        :returns: Required driver instance.
        """
        if len(self.available) == 0:
            driver = createDriver(self.browser)
            self.available.append(driver)
        return self.available.pop(0)

    def release(self, driver):
        """
        """
        self.available.append(driver)

    def page(self, url):
        """
        """
        return Page(url, factory=self)

class Page(Vegetable):
    """Context manager that represents a web document.

    TO DOCUMENT

    """

    def __init__(self, url, factory=None):
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
        if self.factory is None:
            self.root = webdriver.Firefox()
        else:
            self.root = self.factory.driver()
        self.root.get(self.url)
        return self

    def __exit__(self, type, value, traceback):
        """ TO DOCUMENT

        :param type:
        :param value:
        :param traceback:
        """
        if self.factory is None:
            self.root.quit()
        else:
            self.factory.release(self.root)
