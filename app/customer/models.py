#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 25/07/2020 16:27.

from base.models import BaseModel
from django.db import models
from django.urls import reverse

from .utils import StateEnum


# class MyModelManager(models.Manager):
#     def get_queryset(self):
#         return super(MyModelManager, self).get_queryset().order_by('name')


class Customer(BaseModel):
    name = models.CharField("nome", max_length=128)
    email = models.EmailField(max_length=254, blank=True)
    phone_1 = models.CharField("telefone 1", max_length=15, blank=True)
    phone_2 = models.CharField("telefone 2", max_length=15, blank=True)
    cpf = models.CharField("CPF", max_length=14, blank=True)
    cnpj = models.CharField("CNPJ", max_length=18, blank=True)

    street = models.CharField("Rua", max_length=128, blank=True)
    number = models.CharField("Número", max_length=10, blank=True)
    neighborhood = models.CharField("Bairro", max_length=128, blank=True)
    apartment = models.CharField("Apartamento", max_length=10, blank=True)
    block = models.CharField("Bloco", max_length=128, blank=True)
    city = models.ForeignKey("config.City", verbose_name="Cidade", on_delete=models.SET_NULL, null=True, blank=True)
    state = models.CharField("Estado", max_length=2, choices=StateEnum.choices(), blank=True)
    cep = models.CharField("CEP", max_length=9, blank=True)
    address_line = models.CharField("Endereço", max_length=256, blank=True)
    parent_company = models.ForeignKey("customer.Customer", verbose_name="Matriz", on_delete=models.SET_NULL, null=True,
                                       blank=True,
                                       help_text="Qual a matriz dessa empresa?")

    # objects = MyModelManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('customer-edit', kwargs={'pk': self.pk})

    @property
    def get_address(self):
        return "%s, %s" % (self.street, self.number)

    @property
    def del_url(self):
        return 'customer-del'

    @property
    def edit_url(self):
        return 'customer-edit'
