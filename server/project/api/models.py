# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class ServerHeartbeat(models.Model):
    ServerFQDN = models.CharField(max_length=255, null=False)
    Timestamp = models.DateTimeField(auto_now_add=True)

# Create your models here.
