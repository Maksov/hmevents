from django.conf.urls import patterns, url

from events.views import TestPage


urlpatterns = patterns('',
    url(r'^test/$', TestPage.as_view(), name='test'),
)
