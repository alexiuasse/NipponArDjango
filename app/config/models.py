#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 31/07/2020 14:45.

from base.models import BaseModel
from django.db import models
from django.urls import reverse, reverse_lazy


class BaseConfigModel(BaseModel):
    name = models.CharField("nome", max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

    def get_absolute_url(self):
        return reverse_lazy('{}:{}:view'.format(self._meta.app_label, self._meta.model_name))


class Brand(BaseConfigModel):
    pass


class Model(BaseConfigModel):
    pass


class Type(BaseConfigModel):
    pass


class Capacity(BaseConfigModel):
    pass


class City(BaseConfigModel):
    pass
