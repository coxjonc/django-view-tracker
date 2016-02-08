import datetime

from django.db import models
from django.utils import timezone

class Byline(models.Model):
    name = models.CharField(max_length=250, unique=True)
    view_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['-view_count']

    def get_view_count(self):
        self.view_count = sum([x.views for x in self.articles.all()])

    def __unicode__(self):
        return self.name

class Article(models.Model): 
    byline = models.ForeignKey(Byline, related_name='articles', null=True)
    boring = models.BooleanField()
    url = models.URLField(max_length=300, unique=True)
    title = models.CharField(max_length=250, null=True)
    views = models.IntegerField(null=True) 
    last_updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['-views']

    def boring(self):
        return self.last_updated <= timezone.now() - datetime.timedelta(days=7)

    def __unicode__(self):
        return self.url