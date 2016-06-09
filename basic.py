
from seleniumsoup.browser import Browser

if __name__ == '__main__':
    browser = Browser('http://google.fr')
    form = browser('tsf')
