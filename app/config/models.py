#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 18/07/2020 11:57.

from base.models import BaseModel
from django.db import models
from django.urls import reverse


class BaseConfigModel(BaseModel):
    name = models.CharField("nome", max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Brand(BaseConfigModel):

    def get_absolute_url(self):
        return reverse('config-brand-edit', kwargs={'pk': self.pk})

    @property
    def del_url(self):
        return 'config-brand-del'

    @property
    def edit_url(self):
        return 'config-brand-edit'


class Model(BaseConfigModel):

    def get_absolute_url(self):
        return reverse('config-model-edit', kwargs={'pk': self.pk})

    @property
    def del_url(self):
        return 'config-model-del'

    @property
    def edit_url(self):
        return 'config-model-edit'


class Type(BaseConfigModel):
    pass


class Unit(BaseConfigModel):
    pass


class Capacity(BaseConfigModel):
    unit = models.ForeignKey(Unit, verbose_name="Unidade", on_delete=models.CASCADE, null=True)
