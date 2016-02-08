from bs4 import BeautifulSoup
import html

from baseparser import BaseParser 


class KTParser(BaseParser):
    domains = ['www.khmertimeskh.com']
    feeder_pat = '^http://www.khmertimeskh.com/news/[^1]\d{4}/[\w]'
    feeder_pages = ['http://www.khmertimeskh.com']

    def _parse(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        meta = soup.find_all('meta')
        try:
            self.title = soup.find('h1', 
                                   attrs={'class':'title'}).get_text()
            views_str = soup.find('div', 
                                  attrs={'class':'view-count'}).get_text()
            self.views = [int(x) for x in views_str.split() if x.isdigit()][0]
            full_byline = soup.find('div', 
                               attrs={'class':'journalist'}).get_text()
            clean = full_byline.strip()
            name = ' '.join(clean.split()[3:])
            if name != '':
                self.byline = name
            else: 
                self.real_article = False
                return
        except:
            self.real_article = False
            return