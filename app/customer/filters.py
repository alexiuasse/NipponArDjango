#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 25/07/2020 22:44.
from django_filters import FilterSet

from .models import *


class IndividualCustomerFilter(FilterSet):
    class Meta:
        model = IndividualCustomer
        fields = {'name': ['icontains'], }


class JuridicalCustomerFilter(FilterSet):
    class Meta:
        model = JuridicalCustomer
        fields = {'name': ['icontains'], }
