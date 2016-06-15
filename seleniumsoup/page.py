#!/usr/bin/python

"""Page module is the entry point of the seleniumsoup library,
by providing context manager which manages web driver instance
as web document.

TODO : Document with usage section.
"""

from selenium import webdriver

from seleniumsoup.vegetable import Vegetable

def createDriver(browser):
    """Creates and returns new webdriver instance.

    :param browser: Browser to create driver for.
    :returns: Created driver instance.
    """
    if browser == 'phantomjs':
        pass # TODO : Creates PhantomJS driver instance.
    elif browser == 'chrome':
        pass # TODO : Creates Chrome driver instance.
    return webdriver.Firefox()

class PageFactory:
    """A PageFactory instance acts as a webdriver cache
    which can be controlled using context manager.

    Such factory should be used to create page(s), which will be
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
        """Context manager API __enter__ implementation. """
        return self

    def __exit__(self, type, value, traceback):
        """ Context manager API __exit__ implementation. """
        self.quit()

    def quit(self):
        """ Kills every web driver instance that belongs to this factory. """
        for driver in self.available:
            driver.quit()
        for driver in self.used:
            driver.quit()
        del self.available[:]
        del self.used[:]

    def driver(self):
        """Retrieves a web driver instance from the cache.

        If there is no instance available, it will create one.

        :returns: Required web driver instance.
        """
        if len(self.available) == 0:
            driver = createDriver(self.browser)
            self.available.append(driver)
        instance = self.available.pop(0)
        self.used.append(instance)
        return instance

    def release(self, driver):
        """Releases the given web driver instance.

        :param driver: Web driver instance to release.
        """
        self.used.remove(driver)
        self.available.append(driver)

    def page(self, url):
        """Factory method that creates a page instance.

        :param url: URL to create page for.
        :returns: Created page instance linked to this factory.
        """
        return Page(url, factory=self)

class Page(Vegetable):
    """Context manager that represents a web document.

    Example:
        Page should be used through context manager using with keyword as
        following :
            with Page('target_url') as page:
                print(page.text())
    """

    def __init__(self, url, factory=None):
        """Default constructor.

        If factory parameter is missing then the module default factory will be
        used.

        :param url: URL of the contextual web document.
        :param factory: (Optional) Factory instance this page will belong to.
        :return: Page instance.
        """
        self.url = url
        self.factory = factory

    def title(self):
        """Page title getter.

        :returns: Page title.
        """
        if self.root is None:
            return '' # TODO : Consider returning None
        return self.root.title

    def __enter__(self):
        """ Context manager API __enter__ implementation. """
        if self.factory is None:
            self.root = createDriver('firefox')
        else:
            self.root = self.factory.driver()
        self.root.get(self.url)
        return self

    def __exit__(self, type, value, traceback):
        """Context manager API exit implementation. """
        if self.factory is None:
            self.root.quit()
        else:
            self.factory.release(self.root)
