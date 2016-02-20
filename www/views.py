import os
import datetime
from collections import OrderedDict

from django.shortcuts import render, HttpResponse
from django.utils import timezone
from django.db.models import Max

from rest_framework import viewsets

from .models import Byline, Article
from .serializers import BylineSerializer, ArticleSerializer

class BylineViewSet(viewsets.ModelViewSet):
    """API endpoint for listing information
    about reporters"""
    queryset = Byline.objects.all()
    serializer_class = BylineSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    """API endpoint for listing information
    about articles"""
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
