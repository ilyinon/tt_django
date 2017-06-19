from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework import routers
from project.api import views

#router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)
#router.register(r'server', views.ServerViewSet)
#router.register(r'uptime', views.UptimeViewSet)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', views.serverheartbeat_view),
    url(r'^status/$', views.serverheartbeat_status),
]
urlpatterns = format_suffix_patterns(urlpatterns)

#urlpatterns = patterns(
#    'api.views',
#    url(r'^server/$', 'server_list', name='serverlist'),
#    url(r'^server/(?P<pk>[0-9]+)$', 'task_detail', name='task_detail'),
#)
