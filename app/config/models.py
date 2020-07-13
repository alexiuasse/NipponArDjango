from django.db import models
from base.models import BaseModel

class BaseConfigModel(BaseModel):
    name = models.CharField("nome", max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class Brand(BaseConfigModel):

    @property
    def del_url(self):
        return 'config-brand-del'

    @property
    def edit_url(self):
        return 'config-brand-edit'

class Model(BaseConfigModel):
    pass

class Type(BaseConfigModel):
    pass

class Unit(BaseConfigModel):
    pass

class Capacity(BaseConfigModel):
    unit = models.ForeignKey(Unit, verbose_name="Unidade", on_delete=models.CASCADE, null=True)
