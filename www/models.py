import datetime

from django.db import models
from django.db.models import Max
from django.utils import timezone
from django.template.defaultfilters import slugify 

class Byline(models.Model):
    name = models.CharField(max_length=250, unique=True)    
    most_viewed_all_time = models.ForeignKey('Article', null=True, related_name='all_time_most_viewed')
    most_viewed_weekly = models.ForeignKey('Article', null=True, related_name='weekly_most_viewed')
    all_views = models.IntegerField(null=True)
    weekly_views = models.IntegerField(null=True)
    weekly_rank = models.IntegerField(null=True)
    all_time_rank = models.IntegerField(null=True)

    class Meta: 
        ordering = ['-all_views']

    def __unicode__(self):
        return self.name

    def update(self, *args, **kwargs):
        
        #calculate all time statistics        
        all_articles = self.articles.all()
        max_views = all_articles.aggregate(Max('views'))
        self.most_viewed_all_time = all_articles.filter(views=max_views['views__max'])[0]
        self.all_views = sum([x.views for x in all_articles if x.views])

        #calculate weekly statistics
        week_articles = self.articles.filter(pub_date__gte=timezone.now()-datetime.timedelta(days=7))
        max_views = week_articles.aggregate(Max('views'))
        try:
            self.most_viewed_weekly = week_articles.filter(views=max_views['views__max'])[0]
            self.weekly_views = sum([x.views for x in week_articles])
        except IndexError:
            pass

        super(Byline, self).save(*args, **kwargs)

    

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
