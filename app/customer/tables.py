#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 22/07/2020 18:05.
from django.utils.html import format_html
from django_tables2 import tables, Column, TemplateColumn

from .models import *


class CustomerTable(tables.Table):
    name = Column(linkify=True)
    _ = TemplateColumn(template_name='config/table/buttons.html')

    class Meta:
        model = Customer
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 10
        fields = ['id', 'name', 'created_by', 'created_in']

    @staticmethod
    def render_name(value):
        return format_html('<span class="name text-primary font-weight-bold">{}</span>', value)


class CustomerAddressTable(tables.Table):
    customer = Column(linkify=True)
    id = Column(linkify=True)
    city = Column(linkify=True)
    _ = TemplateColumn(template_name='config/table/buttons.html')

    class Meta:
        model = CustomerAddress
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 10
        fields = ['id', 'customer', 'street', 'number', 'city', 'state', 'cep', 'address_line']

    @staticmethod
    def render_name(value):
        return format_html('<span class="name text-primary font-weight-bold">{}</span>', value)
