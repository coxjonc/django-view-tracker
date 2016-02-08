from django.shortcuts import render, HttpResponse

from .models import Byline

def scores(request):
    return HttpResponse('ok')
    #return render(request, 'www/index.html', {'bylines':Byline.objects.all()})