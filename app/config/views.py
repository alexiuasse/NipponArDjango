#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 31/07/2020 15:23.
from typing import Dict, Any

from django.conf import settings
from django.contrib.admin.utils import NestedObjects
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django_filters.views import FilterView
from django_tables2.paginators import LazyPaginator
from django_tables2.views import SingleTableMixin

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
                    'header': settings.HEADER_CLASS_CONFIG_GENERAL,
                },
                'city': {
                    'name': "Cidades",
                    'link': reverse_lazy('config:city:view'),
                    'badge_text': City.objects.count(),
                    'badge_class': 'badge-success',
                    'icon': 'settings',
                }
            },
            'Assistência Técnica': {
                'config': {
                    'header': settings.HEADER_CLASS_CONFIG_TECHNICAL,
                },
                'brand': {
                    'name': "Marcas",
                    'link': reverse_lazy('config:brand:view'),
                    'badge_text': Brand.objects.count(),
                    'badge_class': 'badge-success',
                    'icon': 'settings',
                },
                'model': {
                    'name': "Modelos",
                    'link': reverse_lazy('config:model:view'),
                    'badge_text': Model.objects.count(),
                    'badge_class': 'badge-success',
                    'icon': 'settings',
                },
                'type': {
                    'name': "Tipos",
                    'link': reverse_lazy('config:type:view'),
                    'badge_text': Type.objects.count(),
                    'badge_class': 'badge-success',
                    'icon': 'settings',
                },
                'capacity': {
                    'name': "Capacidades",
                    'link': reverse_lazy('config:capacity:view'),
                    'badge_text': Capacity.objects.count(),
                    'badge_class': 'badge-success',
                    'icon': 'settings',
                },
            },
            'Financeiro': {
                'config': {
                    'header': settings.HEADER_CLASS_CONFIG_FINANTIAL,
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
    title = settings.TITLE_VIEW_CONFIG_BRAND
    subtitle = settings.SUBTITLE_VIEW_CONFIG_BRAND
    new = reverse_lazy('config:brand:create')
    back_url = reverse_lazy('config:index')
    header_class = settings.HEADER_CLASS_CONFIG_TECHNICAL


class BrandCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Brand
    form_class = BrandForm
    template_name = 'base/form.html'
    permission_required = 'config.create_brand'
    # success_url = reverse_lazy('config:brand:view')
    back_url = reverse_lazy('config:brand:view')
    title = settings.TITLE_CREATE_CONFIG_BRAND
    subtitle = settings.SUBTITLE_VIEW_CONFIG_BRAND
    header_class = settings.HEADER_CLASS_CONFIG_TECHNICAL


class BrandEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Brand
    form_class = BrandForm
    template_name = 'base/form.html'
    permission_required = 'config.edit_brand'
    success_url = reverse_lazy('config:brand:view')
    title = settings.TITLE_EDIT_CONFIG_BRAND
    subtitle = settings.SUBTITLE_VIEW_CONFIG_BRAND
    header_class = settings.HEADER_CLASS_CONFIG_TECHNICAL


class BrandDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Brand
    template_name = "base/confirm_delete.html"
    permission_required = 'config.del_brand'
    success_url = reverse_lazy('config:brand:view')
    title = settings.TITLE_DEL_CONFIG_BRAND
    subtitle = settings.SUBTITLE_VIEW_CONFIG_BRAND
    header_class = settings.HEADER_CLASS_CONFIG_TECHNICAL

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
    title = settings.TITLE_VIEW_CONFIG_CAPACITY
    subtitle = settings.SUBTITLE_VIEW_CONFIG_CAPACITY
    new = reverse_lazy('config:capacity:create')
    back_url = reverse_lazy('config:index')
    header_class = settings.HEADER_CLASS_CONFIG_TECHNICAL


class CapacityCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Capacity
    form_class = CapacityForm
    template_name = 'base/form.html'
    permission_required = 'config.create_capacity'
    # success_url = reverse_lazy('config:capacity:view')
    back_url = reverse_lazy('config:capacity:view')
    title = settings.TITLE_CREATE_CONFIG_CAPACITY
    subtitle = settings.SUBTITLE_VIEW_CONFIG_CAPACITY
    header_class = settings.HEADER_CLASS_CONFIG_TECHNICAL


class CapacityEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Capacity
    form_class = CapacityForm
    template_name = 'base/form.html'
    permission_required = 'config.edit_capacity'
    # success_url = reverse_lazy('config:capacity:view')
    back_url = reverse_lazy('config:capacity:view')
    title = settings.TITLE_EDIT_CONFIG_CAPACITY
    subtitle = settings.SUBTITLE_VIEW_CONFIG_CAPACITY
    header_class = settings.HEADER_CLASS_CONFIG_TECHNICAL


class CapacityDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Capacity
    template_name = "base/confirm_delete.html"
    permission_required = 'config.del_capacity'
    success_url = reverse_lazy('config:capacity:view')
    title = settings.TITLE_DEL_CONFIG_CAPACITY
    subtitle = settings.SUBTITLE_VIEW_CONFIG_CAPACITY
    header_class = settings.HEADER_CLASS_CONFIG_TECHNICAL

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
    title = settings.TITLE_VIEW_CONFIG_MODEL
    subtitle = settings.SUBTITLE_VIEW_CONFIG_MODEL
    new = reverse_lazy('config:model:create')
    back_url = reverse_lazy('config:index')
    header_class = settings.HEADER_CLASS_CONFIG_TECHNICAL


class ModelCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Model
    form_class = ModelForm
    template_name = 'base/form.html'
    permission_required = 'config.create_model'
    # success_url = reverse_lazy('config:model:view')
    back_url = reverse_lazy('config:model:view')
    title = settings.TITLE_CREATE_CONFIG_MODEL
    subtitle = settings.SUBTITLE_VIEW_CONFIG_MODEL
    header_class = settings.HEADER_CLASS_CONFIG_TECHNICAL


class ModelEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Model
    form_class = ModelForm
    template_name = 'base/form.html'
    permission_required = 'config.edit_model'
    success_url = reverse_lazy('config:model:view')
    title = settings.TITLE_EDIT_CONFIG_MODEL
    subtitle = settings.SUBTITLE_VIEW_CONFIG_MODEL
    header_class = settings.HEADER_CLASS_CONFIG_TECHNICAL


class ModelDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Model
    template_name = "base/confirm_delete.html"
    permission_required = 'config.del_model'
    success_url = reverse_lazy('config:model:view')
    title = settings.TITLE_DEL_CONFIG_MODEL
    subtitle = settings.SUBTITLE_VIEW_CONFIG_MODEL
    header_class = settings.HEADER_CLASS_CONFIG_TECHNICAL

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
    title = settings.TITLE_VIEW_CONFIG_TYPE
    subtitle = settings.SUBTITLE_VIEW_CONFIG_TYPE
    new = reverse_lazy('config:type:create')
    back_url = reverse_lazy('config:index')
    header_class = settings.HEADER_CLASS_CONFIG_TECHNICAL


class TypeCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Type
    form_class = TypeForm
    template_name = 'base/form.html'
    permission_required = 'config.create_model'
    # success_url = reverse_lazy('config:type:view')
    back_url = reverse_lazy('config:type:view')
    title = settings.TITLE_CREATE_CONFIG_TYPE
    subtitle = settings.SUBTITLE_VIEW_CONFIG_TYPE
    header_class = settings.HEADER_CLASS_CONFIG_TECHNICAL


class TypeEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Type
    form_class = TypeForm
    template_name = 'base/form.html'
    permission_required = 'config.edit_model'
    success_url = reverse_lazy('config:type:view')
    title = settings.TITLE_EDIT_CONFIG_TYPE
    subtitle = settings.SUBTITLE_VIEW_CONFIG_TYPE
    header_class = settings.HEADER_CLASS_CONFIG_TECHNICAL


class TypeDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Type
    template_name = "base/confirm_delete.html"
    permission_required = 'config.del_model'
    success_url = reverse_lazy('config:type:view')
    title = settings.TITLE_DEL_CONFIG_TYPE
    subtitle = settings.SUBTITLE_VIEW_CONFIG_TYPE
    header_class = settings.HEADER_CLASS_CONFIG_TECHNICAL

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
    title = settings.TITLE_VIEW_CONFIG_CITY
    subtitle = settings.SUBTITLE_VIEW_CONFIG_CITY
    new = reverse_lazy('config:city:create')
    back_url = reverse_lazy('config:index')
    header_class = settings.HEADER_CLASS_CONFIG_GENERAL


class CityCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = 'base/form.html'
    permission_required = 'config.create_city'
    # success_url = reverse_lazy('config:city:view')
    back_url = reverse_lazy('config:city:view')
    title = settings.TITLE_CREATE_CONFIG_CITY
    subtitle = settings.SUBTITLE_VIEW_CONFIG_CITY
    header_class = settings.HEADER_CLASS_CONFIG_GENERAL


class CityEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'base/form.html'
    permission_required = 'config.edit_city'
    success_url = reverse_lazy('config:city:view')
    title = settings.TITLE_EDIT_CONFIG_CITY
    subtitle = settings.SUBTITLE_VIEW_CONFIG_CITY
    header_class = settings.HEADER_CLASS_CONFIG_GENERAL


class CityDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = City
    template_name = "base/confirm_delete.html"
    permission_required = 'config.del_city'
    success_url = reverse_lazy('config:city:view')
    title = settings.TITLE_DEL_CONFIG_CITY
    subtitle = settings.SUBTITLE_VIEW_CONFIG_CITY
    header_class = settings.HEADER_CLASS_CONFIG_GENERAL

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific database
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context
