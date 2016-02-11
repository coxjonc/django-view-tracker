import html
import re
import itertools
import logging

from bs4 import BeautifulSoup

from baseparser import BaseParser 

#begin logging settings
logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
#end logging settings


class KTParser(BaseParser):
    domains = ['www.khmertimeskh.com']
    feeder_pat = '^http://www.khmertimeskh.com/news/[^1]\d{4}/[\w]'
    feeder_pages = ['http://www.khmertimeskh.com']
    reporters = [
        'May Titthara',
        'Phun Chan Ousaphea'
        'Mom Kunthear',
        'Taing Vida',
        'Vannak Chea'
        'So Nyka'
        'Srey Kumneth',
        'Nou Sotheavy',
        'Sum Manet'
        'Va Sonyka',
        'Chea Vannak',
        'Pav Suy',
        'Ros Chanveasna',
        'Ven Rathavong',
        'Chea Takihiro',
        'Cheang Sokha',
        'Ban Sokrith',
        'Sok Chan',
        'James Reddick',
        'Vincent MacIsaac'
        'Jonathan Greig',
        'Maddy Crowell',
        'Jonathan Cox',
    ]

    def _parse(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        meta = soup.find_all('meta')
        # Get title
        try: 
            self.title = soup.find('h1', 
                attrs={'class':'title'}).get_text()
            logger.debug('Title: {}'.format(self.title.encode('ascii', 'ignore')))
        except:
            logger.debug('Parser couldn\'t find title')
            self.real_article = False
            return
        # Get views
        try: 
            views_str = soup.find('div', 
                attrs={'class':'view-count'}).get_text()
            self.views = [int(x) for x in views_str.split() if x.isdigit()][0]
            logger.debug('Views: {}'.format(self.views))
        except:
            logger.debug('Parser couldn\'t find views')
            self.real_article = False
            return
        # Get byline
        try: 
            full_byline = soup.find('div', 
                attrs={'class':'journalist'}).get_text()
            # Split byline into a list of words
            clean = re.findall(r'[\w]+', full_byline)
        except:
            logger.debug('No journalist class tag in markup')
            self.real_article = False
            return
        # If necessary, cut Khmer Times off front of byline
        if clean[0].lower() == 'khmer':
            try:
                clean = clean[2:]
            except:
                self.real_article = False
                logger.debug('Byline is just Khmer Times')
                return
        # If multiple reporters, split byline into sublists on 'and'
        clean_split = [list(g) for k,g in itertools.groupby(clean,lambda x:x == 'and') if not k]
        # It's possible for a byline to contain both staff and non-staff writers
        reporter_names = [' '.join(x) for x in clean_split if ' '.join(x) in self.reporters]
        if reporter_names:
            for x in reporter_names:
                logger.debug('Author: {}'.format(x))
                self.bylines.append(x)
        else:
            self.real_article = False
            logger.debug('No name in byline')
            return
