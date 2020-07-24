#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 24/07/2020 15:57.
from django.utils.html import format_html
from django_tables2 import tables, Column, TemplateColumn

from .models import *


class CustomerTable(tables.Table):
    name = Column(linkify=True)
    all = Column(accessor='get_address', verbose_name='Endereço')
    _ = TemplateColumn(template_name='base/table/buttons.html')

    class Meta:
        model = Customer
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 10
        fields = ['id', 'name']

    @staticmethod
    def render_name(value):
        return format_html('<span class="text-primary font-weight-bold">{}</span>', value)
