# Seleniumsoup

[![CircleCI](https://circleci.com/gh/Faylixe/seleniumsoup.svg?style=svg)](https://circleci.com/gh/Faylixe/seleniumsoup)

Selenium soup is a wrapper for selenium framework which allows to manipulate webpage as Python object.

# Sample

```python
from seleniumsoup.vegetable import Page

url = 'https://cbracco.github.io/html5-test-page/'

with Page(url) as page:
    for link in page.nav.a:
      print(link.text())
```
