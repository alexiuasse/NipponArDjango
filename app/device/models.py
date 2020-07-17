#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 12/07/2020 20:01.

from django.db import models
from base.models import BaseModel

class Device(BaseModel):
    name = models.CharField("nome", max_length=128, blank=True)
    patrimony = models.CharField("patrimônio", max_length=128, blank=True)
    entry_date = models.DateField("data de entrada", blank=True)
    departure_date = models.DateField("data de saída", blank=True)
    observation = models.TextField("observações", blank=True)

    customer = models.ForeignKey("customer.Customer", verbose_name="Cliente", on_delete=models.CASCADE)
    brand = models.ForeignKey("config.Brand", verbose_name="Marca", on_delete=models.SET_NULL, null=True)
    model = models.ForeignKey("config.Model", verbose_name="Modelo", on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey("config.Type", verbose_name="Tipo", on_delete=models.SET_NULL, null=True)
    capacity = models.ForeignKey("config.Capacity", verbose_name="Capacidade", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
