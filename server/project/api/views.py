from django.contrib.auth.models import User, Group
from .models import Server, Uptime
from rest_framework import viewsets
from project.api.serializers import UserSerializer, GroupSerializer, ServerSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ServerViewSet(viewset.ModelViewSet):
    """
    API endpoint that allows servers to be viewed or edited.
    """
    queryset = Server.objects.all()
    serializer_class = ServerSerializer

