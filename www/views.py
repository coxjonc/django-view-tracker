from django.shortcuts import render

from .models import Byline

def scores(request):
    return render(request, 'www/index.html', {'bylines':Byline.objects.all()})