#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 18/07/2020 14:50.
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


class CapacityView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = Capacity
    table_class = CapacityTable
    filterset_class = CapacityFilter
    paginator_class = LazyPaginator
    permission_required = 'config.view_capacity'
    template_name = 'config/models_view.html'
    title = "Capacidade"
    subtitle = "Configuração de capacidades"
    new = reverse_lazy('config-capacity-create')


class CapacityCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Capacity
    form_class = CapacityForm
    template_name = 'config/form.html'
    permission_required = 'config.create_capacity'
    success_url = reverse_lazy('config-capacity')
    title = "Nova Capacidade"
    subtitle = "Configuração de capacidades"


class CapacityEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Capacity
    form_class = CapacityForm
    template_name = 'config/form.html'
    permission_required = 'config.edit_capacity'
    success_url = reverse_lazy('config-capacity')
    title = "Editar Capacidade"
    subtitle = "Configuração de capacidades"


class CapacityDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Capacity
    template_name = "config/confirm_delete.html"
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
