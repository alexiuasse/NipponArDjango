#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 12/08/2020 17:44.

from django.conf import settings
from django.db import models
from django.urls import reverse
from simple_history.models import HistoricalRecords

from .middleware import local


class BaseModel(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name='%(class)s_created_by', verbose_name="Criado por",
                                   help_text="Usuário que criou.")
    # updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
    #                                related_name='%(class)s_updated_by', verbose_name="Atualizado por",
    #                                help_text="Usuário que modificou.")
    created_in = models.DateField("criado em", auto_now_add=True, help_text="Data em que foi criado.")
    # updated_in = models.DateField("atualizado em", auto_now=True, help_text="Data em que foi atualizado.")
    history = HistoricalRecords(inherit=True)

    def save(self, *args, **kwargs):
        if self.pk is None and hasattr(local, 'user'):
            self.created_by = local.user
        # elif hasattr(local, 'user'):
        #     self.updated_by = local.user
        return super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True

    @property
    def get_delete_url(self):
        return reverse('{}:{}:delete'.format(self._meta.app_label, self._meta.model_name), kwargs={'pk': self.pk})

    @property
    def get_edit_url(self):
        return reverse('{}:{}:edit'.format(self._meta.app_label, self._meta.model_name), kwargs={'pk': self.pk})

    @property
    def get_back_url(self):
        return reverse('{}:{}:view'.format(self._meta.app_label, self._meta.model_name))
