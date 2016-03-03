from django.conf.urls import include, url

from www.urls import router

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^', include('www.urls')),
]
