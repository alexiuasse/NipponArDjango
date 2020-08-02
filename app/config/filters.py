#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 01/08/2020 13:29.

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


class CapacityFilter(FilterSet):
    class Meta:
        model = Capacity
        fields = {'name': ['icontains'], }


class CityFilter(FilterSet):
    class Meta:
        model = City
        fields = {'name': ['icontains'], }


class TypeOfServiceFilter(FilterSet):
    class Meta:
        model = TypeOfService
        fields = {'name': ['icontains'], }


class StatusServiceFilter(FilterSet):
    class Meta:
        model = StatusService
        fields = {'name': ['icontains'], }


class DevicePartsFilter(FilterSet):
    class Meta:
        model = DeviceParts
        fields = {'name': ['icontains'], }
