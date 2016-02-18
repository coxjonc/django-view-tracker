import datetime

from django.db import models
from django.db.models import Max
from django.utils import timezone

class Byline(models.Model):
    name = models.CharField(max_length=250, unique=True)    

    class Meta: 
        ordering = ['name']

    def __unicode__(self):
        return self.name

class Article(models.Model): 
    bylines = models.ManyToManyField(Byline, related_name='articles')
    boring = models.BooleanField(default=False)
    url = models.URLField(max_length=300, unique=True)
    title = models.CharField(max_length=250, null=True)
    views = models.IntegerField(null=True) 
    last_updated = models.DateTimeField(auto_now=True, null=True)
    pub_date = models.DateTimeField(null=True)

    class Meta:
        ordering = ['-views']
        get_latest_by = 'last_updated'

    def outdated(self, views):
        return self.last_updated <= timezone.now() - datetime.timedelta(days=7)

    def __unicode__(self):
        return self.title
