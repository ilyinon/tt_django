# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Server(models.Model):
    fqdn = models.CharField(max_length=255, null=False)

class Uptime(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name='+',)
    timespamp = models.DateTimeField('timespamp')

class ServerHeartbeat(models.Model):
    ServerFQDN = models.CharField(max_length=255, null=False)
    Timestamp = models.DateTimeField(auto_now_add=True)

# Create your models here.
