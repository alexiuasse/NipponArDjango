#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 17/07/2020 19:30.

from django_tables2 import tables

from .models import *


class BrandTable(tables.Table):
    # acoes = TemplateColumn(template_name='config/table/buttons.html')

    class Meta:
        model = Brand
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 10
        order_by = '-id'
        fields = ['id', 'name', 'quantity', ]


class ModelTable(tables.Table):
    # acoes = TemplateColumn(template_name='config/table/buttons.html')

    class Meta:
        model = Model
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 10
        order_by = '-id'
        fields = ['id', 'name', 'quantity', ]
