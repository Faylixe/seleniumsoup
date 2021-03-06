# Seleniumsoup

[![Build Status](https://travis-ci.org/Faylixe/seleniumsoup.svg?branch=master)](https://travis-ci.org/Faylixe/seleniumsoup) [![codecov](https://codecov.io/gh/Faylixe/seleniumsoup/branch/master/graph/badge.svg)](https://codecov.io/gh/Faylixe/seleniumsoup) [![Code Issues](https://www.quantifiedcode.com/api/v1/project/3d5fa5f799bd47eb80587b1d084ed695/badge.svg)](https://www.quantifiedcode.com/app/project/3d5fa5f799bd47eb80587b1d084ed695)


Selenium soup is a wrapper for selenium framework which allows to manipulate webpage as Python object.

* [Installation](#installation)
* [Usage](#usage)
  * [Simple page Parsing](#simple-page-parsing)
  * [Accessing elements](#accesing-elements)
  * [Page factory and browser caching](#page-factory-and-browser-caching)

## Installation

>Not available yet.

## Usage

### Simple page parsing

Parsing a page using **seleniumsoup** is as easy as this :

```python
from seleniumsoup.page import Page

url = 'http://faylixe.fr/seleniumsoup/testpage.html'

with Page(url) as page:
  print(page.text())
```

It will open a ``Firefox`` instance, load the given URL, and print the page
text. The browser instance will be closed once out of the context manager
scope.

### Accessing elements

>To be documented.

```python
from seleniumsoup.page import Page

url = 'http://faylixe.fr/seleniumsoup/testpage.html'

with Page(url) as page:
  # Locating by tagname
  for span in page.span:
    print(span.text())
  # Locating by id using attribute filtering.
  for input in page(id='testform').input:
    print(input.value())
  # Attribute filtering and access.
  text_input = page.input(type='text')
  print(text_input[0]['value'])
```

### Page factory and browser caching

```python
from seleniumsoup.page import PageFactory

url = 'http://faylixe.fr/seleniumsoup/testpage.html'

with PageFactory('firefox') as factory:
  with factory.page(url) as page:
    # ... Apply page processing here ...
```
