# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Servers(models.Model):
    fqdn = models.CharField(max_length=255, null=False)
    time

class Uptime(models.Model):
    server = models.ForeignKey(Servers, related_name='fqdn')
    timespamp = models.DateTimeField('timespamp')

# Create your models here.
