from django.contrib.auth.models import User, Group
from django.db.models import Count, FloatField, DecimalField
from django.db.models.functions import Cast
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
        uptime = ServerHeartbeat.objects.values('ServerFQDN').order_by().annotate(uptime=Cast(Count('Timestamp') / ( 60.0 * 24.0  ), DecimalField(max_digits=5, decimal_places=2)))
        full_answer=[]
        for i in uptime:
            local_dict = {}
            local_dict['serverfqdn'] = i['ServerFQDN']
            local_dict['uptime'] = i['uptime']
            full_answer.append(local_dict)


        return Response(full_answer)

    elif request.method == 'POST':
        serializer = ServerHeartbeatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



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

