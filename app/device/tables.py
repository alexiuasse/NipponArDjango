#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 02/08/2020 12:34.
from django_tables2 import tables, TemplateColumn

from .models import *


class DeviceTable(tables.Table):
    _ = TemplateColumn(template_name='base/table/buttons.html')

    class Meta:
        model = Device
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 10
        fields = ['name']
