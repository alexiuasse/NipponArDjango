#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 25/07/2020 22:44.
from django_tables2 import tables, Column, TemplateColumn

from .models import *


class IndividualCustomerTable(tables.Table):
    # name = Column(linkify=True)
    # parent_company = Column(linkify=True)
    # all = Column(accessor='get_address', verbose_name='Endereço')
    _ = TemplateColumn(template_name='base/table/buttons.html')

    class Meta:
        model = IndividualCustomer
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 10
        fields = ['name', 'phone_1']

    # @staticmethod
    # def render_name(value):
    #     return format_html('<span class="text-primary font-weight-bold">{}</span>', value)


class JuridicalCustomerTable(tables.Table):
    # name = Column(linkify=True)
    parent_company = Column(linkify=True)
    # all = Column(accessor='get_address', verbose_name='Endereço')
    _ = TemplateColumn(template_name='base/table/buttons.html')

    class Meta:
        model = JuridicalCustomer
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 10
        fields = ['name', 'parent_company', 'phone_1']

    # @staticmethod
    # def render_name(value):
    #     return format_html('<span class="text-primary font-weight-bold">{}</span>', value)
