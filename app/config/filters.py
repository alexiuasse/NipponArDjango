#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 12/07/2020 20:20.

import django_filters
from .models import *

class BrandFilter(django_filters.FilterSet):

    class Meta:
        model = Brand
        fields = {'name':['icontains'],}
