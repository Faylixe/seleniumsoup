# Seleniumsoup

[![CircleCI](https://circleci.com/gh/Faylixe/seleniumsoup.svg?style=svg)](https://circleci.com/gh/Faylixe/seleniumsoup) [![Code Health](https://landscape.io/github/Faylixe/seleniumsoup/master/landscape.svg?style=plastic)](https://landscape.io/github/Faylixe/seleniumsoup/master)

* [Installation](#installation)
* [Usage](#usage)
  * [Simple page Parsing](#simple-page-parsing)
  * [Accessing elements](#accesing-elements)
  * [Page factory and browser caching](#page-factory-and-browser-caching)

Selenium soup is a wrapper for selenium framework which allows to manipulate webpage as Python object.

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
