#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 26/07/2020 13:28.
from typing import Dict, Any

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
                'city': {
                    'name': "Cidades",
                    'link': reverse_lazy('config-city'),
                    'quantity': City.objects.count(),
                }
            },
            'Assistência Técnica': {
                'brand': {
                    'name': "Marcas",
                    'link': reverse_lazy('config-brand'),
                    'quantity': Brand.objects.count(),
                },
                'model': {
                    'name': "Modelos",
                    'link': reverse_lazy('config-model'),
                    'quantity': Model.objects.count(),
                },
                'type': {
                    'name': "Tipos",
                    'link': reverse_lazy('config-type'),
                    'quantity': Type.objects.count(),
                },
                'capacity': {
                    'name': "Capacidades",
                    'link': reverse_lazy('config-capacity'),
                    'quantity': Capacity.objects.count(),
                },
            },
            'Financeiro': {

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
    title = "Marca"
    subtitle = "Configuração de marcas"
    new = reverse_lazy('config-brand-create')


class BrandCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Brand
    form_class = BrandForm
    template_name = 'base/form.html'
    permission_required = 'config.create_brand'
    success_url = reverse_lazy('config-brand')
    title = "Nova Marca"
    subtitle = "Configuração de marcas"


class BrandEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Brand
    form_class = BrandForm
    template_name = 'base/form.html'
    permission_required = 'config.edit_brand'
    success_url = reverse_lazy('config-brand')
    title = "Editar Marca"
    subtitle = "Configuração de marcas"


class BrandDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Brand
    template_name = "base/confirm_delete.html"
    permission_required = 'config.del_brand'
    success_url = reverse_lazy('config-brand')
    title = "Deletar Marca"
    subtitle = "Configuração de marcas"

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
    title = "Capacidade"
    subtitle = "Configuração de capacidades"
    new = reverse_lazy('config-capacity-create')


class CapacityCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Capacity
    form_class = CapacityForm
    template_name = 'base/form.html'
    permission_required = 'config.create_capacity'
    success_url = reverse_lazy('config-capacity')
    title = "Nova Capacidade"
    subtitle = "Configuração de capacidades"


class CapacityEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Capacity
    form_class = CapacityForm
    template_name = 'base/form.html'
    permission_required = 'config.edit_capacity'
    success_url = reverse_lazy('config-capacity')
    title = "Editar Capacidade"
    subtitle = "Configuração de capacidades"


class CapacityDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Capacity
    template_name = "base/confirm_delete.html"
    permission_required = 'config.del_capacity'
    success_url = reverse_lazy('config-capacity')
    title = "Deletar Capacidade"
    subtitle = "Configuração de capacidades"

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
    title = "Cidade"
    subtitle = "Configuração de cidades"
    new = reverse_lazy('config-city-create')


class CityCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = 'base/form.html'
    permission_required = 'config.create_city'
    success_url = reverse_lazy('config-city')
    title = "Nova Cidade"
    subtitle = "Configuração de cidades"


class CityEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'base/form.html'
    permission_required = 'config.edit_city'
    success_url = reverse_lazy('config-city')
    title = "Editar Cidade"
    subtitle = "Configuração de cidades"


class CityDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = City
    template_name = "base/confirm_delete.html"
    permission_required = 'config.del_city'
    success_url = reverse_lazy('config-city')
    title = "Deletar Cidade"
    subtitle = "Configuração de cidades"

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
    title = "Modelo"
    subtitle = "Configuração de modelos"
    new = reverse_lazy('config-model-create')


class ModelCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Model
    form_class = ModelForm
    template_name = 'base/form.html'
    permission_required = 'config.create_model'
    success_url = reverse_lazy('config-model')
    title = "Novo Modelo"
    subtitle = "Configuração de modelos"


class ModelEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Model
    form_class = ModelForm
    template_name = 'base/form.html'
    permission_required = 'config.edit_model'
    success_url = reverse_lazy('config-model')
    title = "Editar Modelo"
    subtitle = "Configuração de modelos"


class ModelDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Model
    template_name = "base/confirm_delete.html"
    permission_required = 'config.del_model'
    success_url = reverse_lazy('config-model')
    title = "Deletar Modelo"
    subtitle = "Configuração de modelos"

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
    title = "Tipo"
    subtitle = "Configuração de tipos"
    new = reverse_lazy('config-type-create')


class TypeCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Type
    form_class = TypeForm
    template_name = 'base/form.html'
    permission_required = 'config.create_model'
    success_url = reverse_lazy('config-type')
    title = "Novo Tipo"
    subtitle = "Configuração de tipos"


class TypeEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Type
    form_class = TypeForm
    template_name = 'base/form.html'
    permission_required = 'config.edit_model'
    success_url = reverse_lazy('config-type')
    title = "Editar Tipo"
    subtitle = "Configuração de tipos"


class TypeDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Type
    template_name = "base/confirm_delete.html"
    permission_required = 'config.del_model'
    success_url = reverse_lazy('config-type')
    title = "Deletar Tipo"
    subtitle = "Configuração de tipos"

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific database
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context
