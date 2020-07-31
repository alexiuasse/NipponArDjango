#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 30/07/2020 20:54.
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


class CustomerProfile(LoginRequiredMixin, View):
    template = 'customer/profile.html'

    def get(self, request, pk, tp):
        customer = IndividualCustomer.objects.get(pk=pk) if tp == 0 else JuridicalCustomer.objects.get(pk=pk)
        header = settings.HEADER_CLASS_INDIVIDUAL_CUSTOMER if tp == 0 else settings.HEADER_CLASS_JURIDICAL_CUSTOMER

        context = {
            'config': {
                'header': header
            },
            'customer': customer
        }
        return render(request, self.template, context)


class Customer(LoginRequiredMixin, View):
    template = 'customer/view.html'
    title = settings.TITLE_VIEW_CUSTOMER
    subtitle = settings.SUBTITLE_VIEW_CUSTOMER

    def get(self, request):
        links = {
            'Pessoas Físicas': {
                'config': {
                    'header': settings.HEADER_CLASS_INDIVIDUAL_CUSTOMER,
                },
                'Pessoa Física': {
                    'name': "Pessoa Física",
                    'link': reverse_lazy('customer:individual:view'),
                    'badge_text': IndividualCustomer.objects.count(),
                    'badge_class': 'badge-success',
                    'icon': 'person',
                },
                'Novo Cadastro': {
                    'name': "Novo Cadastro",
                    'link': reverse_lazy('customer:individual:create'),
                    'badge_text': "Novo",
                    'badge_class': 'badge-primary',
                    'icon': 'add',
                },
            },
            'Pessoas Jurídicas': {
                'config': {
                    'header': settings.HEADER_CLASS_JURIDICAL_CUSTOMER,
                },
                'Pessoa Jurídica': {
                    'name': "Pessoa Jurídica",
                    'link': reverse_lazy('customer:juridical:view'),
                    'badge_text': JuridicalCustomer.objects.count(),
                    'badge_class': 'badge-success',
                    'icon': 'person',
                },
                'Novo Cadastro': {
                    'name': "Novo Cadastro",
                    'link': reverse_lazy('customer:juridical:create'),
                    'badge_text': "Novo",
                    'badge_class': 'badge-primary',
                    'icon': 'add',
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
class IndividualCustomerView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = IndividualCustomer
    table_class = IndividualCustomerTable
    filterset_class = IndividualCustomerFilter
    paginator_class = LazyPaginator
    permission_required = 'customer.view_individualcustomer'
    template_name = 'base/view.html'
    title = settings.TITLE_VIEW_INDIVIDUAL_CUSTOMER
    subtitle = settings.SUBTITLE_INDIVIDUAL_CUSTOMER
    new = reverse_lazy('customer:individual:create')
    header_class = settings.HEADER_CLASS_INDIVIDUAL_CUSTOMER


class IndividualCustomerCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = IndividualCustomer
    form_class = IndividualCustomerForm
    template_name = 'base/form.html'
    permission_required = 'customer.create_individualcustomer'
    success_url = reverse_lazy('customer:individual:view')
    title = settings.TITLE_CREATE_INDIVIDUAL_CUSTOMER
    subtitle = settings.SUBTITLE_INDIVIDUAL_CUSTOMER
    header_class = settings.HEADER_CLASS_INDIVIDUAL_CUSTOMER


class IndividualCustomerEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = IndividualCustomer
    form_class = IndividualCustomerForm
    template_name = 'base/form.html'
    permission_required = 'customer.edit_individualcustomer'
    success_url = reverse_lazy('customer:individual:view')
    title = settings.TITLE_EDIT_INDIVIDUAL_CUSTOMER
    subtitle = settings.SUBTITLE_INDIVIDUAL_CUSTOMER
    header_class = settings.HEADER_CLASS_INDIVIDUAL_CUSTOMER


class IndividualCustomerDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = IndividualCustomer
    template_name = "base/confirm_delete.html"
    permission_required = 'customer.del_individualcustomer'
    success_url = reverse_lazy('customer:individual:view')
    title = settings.TITLE_DEL_INDIVIDUAL_CUSTOMER
    subtitle = settings.SUBTITLE_INDIVIDUAL_CUSTOMER
    header_class = settings.HEADER_CLASS_INDIVIDUAL_CUSTOMER

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
    title = settings.TITLE_VIEW_JURIDICAL_CUSTOMER
    subtitle = settings.SUBTITLE_JURIDICAL_CUSTOMER
    new = reverse_lazy('customer:juridical:create')
    header_class = settings.HEADER_CLASS_JURIDICAL_CUSTOMER


class JuridicalCustomerCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = JuridicalCustomer
    form_class = JuridicalCustomerForm
    template_name = 'base/form.html'
    permission_required = 'customer.create_juridicalcustomer'
    success_url = reverse_lazy('customer:juridical:view')
    title = settings.TITLE_CREATE_JURIDICAL_CUSTOMER
    subtitle = settings.SUBTITLE_JURIDICAL_CUSTOMER
    header_class = settings.HEADER_CLASS_JURIDICAL_CUSTOMER


class JuridicalCustomerEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = JuridicalCustomer
    form_class = JuridicalCustomerForm
    template_name = 'base/form.html'
    permission_required = 'customer.edit_juridicalcustomer'
    success_url = reverse_lazy('customer:juridical:view')
    title = settings.TITLE_EDIT_JURIDICAL_CUSTOMER
    subtitle = settings.SUBTITLE_JURIDICAL_CUSTOMER
    header_class = settings.HEADER_CLASS_JURIDICAL_CUSTOMER


class JuridicalCustomerDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = JuridicalCustomer
    template_name = "base/confirm_delete.html"
    permission_required = 'customer.del_juridicalcustomer'
    success_url = reverse_lazy('customer:juridical:view')
    title = settings.TITLE_DEL_JURIDICAL_CUSTOMER
    subtitle = settings.SUBTITLE_JURIDICAL_CUSTOMER
    header_class = settings.HEADER_CLASS_JURIDICAL_CUSTOMER

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific database
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context
