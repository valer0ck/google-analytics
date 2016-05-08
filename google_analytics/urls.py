from django.conf.urls import patterns, include, url
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'', include('google_analytics.analytics.urls')),
    url(r'^admin/', admin.site.urls),
]
