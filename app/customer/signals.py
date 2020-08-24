#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 24/08/2020 17:54.
from django.db.models.signals import post_delete, pre_delete
from django.dispatch import receiver

from .models import IndividualCustomer, JuridicalCustomer


@receiver(pre_delete, sender=IndividualCustomer)
def individualcustomer_forward_delete(sender, instance, using, **kwargs):
    for o in instance.devices.all():
        o.delete()


@receiver(pre_delete, sender=JuridicalCustomer)
def juridicalcustomer_forward_delete(sender, instance, using, **kwargs):
    for o in instance.devices.all():
        o.delete()
