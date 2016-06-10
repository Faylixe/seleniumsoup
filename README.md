# Seleniumsoup

[![CircleCI](https://circleci.com/gh/Faylixe/seleniumsoup.svg?style=svg)](https://circleci.com/gh/Faylixe/seleniumsoup)

Selenium soup is a wrapper for selenium framework which allows to manipulate webpage as Python object.

## Installation

>Not available yet.

## Usage

### Simple page parsing

Parsing a page using **seleniumsoup** is as easy as this :

```python
from seleniumsoup.page import Page

url = 'https://cbracco.github.io/html5-test-page/'

with Page(url) as page:
    for link in page.nav.a:
      print(link.text())
```

It will open a ``Firefox`` instance, load the given URL, and print all links
text. The browser instance will be closed once out of the context manager scope.

### Reusing browser

```python
from seleniumsoup.page import PageFactory

url1 = 'https://cbracco.github.io/html5-test-page/'
url2 = 'https://github.com/'

def printLinks(page):
  for link in page.nav.a:
    print(link.text())

with PageFactory() as factory:
  with factory.page(url1) as page:
    printLinks(page)
  with factory.page(url2) as page:
    printLinks(page)
```
