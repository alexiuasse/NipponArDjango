#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 18/07/2020 12:17.

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


class TypeFilter(FilterSet):
    class Meta:
        model = Type
        fields = {'name': ['icontains'], }
