from django.conf.urls import include, url
from django.contrib import admin

from www.urls import router

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^', include('www.urls')),
]
