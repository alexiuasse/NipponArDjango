#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 17/07/2020 11:56.

from django_tables2 import tables, TemplateColumn

from .models import *


class BrandTable(tables.Table):
    ações = TemplateColumn(template_name='config/table/buttons.html')

    class Meta:
        model = Brand
        attrs = {'class': 'table table-sm table-striped table-hover'}
        per_page = 10
        order_by = '-id'
        fields = ['id', 'name', 'ações']
