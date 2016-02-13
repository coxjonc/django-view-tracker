import requests
import re
import socket
import time
from bs4 import BeautifulSoup

# Begin utility functions

def grab_url(url, max_depth=5):
    retry = False
    try: 
        text = requests.get(url, timeout=5, allow_redirects=False)
    except requests.exceptions.ConnectionError:
        retry = True
    if retry:
        if max_depth == 0:
            raise Exception('Too many attempts to downoad {}'.format(url))
        time.sleep(0.5)
        return grab_url(url, max_depth-1)
    return text

def concat(domain, url):
    return domain + url if url.startswith('/') else domain + '/' + url

# End utility functions

# Base Parser
# To create a new parser, subclass and define _parse(html)
class BaseParser(object):
    url = None
    domains = [] # List of domains this should parse
    reporters = []

    # These should be filled in by self._parse(html)
    title = None
    bylines = None
    views = None
    pub_date = None

    real_article = True # If set to False, ignore this article

    # Used when finding articles to parse
    feeder_pat = None # Look for links matching this regular expression
    feeder_pages = [] # On these pages

    feeder_bs = BeautifulSoup # Use this version of Beautiful Soup

    def __init__(self, url):
        self.url = url
        self.html = grab_url(self.url)
        if self.html.status_code != requests.codes.ok:
            self.real_article = False
            return
        self._parse(self.html.content)

    def _parse(self, html):
        """
        Should take html and populate self.(date, title, byline, views)
        If the article ain't valid, set self.real_article to False and return
        """
        raise NotImplementedError()

    @classmethod
    def feed_urls(cls):
        all_urls = []
        for feeder_url in cls.feeder_pages:
            html = grab_url(feeder_url).content
            soup = cls.feeder_bs(html, 'html.parser')

            urls = [a.get('href') for a in soup.find_all('a')]
            domain = '/'.join(feeder_url.split('/')[:3])
            urls = [url.strip() if '://' in url else concat(domain, url) for url in urls]

            all_urls = all_urls + [url for url in urls if
                                        re.search(cls.feeder_pat, url)]

            return all_urls
