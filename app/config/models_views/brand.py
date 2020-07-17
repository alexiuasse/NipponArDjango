#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 17/07/2020 19:36.
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
from ..models import Brand
from ..tables import *


class BrandView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = Brand
    table_class = BrandTable
    filterset_class = BrandFilter
    paginator_class = LazyPaginator
    permission_required = 'config.view_brand'
    template_name = 'config/models_view.html'
    title = "Marca"
    subtitle = "Configuração de marcas"
    new = reverse_lazy('config-brand-create')


class BrandCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Brand
    form_class = BrandForm
    template_name = 'config/form.html'
    permission_required = 'config.create_brand'
    success_url = reverse_lazy('config-brand')
    title = "Nova Marca"
    subtitle = "Configuração de marcas"


class BrandEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Brand
    form_class = BrandForm
    template_name = 'config/form.html'
    permission_required = 'config.edit_brand'
    success_url = reverse_lazy('config-brand')
    title = "Editar Marca - "
    subtitle = "Configuração de marcas"


class BrandDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Brand
    template_name = "config/confirm_delete.html"
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
