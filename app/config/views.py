#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 12/08/2020 20:04.
from typing import Dict, Any

from django.contrib.admin.utils import NestedObjects
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django_filters.views import FilterView
from django_tables2.paginators import LazyPaginator
from django_tables2.views import SingleTableMixin

from .conf import *
from .filters import *
from .forms import *
from .tables import *


class Config(LoginRequiredMixin, View):
    template = 'config/view.html'
    title = 'Configurações'
    subtitle = 'Configuração do sistema'

    def get(self, request):
        links = {
            'Geral': {
                'config': {
                    'header': HEADER_CLASS_CONFIG_GENERAL,
                },
                'city': {
                    'name': "Cidades",
                    'link': reverse_lazy('config:city:view'),
                    'badge_text': City.objects.count(),
                }
            },
            'Equipamento': {
                'config': {
                    'header': HEADER_CLASS_CONFIG_TECHNICAL,
                },
                'brand': {
                    'name': "Marcas",
                    'link': reverse_lazy('config:brand:view'),
                    'badge_text': Brand.objects.count(),
                },
                'model': {
                    'name': "Modelos",
                    'link': reverse_lazy('config:model:view'),
                    'badge_text': Model.objects.count(),
                },
                'type': {
                    'name': "Tipos",
                    'link': reverse_lazy('config:type:view'),
                    'badge_text': Type.objects.count(),
                },
                'capacity': {
                    'name': "Capacidades",
                    'link': reverse_lazy('config:capacity:view'),
                    'badge_text': Capacity.objects.count(),
                },
                'device_parts': {
                    'name': "Peças",
                    'link': reverse_lazy('config:deviceparts:view'),
                    'badge_text': DeviceParts.objects.count(),
                },
            },
            'Ordem de Serviço': {
                'config': {
                    'header': HEADER_CLASS_CONFIG_TECHNICAL,
                },
                'status_service': {
                    'name': "Status do Serviço",
                    'link': reverse_lazy('config:statusservice:view'),
                    'badge_text': StatusService.objects.count(),
                },
                'type_of_service': {
                    'name': "Tipo de Serviço",
                    'link': reverse_lazy('config:typeofservice:view'),
                    'badge_text': TypeOfService.objects.count(),
                },
            },
            'Financeiro': {
                'config': {
                    'header': HEADER_CLASS_CONFIG_FINANTIAL,
                },
            },
        }
        context = {
            'title': self.title,
            'subtitle': self.subtitle,
            'links': links
        }
        return render(request, self.template, context)


########################################################################################################################

class BrandView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = Brand
    table_class = BrandTable
    filterset_class = BrandFilter
    paginator_class = LazyPaginator
    permission_required = 'config.view_brand'
    template_name = 'base/view.html'
    title = TITLE_VIEW_CONFIG_BRAND
    subtitle = SUBTITLE_VIEW_CONFIG_BRAND
    new = reverse_lazy('config:brand:create')
    back_url = reverse_lazy('config:index')
    header_class = HEADER_CLASS_CONFIG_TECHNICAL


class BrandCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Brand
    form_class = BrandForm
    template_name = 'base/form.html'
    permission_required = 'config.create_brand'
    # success_url = reverse_lazy('config:brand:view')
    back_url = reverse_lazy('config:brand:view')
    title = TITLE_CREATE_CONFIG_BRAND
    subtitle = SUBTITLE_VIEW_CONFIG_BRAND
    header_class = HEADER_CLASS_CONFIG_TECHNICAL

    def get_back_url(self):
        return self.back_url


class BrandEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Brand
    form_class = BrandForm
    template_name = 'base/form.html'
    permission_required = 'config.edit_brand'
    success_url = reverse_lazy('config:brand:view')
    title = TITLE_EDIT_CONFIG_BRAND
    subtitle = SUBTITLE_VIEW_CONFIG_BRAND
    header_class = HEADER_CLASS_CONFIG_TECHNICAL


class BrandDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Brand
    template_name = "base/confirm_delete.html"
    permission_required = 'config.del_brand'
    success_url = reverse_lazy('config:brand:view')
    title = TITLE_DEL_CONFIG_BRAND
    subtitle = SUBTITLE_VIEW_CONFIG_BRAND
    header_class = HEADER_CLASS_CONFIG_TECHNICAL

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific database
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context


########################################################################################################################

