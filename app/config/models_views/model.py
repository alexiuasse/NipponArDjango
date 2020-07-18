#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 17/07/2020 20:23.
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


class ModelView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = Model
    table_class = ModelTable
    filterset_class = ModelFilter
    paginator_class = LazyPaginator
    permission_required = 'config.view_model'
    template_name = 'config/models_view.html'
    title = "Modelo"
    subtitle = "Configuração de modelos"
    new = reverse_lazy('config-model-create')


class ModelCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Model
    form_class = ModelForm
    template_name = 'config/form.html'
    permission_required = 'config.create_model'
    success_url = reverse_lazy('config-model')
    title = "Novo Modelo"
    subtitle = "Configuração de modelos"


class ModelEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Model
    form_class = ModelForm
    template_name = 'config/form.html'
    permission_required = 'config.edit_model'
    success_url = reverse_lazy('config-model')
    title = "Editar Modelo"
    subtitle = "Configuração de modelos"


class ModelDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Model
    template_name = "config/confirm_delete.html"
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
