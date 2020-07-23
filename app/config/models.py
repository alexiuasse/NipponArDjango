#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 22/07/2020 17:23.

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

    def get_absolute_url(self):
        return reverse('config-type-edit', kwargs={'pk': self.pk})

    @property
    def del_url(self):
        return 'config-type-del'

    @property
    def edit_url(self):
        return 'config-type-edit'


class Capacity(BaseConfigModel):

    def get_absolute_url(self):
        return reverse('config-capacity-edit', kwargs={'pk': self.pk})

    @property
    def del_url(self):
        return 'config-capacity-del'

    @property
    def edit_url(self):
        return 'config-capacity-edit'


class City(BaseConfigModel):

    def get_absolute_url(self):
        return reverse('config-city-edit', kwargs={'pk': self.pk})

    @property
    def del_url(self):
        return 'config-city-del'

    @property
    def edit_url(self):
        return 'config-city-edit'
