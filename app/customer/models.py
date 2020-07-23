#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 22/07/2020 22:52.

from base.models import BaseModel
from django.db import models
from django.urls import reverse

from .utils import StateEnum


class Customer(BaseModel):
    name = models.CharField("nome", max_length=128)
    email = models.EmailField(max_length=254, blank=True)
    phone_1 = models.CharField("telefone 1", max_length=15, blank=True)
    phone_2 = models.CharField("telefone 2", max_length=15, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('customer-edit', kwargs={'pk': self.pk})

    @property
    def del_url(self):
        return 'customer-del'

    @property
    def edit_url(self):
        return 'customer-edit'


class CustomerAddress(BaseModel):
    customer = models.ForeignKey(Customer, verbose_name="Cliente", on_delete=models.CASCADE)
    street = models.CharField("Rua", max_length=128, blank=True)
    number = models.CharField("Número", max_length=10, blank=True)
    city = models.ForeignKey("config.City", verbose_name="Cidade", on_delete=models.SET_NULL, null=True, blank=True)
    state = models.CharField("Estado", max_length=2, choices=StateEnum.choices(), blank=True)
    cep = models.CharField("CEP", max_length=9, blank=True)
    address_line = models.CharField("Endereço", max_length=256, blank=True)

    def __str__(self):
        return self.customer

    def get_absolute_url(self):
        return reverse('customer-address-edit', kwargs={'pk': self.pk})

    @property
    def del_url(self):
        return 'customer-address-del'

    @property
    def edit_url(self):
        return 'customer-address-edit'
