from rest_framework import serializers

from django.contrib.auth.models import User

from .models import Byline, Article

class BylineSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Byline
        fields = ('name', 'articles', 'most_viewed_all_time', 'most_viewed_weekly', 'all_views', 'weekly_views', 'all_time_rank') 

class ArticleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Article
        fields = ('url', 'bylines', 'boring', 'title', 'views', 'last_updated', 'pub_date')
