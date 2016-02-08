import datetime

from django.core.management.base import BaseCommand
from django.utils import timezone

from parsers import kt

from www.models import Article, Byline


class Command(BaseCommand):
    help = """Scrape websites.

    By default, scan front pages for new articles, and scan existing articles
    to record changes in the view count.

    Articles older than a certain range are skipped.
    """
    def handle(self, *args, **options):
        update_articles_list()
        update_article_views()
        update_counts()

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
    for article in Article.objects.all():
        if article.boring == True:
            continue
        parsed_article = load_article(article.url)
        if parsed_article is None:
            continue
        try:
            a = Article.objects.get(url=parsed_article.url)
        except:
            continue
        if a.views == parsed_article.views and a.boring(): 
            a.boring = True
        else:
            print parsed_article.title
            a.title = parsed_article.title
            a.views = parsed_article.views
            byline = Byline.objects.get_or_create(name=parsed_article.byline)
            a.byline = byline[0]
            a.save()

def update_articles_list():
    all_urls = get_all_article_urls()
    for url in all_urls:
        Article.objects.get_or_create(url=url)

def update_counts():
    for byline in Byline.objects.all():
        byline.get_view_count()
        byline.save()
