#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 31/07/2020 13:06.

from datetime import datetime

from base.models import BaseModel
from django.db import models
from django.urls import reverse


class Device(BaseModel):
    name = models.CharField("nome", max_length=128, blank=True)
    identifier = models.CharField("identificador", max_length=128, blank=True)
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

    def get_customer(self):
        return self.individualcustomer_set.all().first() if self.individualcustomer_set.all().first() \
            else self.juridicalcustomer_set.all().first()

    def get_cpk_ctp_customer(self):
        customer = self.get_customer()
        return customer.pk, customer.type

    def get_absolute_url(self):
        cpk, ctp = self.get_cpk_ctp_customer()
        return reverse('device:profile', kwargs={'cpk': cpk, 'ctp': ctp, 'pk': self.pk})

    def get_delete_url(self):
        cpk, ctp = self.get_cpk_ctp_customer()
        return reverse('device:delete', kwargs={'cpk': cpk, 'ctp': ctp, 'pk': self.pk})

    def get_edit_url(self):
        cpk, ctp = self.get_cpk_ctp_customer()
        return reverse('device:edit', kwargs={'cpk': cpk, 'ctp': ctp, 'pk': self.pk})

    def get_back_url(self):
        cpk, ctp = self.get_cpk_ctp_customer()
        return reverse('customer:profile', kwargs={'pk': cpk, 'tp': ctp})

    def get_full_name(self):
        return "{} {} {} {} BTU".format(self.type, self.brand, self.model, self.capacity)

    def get_dict_data(self):
        return {
            'Nome': "{} {} {} {} BTU".format(self.type, self.brand, self.model, self.capacity),
            'Identificador': self.identifier,
            'Patrimônio': self.patrimony,
            'Data de Entrada': self.entry_date,
            'Data de Saída': self.departure_date,
            'Localização': self.location,
            'Observação': self.observation,
        }
