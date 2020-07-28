#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 28/07/2020 10:04.

from datetime import datetime

from base.models import BaseModel
from django.db import models
from django.urls import reverse


class Device(BaseModel):
    name = models.CharField("nome", max_length=128, blank=True)
    patrimony = models.CharField("patrimônio", max_length=128, blank=True)
    entry_date = models.DateField("data de entrada", default=datetime.today, blank=True)
    departure_date = models.DateField("data de saída", blank=True, null=True)
    observation = models.TextField("observações", blank=True)
    location = models.TextField("localização", blank=True)
    brand = models.ForeignKey("config.Brand", verbose_name="Marca", on_delete=models.SET_NULL, null=True)
    model = models.ForeignKey("config.Model", verbose_name="Modelo", on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey("config.Type", verbose_name="Tipo", on_delete=models.SET_NULL, null=True)
    capacity = models.ForeignKey("config.Capacity", verbose_name="Capacidade", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.patrimony

    def get_absolute_url(self):
        return reverse('device-edit', kwargs={'pk': self.pk})

    @property
    def del_url(self):
        return 'device-del'

    @property
    def edit_url(self):
        return 'device-edit'
