#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 17/07/2020 11:56.

import django_filters

from .models import *


class BrandFilter(django_filters.FilterSet):
    class Meta:
        model = Brand
        fields = {'name': ['icontains'], }
