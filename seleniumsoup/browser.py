#!/usr/bin/python

from selenium import webdriver
from seleniumsoup.vegetable import Vegetable

class Browser(Vegetable):
    """ Top level matcher.
    """

    def __init__(self, url, driver=None):
        """Default constructor.
        """
        browser = webdriver.Firefox() # TODO : Use driver parameter.
        browser.get(url)
        Vegetable.__init__(self, browser)
