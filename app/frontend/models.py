#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 10/08/2020 11:56.
from django.db import models


class NotificationsMessages(models.Model):
    text = models.CharField(max_length=128, blank=True, null=True)
    link = models.CharField(max_length=128, blank=True, null=True)
    show = models.BooleanField(default=True)
    important = models.BooleanField(default=False)
