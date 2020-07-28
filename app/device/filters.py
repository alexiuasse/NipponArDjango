#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 28/07/2020 08:40.
from django_filters import FilterSet

from .models import *


class DeviceFilter(FilterSet):
    class Meta:
        model = Device
        fields = {'name': ['icontains'], 'patrimony': ['icontains'], }
