import os
import datetime
from collections import OrderedDict

from django.shortcuts import render, HttpResponse
from django.utils import timezone
from django.db.models import Max

from .models import Byline, Article

def index(request):

    byl_dict = {}

# Begin utility functions
    
    def all_time_views(byl):
        articles = byl.articles.all()
        return sum([x.views for x in articles])
    
    def all_time_most_viewed(byl):
        articles = byl.articles.all()
        max_views = articles.aggregate(Max('views'))
        all_time_most_viewed = articles.filter(views=max_views['views__max'])[0]
        return all_time_most_viewed

    def weekly_views(byl):
        articles = byl.articles.filter(pub_date__gte=timezone.now()-datetime.timedelta(days=7))
        return sum([x.views for x in articles])
        
    def weekly_most_viewed(byl):
        articles = byl.articles.filter(pub_date__gte=timezone.now()-datetime.timedelta(days=7))
        max_views = articles.aggregate(Max('views'))
        return articles.filter(views=max_views['views__max'])[0]
    
# End utility functions

    for author in Byline.objects.all():

        byl_dict[author.name] = [
            ('all time views', all_time_views(author)),
            ('all time most viewed', all_time_most_viewed(author)),
            ('views this week', weekly_views(author)),
            ('most viewed this week', weekly_most_viewed(author)),
        ]
    print byl_dict
    return render(request, 'index.html', {'bylines': byl_dict})
