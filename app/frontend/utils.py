#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 10/08/2020 12:04.
from datetime import datetime

from config.models import StatusService
from service.models import OrderOfService

from .models import *


def context_dashboard():
    status = {}
    for s in StatusService.objects.all():
        status[s.name] = {
            'name': s.name,
            'obj': s,
            'services': OrderOfService.objects.filter(status=s, date__month=datetime.today().month).count()
        }
    notifications = {
        'quantity': NotificationsMessages.objects.count(),
    }
    for n in NotificationsMessages.objects.filter(show=True):
        notifications[n.pk] = {
            'text': n.text,
            'link': n.link,
            'important': n.important,
        }
    return {
        'status': status,
        'notifications': notifications,
    }
