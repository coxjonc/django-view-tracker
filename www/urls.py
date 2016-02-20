from django.conf.urls import url
from django.views.generic import TemplateView

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'bylines', views.BylineViewSet)
router.register(r'articles', views.ArticleViewSet)

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='www/all-stats.html'))
]
