from django.contrib.auth.models import User, Group
from django.db.models import Count
from .models import Server, Uptime, ServerHeartbeat
from rest_framework import viewsets
from project.api.serializers import UserSerializer, GroupSerializer, ServerSerializer, UptimeSerializer, ServerHeartbeatSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def serverheartbeat_view(request, format=None):

    if request.method == 'GET':
        serverheartbeat = ServerHeartbeat.objects.all()
        serializer = ServerHeartbeatSerializer(serverheartbeat, many=True)
        common_status = ServerHeartbeat.objects.all().count()
        uptime = ServerHeartbeat.objects.values('ServerFQDN').order_by().annotate(the_count=Count('Timestamp'))
#        count = 1000
#        uptime = float(common_status) / 60 * 24
        return Response(uptime)

    elif request.method == 'POST':
        serializer = ServerHeartbeatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'POST'])
def server_list(request, format=None):

    if request.method == 'GET':
        server = Server.objects.all()
        serializer = ServerSerializer(server, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ServerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def server_detail(request, pk):

    try:
        server = Server.objects.get(pk=pk)
    except Server.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ServerSerializer(server)
        return Response(serializer.data)


    elif request.method == 'PUT':
        serializer = ServerSerializer(server, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        server.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




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