class CapacityView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = Capacity
    table_class = CapacityTable
    filterset_class = CapacityFilter
    paginator_class = LazyPaginator
    permission_required = 'config.view_capacity'
    template_name = 'base/view.html'
    title = TITLE_VIEW_CONFIG_CAPACITY
    subtitle = SUBTITLE_VIEW_CONFIG_CAPACITY
    new = reverse_lazy('config:capacity:create')
    back_url = reverse_lazy('config:index')
    header_class = HEADER_CLASS_CONFIG_TECHNICAL


class CapacityCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Capacity
    form_class = CapacityForm
    template_name = 'base/form.html'
    permission_required = 'config.create_capacity'
    # success_url = reverse_lazy('config:capacity:view')
    back_url = reverse_lazy('config:capacity:view')
    title = TITLE_CREATE_CONFIG_CAPACITY
    subtitle = SUBTITLE_VIEW_CONFIG_CAPACITY
    header_class = HEADER_CLASS_CONFIG_TECHNICAL

    def get_back_url(self):
        return self.back_url


class CapacityEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Capacity
    form_class = CapacityForm
    template_name = 'base/form.html'
    permission_required = 'config.edit_capacity'
    # success_url = reverse_lazy('config:capacity:view')
    back_url = reverse_lazy('config:capacity:view')
    title = TITLE_EDIT_CONFIG_CAPACITY
    subtitle = SUBTITLE_VIEW_CONFIG_CAPACITY
    header_class = HEADER_CLASS_CONFIG_TECHNICAL


class CapacityDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Capacity
    template_name = "base/confirm_delete.html"
    permission_required = 'config.del_capacity'
    success_url = reverse_lazy('config:capacity:view')
    title = TITLE_DEL_CONFIG_CAPACITY
    subtitle = SUBTITLE_VIEW_CONFIG_CAPACITY
    header_class = HEADER_CLASS_CONFIG_TECHNICAL

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific database
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context


########################################################################################################################

class ModelView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = Model
    table_class = ModelTable
    filterset_class = ModelFilter
    paginator_class = LazyPaginator
    permission_required = 'config.view_model'
    template_name = 'base/view.html'
    title = TITLE_VIEW_CONFIG_MODEL
    subtitle = SUBTITLE_VIEW_CONFIG_MODEL
    new = reverse_lazy('config:model:create')
    back_url = reverse_lazy('config:index')
    header_class = HEADER_CLASS_CONFIG_TECHNICAL


class ModelCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Model
    form_class = ModelForm
    template_name = 'base/form.html'
    permission_required = 'config.create_model'
    # success_url = reverse_lazy('config:model:view')
    back_url = reverse_lazy('config:model:view')
    title = TITLE_CREATE_CONFIG_MODEL
    subtitle = SUBTITLE_VIEW_CONFIG_MODEL
    header_class = HEADER_CLASS_CONFIG_TECHNICAL

    def get_back_url(self):
        return self.back_url


class ModelEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Model
    form_class = ModelForm
    template_name = 'base/form.html'
    permission_required = 'config.edit_model'
    success_url = reverse_lazy('config:model:view')
    title = TITLE_EDIT_CONFIG_MODEL
    subtitle = SUBTITLE_VIEW_CONFIG_MODEL
    header_class = HEADER_CLASS_CONFIG_TECHNICAL


class ModelDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Model
    template_name = "base/confirm_delete.html"
    permission_required = 'config.del_model'
    success_url = reverse_lazy('config:model:view')
    title = TITLE_DEL_CONFIG_MODEL
    subtitle = SUBTITLE_VIEW_CONFIG_MODEL
    header_class = HEADER_CLASS_CONFIG_TECHNICAL

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific database
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context


########################################################################################################################

class TypeView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = Type
    table_class = TypeTable
    filterset_class = TypeFilter
    paginator_class = LazyPaginator
    permission_required = 'config.view_type'
    template_name = 'base/view.html'
    title = TITLE_VIEW_CONFIG_TYPE
    subtitle = SUBTITLE_VIEW_CONFIG_TYPE
    new = reverse_lazy('config:type:create')
    back_url = reverse_lazy('config:index')
    header_class = HEADER_CLASS_CONFIG_TECHNICAL


class TypeCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Type
    form_class = TypeForm
    template_name = 'base/form.html'
    permission_required = 'config.create_model'
    # success_url = reverse_lazy('config:type:view')
    back_url = reverse_lazy('config:type:view')
    title = TITLE_CREATE_CONFIG_TYPE
    subtitle = SUBTITLE_VIEW_CONFIG_TYPE
    header_class = HEADER_CLASS_CONFIG_TECHNICAL

    def get_back_url(self):
        return self.back_url


class TypeEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Type
    form_class = TypeForm
    template_name = 'base/form.html'
    permission_required = 'config.edit_model'
    success_url = reverse_lazy('config:type:view')
    title = TITLE_EDIT_CONFIG_TYPE
    subtitle = SUBTITLE_VIEW_CONFIG_TYPE
    header_class = HEADER_CLASS_CONFIG_TECHNICAL


class TypeDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Type
    template_name = "base/confirm_delete.html"
    permission_required = 'config.del_model'
    success_url = reverse_lazy('config:type:view')
    title = TITLE_DEL_CONFIG_TYPE
    subtitle = SUBTITLE_VIEW_CONFIG_TYPE
    header_class = HEADER_CLASS_CONFIG_TECHNICAL

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific database
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context


########################################################################################################################

class CityView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = City
    table_class = CityTable
    filterset_class = CityFilter
    paginator_class = LazyPaginator
    permission_required = 'config.view_city'
    template_name = 'base/view.html'
    title = TITLE_VIEW_CONFIG_CITY
    subtitle = SUBTITLE_VIEW_CONFIG_CITY
    new = reverse_lazy('config:city:create')
    back_url = reverse_lazy('config:index')
    header_class = HEADER_CLASS_CONFIG_GENERAL


class CityCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = 'base/form.html'
    permission_required = 'config.create_city'
    # success_url = reverse_lazy('config:city:view')
    back_url = reverse_lazy('config:city:view')
    title = TITLE_CREATE_CONFIG_CITY
    subtitle = SUBTITLE_VIEW_CONFIG_CITY
    header_class = HEADER_CLASS_CONFIG_GENERAL

    def get_back_url(self):
        return self.back_url


class CityEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'base/form.html'
    permission_required = 'config.edit_city'
    success_url = reverse_lazy('config:city:view')
    title = TITLE_EDIT_CONFIG_CITY
    subtitle = SUBTITLE_VIEW_CONFIG_CITY
    header_class = HEADER_CLASS_CONFIG_GENERAL


class CityDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = City
    template_name = "base/confirm_delete.html"
    permission_required = 'config.del_city'
    success_url = reverse_lazy('config:city:view')
    title = TITLE_DEL_CONFIG_CITY
    subtitle = SUBTITLE_VIEW_CONFIG_CITY
    header_class = HEADER_CLASS_CONFIG_GENERAL

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific database
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context


########################################################################################################################

class TypeOfServiceView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = TypeOfService
    table_class = TypeOfServiceTable
    filterset_class = TypeOfServiceFilter
    paginator_class = LazyPaginator
    permission_required = 'config.view_typeofservice'
    template_name = 'base/view.html'
    title = TITLE_VIEW_CONFIG_TYPE_OF_SERVICE
    subtitle = SUBTITLE_VIEW_CONFIG_TYPE_OF_SERVICE
    new = reverse_lazy('config:typeofservice:create')
    back_url = reverse_lazy('config:index')
    header_class = HEADER_CLASS_CONFIG_GENERAL


class TypeOfServiceCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = TypeOfService
    form_class = TypeOfServiceForm
    template_name = 'base/form.html'
    permission_required = 'config.create_typeofservice'
    # success_url = reverse_lazy('config:city:view')
    back_url = reverse_lazy('config:typeofservice:view')
    title = TITLE_CREATE_CONFIG_TYPE_OF_SERVICE
    subtitle = SUBTITLE_VIEW_CONFIG_TYPE_OF_SERVICE
    header_class = HEADER_CLASS_CONFIG_GENERAL

    def get_back_url(self):
        return self.back_url


class TypeOfServiceEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = TypeOfService
    form_class = TypeOfServiceForm
    template_name = 'base/form.html'
    permission_required = 'config.edit_typeofservice'
    success_url = reverse_lazy('config:typeofservice:view')
    title = TITLE_EDIT_CONFIG_TYPE_OF_SERVICE
    subtitle = SUBTITLE_VIEW_CONFIG_TYPE_OF_SERVICE
    header_class = HEADER_CLASS_CONFIG_GENERAL


class TypeOfServiceDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = TypeOfService
    template_name = "base/confirm_delete.html"
    permission_required = 'config.del_typeofservice'
    success_url = reverse_lazy('config:typeofservice:view')
    title = TITLE_DEL_CONFIG_TYPE_OF_SERVICE
    subtitle = SUBTITLE_VIEW_CONFIG_TYPE_OF_SERVICE
    header_class = HEADER_CLASS_CONFIG_GENERAL

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific database
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context


########################################################################################################################

class StatusServiceView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = StatusService
    table_class = StatusServiceTable
    filterset_class = StatusServiceFilter
    paginator_class = LazyPaginator
    permission_required = 'config.view_statuservice'
    template_name = 'base/view.html'
    title = TITLE_VIEW_CONFIG_STATUS_SERVICE
    subtitle = SUBTITLE_VIEW_CONFIG_STATUS_SERVICE
    new = reverse_lazy('config:statusservice:create')
    back_url = reverse_lazy('config:index')
    header_class = HEADER_CLASS_CONFIG_GENERAL


class StatusServiceCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = StatusService
    form_class = StatusServiceForm
    template_name = 'base/form.html'
    permission_required = 'config.create_statuservice'
    # success_url = reverse_lazy('config:city:view')
    back_url = reverse_lazy('config:statusservice:view')
    title = TITLE_CREATE_CONFIG_STATUS_SERVICE
    subtitle = SUBTITLE_VIEW_CONFIG_STATUS_SERVICE
    header_class = HEADER_CLASS_CONFIG_GENERAL

    def get_back_url(self):
        return self.back_url


class StatusServiceEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = StatusService
    form_class = StatusServiceForm
    template_name = 'base/form.html'
    permission_required = 'config.edit_statuservice'
    success_url = reverse_lazy('config:statusservice:view')
    title = TITLE_EDIT_CONFIG_STATUS_SERVICE
    subtitle = SUBTITLE_VIEW_CONFIG_STATUS_SERVICE
    header_class = HEADER_CLASS_CONFIG_GENERAL


class StatusServiceDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = StatusService
    template_name = "base/confirm_delete.html"
    permission_required = 'config.del_statusservice'
    success_url = reverse_lazy('config:statusservice:view')
    title = TITLE_DEL_CONFIG_STATUS_SERVICE
    subtitle = SUBTITLE_VIEW_CONFIG_STATUS_SERVICE
    header_class = HEADER_CLASS_CONFIG_GENERAL

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific database
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context


########################################################################################################################

class DevicePartsView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = DeviceParts
    table_class = DevicePartsTable
    filterset_class = DevicePartsFilter
    paginator_class = LazyPaginator
    permission_required = 'config.view_deviceparts'
    template_name = 'base/view.html'
    title = TITLE_VIEW_CONFIG_DEVICE_PARTS
    subtitle = SUBTITLE_VIEW_CONFIG_DEVICE_PARTS
    new = reverse_lazy('config:deviceparts:create')
    back_url = reverse_lazy('config:index')
    header_class = HEADER_CLASS_CONFIG_GENERAL


class DevicePartsCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = DeviceParts
    form_class = DevicePartsForm
    template_name = 'base/form.html'
    permission_required = 'config.create_deviceparts'
    # success_url = reverse_lazy('config:city:view')
    back_url = reverse_lazy('config:deviceparts:view')
    title = TITLE_CREATE_CONFIG_DEVICE_PARTS
    subtitle = SUBTITLE_VIEW_CONFIG_DEVICE_PARTS
    header_class = HEADER_CLASS_CONFIG_GENERAL

    def get_back_url(self):
        return self.back_url


class DevicePartsEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = DeviceParts
    form_class = DevicePartsForm
    template_name = 'base/form.html'
    permission_required = 'config.edit_deviceparts'
    success_url = reverse_lazy('config:deviceparts:view')
    title = TITLE_EDIT_CONFIG_DEVICE_PARTS
    subtitle = SUBTITLE_VIEW_CONFIG_DEVICE_PARTS
    header_class = HEADER_CLASS_CONFIG_GENERAL


class DevicePartsDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = DeviceParts
    template_name = "base/confirm_delete.html"
    permission_required = 'config.del_deviceparts'
    success_url = reverse_lazy('config:deviceparts:view')
    title = TITLE_DEL_CONFIG_DEVICE_PARTS
    subtitle = SUBTITLE_VIEW_CONFIG_DEVICE_PARTS
    header_class = HEADER_CLASS_CONFIG_GENERAL

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific database
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context
