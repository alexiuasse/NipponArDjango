#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 24/08/2020 17:44.
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

from .conf import *
from .filters import *
from .forms import *
from .tables import *
from frontend.icons import ICON_PERSON, ICON_NEW_PERSON


class CustomerProfile(LoginRequiredMixin, View):
    template = 'customer/profile.html'

    def get(self, request, pk, tp):
        obj = IndividualCustomer.objects.get(pk=pk) if tp == 0 else JuridicalCustomer.objects.get(pk=pk)
        header = HEADER_CLASS_INDIVIDUAL_CUSTOMER if tp == 0 else HEADER_CLASS_JURIDICAL_CUSTOMER
        context = {
            'config': {
                'header': header
            },
            'obj': obj,
        }
        return render(request, self.template, context)


class Customer(LoginRequiredMixin, View):
    template = 'customer/view.html'
    title = TITLE_VIEW_CUSTOMER
    subtitle = SUBTITLE_VIEW_CUSTOMER

    def get(self, request):
        links = {
            'Pessoas Físicas': {
                'Pessoa Física': {
                    'name': "Ver Todas Pessoas Físicas",
                    'link': reverse_lazy('customer:individualcustomer:view'),
                    'contextual': 'success',
                    'icon': ICON_PERSON,
                },
                'Novo Cadastro': {
                    'name': "Novo Cadastro",
                    'link': reverse_lazy('customer:individualcustomer:create'),
                    'contextual': 'primary',
                    'icon': ICON_NEW_PERSON,
                },
            },
            'Pessoas Jurídicas': {
                'Pessoa Jurídica': {
                    'name': "Ver Todas Pessoas Jurídicas",
                    'link': reverse_lazy('customer:juridicalcustomer:view'),
                    'contextual': 'success',
                    'icon': ICON_PERSON,
                },
                'Novo Cadastro': {
                    'name': "Novo Cadastro",
                    'link': reverse_lazy('customer:juridicalcustomer:create'),
                    'contextual': 'primary',
                    'icon': ICON_NEW_PERSON,
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
    title = TITLE_VIEW_INDIVIDUAL_CUSTOMER
    subtitle = SUBTITLE_INDIVIDUAL_CUSTOMER
    new = reverse_lazy('customer:individualcustomer:create')
    back_url = reverse_lazy('customer:index')
    header_class = HEADER_CLASS_INDIVIDUAL_CUSTOMER


class IndividualCustomerCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = IndividualCustomer
    form_class = IndividualCustomerForm
    template_name = 'customer/form.html'
    permission_required = 'customer.create_individualcustomer'
    title = TITLE_CREATE_INDIVIDUAL_CUSTOMER
    subtitle = SUBTITLE_INDIVIDUAL_CUSTOMER
    header_class = HEADER_CLASS_INDIVIDUAL_CUSTOMER

    @staticmethod
    def get_back_url():
        return reverse_lazy('customer:individualcustomer:view')


class IndividualCustomerEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = IndividualCustomer
    form_class = IndividualCustomerForm
    template_name = 'customer/form.html'
    permission_required = 'customer.edit_individualcustomer'
    title = TITLE_EDIT_INDIVIDUAL_CUSTOMER
    subtitle = SUBTITLE_INDIVIDUAL_CUSTOMER
    header_class = HEADER_CLASS_INDIVIDUAL_CUSTOMER


# delete all services
class IndividualCustomerDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = IndividualCustomer
    template_name = "base/confirm_delete.html"
    permission_required = 'customer.del_individualcustomer'
    success_url = reverse_lazy('customer:individualcustomer:view')
    title = TITLE_DEL_INDIVIDUAL_CUSTOMER
    subtitle = SUBTITLE_INDIVIDUAL_CUSTOMER
    header_class = HEADER_CLASS_INDIVIDUAL_CUSTOMER

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
    title = TITLE_VIEW_JURIDICAL_CUSTOMER
    subtitle = SUBTITLE_JURIDICAL_CUSTOMER
    new = reverse_lazy('customer:juridicalcustomer:create')
    back_url = reverse_lazy('customer:index')
    header_class = HEADER_CLASS_JURIDICAL_CUSTOMER


class JuridicalCustomerCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = JuridicalCustomer
    form_class = JuridicalCustomerForm
    template_name = 'base/form.html'
    permission_required = 'customer.create_juridicalcustomer'
    title = TITLE_CREATE_JURIDICAL_CUSTOMER
    subtitle = SUBTITLE_JURIDICAL_CUSTOMER
    header_class = HEADER_CLASS_JURIDICAL_CUSTOMER

    @staticmethod
    def get_back_url():
        return reverse_lazy('customer:juridicalcustomer:view')


class JuridicalCustomerEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = JuridicalCustomer
    form_class = JuridicalCustomerForm
    template_name = 'base/form.html'
    permission_required = 'customer.edit_juridicalcustomer'
    title = TITLE_EDIT_JURIDICAL_CUSTOMER
    subtitle = SUBTITLE_JURIDICAL_CUSTOMER
    header_class = HEADER_CLASS_JURIDICAL_CUSTOMER


# delete all services
class JuridicalCustomerDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = JuridicalCustomer
    template_name = "base/confirm_delete.html"
    permission_required = 'customer.del_juridicalcustomer'
    success_url = reverse_lazy('customer:juridicalcustomer:view')
    title = TITLE_DEL_JURIDICAL_CUSTOMER
    subtitle = SUBTITLE_JURIDICAL_CUSTOMER
    header_class = HEADER_CLASS_JURIDICAL_CUSTOMER

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific database
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context

