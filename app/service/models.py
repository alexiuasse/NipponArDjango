#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 02/08/2020 12:00.
from datetime import datetime

from base.models import BaseModel
from django.db import models
from django.urls import reverse

from .enums import ServiceStatusEnum


class OrderOfService(BaseModel):
    type_of_service = models.ForeignKey("config.TypeOfService", verbose_name="Tipo de Serviço",
                                        on_delete=models.SET_NULL, null=True)
    status = models.IntegerField("Status", choices=ServiceStatusEnum.choices(), default=0)
    parts = models.ManyToManyField("config.DeviceParts", verbose_name="Peças", blank=True)
    start_date = models.DateField("data de início", default=datetime.today)
    end_date = models.DateField("data de término", blank=True, null=True)
    defect = models.TextField("defeito", blank=True)
    observation = models.TextField("observação", blank=True)

    def __str__(self):
        return "{}".format(self.type_of_service)

    def get_device(self):
        return self.device_set.all().first()

    def get_absolute_url(self):
        device = self.get_device()
        cpk, ctp = device.get_cpk_ctp_customer()
        return reverse('service:profile', kwargs={'cpk': cpk, 'ctp': ctp, 'dev': device.pk, 'pk': self.pk})

    def get_delete_url(self):
        device = self.get_device()
        cpk, ctp = self.get_device().get_cpk_ctp_customer()
        return reverse('service:delete', kwargs={'cpk': cpk, 'ctp': ctp, 'dev': device.pk, 'pk': self.pk})

    def get_edit_url(self):
        device = self.get_device()
        cpk, ctp = self.get_device().get_cpk_ctp_customer()
        return reverse('service:edit', kwargs={'cpk': cpk, 'ctp': ctp, 'dev': device.pk, 'pk': self.pk})

    def get_back_url(self):
        device = self.get_device()
        cpk, ctp = self.get_device().get_cpk_ctp_customer()
        return reverse('device:profile', kwargs={'cpk': cpk, 'ctp': ctp, 'pk': device.pk})

    def get_full_name(self):
        return "{}".format(self.type_of_service)

    def get_dict_data(self):
        return {
            'Tipo de Serviço': "{}".format(self.type_of_service),
            'Status': self.status,
            'Peças': self.parts,
            'Data de Início': self.start_date,
            'Data de Término': self.end_date,
            'Defeito': self.defect,
            'Observação': self.observation,
        }
