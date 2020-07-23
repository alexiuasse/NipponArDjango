#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 22/07/2020 18:12.
from django_filters import FilterSet

from .models import *


class CustomerFilter(FilterSet):
    class Meta:
        model = Customer
        fields = {'name': ['icontains'], }


class CustomerAddressFilter(FilterSet):
    class Meta:
        model = CustomerAddress
        fields = {'customer': [], 'street': ['icontains'], }
