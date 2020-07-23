#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 22/07/2020 22:57.
from typing import Dict, Any

from django.contrib.admin.utils import NestedObjects
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django_filters.views import FilterView
from django_tables2.paginators import LazyPaginator
from django_tables2.views import SingleTableMixin

from .filters import *
from .forms import *
from .tables import *


class CustomerView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = Customer
    table_class = CustomerTable
    filterset_class = CustomerFilter
    paginator_class = LazyPaginator
    permission_required = 'customer.view_customer'
    template_name = 'customer/view.html'
    title = "Cliente"
    subtitle = "Configuração de clientes"
    new = reverse_lazy('customer-create')


class CustomerCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer/form.html'
    permission_required = 'customer.create_customer'
    success_url = reverse_lazy('customer')
    title = "Novo Cliente"
    subtitle = "Configuração de clientes"


class CustomerEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer/form.html'
    permission_required = 'customer.edit_customer'
    success_url = reverse_lazy('customer')
    title = "Editar Cliente"
    subtitle = "Configuração de clientes"


class CustomerDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Customer
    template_name = "customer/confirm_delete.html"
    permission_required = 'customer.del_customer'
    success_url = reverse_lazy('customer')
    title = "Deletar Cliente"
    subtitle = "Configuração de clientes"

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific database
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context


class CustomerAddressView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = CustomerAddress
    table_class = CustomerAddressTable
    filterset_class = CustomerAddressFilter
    paginator_class = LazyPaginator
    permission_required = 'customer.view_customeraddress'
    template_name = 'customer/view.html'
    title = "Endereço de Cliente"
    subtitle = "Configuração de endereço de cliente"
    new = reverse_lazy('customer-address-create')


class CustomerAddressCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = CustomerAddress
    form_class = CustomerAddressForm
    template_name = 'customer/form.html'
    permission_required = 'customer.create_customeraddress'
    success_url = reverse_lazy('customer-address')
    title = "Novo Endereço de Cliente"
    subtitle = "Configuração de endereço de cliente"


class CustomerAddressEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = CustomerAddress
    form_class = CustomerAddressForm
    template_name = 'customer/form.html'
    permission_required = 'customer.edit_customeraddress'
    success_url = reverse_lazy('customer-address')
    title = "Endereço de Cliente"
    subtitle = "Configuração de endereço de cliente"


class CustomerAddressDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = CustomerAddress
    template_name = "customer/confirm_delete.html"
    permission_required = 'customer.del_customeraddress'
    success_url = reverse_lazy('customer-address')
    title = "Deletar Endereço de Cliente"
    subtitle = "Configuração de endereço de cliente"

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific database
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context
