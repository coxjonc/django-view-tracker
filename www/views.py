import os

from django.shortcuts import render, HttpResponse

from react.render import render_component

from .models import Byline

def index(request):
    rendered = render_component(os.path.join(os.getcwd(), 'assets', 'js', 'index.js'), {'foo':'bar'})
    return render(request, 'www/index.html', {'rendered':rendered})