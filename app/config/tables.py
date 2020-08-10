#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 10/08/2020 10:16.
from django.utils.html import format_html
from django_tables2 import tables, Column, TemplateColumn

from .models import *


class BrandTable(tables.Table):
    # name = Column(linkify=True)
    _ = TemplateColumn(template_name='base/table/buttons.html')

    class Meta:
        model = Brand
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 10
        fields = ['name']

    # @staticmethod
    # def render_name(value):
    #     return format_html('<span class="name text-primary font-weight-bold">{}</span>', value)


class ModelTable(tables.Table):
    # name = Column(linkify=True)
    _ = TemplateColumn(template_name='base/table/buttons.html')

    class Meta:
        model = Model
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 10
        fields = ['name']

    # @staticmethod
    # def render_name(value):
    #     return format_html('<span class="name text-primary font-weight-bold">{}</span>', value)


class TypeTable(tables.Table):
    # name = Column(linkify=True)
    _ = TemplateColumn(template_name='base/table/buttons.html')

    class Meta:
        model = Type
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 10
        fields = ['name']

    # @staticmethod
    # def render_name(value):
    #     return format_html('<span class="name text-primary font-weight-bold">{}</span>', value)


class CapacityTable(tables.Table):
    # name = Column(linkify=True)
    _ = TemplateColumn(template_name='base/table/buttons.html')

    class Meta:
        model = Capacity
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 10
        fields = ['name']

    # @staticmethod
    # def render_name(value):
    #     return format_html('<span class="name text-primary font-weight-bold">{}</span>', value)


class CityTable(tables.Table):
    # name = Column(linkify=True)
    _ = TemplateColumn(template_name='base/table/buttons.html')

    class Meta:
        model = City
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 10
        fields = ['name']
        # fields = ['id', 'name', 'created_by', 'created_in']

    # @staticmethod
    # def render_name(value):
    #     return format_html('<span class="name text-primary font-weight-bold">{}</span>', value)


class TypeOfServiceTable(tables.Table):
    _ = TemplateColumn(template_name='base/table/buttons.html')

    class Meta:
        model = TypeOfService
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 10
        fields = ['name']


class StatusServiceTable(tables.Table):
    _ = TemplateColumn(template_name='base/table/buttons.html')

    class Meta:
        model = StatusService
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 10
        fields = ['name', 'contextual']


class DevicePartsTable(tables.Table):
    _ = TemplateColumn(template_name='base/table/buttons.html')

    class Meta:
        model = DeviceParts
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 10
        fields = ['name']
