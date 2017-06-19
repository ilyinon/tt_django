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
    url(r'^server/$', views.server_list),
    url(r'^server/(?P<pk>[0-9]+)$', views.server_detail),
#    url(r'^', include(router.urls)),
#    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#    url(r'^server/$', server_list, name='server-list'),
]
urlpatterns = format_suffix_patterns(urlpatterns)

#urlpatterns = patterns(
#    'api.views',
#    url(r'^server/$', 'server_list', name='serverlist'),
#    url(r'^server/(?P<pk>[0-9]+)$', 'task_detail', name='task_detail'),
#)
