#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 17/07/2020 19:30.

from django_filters import FilterSet

from .models import *


class BrandFilter(FilterSet):
    class Meta:
        model = Brand
        fields = {'name': ['icontains'], }


class ModelFilter(FilterSet):
    class Meta:
        model = Model
        fields = {'name': ['icontains'], }
