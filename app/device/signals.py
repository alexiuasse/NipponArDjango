#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 24/08/2020 17:57.
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from .models import Device


@receiver(pre_delete, sender=Device)
def device_forward_delete(sender, instance, using, **kwargs):
    for o in instance.order_of_services.all():
        o.delete()
