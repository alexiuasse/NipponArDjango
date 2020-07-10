from django.db import models
from base.models import BaseModel

class Customer(BaseModel):
    name = models.CharField("nome", max_length=128)

    def __str__(self):
        return self.name

class Address(BaseModel):
    customer = models.ForeignKey(Customer, verbose_name="Cliente", on_delete=models.CASCADE)

    def __str__(self):
        return self.customer
