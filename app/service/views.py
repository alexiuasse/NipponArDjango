#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 02/08/2020 13:31.
from typing import Dict, Any

from customer.models import IndividualCustomer, JuridicalCustomer
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
from device.models import Device


class OrderOfServiceProfile(LoginRequiredMixin, View):
    template = 'service/profile.html'
    title = TITLE_VIEW_ORDER_OF_SERVICE
    subtitle = SUBTITLE_ORDER_OF_SERVICE

    def get(self, request, cpk, ctp, dev, pk):
        """
        
        :param request: 
        :param cpk: customer primary key
        :param ctp: customer type
        :param dev: device primary key
        :param pk: primary key of object
        :return: render of layout
        """
        header = HEADER_CLASS_ORDER_OF_SERVICE

        context = {
            'config': {
                'header': header
            },
            'obj': OrderOfService.objects.get(pk=pk),
            'cpk': cpk,
            'ctp': ctp,
        }
        return render(request, self.template, context)


class OrderOfServiceIndex(LoginRequiredMixin, View):
    template = 'device/view.html'
    title = TITLE_VIEW_ORDER_OF_SERVICE
    subtitle = SUBTITLE_ORDER_OF_SERVICE

    def get(self, request):
        links = {
            'Equipamentos': {
                'config': {
                    'header': HEADER_CLASS_ORDER_OF_SERVICE,
                },
                'Equipamentos': {
                    'name': "Equipamentos",
                    'link': reverse_lazy('device:view'),
                    'badge_text': OrderOfService.objects.count(),
                    'badge_class': 'badge-success',
                    'icon': 'person',
                },

            },
        }
        context = {
            'title': self.title,
            'subtitle': self.subtitle,
            'links': links
        }
        return render(request, self.template, context)


class OrderOfServiceView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = OrderOfService
    table_class = OrderOfServiceTable
    filterset_class = OrderOfServiceFilter
    paginator_class = LazyPaginator
    permission_required = 'service.view_orderofservice'
    template_name = 'base/view.html'
    title = TITLE_VIEW_ORDER_OF_SERVICE
    subtitle = SUBTITLE_ORDER_OF_SERVICE
    new = reverse_lazy('service:index')
    # new = reverse_lazy('orderofservice:create')
    header_class = HEADER_CLASS_ORDER_OF_SERVICE


class OrderOfServiceCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = OrderOfService
    form_class = OrderOfServiceForm
    template_name = 'base/form.html'
    permission_required = 'service.create_orderofservice'
    title = TITLE_CREATE_ORDER_OF_SERVICE
    subtitle = SUBTITLE_ORDER_OF_SERVICE
    header_class = HEADER_CLASS_ORDER_OF_SERVICE

    def get_success_url(self):
        return reverse_lazy('device:profile',
                            kwargs={'cpk': self.kwargs['cpk'], 'ctp': self.kwargs['ctp'], 'pk': self.kwargs['dev']})

    def get_back_url(self):
        return reverse_lazy('device:profile',
                            kwargs={'cpk': self.kwargs['cpk'], 'ctp': self.kwargs['ctp'], 'pk': self.kwargs['dev']})

    def form_valid(self, form):
        response = super(OrderOfServiceCreate, self).form_valid(form)
        if self.object:
            Device.objects.get(pk=self.kwargs['dev']).order_of_services.add(self.object)
        return response


class OrderOfServiceEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = OrderOfService
    form_class = OrderOfServiceForm
    template_name = 'base/form.html'
    permission_required = 'service.edit_orderofservice'
    title = TITLE_EDIT_ORDER_OF_SERVICE
    subtitle = SUBTITLE_ORDER_OF_SERVICE
    header_class = HEADER_CLASS_ORDER_OF_SERVICE

    def get_delete_url(self):
        return reverse_lazy('service:delete',
                            kwargs={'cpk': self.kwargs['cpk'], 'ctp': self.kwargs['ctp'], 'dev': self.kwargs['dev'],
                                    'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        return super(OrderOfServiceEdit, self).get_context_data(**kwargs)


class OrderOfServiceDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = OrderOfService
    template_name = "base/confirm_delete.html"
    permission_required = 'service.del_orderofservice'
    title = TITLE_DEL_ORDER_OF_SERVICE
    subtitle = SUBTITLE_ORDER_OF_SERVICE
    header_class = HEADER_CLASS_ORDER_OF_SERVICE

    def get_success_url(self):
        return reverse_lazy('device:profile',
                            kwargs={'cpk': self.kwargs['cpk'], 'ctp': self.kwargs['ctp'], 'pk': self.kwargs['dev']})

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific database
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context
