#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 02/08/2020 09:54.
from django_tables2 import tables, TemplateColumn

from .models import *


class OrderOfServiceTable(tables.Table):
    _ = TemplateColumn(template_name='base/table/buttons.html')

    class Meta:
        model = OrderOfService
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 10
        fields = ['type_of_service', 'status']
