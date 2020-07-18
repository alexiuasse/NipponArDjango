#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 18/07/2020 13:57.
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


class TypeView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = Type
    table_class = TypeTable
    filterset_class = TypeFilter
    paginator_class = LazyPaginator
    permission_required = 'config.view_type'
    template_name = 'config/models_view.html'
    title = "Tipo"
    subtitle = "Configuração de tipos"
    new = reverse_lazy('config-type-create')


class TypeCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Type
    form_class = TypeForm
    template_name = 'config/form.html'
    permission_required = 'config.create_model'
    success_url = reverse_lazy('config-type')
    title = "Novo Tipo"
    subtitle = "Configuração de tipos"


class TypeEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Type
    form_class = TypeForm
    template_name = 'config/form.html'
    permission_required = 'config.edit_model'
    success_url = reverse_lazy('config-type')
    title = "Editar Tipo"
    subtitle = "Configuração de tipos"


class TypeDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Type
    template_name = "config/confirm_delete.html"
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
