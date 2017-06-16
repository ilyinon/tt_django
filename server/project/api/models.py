# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Server(models.Model):
    fqdn = models.CharField(max_length=255, null=False)

class Uptime(models.Model):
    server = models.ForeignKey(Server, related_name='fqdn')
    timespamp = models.DateTimeField('timespamp')

# Create your models here.
