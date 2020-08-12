#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 12/08/2020 15:38.

from base.models import BaseModel
from django.db import models
from django.urls import reverse

from .enums import StateEnum


# class MyModelManager(models.Manager):
#     def get_queryset(self):
#         return super(MyModelManager, self).get_queryset().order_by('name')


class Customer(BaseModel):
    email = models.EmailField(max_length=254, blank=True)
    phone_1 = models.CharField("telefone", max_length=15, blank=True)
    phone_2 = models.CharField("celular", max_length=15, blank=True)
    street = models.CharField("Rua", max_length=128, blank=True)
    number = models.CharField("Número", max_length=10, blank=True)
    neighborhood = models.CharField("Bairro", max_length=128, blank=True)
    apartment = models.CharField("Apartamento", max_length=10, blank=True)
    block = models.CharField("Bloco", max_length=128, blank=True)
    city = models.ForeignKey("config.City", verbose_name="Cidade", on_delete=models.SET_NULL, null=True, blank=True)
    state = models.CharField("Estado", max_length=2, choices=StateEnum.choices(), blank=True)
    cep = models.CharField("CEP", max_length=9, blank=True)
    address_line = models.CharField("Endereço", max_length=256, blank=True)
    devices = models.ManyToManyField("device.Device", verbose_name="Equipamentos", blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.address_line = "{}, {}, {}, {}, {}, {} - {}, {}".format(self.street, self.number, self.neighborhood,
                                                                     self.apartment, self.block, self.city, self.state,
                                                                     self.cep)
        super(Customer, self).save(*args, **kwargs)

    def get_full_name(self):
        return self.name

    def get_personal_to_dict(self):
        return {
            'Nome': self.name,
            'CPF' if hasattr(self, 'cpf') else 'CNPJ': self.cpf if hasattr(self, 'cpf') else self.cnpj,
            'Telefone': self.phone_1,
            'Celular': self.phone_2,
            'E-mail': self.email,
        }

    def get_category_name(self):
        return "{}".format(self.address_line)

    def get_address_to_dict(self):
        return {
            'Endereço': self.address_line,
            'Rua': self.street,
            'Número': self.number,
            'Bairro': self.neighborhood,
            'Apt': self.apartment,
            'Bloco': self.block,
            'Cidade': self.city,
            'Estado': self.state,
            'CEP': self.cep,
        }

    def get_absolute_url(self):
        return reverse('{}:profile'.format(self._meta.app_label), kwargs={'pk': self.pk, 'tp': self.type})


class IndividualCustomer(Customer):
    name = models.CharField("nome", max_length=128)
    cpf = models.CharField("CPF", max_length=14, blank=True)
    type = models.IntegerField(default=0)


class JuridicalCustomer(Customer):
    name = models.CharField("razão Social", max_length=128)
    cnpj = models.CharField("CNPJ", max_length=18, blank=True)
    parent_company = models.ForeignKey("customer.JuridicalCustomer", verbose_name="Matriz", on_delete=models.CASCADE,
                                       null=True, blank=True, help_text="Qual a matriz dessa empresa?")
    type = models.IntegerField(default=1)
