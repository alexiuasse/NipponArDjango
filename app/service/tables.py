#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 14/08/2020 16:18.
from django_tables2 import tables, TemplateColumn, Column

from .models import *


class OrderOfServiceTable(tables.Table):
    _ = TemplateColumn(template_name='base/table/buttons.html')
    device = Column(accessor='get_device_name', verbose_name='Equipamento')
    customer = Column(accessor='get_customer_name', verbose_name='Cliente')

    class Meta:
        model = OrderOfService
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 20
        fields = ['type_of_service', 'status', 'date', 'device', 'customer']
