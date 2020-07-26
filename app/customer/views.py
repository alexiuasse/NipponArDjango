#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 25/07/2020 23:05.
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


class Customer(LoginRequiredMixin, View):
    template = 'customer/view.html'
    title = 'Clientes'
    subtitle = 'Manejamento de clientes'

    def get(self, request):
        links = {
            'Clientes - Pessoa Física': {
                'header': 'card-header-warning',
                'Pessoa Física': {
                    'name': "Pessoa Física",
                    'link': reverse_lazy('customer-individual'),
                },
            },
            'Clientes - Pessoa Jurídica': {
                'header': 'card-header-danger',
                'Pessoa Jurídica': {
                    'name': "Pessoa Jurídica",
                    'link': reverse_lazy('customer-juridical')
                }
            },
        }
        context = {
            'title': self.title,
            'subtitle': self.subtitle,
            'links': links
        }
        return render(request, self.template, context)


########################################################################################################################
class IndividualCustomerView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = IndividualCustomer
    table_class = IndividualCustomerTable
    filterset_class = IndividualCustomerFilter
    paginator_class = LazyPaginator
    permission_required = 'customer.view_individualcustomer'
    template_name = 'base/view.html'
    title = "Cliente - Pessoa Física"
    subtitle = "Configuração de clientes"
    new = reverse_lazy('customer-individual-create')


class IndividualCustomerCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = IndividualCustomer
    form_class = IndividualCustomerForm
    template_name = 'base/form.html'
    permission_required = 'customer.create_individualcustomer'
    success_url = reverse_lazy('customer-individual')
    title = "Novo Cliente - Pessoa Física"
    subtitle = "Configuração de clientes"


class IndividualCustomerEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = IndividualCustomer
    form_class = IndividualCustomerForm
    template_name = 'base/form.html'
    permission_required = 'customer.edit_individualcustomer'
    success_url = reverse_lazy('customer-individual')
    title = "Editar Cliente - Pessoa Física"
    subtitle = "Configuração de clientes"


class IndividualCustomerDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = IndividualCustomer
    template_name = "base/confirm_delete.html"
    permission_required = 'customer.del_individualcustomer'
    success_url = reverse_lazy('customer-individual')
    title = "Deletar Cliente - Pessoa Física"
    subtitle = "Configuração de clientes"

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific database
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context


########################################################################################################################
class JuridicalCustomerView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = JuridicalCustomer
    table_class = JuridicalCustomerTable
    filterset_class = JuridicalCustomerFilter
    paginator_class = LazyPaginator
    permission_required = 'customer.view_juridicalcustomer'
    template_name = 'base/view.html'
    title = "Cliente - Pessoa Jurídica"
    subtitle = "Configuração de clientes"
    new = reverse_lazy('customer-juridical-create')


class JuridicalCustomerCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = JuridicalCustomer
    form_class = JuridicalCustomerForm
    template_name = 'base/form.html'
    permission_required = 'customer.create_juridicalcustomer'
    success_url = reverse_lazy('customer-juridical')
    title = "Novo Cliente - Pessoa Jurídica"
    subtitle = "Configuração de clientes"


class JuridicalCustomerEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = JuridicalCustomer
    form_class = JuridicalCustomerForm
    template_name = 'base/form.html'
    permission_required = 'customer.edit_juridicalcustomer'
    success_url = reverse_lazy('customer-juridical')
    title = "Editar Cliente - Pessoa Jurídica"
    subtitle = "Configuração de clientes"


class JuridicalCustomerDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = JuridicalCustomer
    template_name = "base/confirm_delete.html"
    permission_required = 'customer.del_juridicalcustomer'
    success_url = reverse_lazy('customer-juridical')
    title = "Deletar Cliente - Pessoa Jurídica"
    subtitle = "Configuração de clientes"

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific database
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context
