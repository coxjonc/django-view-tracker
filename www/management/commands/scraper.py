import datetime
import logging

from django.core.management.base import BaseCommand
from django.utils import timezone

from www.parsers import kt
from www.models import Article, Byline
        
class Command(BaseCommand):
    help = """Scrape Khmer Times.

    By default, scan the front page for new articles, and scan existing articles
    to record changes in the view count.

    Articles whose views haven't changed since the last scrape, 
    and which are more than one week old, are skipped.
    """
    def handle(self, *args, **options):
        update_article_views()

def get_all_article_urls():
    ans = set()
    urls = kt.KTParser.feed_urls()
    ans = ans.union(urls)
    return ans

def load_article(url):
    try:
        parser = kt.KTParser
    except KeyError:
        return
    parsed_article = parser(url)
    if not parsed_article.real_article:
        return
    return parsed_article

def update_article_views():
    for url in get_all_article_urls():
        parsed_article = load_article(url)        
        if parsed_article is None:
            continue
        a = Article.objects.get_or_create(url=parsed_article.url)[0]
        if a.views == parsed_article.views and a.outdated(): 
            a.boring = True
        else:
            a.title = parsed_article.title
            a.views = parsed_article.views
            a.pub_date = parsed_article.pub_date
            for name in parsed_article.bylines:
                byline = Byline.objects.get_or_create(name=name)
                a.bylines.add(byline[0])
                byline[0].update()
            a.save()
