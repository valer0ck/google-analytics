from django.conf.urls import patterns, url
from google_analytics.analytics.views import *

urlpatterns = patterns('google_analytics.analytics.views',
    url(r'', 'analytics', name="analytics"),
)
