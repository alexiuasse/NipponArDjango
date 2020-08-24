#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 24/08/2020 15:30.

from base.models import BaseModel
from django.db import models
from django.urls import reverse


class Device(BaseModel):
    name = models.CharField("nome", max_length=128, blank=True)
    identifier = models.CharField("identificador", max_length=128, blank=True)
    patrimony = models.CharField("patrimônio", max_length=128, blank=True)
    observation = models.TextField("observações", blank=True)
    location = models.TextField("localização", blank=True)
    brand = models.ForeignKey("config.Brand", verbose_name="Marca", on_delete=models.SET_NULL, null=True, blank=True)
    model = models.ForeignKey("config.Model", verbose_name="Modelo", on_delete=models.SET_NULL, null=True, blank=True)
    type = models.ForeignKey("config.Type", verbose_name="Tipo", on_delete=models.SET_NULL, null=True, blank=True)
    capacity = models.ForeignKey("config.Capacity", verbose_name="Capacidade", on_delete=models.SET_NULL, null=True,
                                 blank=True)
    order_of_services = models.ManyToManyField("service.OrderOfService", verbose_name="Ordem de Serviços", blank=True)

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

    def get_new_service_url(self):
        cpk, ctp = self.get_cpk_ctp_customer()
        return reverse('service:create', kwargs={'cpk': cpk, 'ctp': ctp, 'dev': self.pk})

    def get_full_name(self):
        return "{} {} {} {} BTU".format(
            self.type if self.type else "",
            self.brand if self.brand else "",
            self.model if self.model else "",
            self.capacity if self.capacity else ""
        )

    def get_category_name(self):
        return "Cliente {}".format(self.get_customer())

    def get_dict_data(self):
        return {
            'Nome': self.get_full_name(),
            'Identificador': self.identifier,
            'Patrimônio': self.patrimony,
            'Localização': self.location,
            'Observação': self.observation,
        }

    def get_service_sorted_by_entry_date(self):
        retDict = {}
        for s in self.order_of_services.all().order_by('-date', '-id'):
            m_y = "{}/{}".format(s.date.month, s.date.year)
            if m_y in retDict:
                retDict[m_y]['services'].append(s)
            else:
                retDict[m_y] = {}
                retDict[m_y]['services'] = []
                retDict[m_y]['services'].append(s)
        return retDict
