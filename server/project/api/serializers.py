from django.contrib.auth.models import User, Group
from .models import Server, Uptime, ServerHeartbeat
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ServerHeartbeatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServerHeartbeat
        fields = ('ServerFQDN', 'Timestamp')

class ServerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Server
        fields = ('id', 'fqdn')

class UptimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Uptime
        fields = ('server', 'timespamp')

