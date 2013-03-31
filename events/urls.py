from django.conf.urls import patterns, url

from events.views import TestPage


urlpatterns = patterns('',
    url(r'^$', TestPage.as_view(), name='test'),
)
