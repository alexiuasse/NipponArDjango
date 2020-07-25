#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 25/07/2020 15:19.
from typing import Dict, Any

from django.contrib.admin.utils import NestedObjects
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django_filters.views import FilterView
from django_tables2.paginators import LazyPaginator
from django_tables2.views import SingleTableMixin

from ..filters import *
from ..forms import *
from ..tables import *


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
