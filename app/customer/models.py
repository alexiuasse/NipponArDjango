#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 17/07/2020 11:56.

from base.models import BaseModel
from django.db import models


class Customer(BaseModel):
    name = models.CharField("nome", max_length=128)

    def __str__(self):
        return self.name


class Address(BaseModel):
    customer = models.ForeignKey(Customer, verbose_name="Cliente", on_delete=models.CASCADE)

    def __str__(self):
        return self.customer
