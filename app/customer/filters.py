#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 24/07/2020 15:54.
from django_filters import FilterSet

from .models import *


class CustomerFilter(FilterSet):
    class Meta:
        model = Customer
        fields = {'name': ['icontains'], }
