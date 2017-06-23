from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework import routers
from project.api import views

urlpatterns = [
    url(r'^status/$', views.serverheartbeat_view),
]
urlpatterns = format_suffix_patterns(urlpatterns)
